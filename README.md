# 亚马逊团队技能库

把选品、市场调研、Listing、广告、库存和复盘中已经验证的工作方法，整理成团队可复用的 AI Skills。每个技能独立存放，成员可以按需安装，也可以提交自己的技能。

仓库地址：https://github.com/dreamtotoon/amazon-skills

本仓库公开可读，下载和使用不需要 GitHub 账号。请只提交可公开的流程与脱敏示例。

## 已有技能

| 技能 | 用途 | 调用示例 |
| --- | --- | --- |
| [amazon-workflow-to-skill](skills/amazon-workflow-to-skill/SKILL.md) | 从实际任务、复盘记录或对话中提炼可复用流程，整理为独立技能 | `$amazon-workflow-to-skill 把刚才验证过的广告报表核对流程整理成技能。` |
| [amazon-product-fact-verification](skills/amazon-product-fact-verification/SKILL.md) | 核对规格、包装、兼容性和其他商品事实的证据 | `$amazon-product-fact-verification 核对这份规格表和供应商答复。` |
| [amazon-keyword-architecture](skills/amazon-keyword-architecture/SKILL.md) | 整理词表、标注关键词意图，并映射到 Listing 字段 | `$amazon-keyword-architecture 整理这份美国站关键词表。` |
| [amazon-listing-copy](skills/amazon-listing-copy/SKILL.md) | 根据商品事实及关键词生成指定站点的文案草稿 | `$amazon-listing-copy 用这份规格和词表起草美国站 Listing。` |
| [amazon-listing-audit](skills/amazon-listing-audit/SKILL.md) | 对照站点规则和商品证据审核现有 Listing | `$amazon-listing-audit 核对这份文案与证据是否一致。` |
| [amazon-image-planning-review](skills/amazon-image-planning-review/SKILL.md) | 编制图片需求、核对图片与商品事实并整理审核项 | `$amazon-image-planning-review 根据事实表编制图片任务单。` |
| [amazon-product-selection-scoring](skills/amazon-product-selection-scoring/SKILL.md) | 按项目的版本化评分规则比较选品候选并列出待补证据 | `$amazon-product-selection-scoring 按所附规则评审这三款候选产品。` |

六个业务技能从 [amazon-ai-ops](https://github.com/dreamtotoon/amazon-ai-ops) 整理而来。使用自己的项目资料、目标站点规则和有权限的数据源。清洗、规则校验及正式评分仍使用项目提供的确定性工具。资料或工具缺失时，技能会标注待验证项。

## 安装和调用

### 在 ChatGPT 工作空间中安装

1. 管理员在 **Admin → Plugins → Add → Import marketplace** 输入这个仓库的 GitHub 地址。目录留空，分支使用 `main`。
2. 导入成功后，在插件 **amazon-skills** 的安装策略中选择 **Installed for workspace**，核对角色的安装策略。
3. 成员在新对话中输入 `@`，从技能列表选择所需技能。需要外部数据的任务使用成员已获授权的数据源。

[工作空间导入与同步](https://learn.chatgpt.com/docs/enterprise/plugin-management)

### 在 Codex 中安装单个技能

把下面这段话复制给 Codex：

```text
使用 $skill-installer，从 https://github.com/dreamtotoon/amazon-skills/tree/main/skills/amazon-workflow-to-skill 安装技能。
```

安装完成后，在下一轮输入：

```text
$amazon-workflow-to-skill 根据这次任务中已验证的步骤、判断依据和纠错记录，整理一个团队可复用的亚马逊技能。
```

安装仓库中的其他技能时，将链接最后的技能名称替换成对应文件夹名称。仓库地址是技能的来源，使用前需要在自己的 AI 工具中安装或加载；技能依赖的数据源仍需使用者自行配置和授权。

通过插件安装时，在 Codex 的技能选择器中查找 `amazon-skills`，例如 `$amazon-skills:amazon-listing-audit`。

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
.agents/plugins/marketplace.json
plugin.json
skills/
  amazon-workflow-to-skill/
    SKILL.md
    agents/openai.yaml
  <其他技能>/
    SKILL.md
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
