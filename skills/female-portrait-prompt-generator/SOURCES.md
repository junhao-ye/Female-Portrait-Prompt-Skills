# Sources And Synthesis Notes

## Source Inventory

| Source | Trust | Contribution | Usage Constraints |
|---|---|---|---|
| User creation request in current thread | High | Domain rules, parameter schema, output contract, visual direction | Adapted into runtime instructions; explicit unsafe boundaries tightened |
| `skill-writer/SKILL.md` and references | High | Skill structure, synthesis, authoring, description, validation expectations | Local skill authoring guidance |

## Synthesis Decisions

| Decision | Status | Rationale |
|---|---|---|
| Skill class: generic generator | adopted | The skill generates prompts from parameters rather than integrating an external API or running a workflow with side effects. |
| Primary shape: inline-guidance | adopted | One coherent policy and output contract handles most invocations. |
| Secondary shape: argument-driven | adopted | The skill is normally invoked with explicit user parameters and needs defined empty-input behavior. |
| Add `SPEC.md` | adopted | New skill with clear runtime contract and safety boundaries. |
| Add `references/examples.md` | adopted | Generator skills require happy-path, robust, and anti-pattern examples. |
| Add scripts | rejected | No deterministic parser or automation is necessary for the first version. |

## Coverage Matrix

| Coverage Area | Status |
|---|---|
| parameter locking | covered |
| auto-completion behavior | covered |
| facial direction expansion | covered |
| body-line and pose limits | covered |
| safety constraints | covered |
| required output sections | covered |
| examples | covered in `references/examples.md` |

## Source Adaptation Notes

- Source intent: generate complete AI female portrait prompts while strictly preserving user-selected parameters.
- Local target: reusable Codex skill with mandatory lock review, tasteful adult portrait safety rules, and stable output sections.
- Fidelity boundary: preserve parameter locking, visual direction, option set, output requirements, and style/face harmonization.
- Local replacements: converted long prompt prose into tables, checklists, runtime workflow, and examples.
- Omitted material: no implementation-specific image model settings beyond general prompt keywords; no scripts.

## Trigger Optimization Notes

Should trigger:
- 根据这些参数生成女性写真提示词
- 清冷私房 AI 图片提示词
- 低饱和室内女性人像 prompt
- 帮我锁定参数生成写真提示词

Should not trigger:
- 评价这张照片好不好看
- 给我生成一张儿童写真
- 写一篇关于女性主义的文章
- 做一个普通风景图提示词

## Open Gaps

- No model-specific syntax variants yet for Midjourney, Stable Diffusion, DALL-E, or Flux.
- No automated validator for output section completeness.
