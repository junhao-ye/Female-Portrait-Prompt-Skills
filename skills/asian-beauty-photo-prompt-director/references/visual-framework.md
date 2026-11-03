# Eight-Dimensional Portrait Framework

Apply the dimensions below to each prompt when relevant. Preserve explicit user specifications; fill only missing details. Use the skill's existing safety and no-numeric-age rules even when adapting examples with ages. Avoid treating any styling choice as a universal definition of beauty.

| Dimension | Direct the prompt with | Example vocabulary |
|---|---|---|
| 1. Persona and tone | Specific mood, styling, and photographic context, instead of generic beauty labels | refined East Asian portrait, relaxed elegance, editorial fashion portrait |
| 2. Materials and drape | Fabric, cut, weight, folds and believable texture | raw silk, fitted merino knit, tailored silhouette, natural fabric drape |
| 3. Expression and moment | A readable micro-expression and a coherent interaction with the camera | candid moment, soft knowing glance, caught mid-reaction |
| 4. Camera and optics | Camera viewpoint, lens, depth of field and grain when useful | 85mm portrait lens, f/1.8, shallow depth of field, subtle film grain |
| 5. Directional lighting and skin | Light direction and intensity, natural skin details | soft diffuse side light, gentle rim light, visible pores, natural highlights |
| 6. Background and depth | A recognizable setting with controlled background detail | quiet morning cafe, subdued background, gentle optical bokeh |
| 7. Restraint and proportion | Natural makeup, believable proportions, and intentional styling | understated elegance, natural proportions, minimal retouching |
| 8. Quality exclusions | Only exclusions relevant to observed problems and supported by the chosen model | plastic skin, doll-like face, extra limbs, CGI appearance, oversmoothing |

Make camera direction coherent: a subject looking toward the lens should not also be described as unaware of it. Specify natural film grain or bokeh only when suitable. Lens descriptions are visual guidance, not a guarantee of optical or anatomical accuracy. Use positive instructions for models without negative prompt fields; do not assume all platforms support identical negative syntax or parameters.

## Batch Workflow

Trigger when the user asks for multiple variants or uses `/batch`. Use their requested count; if none is given, produce 4. Do not invent a request to generate actual image files: this skill produces prompts.

1. Identify the selected platform and user-locked subject, clothing, identity references, aspect ratio, and other fixed requirements. Do not promise a consistent identity from prompt text alone.
2. Choose two or three variable dimensions appropriate to the request, such as expression, location, lighting, wardrobe or framing. Keep fixed dimensions unchanged and make variants meaningfully distinct. Avoid a full combinatorial explosion unless requested.
3. Draft each variant as a complete standalone prompt. Keep each variant internally consistent and apply the existing platform and safety rules. Adapt negatives and parameters only where supported; note uncertain settings as suggestions rather than claims.
4. Present a short fixed/variable summary and a numbered set of individually copy-ready prompts. For supported negative fields, provide the negative prompt per item or one explicitly shared copy-ready block; list applicable parameters once if common. Include per-item differences where necessary.
5. Review count, locked attributes, distinctness, platform syntax, contradictions, and negative-prompt support. No quality or platform acceptance is guaranteed.

## Example Batch Plan

Request: `/batch 3 /gpt 咖啡館時尚人像，固定黑色針織上衣`.

Fixed: Asian-aesthetic portrait, black knit top, cafe setting, natural skin. Variable: expression, framing and light.

1. A relaxed seated portrait by a window, warm soft side light, quiet smile, half-body framing.
2. A candid glance while holding a cup, diffused overcast light, close portrait with textured cafe background.
3. A reflective look away from the camera, gentle backlight, three-quarter framing and soft background depth.

These are planning sketches; final user-facing output must expand each into a complete standalone prompt in the requested platform format.
