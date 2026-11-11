---
name: drama-dialogue-localizer
description: Use when localizing Chinese short-drama dialogue only into natural North American English for DramaBox/ReelShort/Tallflix-style vertical dramas. Trigger for requests like "只翻译台词", "对白本地化", "中文台词后加英文", "把英文台词插入剧本", "只处理对白不翻译动作线", or "用美国人日常会说的台词". This skill keeps action lines unchanged, preserves Chinese dialogue, inserts localized English on the next line when requested, and uses Chinese as the source of truth when existing English differs from the Chinese.
---

# Drama Dialogue Localizer

## 提问引导模式（用户主动选择）

用户说“带我完成这一步”“带我想”“先问我几个问题”“引导我思考”或明确要求先问后写时启用；普通创作、分析或改稿请求沿用直接执行。此模式优先于本技能默认连续执行或固定问卷；通过统一入口、兼容入口或下游模块调用时传递本模式，不重复问诊。

1. 先读本次材料与有效上下文，区分已确定内容、锁定项和真正未决的选择；已有答案不重复问。缺少必要材料时只索取最小缺口，不编造前情。
2. 找出最影响本步结果的未决决定，每轮最多问三个独立关键问题，按影响排序；不在一个问题里塞多个子问题，不为凑数提问，也不把选择题伪装成预定答案。
3. 每题说明为什么影响结果；适合比较时给二至三个方向，具体说明各自如何影响人物、关系、剧情、期待或本任务的交付，并允许用户提出自己的方向。只分析原稿时不强迫用户改故事。
4. 提问后等待用户回答，再把选择落成当前授权的方案。可以给解释选项所需的短例子，不提前交完整方案、定稿或替用户决定核心创意；仅回答部分问题时，继续不依赖未答项的部分，不能把沉默当选择。
5. 回答后简述已确认选择，将其落实到人物、事件、节奏或其他对应产物，检查连带影响；仍有关键未决项才进入下一轮。没有未决项时说明已有依据并完成本步，不硬凑问题。
6. 用户说“你决定”“按你的判断直接做”时，对已委托范围退出等待并继续；仍保留已有锁定项。只把选择用于当前项目，不自动写成其他项目的通用规则。

可直接开场：“请使用【技能名】带我完成这一步。先读我的材料，找出最影响结果、但我还没有作出的创作决定。每轮最多问我三个关键问题，说明不同选择会怎样影响人物和剧情；已有答案的不要重复问。等我回答后，再把选择落成方案。”

## Purpose

Localize dialogue, not the whole script. Preserve action lines, scene headings, beats, and plot events unless the user explicitly asks otherwise.

Default target:

- Platforms: DramaBox / ReelShort / Tallflix and similar overseas vertical-drama apps.
- Audience: North American women, roughly 20-40.
- Style: fast, short, sharp, emotional, natural spoken English, aiming for 9.8/10口语真实度.

## Fixed Prompt Contract

When the user provides a Chinese script for dialogue localization, operate under this contract:

- Only process dialogue.
- Do not translate action lines.
- Do not rewrite action lines.
- Do not add plot events.
- Preserve Chinese dialogue and write the localized English dialogue on the next line.
- Do not output analysis, scene formatting, unrelated explanation, or Chinese explanation unless the user asks.

Internal process:

1. Extract every dialogue line that needs localization.
2. Understand context, relationships, conflict, emotion, and subtext for each line.
3. Preserve plot information, relationship facts, props, threats, reversals, humiliation, flirtation, and emotional turns.
4. Rewrite the English into North American vertical-drama spoken dialogue.
5. Output only the Chinese dialogue line plus its localized English line.

English dialogue requirements:

- Use natural American English, not Chinese-translated English.
- Use contractions where natural, such as don't, can't, I'm, you're.
- Prefer 1-8 words per line when the information allows it.
- Make lines short, sharp, direct, and emotionally playable.
- Give villains pressure and menace.
- Make protagonists sound like real people, not translation drafts.
- Preserve subtext in flirtation, threat, humiliation, and counterattack.
- Do not add plot.
- Do not change motivations.
- Do not change relationships.
- Do not replace key props.
- Do not state emotions already visible in the action.
- Do not use em dashes in English dialogue.
- Do not write long monologues.

Default output:

```text
【Localized Dialogue】

人物：中文原台词
Localized English dialogue.

人物：中文原台词
Localized English dialogue.
```

## Core Rule

Do not translate Chinese sentence by sentence. Translate the character intent, scene function, power move, and subtext into what an American short-drama character would actually say.

Good pattern:

```text
给我搜！她一定就在这附近！
She's close. Find her!
```

Avoid mechanically mirroring the Chinese structure:

```text
Search for me! She must be nearby!
```

## Source Priority

Use Chinese as the source of truth.

- If existing English conflicts with the Chinese, rewrite the English from the Chinese.
- If prior localized dialogue exists and mostly works, reuse it, but correct any mismatch against the Chinese.
- Do not sacrifice plot-critical information just to make a line shorter.

Plot-critical information includes:

- who is connected to whom, such as blood bond, fiance, family status, adoption, sworn pact
- supernatural mechanics, such as fated Luna, Alpha King, wolfsbane, Blackthorne scent, mark, secret passage
- threats, conditions, leverage, evidence, pregnancy, inheritance, titles, and vows
- named houses, titles, and key objects

## Output Formats

### Dialogue-Only

Use when the user asks for dialogue extraction or a clean dialogue list.

```text
【Localized Dialogue】

人物（语境标记）：中文原台词
Localized English dialogue.

人物：中文原台词
Localized English dialogue.
```

### Embedded Script

Use when the user asks to insert English into a script file.

- Keep all original script content unchanged.
- Insert the English line immediately after its matching Chinese dialogue line.
- Do not translate action lines.
- Do not add English under scene headings, action descriptions, captions, SFX, or outline paragraphs unless the user explicitly asks.
- If the file has a synopsis/outline before the actual script, insert only in the script section by default.
- If editing a real file, create a backup first unless the user explicitly says not to.

Example:

```text
**阿德里安**（转向吸血鬼暴徒，一挥手）：给我搜！她一定就在这附近！
She's close. Find her!
```

## Workflow

1. Identify the scope: dialogue-only output, embedded script, or both.
2. If working inside a script project and a `_真源指针.md` exists, read it before modifying project files. If the user targets a non-true-source file, create or modify that explicit target without silently changing the true source.
3. Find the actual script body. Ignore outlines and episode summaries unless the user asks to localize them.
4. Extract dialogue lines and the minimum context needed to understand the line.
5. Localize each line from the Chinese, preserving plot facts and character intent.
6. Keep the Chinese dialogue line unchanged; place the English line directly below it.
7. Validate that every extracted dialogue line has exactly one English line and that no action lines were translated.

## Voice Guide

- **Lucien / Alpha male lead**: short, calm, controlling. Use commands and clipped statements. Avoid overexplaining.
- **Seraphina / vulnerable heroine**: natural fear, breath, confusion, and resistance. Avoid stiff literal phrasing.
- **Adrian / male villain**: entitled, cruel, possessive. Use short orders and humiliating threats.
- **Morgaine / female villain**: sweet with a knife, passive-aggressive, predatory, sometimes theatrical.
- **Vivian / evil mother figure**: shame, guilt, class contempt, family-honor pressure.
- **Vampires / thugs**: predatory and scary, not polished.

## Line-Level Rules

- Use contractions where natural: don't, can't, I'm, you're, she's.
- Prefer 1-8 words when the information allows it.
- A line may be longer when needed to preserve a blood pact, relationship, threat, or mechanism.
- Replace Chinese explanatory phrasing with playable English subtext.
- Make villain lines sharper and scarier when the scene is a hunt, threat, humiliation, or power play.
- Keep recurring fantasy terms if they are world terms: Alpha King, fated Luna, wolfsbane, House Blackthorne.
- Avoid em dashes in English dialogue.
- Avoid Chinese-translation phrasing such as "you have no qualification", "what kind of person are you", "you actually dare".

## Calibration Examples

```text
我和她……有血脉羁绊？
There's a blood bond between us?

这气味……难道，就是我寻找了多年的宿命 Luna？
That scent... Is she my fated Luna?

这个女人中了狼毒，不过，她身上还有索恩家族的味道……
She's been dosed with wolfsbane. But she smells like Blackthorne.

你只不过是我们收养的一个孤儿。要不是你父亲与公爵大人定下婚约血契，你早死在外面了。
You're nothing but the orphan we took in. If your father hadn't sworn that blood pact with the Duke, you'd be dead in a ditch.

给我搜！她一定就在这附近！
She's close. Find her!

滚开，人类医生！你挡着他们道了。
Move, human doctor. Let them feed.
```

## Validation Checklist

Before finishing:

- Confirm the output contains only the requested scope.
- Confirm Chinese dialogue lines remain unchanged.
- Confirm every localized dialogue line sits directly below the matching Chinese line.
- Confirm action lines were not translated.
- Confirm critical story facts were not dropped.
- Confirm English sounds speakable, not subtitle-like.
- Confirm English dialogue has no em dashes.
