#!/usr/bin/env python3
# scripts/check_repository_governance.py
"""Dependency-free repository governance checks for agent-managed projects."""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

REQUIRED_DOCS = (
    "AGENTS.md",
    "README.md",
    "TODO.md",
    "CHANGELOG.md",
)

FORBIDDEN_PARTS = {
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".ruff_cache",
    ".tox",
    ".venv",
    "venv",
    "node_modules",
}

FORBIDDEN_SUFFIXES = {
    ".pyc",
    ".pyo",
    ".swp",
    ".swo",
}

SECRET_FILENAMES = {
    ".env",
    "id_rsa",
    "id_ed25519",
    "credentials.json",
    "service-account.json",
}

FLOATING_ACTION_RE = re.compile(r"\buses:\s*[^\s@]+@(main|master|head|latest)\b", re.IGNORECASE)
ACTION_RE = re.compile(r"\buses:\s*([^\s]+)")
LATEST_IMAGE_RE = re.compile(r"\b(?:FROM|image:)\s+[^\s:#]+(?::latest)?\s*$", re.IGNORECASE | re.MULTILINE)


@dataclass(frozen=True, slots=True)
class Finding:
    path: Path
    line: int
    code: str
    message: str

    def render(self, root: Path) -> str:
        try:
            display = self.path.relative_to(root)
        except ValueError:
            display = self.path
        return f"{display}:{self.line}: {self.code} {self.message}"


def git_tracked_files(root: Path) -> list[Path]:
    result = subprocess.run(
        ["git", "ls-files", "-z"],
        cwd=root,
        check=False,
        capture_output=True,
    )
    if result.returncode != 0:
        raise RuntimeError("git ls-files failed; run this checker inside a Git repository")
    return [root / raw.decode("utf-8") for raw in result.stdout.split(b"\0") if raw]


def line_number(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def check_required_docs(root: Path) -> list[Finding]:
    findings: list[Finding] = []
    for name in REQUIRED_DOCS:
        path = root / name
        if not path.is_file():
            findings.append(Finding(path, 1, "GOV001", f"required governance document {name} is missing"))
    return findings


def check_tracked_hygiene(root: Path, paths: list[Path], max_bytes: int) -> list[Finding]:
    findings: list[Finding] = []
    for path in paths:
        relative = path.relative_to(root)
        if any(part in FORBIDDEN_PARTS for part in relative.parts):
            findings.append(Finding(path, 1, "GOV100", "generated/cache path is tracked"))
        if path.suffix.lower() in FORBIDDEN_SUFFIXES:
            findings.append(Finding(path, 1, "GOV101", "generated temporary/compiled file is tracked"))
        if path.name.lower() in SECRET_FILENAMES:
            findings.append(Finding(path, 1, "GOV102", "credential-like filename is tracked; use an example/template instead"))
        try:
            size = path.stat().st_size
        except OSError:
            continue
        if size > max_bytes:
            findings.append(Finding(path, 1, "GOV103", f"tracked file is {size} bytes; review large-file storage strategy"))
    return findings


def read_text(path: Path) -> str | None:
    try:
        return path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        return None


def check_workflows(root: Path, paths: list[Path]) -> list[Finding]:
    findings: list[Finding] = []
    for path in paths:
        relative = path.relative_to(root)
        if len(relative.parts) < 3 or relative.parts[:2] != (".github", "workflows"):
            continue
        if path.suffix.lower() not in {".yml", ".yaml"}:
            continue
        text = read_text(path)
        if text is None:
            continue

        if not re.search(r"(?m)^permissions:\s*(?:$|read-all\s*$|\{)", text):
            findings.append(Finding(path, 1, "GOV200", "workflow should declare top-level permissions"))

        for match in FLOATING_ACTION_RE.finditer(text):
            findings.append(Finding(path, line_number(text, match.start()), "GOV201", "CI action uses a floating branch/tag reference"))

        for match in ACTION_RE.finditer(text):
            action = match.group(1)
            if action.startswith("./") or action.startswith("docker://"):
                continue
            if "@" not in action:
                findings.append(Finding(path, line_number(text, match.start()), "GOV202", "CI action reference has no explicit version/ref"))
    return findings


def check_dockerfiles(root: Path, paths: list[Path]) -> list[Finding]:
    findings: list[Finding] = []
    for path in paths:
        if not (path.name == "Dockerfile" or path.name.startswith("Dockerfile.")):
            continue
        text = read_text(path)
        if text is None:
            continue
        for match in LATEST_IMAGE_RE.finditer(text):
            line = match.group(0)
            if ":" not in line.split()[-1] or line.split()[-1].endswith(":latest"):
                findings.append(Finding(path, line_number(text, match.start()), "GOV300", "container base image should use an explicit version rather than latest/implicit latest"))
        if not re.search(r"(?mi)^USER\s+[^\s]+", text):
            findings.append(Finding(path, 1, "GOV301", "Dockerfile has no explicit runtime USER; review non-root execution"))
    return findings


def check_release_docs(root: Path) -> list[Finding]:
    findings: list[Finding] = []
    changelog = root / "CHANGELOG.md"
    text = read_text(changelog)
    if text is not None and "## Unreleased" not in text:
        findings.append(Finding(changelog, 1, "GOV400", "CHANGELOG.md should contain an Unreleased section"))
    return findings


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", default=".", help="repository root")
    parser.add_argument("--max-tracked-bytes", type=int, default=5 * 1024 * 1024, help="large tracked-file warning threshold")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = Path(args.root).resolve()
    try:
        tracked = git_tracked_files(root)
    except RuntimeError as exc:
        print(str(exc), file=sys.stderr)
        return 2

    findings: list[Finding] = []
    findings.extend(check_required_docs(root))
    findings.extend(check_tracked_hygiene(root, tracked, args.max_tracked_bytes))
    findings.extend(check_workflows(root, tracked))
    findings.extend(check_dockerfiles(root, tracked))
    findings.extend(check_release_docs(root))
    findings.sort(key=lambda finding: (str(finding.path), finding.line, finding.code))

    for finding in findings:
        print(finding.render(root))

    if findings:
        print(f"Repository governance failed with {len(findings)} finding(s).", file=sys.stderr)
        return 1

    print("Repository governance checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
