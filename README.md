# 亚马逊团队技能库

把选品、市场调研、Listing、广告、库存和复盘中已经验证的工作方法，整理成团队可复用的 AI Skills。每个技能独立存放，成员可以按需安装，也可以提交自己的技能。

仓库地址：https://github.com/dreamtotoon/amazon-skills

本仓库公开可读，下载和使用不需要 GitHub 账号。请只提交可公开的流程与脱敏示例。

## 已有技能

| 技能 | 用途 | 调用示例 |
| --- | --- | --- |
| [amazon-workflow-to-skill](skills/amazon-workflow-to-skill/SKILL.md) | 从实际任务、复盘记录或对话中提炼可复用流程，整理为独立技能 | `$amazon-workflow-to-skill 把刚才验证过的广告报表核对流程整理成技能。` |

这个初始技能用于整理工作方法；具体选品、广告或库存业务技能由团队结合实际案例持续补充。

## 安装和调用

### 在 Codex 中安装

把下面这段话复制给 Codex：

```text
使用 $skill-installer，从 https://github.com/dreamtotoon/amazon-skills/tree/main/skills/amazon-workflow-to-skill 安装技能。
```

安装完成后，在下一轮输入：

```text
$amazon-workflow-to-skill 根据这次任务中已验证的步骤、判断依据和纠错记录，整理一个团队可复用的亚马逊技能。
```

安装仓库中的其他技能时，将链接最后的技能名称替换成对应文件夹名称。仓库地址是技能的来源，使用前需要在自己的 AI 工具中安装或加载；技能依赖的数据源仍需使用者自行配置和授权。

### 不使用 Git 命令的安装方式

1. 在仓库首页点击 **Code → Download ZIP**，解压文件。
2. 选择 `skills/` 下需要的技能文件夹，完整复制到工作项目的 `.agents/skills/` 下。例如：`.agents/skills/amazon-workflow-to-skill/SKILL.md`。
3. 在 Codex 中打开该工作项目，下一轮用 `$技能名称` 调用。其他支持 `SKILL.md` 的 AI 工具，请按其技能安装说明放置文件夹。

仓库更新不会自动替换成员电脑上的副本。需要更新时重新获取对应技能，并保留自己的定制内容。[Codex 官方技能说明](https://learn.chatgpt.com/docs/customization/overview#skills)

## 向仓库贡献技能

- **没有 GitHub 账号**：把完整技能文件夹和一个脱敏使用示例交给仓库维护者，由维护者提交。
- **有 GitHub 账号**：Fork 仓库，在自己的副本中新增或修改技能，然后向本仓库发起 Pull Request。维护者审核后合并。

无需共享仓库所有者的账号、密码或令牌。详细步骤见 [贡献说明](CONTRIBUTING.md)，新技能可从 [模板](templates/skill/SKILL.md) 开始。

## 目录约定

```text
skills/
  amazon-workflow-to-skill/
    SKILL.md
    agents/openai.yaml
templates/skill/SKILL.md
scripts/validate_skills.py
.github/workflows/validate-skills.yml
```

每个正式技能放在 `skills/<技能名称>/` 下，包含 `SKILL.md`。只有实际需要时才增加 `scripts/`、`references/` 或 `assets/`。模板放在 `templates/`，不会被当作正式技能检查。

## 本地检查

```bash
python3 -m pip install -r requirements-dev.txt
python3 scripts/validate_skills.py
```

提交和 Pull Request 会运行同样的结构检查：技能名称、描述、正文、未填写模板标记，以及 Markdown 中的本地文件链接。检查通过只代表文件结构符合约定，不代表业务方法已经验证。
