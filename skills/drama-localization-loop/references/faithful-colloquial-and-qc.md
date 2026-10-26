# Faithful Colloquialization + QC — Localization Reference

Distilled from a live loop session (Varkas Brothers E01–E09, 2026-06, client note: 英文台词"还是有点人机感/不够口语/不像美国真人"). Load this **with** the tell-catalog whenever a client says the English still reads translated. It covers the one governing rule, a ready phrase-swap dictionary, genre false-friends, profanity calibration, the QC verification recipe, version/output discipline, and macOS tooling.

---

## 0. The rule that governs everything

**忠实本意的口语化重写 ≠ 自由改写.** You may change wording, word order, and sentence length. You may NOT change meaning.

Before rewriting a line, lock its invariants: **人物关系 · 时间 · 事件 · 选择 · 威胁 · 欲望 · 道具 · 因果**. After rewriting, reverse-check against the Chinese: if the English now carries a judgment, motive, result, or image the Chinese doesn't, **delete it.**

- ❌ `Yesterday, Mom dropped a bomb... They were about to ruin me.` — adds "dropped a bomb" + "ruin me": a result/judgment not in 中文.
- ✅ `The day before the wedding, I found out Mom was getting married again. I had no idea I'd get tangled up with my three new stepbrothers...` — same facts, real mouth-feel.

"强刺激版" is for **tone only, never for plot**: lines may get shorter, meaner, more temperamental — but never gain a `ruin me` / `destroy me`-type claim the source lacks.

---

## 1. Candidate phrase checks (context decides)

These are contextual alternatives, not proof of AI authorship or a blacklist. Several examples differ in tense or intent: “remarried” is completed, “was getting married” may be prospective; “I need answers” may express a demand. Preserve those distinctions and keep the original if it suits the scene.

| ❌ AI-tell | ✅ 真人 |
|---|---|
| I never imagined / I never thought | I had no idea |
| Would you believe…? | What if I told you…? |
| For the future of this family | For the good of this family / For this family's sake |
| Something is wrong | Something's off (about them) |
| I need answers | I have to find out / I need to know |
| my mother remarried | Mom was getting married again |
| You shouldn't be here | You're not supposed to be here |
| I understand (clipped ack) | Got it |
| It was just a hunting dog | It was just one of the hounds |
| I can walk myself | I can find my own way |
| Could you dress decently for once? | Could you look decent for one day? |

Treat new examples as evidence to examine, not universal substitutions.

---

## 2. Genre false-friends (werewolf / fated-mate dramas)

- **"mate"** — use only after the supernatural bond is on the table. Before the reveal, 伴侣 / 丈夫 = `husband` / `marry`, NOT `mate`. (`mate` pre-loads the romance and confuses a reader who, like the heroine, doesn't yet know they're wolves.)
- **Keep true world-terms** (Alpha King, fated Luna, wolfsbane, House/family proper names). Do not "naturalize" them away.

---

## 3. Profanity calibration

- Swear **only** where the Chinese intensity already justifies it: 震惊 / 羞辱 / 威胁 / 失控 / 崩溃. (damn / hell / bastard usually suffice; reserve F-words for genuine rage and the project's register.)
- Never bolt profanity onto a plain information line.
- A raunchier reference script (e.g. a BL thriller) is a model for **spoken density and realness, NOT for profanity level.** Copy the cadence, not the crudeness.

---

## 4. QC recipe — verify content and scope

1. **Protected text unchanged:** extract Chinese source, action lines, headings and locked lines from before/after versions and compare by episode/scene. A generic diff may include adjacent unchanged text or miss structured document content; inspect actual protected-field changes.
2. **Contextual phrase review:** inspect candidates from §1 and retain justified wording. Zero hits is not a quality criterion.
3. **Complete coverage:** account for all requested episodes and dialogue. If a requested change quota would force worse or unfaithful edits, report this rather than manufacturing changes; zero edits can be valid after review.
4. **Long-line review:** inspect breath, information load and dramatic rhythm. Length alone is not an error; preserve long lines that serve voice and meaning.
5. **Separate rendered lines:** use blank lines or valid hard breaks in Markdown, separate paragraphs/breaks in DOCX, and inspect actual output.

Anchor edits with episode/scene, speaker and English text; verify uniqueness and compare protected fields afterward. English-only replacement does not alone prove source safety.

---

## 5. Version + output discipline (the trap this came from)

- **Newest timestamp ≠ newest content.** A `.docx` is often just an export of the `.md`. Extract and diff before deciding what's canonical:
  `textutil -convert txt "x.docx" -output _tmp.txt` → compare to the md.
  (This session: client said "the 6.15 docx is latest", but its English was byte-identical to the 6.12 md.)
- Read project evidence and the source pointer; establish a missing pointer when the source is uniquely identifiable. Ask only for unresolved authority conflicts and continue unaffected work.
- Honor the authorized output mode; default to a recoverable new version if unspecified, with a pre-edit backup. Do not automatically restore or overwrite files that may contain other work.

---

## 6. Tooling

Use the current document skill and available tools for Word output. On macOS, `textutil` can extract plain text when available, but plain text loses comments and layout; it is insufficient to verify DOCX fidelity. Do not assume an operating system or conversion dependency.
