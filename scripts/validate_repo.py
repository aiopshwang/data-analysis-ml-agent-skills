"""Validate the plugin, skill metadata, local links, and trigger-eval schema."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote

import yaml

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_SKILLS = {
    "using-data-analysis",
    "running-decision-grade-data-science",
    "auditing-data-and-ground-truth",
    "designing-leakage-safe-experiments",
    "validating-models-and-claims",
    "diagnosing-ml-failures",
    "shipping-reproducible-results",
}
SLUG = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
SEMVER = re.compile(r"^\d+\.\d+\.\d+(?:[-+][0-9A-Za-z.-]+)?$")
MARKDOWN_LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
PLACEHOLDER = re.compile(r"(?:\[TODO[^\]]*\]|\bTBD\b|TODO:)", re.IGNORECASE)


def split_frontmatter(path: Path) -> tuple[dict, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError("missing YAML frontmatter")
    end = text.find("\n---\n", 4)
    if end < 0:
        raise ValueError("unterminated YAML frontmatter")
    metadata = yaml.safe_load(text[4:end])
    if not isinstance(metadata, dict):
        raise ValueError("frontmatter must be a mapping")
    return metadata, text[end + 5 :]


def validate_local_links(path: Path, root: Path = ROOT) -> list[str]:
    violations: list[str] = []
    text = path.read_text(encoding="utf-8")
    for raw_target in MARKDOWN_LINK.findall(text):
        target = raw_target.strip().strip("<>")
        if (
            not target
            or target.startswith(("#", "http://", "https://", "mailto:"))
            or "://" in target
        ):
            continue
        target = unquote(target.split("#", 1)[0])
        resolved = (path.parent / target).resolve()
        try:
            resolved.relative_to(root.resolve())
        except ValueError:
            violations.append(f"link escapes repository: {raw_target}")
            continue
        if not resolved.exists():
            violations.append(f"broken local link: {raw_target}")
    return violations


def validate_skill(skill_dir: Path) -> list[str]:
    violations: list[str] = []
    skill_md = skill_dir / "SKILL.md"
    try:
        metadata, body = split_frontmatter(skill_md)
    except (OSError, ValueError, yaml.YAMLError) as exc:
        return [str(exc)]

    name = metadata.get("name")
    description = metadata.get("description")
    if name != skill_dir.name:
        violations.append("frontmatter name must match the skill directory")
    if not isinstance(name, str) or len(name) > 64 or not SLUG.fullmatch(name):
        violations.append("name must be a kebab-case slug of at most 64 characters")
    if not isinstance(description, str) or not description.strip():
        violations.append("description must be a non-empty string")
    elif "Use when " not in description:
        violations.append("description must state a concrete 'Use when' boundary")
    elif len(description) > 500:
        violations.append("description must be at most 500 characters")

    if not body.strip():
        violations.append("SKILL.md body is empty")
    if len(body.splitlines()) > 180:
        violations.append("SKILL.md body exceeds the 180-line review budget")
    if PLACEHOLDER.search(skill_md.read_text(encoding="utf-8")):
        violations.append("unfinished placeholder in SKILL.md")
    violations.extend(validate_local_links(skill_md))

    openai_path = skill_dir / "agents" / "openai.yaml"
    if not openai_path.exists():
        violations.append("agents/openai.yaml is missing")
    else:
        try:
            agent_meta = yaml.safe_load(openai_path.read_text(encoding="utf-8"))
        except yaml.YAMLError as exc:
            violations.append(f"agents/openai.yaml is invalid YAML: {exc}")
        else:
            interface = agent_meta.get("interface") if isinstance(agent_meta, dict) else None
            if not isinstance(interface, dict):
                violations.append("agents/openai.yaml requires interface metadata")
            else:
                for key in ("display_name", "short_description", "default_prompt"):
                    if not isinstance(interface.get(key), str) or not interface[key].strip():
                        violations.append(f"agents/openai.yaml interface.{key} is missing")
                prompt = interface.get("default_prompt", "")
                if isinstance(prompt, str) and "$" + skill_dir.name not in prompt:
                    violations.append("default_prompt must mention the $skill-name")
                short = interface.get("short_description", "")
                if isinstance(short, str) and len(short) > 64:
                    violations.append("short_description exceeds 64 characters")

    for resource in list((skill_dir / "references").glob("*")) + list(
        (skill_dir / "assets").glob("*")
    ):
        if not resource.is_file():
            continue
        text = resource.read_text(encoding="utf-8")
        if resource.stat().st_size == 0:
            violations.append(f"empty resource: {resource.relative_to(skill_dir)}")
        if PLACEHOLDER.search(text):
            violations.append(
                f"unfinished placeholder: {resource.relative_to(skill_dir)}"
            )
        if resource.suffix.lower() == ".md":
            violations.extend(validate_local_links(resource))
        elif resource.suffix.lower() in {".yaml", ".yml"}:
            try:
                yaml.safe_load(text)
            except yaml.YAMLError as exc:
                violations.append(
                    f"invalid YAML in {resource.relative_to(skill_dir)}: {exc}"
                )
        elif resource.suffix.lower() == ".json":
            try:
                json.loads(text)
            except json.JSONDecodeError as exc:
                violations.append(
                    f"invalid JSON in {resource.relative_to(skill_dir)}: {exc}"
                )
    return violations


def validate_plugin() -> list[str]:
    path = ROOT / ".codex-plugin" / "plugin.json"
    violations: list[str] = []
    try:
        manifest = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [f"invalid plugin manifest: {exc}"]

    required = ("name", "version", "description", "author", "skills", "interface")
    for key in required:
        if key not in manifest:
            violations.append(f"plugin manifest missing {key}")
    if manifest.get("name") != "data-analysis-ml-agent-skills":
        violations.append("plugin name is not the repository slug")
    if not isinstance(manifest.get("version"), str) or not SEMVER.fullmatch(
        manifest.get("version", "")
    ):
        violations.append("plugin version is not semantic versioning")
    if manifest.get("skills") != "./skills/":
        violations.append("plugin skills path must be ./skills/")
    if not (ROOT / "skills").is_dir():
        violations.append("plugin skills directory is missing")
    serialized = json.dumps(manifest)
    if PLACEHOLDER.search(serialized):
        violations.append("unfinished placeholder in plugin manifest")
    return violations


def validate_trigger_evals() -> list[str]:
    path = ROOT / "evals" / "trigger-prompts.yaml"
    if not path.exists():
        return ["evals/trigger-prompts.yaml is missing"]
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except yaml.YAMLError as exc:
        return [f"trigger eval YAML is invalid: {exc}"]
    if not isinstance(data, dict) or not isinstance(data.get("skills"), dict):
        return ["trigger eval root must contain a skills mapping"]

    violations: list[str] = []
    skills = data["skills"]
    if set(skills) != EXPECTED_SKILLS:
        violations.append("trigger eval skills do not match repository skills")
    all_prompts: list[str] = []
    for skill, cases in skills.items():
        if not isinstance(cases, dict):
            violations.append(f"{skill}: eval cases must be a mapping")
            continue
        for group in ("direct", "indirect", "negative"):
            prompts = cases.get(group)
            if not isinstance(prompts, list) or len(prompts) < 2:
                violations.append(f"{skill}: {group} needs at least two prompts")
                continue
            if not all(isinstance(prompt, str) and prompt.strip() for prompt in prompts):
                violations.append(f"{skill}: {group} includes an empty prompt")
            all_prompts.extend(prompts)
    if len(all_prompts) != len(set(all_prompts)):
        violations.append("trigger eval prompts must be unique")
    return violations


def collect_violations() -> dict[str, list[str]]:
    findings: dict[str, list[str]] = {}
    plugin_violations = validate_plugin()
    if plugin_violations:
        findings[".codex-plugin/plugin.json"] = plugin_violations

    skill_dirs = {
        path.parent.name: path.parent for path in (ROOT / "skills").glob("*/SKILL.md")
    }
    if set(skill_dirs) != EXPECTED_SKILLS:
        findings["skills"] = [
            f"expected {sorted(EXPECTED_SKILLS)}, found {sorted(skill_dirs)}"
        ]
    for name, skill_dir in sorted(skill_dirs.items()):
        violations = validate_skill(skill_dir)
        if violations:
            findings[f"skills/{name}"] = violations

    eval_violations = validate_trigger_evals()
    if eval_violations:
        findings["evals/trigger-prompts.yaml"] = eval_violations

    for path in ROOT.rglob("*.md"):
        if set(path.relative_to(ROOT).parts) & {".git", ".venv"}:
            continue
        violations = validate_local_links(path)
        if violations:
            findings.setdefault(path.relative_to(ROOT).as_posix(), []).extend(violations)
    return findings


def main() -> int:
    findings = collect_violations()
    for path, violations in findings.items():
        for violation in violations:
            print(f"{path}: {violation}")
    if not findings:
        print("repository validation passed")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
