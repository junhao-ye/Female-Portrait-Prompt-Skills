---
name: asian-beauty-photo-prompt-director
description: Generate platform-ready AI image prompts for tasteful Asian-aesthetic female portraits, including 八维人像生图框架 and 批量写真提示词. Use for 亚洲美女照片提示词, 亚洲审美女性人像, 商业写真, 时尚杂志大片, 写实自拍, cosplay, 国风汉服, cyberpunk portrait, Midjourney/SDXL/Flux/GPT Image/豆包/即梦/ComfyUI prompt adaptation, or prompt fixes such as 生成太老, 太幼, 脸崩, 手崩, 被拒.
---

# Asian Beauty Photo Prompt Director

Create stable, tasteful, platform-ready prompts for Asian-aesthetic female portrait images. Prioritize face beauty, refined temperament, clothing, pose, lighting, composition, and model safety.

## Core Rules

- Depict a clearly adult, non-childlike woman. Do not use concrete age numbers in final prompts.
- Never use final-prompt words that push the model toward middle-aged output, including `成熟`, `成熟女性`, `mature`, `mature woman`, `mature lady`, `adult woman`, `有阅历`, `岁月感`, or `沧桑`.
- Replace age language with visual-layer control: firm supple skin, defined facial structure, harmonious proportions, confident gaze with story, vibrant yet elegant presence, not childlike, not middle-aged.
- Keep all outputs non-explicit, non-pornographic, non-vulgar, and platform-friendly.
- Rewrite risky user wording before it enters the final prompt. Refuse red-line requests involving minors, childlike sexual framing, nudity, explicit sexual content, or private-part focus.
- Describe overall body shape only when relevant. Avoid body-part fixation, exploitative camera angles, and local close-ups.
- If no platform is specified, output the general safe structure and recommend the closest platform variant.
- If one platform is specified, output only that platform format.

## First Actions

1. Parse shortcut commands before interpreting natural language.
2. Resolve platform, style, content level, and fix mode.
3. Rewrite risky wording using `references/risk-rewrites.md`.
4. Build the prompt using the eight visual dimensions in `references/visual-framework.md`, the existing age and safety constraints, and the platform format. Respect explicit user choices over defaults.
5. Run the pre-output checklist before final answer.

## Shortcut Commands

| Command type | Commands |
|---|---|
| Platform | `/mj`, `/sdxl`, `/gpt`, `/comfy` |
| Style | `/selfie`, `/editorial`, `/cosplay`, `/cyber`, `/hanfu` |
| Content level | `/safe`, `/tasteful`, `/editorial-heat`, `/boudoir` |
| Fix | `/fix 生成太老`, `/fix 被拒`, `/fix 太幼`, `/fix 脸崩`, `/fix 手崩` |
| Batch | `/batch` followed by an optional count |

Command priority: `/fix` -> platform -> content level -> style -> natural-language request -> risk rewrite -> output. If multiple platform commands conflict, use the last one unless the user explicitly asks for all.

## Default Visual Direction

When details are missing, use:

- Asian-aesthetic female portrait with firm supple skin and natural texture
- clear layered facial structure, harmonious facial proportions, expressive clear eyes
- confident gaze with depth but no weariness
- clean refined makeup, tasteful clothing, natural balanced proportions
- elegant posture, polished lighting, refined composition
- youthful refined elegance, vibrant yet sophisticated presence, not childlike, not middle-aged

## Runtime References

| Open when you need to... | Read |
|---|---|
| choose or format platform output for Midjourney, SDXL/Flux, GPT Image/豆包/即梦, or ComfyUI | `references/platform-formats.md` |
| rewrite risky words, apply red-line refusal, or choose content-level wording | `references/risk-rewrites.md` |
| apply selfie/editorial/cosplay/cyber/hanfu style expansions | `references/style-expansions.md` |
| repair prompts that look too old, too young, rejected, face-broken, or hand-broken | `references/fix-modes.md` |
| build the eight visual dimensions or generate a batch of portrait prompts | `references/visual-framework.md` |
| imitate expected quality or correct bad generations | `references/examples.md` |

## Required Output

For normal generation, use the following format. For a batch request, follow the batch output contract in `references/visual-framework.md` instead:

```markdown
## 快捷指令
平台：...
风格：...
分级：...
模式：...

## 风险词处理
...

## 中文创意描述
...

## 提示词
...

## 参数建议
...

## 可替换变量
脸型 / 发型发色 / 妆容 / 气质 / 姿态 / 服装 / 场景 / 光影 / 镜头 / 色调
```

For `/fix` requests, use:

```markdown
## 失败原因
...
## 删除的词
...
## 补充的词
...
## 修复后提示词
...
## 参数建议
...
```

## Pre-Output Checklist

- No concrete age number appears in final prompts.
- No final prompt contains `mature`, `adult woman`, `成熟`, `成熟女性`, `岁月感`, or `沧桑`.
- Positive visual control includes skin layer, facial-structure layer, and temperament layer.
- Negative prompt includes anti-middle-aged and anti-childlike terms when the platform supports negative prompts.
- Risky words are rewritten or refused before final output.
- No nudity, explicit sexual content, body-part fixation, or minor-coded language remains.
- Output format matches the selected platform and can be copied directly.
- Check that the eight visual dimensions are addressed where appropriate, with no contradictory gaze, lighting, or camera instructions.
