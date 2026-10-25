# Comparison and usage manual

[English](USAGE.en.md) | [简体中文](USAGE.zh-CN.md) | [繁體中文](USAGE.zh-TW.md) | [日本語](USAGE.ja.md)

[Repository README](../README.md)

## 1. Choose a skill

Generator focuses on complete portrait prompts within a cool, restrained, low-saturation indoor aesthetic. Director adds broader style routing, coherent scene direction, prompt repair, and reference-image workflows. These are workflow differences observed in the supplied documents, not measured evidence that one produces better images.

| Dimension | Generator | Director |
| --- | --- | --- |
| Default style | Cool private indoor portrait or low-saturation portrait | Route chosen from intent; clean lifestyle if unclear |
| Parameter handling | Lock explicit safe values; fill blank, missing, or `自动` fields | Lock explicit values; additionally audit their propagation into the final prompt |
| Visual construction | Face, temperament, body, clothing, scene, pose, camera, light, grading | Also connects a time slice, small event, gaze, actions, fabric movement, and spatial layers |
| Native controls | 17 main fields, including face visibility and retouching | Adds palette relationships, visible richness, platform purpose, output mode, and reference roles |
| Default output | Five sections with one complete Chinese prompt | Four sections with module explanations and an exactly five-paragraph final prompt |
| Optimization and diagnosis | No dedicated task modules | Dedicated task modules |
| Image-to-prompt | Not a declared workflow | Supported workflow |
| Direct generation/editing | Explicitly outside its specification | Requires an explicit image request and available host capability |
| Identity/product references | Identity cloning and image editing are outside scope | Own or authorized adult identity references and product references |
| Complexity | A compact entry point with optional examples | More modular loading and longer standard output |

Both skills preserve specified facial direction. A gentle round face must remain a gentle round face even with a cool photography style. Director further coordinates what happens in the frame: a pause after reading, one hand resting on a page, a consistent gaze, and window light that supports the same moment. Generator also expands details; it is not merely a keyword list.

Use Generator for its focused indoor aesthetic and native face-crop/retouching controls. Use Director for urban, historical fantasy, commercial, sport, travel, complex scene design, or repair tasks. Usually invoke one at a time. If passing a Generator draft to Director, include all original locked fields and ask it to preserve the aesthetic; do not automatically rename `清冷私房` as `纯欲曲线生活照`.

<a id="installation"></a>
## 2. Installation

Prerequisites: Git, a local Codex installation supporting filesystem skills, and access to this repository. Run the clone command from a parent working directory. Then choose either the PowerShell block (Windows) or the Bash block (macOS/Linux), from that same parent directory. The commands copy the two complete directories, not just `SKILL.md`.

Before copying, check whether either destination already exists. Back up or deliberately reconcile an existing installation; the snippets below refuse to replace one. This repository's nested `skills/` layout is for collection packaging. Invocation names remain unchanged after installation.

```powershell
git clone https://github.com/junhao-ye/Female-Portrait-Prompt-Skills.git
```

```powershell
$skillDestination = Join-Path $env:USERPROFILE '.codex\skills'
if ($env:CODEX_HOME) { $skillDestination = Join-Path $env:CODEX_HOME 'skills' }
foreach ($skillName in @('female-portrait-prompt-generator', 'female-portrait-director')) {
    if (Test-Path -LiteralPath (Join-Path $skillDestination $skillName)) {
        throw "Existing skill: $skillName. Back up or reconcile it before installing."
    }
}
New-Item -ItemType Directory -Path $skillDestination -Force | Out-Null
Copy-Item -LiteralPath '.\Female-Portrait-Prompt-Skills\skills\female-portrait-prompt-generator' -Destination $skillDestination -Recurse -ErrorAction Stop
Copy-Item -LiteralPath '.\Female-Portrait-Prompt-Skills\skills\female-portrait-director' -Destination $skillDestination -Recurse -ErrorAction Stop
```

```bash
skill_destination="${CODEX_HOME:-$HOME/.codex}/skills"
for skill_name in female-portrait-prompt-generator female-portrait-director; do
  if [ -e "$skill_destination/$skill_name" ]; then
    printf 'Existing skill: %s. Back up or reconcile it before installing.\n' "$skill_name" >&2
    exit 1
  fi
done
mkdir -p "$skill_destination"
cp -R Female-Portrait-Prompt-Skills/skills/female-portrait-prompt-generator "$skill_destination/"
cp -R Female-Portrait-Prompt-Skills/skills/female-portrait-director "$skill_destination/"
```

Start a new Codex conversation after installation. Invoke `$female-portrait-prompt-generator` or `$female-portrait-director` by name, or select the skill in the UI where supported. If a skill is not found, check that `SKILL.md` is directly inside each installed skill directory. Generator needs no external image service for text prompts; Director's image tasks require a host image-generation or editing capability.

## 3. Parameters and defaults

Examples use canonical Chinese parameter names and values from the source. Keep those keys for reproducibility; add free-form directions in English, Japanese, or Chinese. This guide does not define new translated aliases. You may provide only a subset of fields.

Generator's 17 fields are: `写真风格`, `五官方向`, `场景方向`, `服装方向`, `服装颜色`, `气质标签`, `身形方向`, `线条强调`, `身体线条重点`, `姿态方向`, `镜头方向`, `面部呈现`, `光线方向`, `色调方向`, `精修程度`, `画幅比例`, `画质方向`.

Only blank, missing, or exactly `自动` values are automatically matched. Defaults lean toward a cool indoor portrait, an East Asian adult woman about 22–28, window light, restrained clothing and color, natural skin texture, medium line emphasis, and 9:16. Write a specific adult age when it matters.

Director also exposes `配色方向`, `华丽度`, `年龄特征`, `身形吸引力强度`, `线条重点`, `光线氛围`, `滤镜效果`, `尺寸参数`, `平台用途`, `输出模式`, `补充要求`, plus reference-image controls. Richness means visible material, embroidery, accessories, layering, and background decoration, rather than simply adding the adjective “luxurious.”

| Generator input | Director migration | Preserve this detail |
| --- | --- | --- |
| `写真风格` | `写真风格` | Styles are not all one-to-one |
| `五官方向`, `场景方向`, `气质标签`, `身形方向`, `镜头方向`, `画幅比例` | Same names | Keep explicit values |
| `服装方向` + `服装颜色` | `服装方向` and, if useful, `配色方向` | State garment color in the garment description |
| `线条强调` | `身形吸引力强度` | Similar intent, not a proven identical scale |
| `身体线条重点` | `线条重点` | Keep the specific areas |
| `姿态方向`, `面部呈现` | Preserve the original fields or explicitly put them in `补充要求` | Do not lose pose or face visibility |
| `光线方向` | `光线氛围` | Keep source and direction |
| `色调方向` | `滤镜效果`, optionally palette | Distinguish grading from object colors |
| `精修程度`, `画质方向` | Explicit `补充要求` or appropriate visual fields | Preserve texture and finish |

Director defaults to 9:16; it must not invent pixel dimensions when none were supplied. Aspect ratio and any supplied dimensions belong in the first sentence of the final prompt. Actual tool settings still control available output sizes.

## 4. Director styles, temperament, and tasks

The 14 implemented primary styles are:

| Category | Canonical style values |
| --- | --- |
| Lifestyle | `清纯生活照`, `复古港风写真`, `法式慵懒写真`, `旅行假日写真` |
| Fashion | `都市时尚写真`, `活力运动写真`, `影楼精修写真` |
| Curves | `纯欲曲线生活照`, `东方丰腴写真` |
| Oriental and fantasy | `新中式东方写真`, `古风仙侠美人图`, `清冷仙气古风增强版`, `明媚华贵古风增强版` |
| Commercial | `电商服装模特图` |

Select one main route per image/version. Temperament overlays adjust expression, gaze, posture, makeup, and small styling choices: bright heroine, cold heroine, cool mature, gentle sister, intellectual, mature urban, and sweet cool. They must not replace the selected style or user locks. For multiple styles, request separate versions rather than mixing all routes into one image.

The six task modules handle prompt optimization, failure diagnosis, parameter recommendations, safety rewriting, image-to-prompt, and reference-preserving image generation. A compound request may use them in sequence, for example diagnosis followed by optimization. They are instruction files, not independent APIs or bundled image engines.

Planned styles in the registry, such as jewelry advertising or Japanese translucence, do not become implemented dedicated routes merely because their names appear. Such visual intentions can be described through existing routes, but do not claim a missing module was loaded.

## 5. Output modes

Generator's default output has exactly five sections: `参数锁定复核`, `完整生成提示词`, `本次自动补全部分`, `主要吸睛点`, `负面限制词`. The lock review lists explicit and automatic values, any tension handling, and adult/non-explicit scope; visual hooks number 3–5. Its specification does not define Director's mode selector.

| Director `输出模式` | Result |
| --- | --- |
| `标准` | Default: parameter locks, readable module expansion, final prompt, negative constraints |
| `简洁` | Final prompt and negative constraints only |
| `导演详版` | Standard output plus more explanation of scene and photography decisions |
| `直接生成图片` | Prepare the prompt internally and invoke available image capability |
| `参考图直接生成` | Lock uploaded subjects, generate/edit, return an image with a short note |

In standard mode, the final prompt must have exactly five substantive paragraphs: (1) dimensions, person, adult age, face, makeup, temperament; (2) time slice, small event, actions and gaze; (3) body, clothing, palette, materials, accessories and richness; (4) environment, spatial layers, camera, framing and depth of field; (5) lighting placement, highlights, shadows, grading and texture. Public explanations describe selected visual effects, not private reasoning.

The final prompt and negatives appear in two separate Markdown `text` fences. `只要最终提示词` selects concise output and still includes negatives. A bare parameter block always means prompt generation. If you want an image, explicitly ask for one. Direct image mode may return the image without displaying its internal prompt.

## 6. Copyable examples

These are requests to paste into Codex, not claims that images have already been generated. Bracketed placeholders must be replaced with your own input. All subjects should be clearly adult; text-only defaults are fictional.

### A. Generator: full indoor portrait controls

```text
$female-portrait-prompt-generator

人物为虚构的 26 岁成年东亚女性。未填字段自动补全，已填参数保持不变。
写真风格：清冷私房
五官方向：温柔圆脸型
场景方向：窗边
服装方向：白衬衫
服装颜色：米白
气质标签：安静、克制
身形方向：柔和曲线
线条强调：中
身体线条重点：锁骨肩颈
姿态方向：低头安静
镜头方向：半身近景
面部呈现：完整脸部
光线方向：阴天窗光
色调方向：冷灰蓝
精修程度：自然真实
画幅比例：3:4
画质方向：真实摄影
```

Expected: the five Generator sections, preserving the gentle round face, off-white shirt, complete face, natural finish, and 3:4 ratio. Missing details may be completed without changing these choices.

### B. Director: a complete urban scene

```text
$female-portrait-director

写真风格：都市时尚写真
年龄特征：28 岁成年东方女性
五官方向：知性长脸型
场景方向：雨后城市街角的咖啡馆外
服装方向：深灰色西装外套、米白色内搭、黑色直筒长裤
配色方向：深灰为主，米白为辅，少量银色点缀
华丽度：低，依靠面料与剪裁体现质感
气质标签：知性、冷静、轻熟
身形方向：自然协调
身形吸引力强度：弱
线条重点：肩颈与整体比例
镜头方向：平视，膝盖以上构图
光线氛围：阴天柔光，少量街边暖光
滤镜效果：低饱和，保留自然肤色
画幅比例：3:4
平台用途：个人作品集
输出模式：标准
补充要求：人物为虚构成年女性；设计自然停步的瞬间，不添加文字
```

Expected: standard output, a five-paragraph fused prompt, and separate negatives. The pause, gaze, fabric, light, and rain-wet setting should form one plausible photograph.

### C. Director: concise prompt only

```text
$female-portrait-director

风格：新中式东方写真
场景：有竹影的现代茶室
服装：墨绿色新中式上衣与米白长裙
气质：知性、安静
画幅：3:4
人物为虚构的 30 岁成年女性。
输出模式：简洁
只要最终提示词和负面约束，不要解析。
```

### D. Diagnose and optimize an existing prompt

```text
$female-portrait-director

请先诊断，再优化下面的提示词。
必须保留：温柔圆脸型、墨绿色服装、窗边场景、3:4 画幅。
目前问题：结果变成尖下巴、黑色衣服，背景变成影棚。
请解释可能原因，给出修复后的最终提示词与负面约束。
原提示词：[粘贴原文]
```

Provide the original parameter block and failed output image too, if available. A useful diagnosis distinguishes prompt conflicts, route choice, dropped locks, and model limits instead of treating every failure as insufficient length.

### E. Recommend parameter sets

```text
$female-portrait-director

请推荐 3 组可直接调用的成年女性写真参数。
分别采用复古港风写真、旅行假日写真、新中式东方写真。
每组只选一个主风格，场景与服装颜色不要重复。
统一画幅比例 3:4，不直接生成图片。
```

### F. Reverse an image into a prompt

Upload the image first. This analyzes observable visual features; it does not identify the person or preserve their identity in a generated image.

```text
$female-portrait-director

请分析上传图片的构图、服装、光线、配色和可观察的外貌特征，
反推可用于虚构成年女性人像的提示词。
不识别或推测真实身份；不能确定的内容标为推断。
只输出最终提示词和负面约束，不生成图片。
```

### G. Generate a fictional portrait directly

```text
$female-portrait-director

写真风格：旅行假日写真
年龄特征：30 岁成年女性
场景方向：海边酒店阳台
服装方向：浅蓝色棉麻连衣裙
画幅比例：3:4
输出模式：直接生成图片
补充要求：虚构人物，保持自然摄影质感。
```

### H. Preserve an authorized identity and garment

Upload both images first. Replace the ownership/authorization statement if using an authorized adult model rather than your own photograph; do not make a false claim.

```text
$female-portrait-director

直接生成图片。
图片 1 是我本人，已成年，作为 identity_reference。
图片 2 是有权使用的服装图，作为 product_reference。
写真风格：电商服装模特图
画幅比例：3:4
输出模式：参考图直接生成
保留对象：图片 1 的脸型、眉眼、鼻唇；图片 2 的服装主色、版型、图案、领口结构。
允许改变：发型、姿态、背景与光线。
禁止改变：人物五官身份、服装品类、主色与关键结构。
补充要求：简洁背景、自然站姿、服装完整清楚。
```

## 7. Reference-image workflow

Label each uploaded image as `identity_reference` (own/authorized adult identity), `product_reference` (garment or product), `style_reference` (style only), or `edit_target` (the original to edit). If roles are unclear, clarify them before generation.

By default, identity locking protects observable facial shape, brows/eyes, nose/lips, and recognizability. It does not automatically freeze hairstyle, body, pose, makeup, or framing. Product locking protects category, silhouette, color, material, pattern, and key structures. Expand `保留对象` and `禁止改变` when stricter preservation is needed.

Style references do not imply permission or instructions to copy their person. Image-to-prompt returns text; reference generation returns an image. Director calls for checking identity/product drift and, when appropriate, one targeted retry. Exact logos, small print, and intricate patterns are not guaranteed; precise lettering may require later editing or compositing.

## 8. Troubleshooting and known inconsistencies

| Symptom | Action |
| --- | --- |
| Face, garment, or color is replaced | Supply original locks; remove conflicting defaults; request diagnosis and repair |
| Output is too long | In Director explicitly choose `简洁`; request a custom shorter response for Generator |
| A parameter block returns text | Expected; explicitly request `直接生成图片` for an image |
| Reference identity drifts | Confirm identity role and protected traits; simplify edits; assess the host model's limits |
| Aspect ratio/pixels are wrong | Check final prompt and actual image tool settings; wording alone does not enforce dimensions |
| Skill cannot load | Verify complete directories and entry-point locations; start a new conversation |

Known source-document issues are preserved, not silently repaired:

1. Director's core workflow uses a default adult age of 20–28; its schema uses 24–28. Generator defaults to about 22–28. Specify age explicitly.
2. Some older Director examples have three paragraphs or older templates, while current entry-point rules require five paragraphs in standard mode. Follow the current entry point and canonical workflow.
3. Generator's restrained private/boudoir atmosphere and local crops are not equivalent to Director's `pure-desire-curve` route, which emphasizes lifestyle framing and discourages private/boudoir treatment and body-part closeups. Pick the intended style rather than renaming it.
4. Generator's baseline negatives favor its cool restrained aesthetic, including avoidance of strong flash, highly saturated influencer styling, text, and logos. Do not transfer that list unchanged into a conflicting commercial or fashion task.

Both skills depend on the model interpreting text. Parameter locking is a workflow obligation, not a guarantee of exact pixels, consistent identity across images, or perfect clothing. No image-quality A/B test was performed for this collection. Added instructions and modularity can increase reading/output cost; no timing benchmark is claimed.

## 9. Source, scope, and verification

Read the [Generator entry point](../skills/female-portrait-prompt-generator/SKILL.md), its [specification](../skills/female-portrait-prompt-generator/SPEC.md), the [Director entry point](../skills/female-portrait-director/SKILL.md), [canonical workflow](../skills/female-portrait-director/skill/skill.md), [public instructions](../skills/female-portrait-director/skill/public_instructions.md), and [parameter schema](../skills/female-portrait-director/skill/parameter_schema.md) for authoritative rules.

Use clearly adult, non-explicit subjects within each skill's scope; preserve identity only from your own or authorized adult references. See [licensing and attribution](../LICENSES.md). Generator has no supplied standalone license; Director retains 李岳's MIT terms. Run `python scripts/validate.py` from the repository root for packaging, documentation, and snapshot checks. The manifest verifies supplied bytes, not rights, model quality, or future upstream updates.
