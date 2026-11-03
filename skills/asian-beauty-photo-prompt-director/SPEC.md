# Asian Beauty Photo Prompt Director Specification

## Intent

This skill turns user requests into stable, tasteful AI image prompts for Asian-aesthetic female portrait photography across Midjourney, SDXL, Flux, GPT Image, 豆包, 即梦, and ComfyUI.

It preserves the source prompt's strongest behavior: avoiding middle-aged drift, avoiding childlike framing, rewriting risky sensual wording, and producing copy-ready platform formats.

## Scope

In scope:
- Asian-aesthetic female portrait prompt generation
- Commercial portrait, fashion editorial, selfie, cosplay, cyberpunk, hanfu, and refined boudoir-style prompts
- Platform-specific output contracts
- Risk-word rewriting and prompt repair modes
- Eight-dimensional visual direction and batches of individually copy-ready prompts

Out of scope:
- Explicit sexual content, nudity, minors, childlike sexual framing, or private-part focus
- Generating images directly
- Celebrity impersonation or identity cloning
- Legal, medical, or body-evaluation advice

## Users And Trigger Context

- Primary users: creators who want copy-ready prompts for image models.
- Common requests: 亚洲美女照片提示词, Midjourney 美女人像, SDXL 亚洲脸, 即梦写真提示词, ComfyUI 人像参数, fix 生成太老, fix 脸崩.
- Should not trigger for: general photography education, code-only image pipelines, image editing without prompt generation, or unrelated beauty advice.

## Runtime Contract

- Required first actions: parse shortcut commands, choose platform/style/content level/fix mode, rewrite risky input, then generate.
- Required outputs: normal generation or `/fix` contract from `SKILL.md`, or batch contract from `references/visual-framework.md`.
- Non-negotiable constraints: adult non-childlike subject, no concrete age numbers in final prompts, no middle-aged trigger words in final prompts, no explicit sexual content.
- Expected bundled files loaded at runtime: platform formats, risk rewrites, style expansions, fix modes, examples only when needed.

## Source And Evidence Model

Authoritative sources:
- User-provided pasted prompt specification.
- Existing local skill conventions in `female-portrait-prompt-generator`.
- `skill-writer` authoring workflow.

Useful improvement sources:
- positive examples: high-quality outputs that render stable face/skin/pose
- negative examples: rejected prompts, too-old outputs, too-young outputs, face/hand failures
- validation results: structural checks and manual output-contract review

Data that must not be stored:
- private images or identity references
- secrets
- customer-identifying material not needed for prompt reproduction

## Reference Architecture

- `SKILL.md` contains activation, safety rules, command routing, default behavior, output contracts, and checklist.
- `references/` contains focused runtime lookup leaves for platform formats, risk rewrites, style expansions, fix modes, and examples.
- `scripts/` contains no files.
- `assets/` contains no files.

## Validation

- Lightweight validation: frontmatter, name-directory match, referenced files exist.
- Deeper validation: run example requests through the skill and confirm no forbidden final-prompt terms remain.
- Holdout examples: rejected prompt repair, too-old repair, too-childlike repair, and platform-specific generation.
- Acceptance gates: copy-ready output, correct platform shape, safe wording, no age numbers.

## Known Limitations

- Prompt behavior still varies by model and checkpoint.
- Some platforms may reject wording that is safe in another model; use `/safe` or `/fix 被拒` to reduce sensitivity.
- The skill cannot guarantee face identity consistency without model-specific reference-image workflows.
- Lens terms and negative prompts are creative controls, not guaranteed model behavior; support varies by model.

## Maintenance Notes

- Update `SKILL.md` when triggers, safety boundaries, command priority, or output contracts change.
- Update focused references when platform parameters, risk rewrites, styles, or fix recipes change.
- Update `SOURCES.md` when adding new source material, examples, or validation findings.
