#!/usr/bin/env python3
# scripts/check_python_governance.py
"""Mechanical Python-governance checks for agent-managed repositories."""

from __future__ import annotations

import argparse
import ast
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

IGNORED_DIRS = {
    ".git",
    ".mypy_cache",
    ".pytest_cache",
    ".ruff_cache",
    ".tox",
    ".venv",
    "__pycache__",
    "build",
    "dist",
    "node_modules",
    "venv",
}

FORBIDDEN_TRACKABLE_PARTS = {
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".ruff_cache",
    ".tox",
    ".venv",
    "venv",
}

BLOCKING_ASYNC_CALLS = {
    "time.sleep",
    "requests.get",
    "requests.post",
    "requests.put",
    "requests.patch",
    "requests.delete",
    "requests.request",
    "subprocess.run",
    "subprocess.call",
    "subprocess.check_call",
    "subprocess.check_output",
    "os.system",
}

LEGACY_TYPING_NAMES = {
    "Dict",
    "List",
    "Optional",
    "Set",
    "Tuple",
}


@dataclass(frozen=True, slots=True)
class Finding:
    path: Path
    line: int
    code: str
    message: str

    def render(self, root: Path) -> str:
        try:
            display_path = self.path.relative_to(root)
        except ValueError:
            display_path = self.path
        return f"{display_path}:{self.line}: {self.code} {self.message}"


def iter_python_files(root: Path) -> Iterable[Path]:
    for path in root.rglob("*.py"):
        if any(part in IGNORED_DIRS for part in path.parts):
            continue
        yield path


def dotted_name(node: ast.AST) -> str | None:
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        parent = dotted_name(node.value)
        return f"{parent}.{node.attr}" if parent else node.attr
    return None


def annotation_contains_any(node: ast.AST | None) -> bool:
    if node is None:
        return False
    return any(isinstance(child, ast.Name) and child.id == "Any" for child in ast.walk(node))


class PythonVisitor(ast.NodeVisitor):
    def __init__(self, path: Path) -> None:
        self.path = path
        self.findings: list[Finding] = []
        self.async_depth = 0

    def add(self, node: ast.AST, code: str, message: str) -> None:
        self.findings.append(
            Finding(self.path, getattr(node, "lineno", 1), code, message)
        )

    def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef) -> None:  # noqa: N802
        self._check_public_signature(node)
        self.async_depth += 1
        self.generic_visit(node)
        self.async_depth -= 1

    def visit_ExceptHandler(self, node: ast.ExceptHandler) -> None:  # noqa: N802
        if node.type is None:
            self.add(node, "PYG001", "bare except is forbidden")
        self.generic_visit(node)

    def visit_ImportFrom(self, node: ast.ImportFrom) -> None:  # noqa: N802
        if node.module == "typing":
            for alias in node.names:
                if alias.name in LEGACY_TYPING_NAMES:
                    self.add(
                        node,
                        "PYG002",
                        f"prefer modern built-in typing syntax over typing.{alias.name}",
                    )
        self.generic_visit(node)

    def visit_Call(self, node: ast.Call) -> None:  # noqa: N802
        name = dotted_name(node.func)
        if self.async_depth and name in BLOCKING_ASYNC_CALLS:
            self.add(
                node,
                "PYG003",
                f"blocking call {name} used inside async code; use a native async API or offload it",
            )
        if name in {"eval", "exec"}:
            self.add(node, "PYG004", f"review use of {name}(); never pass untrusted input")
        self.generic_visit(node)

    def visit_FunctionDef(self, node: ast.FunctionDef) -> None:  # noqa: N802
        self._check_public_signature(node)
        self.generic_visit(node)

    def _check_public_signature(
        self, node: ast.FunctionDef | ast.AsyncFunctionDef
    ) -> None:
        if node.name.startswith("_"):
            return
        arguments = [*node.args.posonlyargs, *node.args.args, *node.args.kwonlyargs]
        if any(arg.annotation is None for arg in arguments if arg.arg not in {"self", "cls"}):
            self.add(node, "PYG005", "public function has untyped parameters")
        if node.returns is None:
            self.add(node, "PYG006", "public function has no return annotation")
        if annotation_contains_any(node.returns) or any(
            annotation_contains_any(arg.annotation) for arg in arguments
        ):
            self.add(node, "PYG007", "public interface uses Any; verify that it is necessary")


def scan_python_file(path: Path) -> list[Finding]:
    try:
        source = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return [Finding(path, 1, "PYG900", "Python file is not valid UTF-8")]

    try:
        tree = ast.parse(source, filename=str(path))
    except SyntaxError as exc:
        return [
            Finding(path, exc.lineno or 1, "PYG901", f"syntax error: {exc.msg}")
        ]

    visitor = PythonVisitor(path)
    visitor.visit(tree)
    return visitor.findings


def tracked_paths(root: Path) -> list[Path]:
    try:
        result = subprocess.run(
            ["git", "ls-files", "-z"],
            cwd=root,
            check=True,
            capture_output=True,
            text=False,
        )
    except (FileNotFoundError, subprocess.CalledProcessError):
        return []

    return [root / raw.decode("utf-8") for raw in result.stdout.split(b"\0") if raw]


def check_generated_files(root: Path) -> list[Finding]:
    findings: list[Finding] = []
    for path in tracked_paths(root):
        relative_parts = path.relative_to(root).parts
        if any(part in FORBIDDEN_TRACKABLE_PARTS for part in relative_parts):
            findings.append(
                Finding(path, 1, "PYG100", "generated/cache path should not be committed")
            )
        elif path.suffix in {".pyc", ".pyo"}:
            findings.append(
                Finding(path, 1, "PYG101", "compiled Python artifact should not be committed")
            )
    return findings


def check_strict_project(root: Path) -> list[Finding]:
    findings: list[Finding] = []
    pyproject = root / "pyproject.toml"
    if not pyproject.is_file():
        findings.append(Finding(pyproject, 1, "PYG200", "strict Python project requires pyproject.toml"))
    if not (root / "tests").is_dir():
        findings.append(Finding(root / "tests", 1, "PYG201", "strict Python project requires tests/"))
    if not (root / "src").is_dir():
        findings.append(
            Finding(
                root / "src",
                1,
                "PYG202",
                "strict project expects src/ layout; pass without --strict-project for intentionally different repositories",
            )
        )
    return findings


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", default=".", help="repository root")
    parser.add_argument(
        "--strict-project",
        action="store_true",
        help="also require pyproject.toml, src/, and tests/",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = Path(args.root).resolve()

    findings = check_generated_files(root)
    for path in iter_python_files(root):
        findings.extend(scan_python_file(path))
    if args.strict_project:
        findings.extend(check_strict_project(root))

    findings.sort(key=lambda finding: (str(finding.path), finding.line, finding.code))
    for finding in findings:
        print(finding.render(root))

    if findings:
        print(f"Python governance failed with {len(findings)} finding(s).", file=sys.stderr)
        return 1

    print("Python governance checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
