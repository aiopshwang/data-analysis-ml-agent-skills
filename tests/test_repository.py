from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from scan_public import scan_repo  # noqa: E402
from validate_repo import collect_violations  # noqa: E402


def test_repository_contract():
    assert collect_violations() == {}


def test_public_content_has_no_secret_patterns():
    assert scan_repo(ROOT) == {}


def test_external_denylist_is_honored(tmp_path):
    sample_root = tmp_path / "repo"
    sample_root.mkdir()
    (sample_root / "sample.md").write_text("ConfidentialProject", encoding="utf-8")
    denylist = tmp_path / "denylist.txt"
    denylist.write_text("ConfidentialProject\n", encoding="utf-8")
    findings = scan_repo(sample_root, denylist)
    assert "sample.md" in findings


def test_placeholder_windows_path_is_allowed(tmp_path):
    sample_root = tmp_path / "repo"
    sample_root.mkdir()
    (sample_root / "sample.md").write_text(
        r"Copy into C:\Users\<you>\.codex\skills.", encoding="utf-8"
    )
    assert scan_repo(sample_root) == {}
