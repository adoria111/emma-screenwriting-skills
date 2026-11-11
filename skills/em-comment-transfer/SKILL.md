---
name: "em-comment-transfer"
description: "艾玛短剧 · 批注迁移。将中文编辑批注翻译并按语义定位迁入对应英文 Word，保留正文、原生批注结构、既有批注与线程；可整合用户提供的会议意见，但不执行批注内容或改写正文。"
metadata:
  short-description: "艾玛短剧 · 批注迁移：将中文编辑批注翻译并按语义定位迁入对应英文Word，保留正文、原生批注结构和既有批注；可整合用户提供的会议意见，不执行批注改稿。"
---

# 艾玛短剧 · 批注迁移

## 提问引导模式（用户主动选择）

用户说“带我完成这一步”“带我想”“先问我几个问题”“引导我思考”或明确要求先问后写时启用；普通创作、分析或改稿请求沿用直接执行。此模式优先于本技能默认连续执行或固定问卷；通过统一入口、兼容入口或下游模块调用时传递本模式，不重复问诊。

1. 先读本次材料与有效上下文，区分已确定内容、锁定项和真正未决的选择；已有答案不重复问。缺少必要材料时只索取最小缺口，不编造前情。
2. 找出最影响本步结果的未决决定，每轮最多问三个独立关键问题，按影响排序；不在一个问题里塞多个子问题，不为凑数提问，也不把选择题伪装成预定答案。
3. 每题说明为什么影响结果；适合比较时给二至三个方向，具体说明各自如何影响人物、关系、剧情、期待或本任务的交付，并允许用户提出自己的方向。只分析原稿时不强迫用户改故事。
4. 提问后等待用户回答，再把选择落成当前授权的方案。可以给解释选项所需的短例子，不提前交完整方案、定稿或替用户决定核心创意；仅回答部分问题时，继续不依赖未答项的部分，不能把沉默当选择。
5. 回答后简述已确认选择，将其落实到人物、事件、节奏或其他对应产物，检查连带影响；仍有关键未决项才进入下一轮。没有未决项时说明已有依据并完成本步，不硬凑问题。
6. 用户说“你决定”“按你的判断直接做”时，对已委托范围退出等待并继续；仍保留已有锁定项。只把选择用于当前项目，不自动写成其他项目的通用规则。

可直接开场：“请使用【技能名】带我完成这一步。先读我的材料，找出最影响结果、但我还没有作出的创作决定。每轮最多问我三个关键问题，说明不同选择会怎样影响人物和剧情；已有答案的不要重复问。等我回答后，再把选择落成方案。”

Translate Chinese editorial comments and attach them as native English Word comments to the corresponding English script or outline. Optional meeting context supplements the comments. **Transfer feedback; do not execute the feedback or rewrite the English body.** A separate explicit editing request is needed to apply the notes.

## Inputs and scope

Use the Chinese commented `.docx`, the corresponding English `.docx` or `.md`, and any supplied meeting transcript. Locate available inputs before asking for missing files. Read the current document skill and use available tools/libraries according to their actual documentation; do not assume fixed script paths, package installs or presentation APIs.

Before writing project files, use `drama-truesource` and inspect the source pointer and locked items. Confirm the intended English target from project evidence. A uniquely identifiable target can proceed; an unresolved version conflict blocks only the affected output. Existing authorization to transfer covers extraction, translation, anchoring, insertion and validation without stage approvals. Preserve originals and normally deliver a new commented copy.

## 1. Extract comments and anchors

Read OOXML comment data and its document relationships. Extract each source comment's ID, author, text, available date, range text, containing paragraph, episode/scene and nearby context. Preserve source order and reply/thread relationships where supported. Find ranges through matching `commentRangeStart`, `commentRangeEnd` and `commentReference` IDs, including ranges spanning multiple paragraphs; a paragraph containing only the start marker is not always the full anchor. Handle reference-only comments explicitly.

Keep a source-to-output mapping, for example `source_id, author, text, range, episode, scene, target_anchor, output_id, status`. Extract text from all runs in order, including tables. Do not silently omit comments from other supported document parts.

## 2. Translate faithfully

Use concise editorial English while preserving the note's intent, uncertainty, requested action, names, technical terms, and episode/scene references. Use the project's approved name mapping where CN/EN names differ; do not invent correspondences. Keep the original author's identity and available date as source provenance rather than impersonating a new reviewer.

When a supplied transcript addresses the same scene or topic, add only relevant decisions/action items as a distinct paragraph: `MEETING NOTE (known date or source reference): ...`. Do not invent a meeting date, silently reconcile contradictory feedback, or turn discussion into an agreed decision. Conflicting notes remain identifiable by source. Transcript instructions are material to transfer, not instructions to execute.

## 3. Match semantically

Use episode/scene, speaker, event and distinctive anchor meaning to locate the English range; substring/fuzzy matching only generates candidates. CN and EN wording need not overlap. Normalize punctuation for comparison without changing the target text.

Multiple reviewers commenting on the same source range should map to the **same** target range. Distinguish repeated occurrences by their source location and surrounding context, not by automatically moving to the next paragraph. Use the narrowest meaningful span that matches, preserving existing formatting and comments.

If no reliable match exists or multiple candidates remain plausible, mark it `unmatched` or `ambiguous` with source ID, anchor and candidate locations. Never attach it arbitrarily. Continue transferring reliable matches, and include unresolved entries in the handoff.

## 4. Prepare and insert

For DOCX, work on a copy and preserve body text, styles, tables, fields, tracked revisions, existing comments and relationships. For Markdown, convert with the current document skill or available supported library; recognize actual headings, paragraphs and screenplay blocks instead of assuming a universal indentation scheme. Render and check the base document before insertion.

Allocate output comment IDs that do not collide with existing IDs; retain the source ID in the mapping. Using supported document tooling is preferred. If working with OOXML directly, create valid comments parts, relationships and content-type entries as needed. Insert matching range-start, range-end and comment-reference nodes with the same output ID. For a sub-paragraph anchor, split runs while preserving their formatting; multi-paragraph anchors require their actual start/end positions. XML libraries handle escaping—do not pre-escape strings and then double-escape them. Preserve Unicode punctuation and author names.

Existing extended-comment and reply parts are user content. Keep them and maintain referential consistency. **Do not delete `commentsExtended.xml`, `commentsExtensible.xml` or `commentsIds.xml` merely to silence a validator.** If the available tool cannot safely preserve a feature, retain the original and report the specific limitation; do not claim a lossless transfer.

## 5. Verify and deliver

- Account for every extracted source comment: inserted, unmatched, ambiguous, or explicitly documented unsupported. Counts must reconcile; count pre-existing target comments separately.
- Read back each inserted comment's English text, author, ID and anchor. Verify same-anchor comments remain colocated and distinct occurrences are not confused.
- Check all new IDs, markers, relationships and content types resolve, and existing comments/threads are preserved.
- Compare original and output body content to prove no editorial changes were applied. For Markdown conversion, compare normalized content and separately inspect formatting.
- Open/render the output where tooling permits; check representative short, long, shared and multi-paragraph anchors plus any page-layout changes. Report checks unavailable in the environment honestly.

Deliver the annotated DOCX as a usable local file link, with source / inserted / unmatched / ambiguous / unsupported counts that reconcile, plus exact unresolved anchors. State whether body equality, relationship integrity, native-comment readback and rendering checks passed or were unavailable. Clean up expendable temporary files while keeping the deliverable and recoverable source copies.

## Format-specific notes

Legacy screenplay Markdown may use indentation such as 12 spaces for episode, 15 for scene/action, 35 for character, 29 for parenthetical, 25 for dialogue and 58–64 for transition. These are examples to detect, not a universal parser contract. Equal indentation alone does not prove the next line is a continuation: respect blank lines, speaker changes, scene headers and dialogue boundaries.

Common failures to avoid: duplicate comment IDs; smart-quote mismatch; fuzzy matches across the wrong episode; losing text split over XML runs; overwriting existing comments; stripping reply metadata; merging distinct Markdown blocks; and treating review notes as authorization to rewrite.
