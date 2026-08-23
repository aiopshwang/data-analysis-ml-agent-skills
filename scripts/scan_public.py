"""Scan public repository text for secrets and private-work residue."""
from __future__ import annotations

import argparse
import re
from pathlib import Path

TEXT_SUFFIXES = {
    ".cff",
    ".csv",
    ".ini",
    ".json",
    ".md",
    ".py",
    ".toml",
    ".txt",
    ".tsv",
    ".xml",
    ".yaml",
    ".yml",
}
SKIP_DIRS = {".git", ".pytest_cache", ".venv", "__pycache__"}

PATTERNS = {
    "OpenAI-style secret": re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
    "GitHub token": re.compile(r"\bgh[opurs]_[A-Za-z0-9]{20,}\b"),
    "AWS access key": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    "private key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "concrete Windows user path": re.compile(
        r"\b[A-Za-z]:[\\/]+Users[\\/]+(?!<[^>]+>)[^\\/\s\x60\"']+",
        re.IGNORECASE,
    ),
    "workspace residue": re.compile(
        r"(?:"
        + r"One"
        + r"Drive[\\/]+Play skill|"
        + r"Codex"
        + r"_session|Claude"
        + r"code_session)",
        re.IGNORECASE,
    ),
}


def iter_text_files(root: Path):
    for path in root.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        if set(path.relative_to(root).parts) & SKIP_DIRS:
            continue
        yield path


def load_denylist(path: Path | None) -> list[str]:
    if path is None or not path.exists():
        return []
    return [
        line.strip()
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.lstrip().startswith("#")
    ]


def _contains_term(text: str, term: str) -> bool:
    if term.isascii():
        return re.search(rf"\b{re.escape(term)}\b", text, re.IGNORECASE) is not None
    return term.casefold() in text.casefold()


def scan_file(path: Path, denylist: list[str]) -> list[str]:
    text = path.read_text(encoding="utf-8")
    findings: list[str] = []
    for label, pattern in PATTERNS.items():
        if pattern.search(text):
            findings.append(label)
    for term in denylist:
        if _contains_term(text, term):
            findings.append(f"external denylist term: {term}")
    return findings


def scan_repo(root: Path, denylist_path: Path | None = None) -> dict[str, list[str]]:
    denylist = load_denylist(denylist_path)
    findings: dict[str, list[str]] = {}
    for path in iter_text_files(root):
        violations = scan_file(path, denylist)
        if violations:
            findings[path.relative_to(root).as_posix()] = violations
    return findings


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--denylist", type=Path)
    args = parser.parse_args()

    findings = scan_repo(args.root.resolve(), args.denylist)
    for path, violations in findings.items():
        for violation in violations:
            print(f"{path}: {violation}")
    if not findings:
        print("public-content scan passed")
    return 1 if findings else 0


if __name__ == "__main__":
    raise SystemExit(main())
