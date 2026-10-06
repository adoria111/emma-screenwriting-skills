# 艾玛短剧 · 故事架构师与主编剧（写作规则库公开版）

这两个角色来自历史调用链 `ai-drama-showrunner → 02-story-architect → 03-chief-writer → 对应写作规则库`。现在整理成可独立安装的两个Skill；每个都附带完整的公开版规则正文，不需要旧版总控或私人目录。

| 历史角色 | 公开安装标识 | 交付与规则 |
| --- | --- | --- |
| 02-story-architect | [em-story-architect](skills/em-story-architect/SKILL.md) | 大纲、人物、集纲；6个规则章节 |
| 03-chief-writer | [em-chief-writer](skills/em-chief-writer/SKILL.md) | 指定集数正文；14个规则章节，含真人/AI/漫剧适配 |

它们是历史角色的公开整理版，不等于现行完整版 `em-ai-story`、`em-ai-script` 的原样导出。原有Beta六技能仍位于仓库根目录的 `skills/`，两套可以并存。

## 下载

- [两个Skill及完整规则库合包](https://github.com/adoria111/emma-screenwriting-skills/releases/download/writing-rules-v1.0.0/emma-story-writing-v1.0.0.zip)
- [故事架构师单独下载](https://github.com/adoria111/emma-screenwriting-skills/releases/download/writing-rules-v1.0.0/em-story-architect-v1.0.0.zip)
- [主编剧单独下载](https://github.com/adoria111/emma-screenwriting-skills/releases/download/writing-rules-v1.0.0/em-chief-writer-v1.0.0.zip)
- [故事架构规则正文](skills/em-story-architect/references/writing-rules.md)
- [主编剧规则正文](skills/em-chief-writer/references/writing-rules.md)

## 下载与安装提示词

```text
请帮我下载并安装「艾玛短剧·故事架构师与主编剧」公开版。
仓库：https://github.com/adoria111/emma-screenwriting-skills
固定版本：writing-rules-v1.0.0
安装来源：advanced/story-writing/skills/ 下的 em-story-architect 和 em-chief-writer 两个目录。
请完整保留每个目录里的 SKILL.md、agents/ 和 references/，按当前工具支持的项目级Skills位置安装；已有同名目录先比较并备份，不直接覆盖，不修改其他技能。
安装后核对两个SKILL及其写作规则文件都存在、引用可读取，并列出用途、调用方法和实际安装路径。目录已复制与宿主已加载要分别说明；需要刷新或重启时如实告诉我，不要把未验证的加载状态说成成功。
```

## 普通聊天怎么用

不安装也可以：打开上方规则正文，连同对应SKILL的方法一起粘贴到普通聊天，再附材料和任务。只输入技能名称不代表模型读过方法。

故事架构示例：使用故事架构师，把以下想法整理成我指定集数的核心大纲、人物档案和分集纲；保留这些设定与结局，不写正文。

主编剧示例：使用主编剧，根据我给出的第1—5集集纲写出完整中文分场正文；保留已锁定人物关系、信息揭晓顺序和每集钩子。

## 内容与版本边界

公开版保留卡点、情绪升级、节奏、冲突、人物、台词、格式、信息边界和可见行动等专业方法。将旧版固定审批、模型能力断言、私人项目路径与部分示例改为可移植规则；逐项类型见[来源与公开版说明](来源与公开版说明.json)。角色开发原文件末段不完整，公开版补了明确的视觉锚点表。

目录中的两份规则库是完整的公开整理版，不是历史文件的逐字备份，不含课程录音、第三方完整剧本或私人案例。经验数字不代表最新市场数据；不承诺过稿或市场效果。检查覆盖结构、依赖、安装包完整性，不声称已经做过跨模型创作效果评测。

## 许可

本目录新增Skill、规则库与说明使用仓库[MIT License](LICENSE)。不扩展到原始私人资料或其他未收录材料。
