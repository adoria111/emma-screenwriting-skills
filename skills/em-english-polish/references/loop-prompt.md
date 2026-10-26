# Localization Loop — Copy-Ready Prompt, Tell-Catalog, Templates

Load this when launching a loop or writing the standing instruction for another host (Codex). The copy-ready block is self-contained: it carries its own procedure and stop condition, so the target host does not need this skill loaded.

---

## 1. Copy-Ready Loop Prompt

复制后把首句写成实际目标文件与集场范围，并注明已决定的输出方式。这是任务提示，不是宿主专用调度命令。

```text
任务：打磨指定文件和集场中已经本地化的英文对白，使其忠实、自然、可演，符合项目人物声音。目标文件、集场范围和输出方式以随本提示提供的具体信息为准。

先核对 drama-truesource、_真源指针.md、锁定项和批准的本地化设定。底稿唯一可判定时建立缺失指针并继续；未决真源冲突仅暂停相关写入。已有授权覆盖全部指定范围，不每批确认。

只改英文对白，中文、动作线、场景头、音效和锁定句保持不变。以批准的改编及中文源意核对；若仅有英文，改善自然度并注明未验证对中文忠实度。不要将已批准的改编回退成直译。

按集场检查：
1. 事实与意图：关系、时间、事件、选择、威胁、欲望、道具、因果和揭示时机。
2. 口语可演性：依人物身份使用缩写、停顿与短句，不为字数配额删信息。
3. 翻译腔：查看语义和语域后处理称谓、成语直译、套话与过度解释，例句不机械替换。
4. 人物声音和跨集一致：称呼、术语、回忆复述、钩子与信息差。

意义不变或根据权威源稿纠正误译时直接修改；需要动故事、锁定项或无法裁决的设定冲突时保留该处并提出精确问题，继续其他内容。

短片段直接完成；跨轮或全本任务才维护进度和必要变更日志，记录已覆盖集场与未决项。

完成所有请求单位后检查保护内容前后一致、中英对应、跨集一致与实际分行渲染。同一角色未被动作、他人回应或声音模式切换打断的连续台词，整链合为一个对白段落，只保留一次人物名与归纳后的主导提示；不同语气词本身不构成拆分理由。段内可用多个句号，不改台词信息与顺序，交付前复扫同人连续链。仅改英文任务须保留中文与动作，不破坏中英映射。所有实质问题已处理或明确列出后结束；仅对新修改、检查失败或未决问题追加复查，不追求零新措辞、固定改动数或主观高分。

交付完整修改稿，简述覆盖范围、验证结果与未决项，保留可恢复备份。无新输出约定时用新版本，不自动晋升真源。
```

---

## 2. Native Tell-Catalog (the "c. native体检" detail)

These are possible translation artifacts. A form may be correct for a particular character or register. Use them as contextual diagnostic candidates, not universal mistakes.

> 忠实口语化教条（只改说法不改意义）+ 高AI短语速换表（I never imagined→I had no idea、Would you believe→What if I told you、For the future of this family→For the good of this family、something is wrong→something's off、I need answers→I have to find out…）+ QC 校验方法（保护内容比对 / 语义复核 / 全范围覆盖 / 口语节拍检查）+ 版本输出纪律：见 [faithful-colloquial-and-qc.md](faithful-colloquial-and-qc.md)。

| Tell | 症状 | ❌ → ✅ |
| --- | --- | --- |
| 序号排称谓 | 用数字排兄弟姐妹（大哥二哥三弟） | `my second brother` → `the middle one` |
| 成语/俗语直译 | 先确认隐含意图再换表达 | 笑面虎：保留“笑里藏刀”的危险性，不能换成只表示自鸣得意的漂亮男孩 |
| 点破已可见情绪 | 把动作已表达的情绪又说出来 | `losing your mind with jealousy` → 删 `with jealousy` |
| 华语敬称/身份词 | 依据年代、权力关系和项目命名选择 | 现代情境可用获准姓名或 Mr. + 姓；设定确需时保留特殊敬称 |
| 过度具体的中式表达 | 中文的具体名词直搬 | 腿一定累坏了 `Her legs must be exhausted` → `She must be worn out` |
| 书面/档案腔 | 像说明文不像人说话 | `They have unusual customs` → `They've got their own ways` |
| 中式句式结构 | 直搬中文语序/反问结构 | `Aren't you afraid I'm a monster?` → `You're not scared I'm a monster?` |
| 逐字镜像翻译 | 完全照搬中文结构 | `Search for me! She must be nearby!` → `She's close. Find her!` |
| 破折号 | 检查是否服务打断/表演 | 按项目标点规范处理，不一律删除 |
| 翻译腔套话 | you have no qualification / what kind of person are you / you actually dare | 换成地道说法或删 |
| 定型CP词错位 | 狼人 `mate` 在揭秘前就用上 | 揭秘前 伴侣/丈夫 `mate` → `husband` / `marry`（揭秘后才用 mate） |
| 高AI套话直换 | I never imagined / Would you believe / something is wrong / I need answers… | 见 faithful-colloquial-and-qc.md §1 速换表 |

World terms to KEEP (do not "naturalize" away): Alpha King, fated Luna, wolfsbane, House/family proper names, and any project-specific 世界观专名 set by the truesource.

---

## 3. Optional Long-Task Templates

Use only when task size or continuity benefits from saved progress; a short passage needs no separate files.

### `_本地化优化进度.md`

记录项目名、目标文件、备份、迭代单位，以及每个实际集场的状态、本轮改动与遗留；最后单列跨全本一致性检查。不预建虚构集号或空任务。

### `_本地化优化日志.md`

仅在任务规模需要时记录实际集场、人物、旧句、新句与修改理由；没有发生的改动不写空行占位。

---

## 4. Apply vs preserve-and-ask

- Apply authorized wording improvements and corrections against the authoritative source. Preserve meaning, intensity and character voice; record changes as useful for task scale.
- Preserve a line and ask only if its resolution requires a new story decision, locked-item override or unresolved source choice. Continue the unaffected scope.
- Already authorized changes do not need repeated approval. Do not force an edit on every line or a fixed proportion of the text.
