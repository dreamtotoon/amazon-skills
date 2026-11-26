#!/usr/bin/env python3
"""Validate distributable SKILL.md files without executing skill code."""

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

import yaml


def validate_skill(folder):
    errors = []
    path = folder / "SKILL.md"
    if not path.is_file():
        return ["缺少 SKILL.md"]
    text = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|\Z)(.*)", text, re.S)
    if not match:
        return ["缺少有效的 YAML 文件头"]
    try:
        header = yaml.safe_load(match.group(1))
    except yaml.YAMLError as exc:
        return ["YAML 文件头无法解析: {}".format(exc)]
    if not isinstance(header, dict):
        return ["YAML 文件头必须包含 name 和 description"]
    name = header.get("name")
    if not isinstance(name, str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) or len(name) > 64:
        errors.append("name 须为不超过 64 字符的小写英文、数字和短横线组合")
    elif name != folder.name:
        errors.append("name 与技能文件夹名称不一致")
    description = header.get("description")
    if not isinstance(description, str) or not description.strip() or len(description) > 1024:
        errors.append("description 须为 1–1024 字符的文本")
    if not match.group(2).strip():
        errors.append("缺少技能正文")
    if re.search(r"\bTODO\b|\[待填写\]", text):
        errors.append("仍有未填写的模板标记")
    for target in re.findall(r"(?<!!)\[[^\]]+\]\(([^\s)]+)\)", match.group(2)):
        parsed = urlsplit(target.strip("<>"))
        if parsed.scheme or parsed.netloc or not parsed.path:
            continue
        linked = (folder / unquote(parsed.path)).resolve()
        try:
            linked.relative_to(folder.resolve())
        except ValueError:
            errors.append("本地链接超出技能文件夹: {}".format(target))
            continue
        if not linked.exists():
            errors.append("本地链接不存在: {}".format(target))
    return errors


def main():
    root = Path(__file__).resolve().parents[1] / "skills"
    if not root.is_dir():
        print("检查失败：缺少 skills/ 目录", file=sys.stderr)
        return 1
    folders = sorted(p for p in root.iterdir() if p.is_dir() and not p.name.startswith("."))
    if not folders:
        print("检查失败：没有正式技能", file=sys.stderr)
        return 1
    failures = 0
    for folder in folders:
        errors = validate_skill(folder)
        if errors:
            failures += 1
            for error in errors:
                print("FAIL {}: {}".format(folder.name, error), file=sys.stderr)
        else:
            print("PASS {}".format(folder.name))
    print("已检查 {} 个技能，{} 个失败。".format(len(folders), failures))
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
