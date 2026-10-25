# Female Portrait Prompt Generator Specification

## Intent

This skill turns user-selected portrait parameters into a complete, stable AI image generation prompt for tasteful adult female portrait photography. It preserves explicitly selected parameters through a mandatory parameter-lock review, then expands only blank or `自动` fields.

## Scope

In scope:
- adult East Asian female portrait prompt generation
- cool, restrained, low-saturation indoor portrait aesthetics
- tasteful light boudoir mood, soft sensuality, and body-line emphasis
- parameter locking, auto completion, conflict harmonization, negative prompt generation

Out of scope:
- explicit sexual content, nudity, fetish framing, pornographic or vulgar posing
- underage, childlike, teen, school-uniform, or ambiguous-age imagery
- direct image generation or image editing
- celebrity likeness prompts or identity cloning

## Users And Trigger Context

- Primary users: creators who need stable Chinese prompts for AI portrait generation.
- Common user requests: 女性写真提示词, 清冷私房写真提示词, 低饱和室内人像, 根据参数生成 AI 图片提示词.
- Should not trigger for: general photography critique, non-portrait image prompts, explicit sexual requests, or unrelated skill authoring.

## Runtime Contract

- Required first actions: identify locked parameters, identify `自动` or blank fields, reject or replace unsafe parameters only where needed.
- Required outputs: parameter lock review, complete prompt, automatic completion list, visual hooks, negative restrictions.
- Non-negotiable constraints: locked safe parameters must be preserved; only automatic or blank fields may be auto-matched; output must be adult, tasteful, non-explicit.
- Expected bundled files loaded at runtime: `references/examples.md` only when examples are needed.

## Source And Evidence Model

Authoritative sources:
- User-provided prompt specification in the creation request.
- Local skill-writer guidance for skill structure and validation.

Useful improvement sources:
- positive examples: high-quality outputs that preserve locked parameters.
- negative examples: outputs that swap locked fields, over-sexualize the subject, produce generic AI faces, or omit lock review.
- validation results: structural skill validation and manual prompt-quality review.

Data that must not be stored:
- private user images
- personal identity details
- private model credentials or platform tokens

## Reference Architecture

- `SKILL.md` contains runtime workflow, parameter schema, safety rules, output contract, and default expansions.
- `references/examples.md` contains happy-path, robust variant, and anti-pattern examples.
- `scripts/` contains no files.
- `assets/` contains no files.

## Validation

- Lightweight validation: run the skill structural validator.
- Deeper validation: test one happy path, one all-auto path, and one unsafe parameter correction.
- Holdout examples: requests with locked style/face tension and strong line emphasis.
- Acceptance gates: no locked safe parameter is changed; no unsafe sexual or underage output; all five required output sections appear.

## Known Limitations

- The skill produces text prompts only; final model behavior may vary by image-generation system.
- It cannot guarantee exact facial identity or body shape across different image models.
- Strong body-line emphasis may need stricter negative prompts depending on the target model.

## Maintenance Notes

- Update `SKILL.md` when parameter options, safety boundaries, or output sections change.
- Update `SOURCES.md` when adding new source material or changing synthesis decisions.
- Update `references/examples.md` when recurring output mistakes appear.
