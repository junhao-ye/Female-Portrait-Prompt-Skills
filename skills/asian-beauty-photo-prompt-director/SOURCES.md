# Sources And Decisions

## Source Inventory

| Source | Trust | Confidence | Contribution | Usage constraints |
|---|---|---:|---|---|
| User-provided pasted prompt specification | user-provided upstream prompt | high | core command system, safety rules, visual control phrases, platform formats, risk rewrites, examples | adapted and condensed |
| `female-portrait-prompt-generator` | local prior art | high | skill conventions, safety framing, output discipline | used for style and scope comparison only |
| `skill-writer` | local authoring workflow | high | synthesis, authoring, reference-backed layout, validation expectations | followed for structure |
| User's eight-dimension framework, chat message 2026-11-03 | user-supplied creative direction | high for intended preferences; unverified for performance claims | styling, textiles, candid expression, optics, light, background, restraint, negatives | adapt age example to existing no-numeric-age rule; do not promise outcomes |

## Synthesis Decisions

| Decision | Status | Rationale |
|---|---|---|
| Create new skill instead of overwriting `female-portrait-prompt-generator` | adopted | new source emphasizes multi-platform Asian-aesthetic prompt directing and repair modes, while existing skill focuses parameter locking for tasteful portraits |
| Skill class: generic authoring/generator skill | adopted | it generates prompts and applies policy/routing rather than integrating an API |
| Primary execution shape: reference-backed expert | adopted | platform formats, risk rewrites, style expansions, and fix modes are optional branches that should not overload `SKILL.md` |
| Secondary shape: fixed command routing | adopted | shortcut commands require deterministic priority |
| Provider-specific mechanics | rejected | no Claude/Codex-specific runtime mechanics are needed |
| Scripts | rejected | no fragile deterministic parsing or automation is required |

## Source Adaptation Notes

- Source intent: produce visually attractive, Asian-aesthetic, platform-friendly female portrait prompts with strong control against too-old or too-childlike outputs.
- Local target behavior: a reusable skill that parses user shortcuts, rewrites risky wording, emits the right platform format, and runs a final safety checklist.
- Fidelity boundary: preserve command names, platform coverage, risk rewrites, fix modes, and visual-layer control language.
- Local replacements: condensed long prose into routing tables, focused references, and output contracts.
- Omitted material: repeated explanatory prose and duplicate examples were reduced to one happy path, one robust rewrite, and one anti-pattern correction.

## Coverage Matrix

| Dimension | Status |
|---|---|
| Happy-path generation | covered in `references/examples.md` |
| Robust unsafe-word handling | covered in `references/risk-rewrites.md` and examples |
| Anti-pattern correction | covered in `references/examples.md` |
| Platform-specific formats | covered in `references/platform-formats.md` |
| Fix modes | covered in `references/fix-modes.md` |
| Trigger precision | covered in `SKILL.md` description and should/should-not trigger review |
| Structural validation | pending local validator run after install |

## Description Optimization

Should trigger:
- `亚洲美女照片提示词`
- `/mj /cyber /tasteful 霓虹街头女主`
- `帮我写 SDXL 亚洲女性商业写真提示词`
- `/fix 生成太老`
- `ComfyUI 汉服美女人像参数`

Should not trigger:
- `帮我修一张真实照片`
- `介绍人像摄影布光`
- `写一个图片生成 API 的代码`
- `分析亚洲审美市场`
- `给我真人整形建议`

Final description includes Chinese trigger phrases, platform names, style names, and repair phrases while excluding broad unrelated photography or beauty advice.

## Retrieval Stopping Rationale

The user supplied a complete upstream specification, local prior art exists, and no external provider-specific mechanics are used. Additional web retrieval is currently low-yield.

## Open Gaps

- Add persistent holdout examples later if real failure cases are collected.

## 2026-11-03 Update

- Added `references/visual-framework.md` to operationalize all eight dimensions and provide a copy-ready batch contract.
- Batch workflow is an inferred practical implementation: the user supplied visual principles but no concrete batch algorithm.
- Visual quality and negative prompt behavior remain model-dependent and have not been evaluated through generated images.
