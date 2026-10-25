---
name: female-portrait-prompt-generator
description: Generate complete, stable AI image prompts for tasteful adult female portrait photography from user-selected parameters. Use when the user asks for 女性写真提示词, AI 图片生成提示词, 清冷私房写真, 低饱和室内女性写真, portrait prompt generation, or wants parameters locked and expanded into a complete non-explicit image prompt.
---

# Female Portrait Prompt Generator

Generate one complete, stable AI image prompt for tasteful adult female portrait photography from the user's parameters. The default visual direction is cool, restrained, low-saturation, minimalist indoor portraiture with a private but non-explicit atmosphere.

## Safety And Scope

- Depict only clearly adult women. Default: young adult East Asian woman, visual age about 22-28.
- Keep the result tasteful, non-explicit, non-pornographic, non-vulgar, and suitable for refined portrait photography.
- Allow light boudoir mood, soft sensuality, body-line emphasis, and private atmosphere only when framed as adult, clothed, restrained, and non-graphic.
- Do not generate underage, childlike, school-uniform, teen, barely legal, explicit nudity, sexual acts, fetish framing, vulgar poses, exposed genitals, or exploitative wording.
- If a user parameter asks for unsafe or explicit content, state that part cannot be used and replace only that unsafe part with a tasteful adult photography alternative. Preserve all safe locked parameters.

## Parameter Locking Rule

Before writing the prompt, perform a parameter lock review.

1. Treat every explicit user-filled value as locked.
2. Do not replace, weaken, rewrite, optimize away, or swap locked values.
3. Only expand locked values with compatible detail.
4. Only auto-match values that are blank, missing, or exactly `自动`.
5. If two locked values seem stylistically tense, keep both and harmonize through makeup, expression, clothing detail, lighting, posture tension, and color grading.
6. The final image must be "a person with the locked facial direction, photographed in the locked photography style", not a different face or different style that feels more convenient.

## Expected Inputs

The user may provide any subset of these fields:

| Field | Options Or Meaning |
|---|---|
| 写真风格 | 自动 / 清冷私房 / 轻性感氛围 / 极简韩系 / 日系柔焦 / 高级影棚 / 居家自然 / 冷淡电影感 / 低饱和写真 / 都市内景 |
| 五官方向 | 自动 / 清冷高级脸 / 温柔圆脸型 / 古典鹅蛋脸 / 自然生活感脸 / 东方丹凤眼 / 明艳浓颜脸 / 甜酷小方脸 / 知性长脸型 / 电影故事脸 |
| 场景方向 | 自动 / 白墙 / 灰墙 / 窗边 / 床边 / 高级卧室 / 极简房间角落 / 浴室干区 / 影棚灰背景 / 城市公寓内景 |
| 服装方向 | 自动 / 细肩带背心 / 短款吊带 / 修身针织背心 / 简约 bralette / 蕾丝内衣外搭 / 白衬衫 / 低腰牛仔裤 / 宽松白色长裤 / 居家棉质套装 / 深色极简内搭 |
| 服装颜色 | 自动 / 白色 / 灰色 / 黑色 / 米白 / 浅蓝 / 淡粉 / 深绿色 / 低饱和冷色 |
| 气质标签 | 自动 / 清冷 / 安静 / 松弛 / 温柔 / 克制 / 慵懒 / 知性 / 轻熟 / 电影感 |
| 身形方向 | 自动 / 柔和曲线 / 丰腴曲线 / 纤细腰身 / 健康紧致 / 自然微肉感 |
| 线条强调 | 自动 / 弱 / 中 / 强 |
| 身体线条重点 | 自动 / 锁骨肩颈 / 腰腹线条 / 腰胯曲线 / 侧身轮廓 / 腿部比例 / 整体 S 型曲线 |
| 姿态方向 | 自动 / 靠墙站立 / 侧身回望 / 坐在床边 / 微微扭腰 / 单手抬起 / 低头安静 / 自然站姿 / 近距离自拍感 |
| 镜头方向 | 自动 / 半身近景 / 半身到大腿 / 腰腹近景 / 侧身构图 / 电影感近景 / 局部裁切 / 全身竖构图 |
| 面部呈现 | 自动 / 完整脸部 / 下半脸入镜 / 眼睛裁切 / 侧脸局部 / 低头遮挡 / 头发自然遮挡 |
| 光线方向 | 自动 / 阴天窗光 / 柔和自然光 / 冷灰蓝柔光 / 暗调室内光 / 高级影棚柔光 / 清晨淡光 |
| 色调方向 | 自动 / 冷灰蓝 / 低饱和米白 / 灰粉色 / 淡蓝色 / 黑白灰 / 柔和胶片感 |
| 精修程度 | 自动 / 自然真实 / 轻度精修 / 高级精修 / 影楼精修 |
| 画幅比例 | 9:16 / 3:4 / 2:3 / 1:1 / 16:9 |
| 画质方向 | 自动 / 真实摄影 / 高级商业写真 / 柔焦胶片 / 高清精修 / 自然生活感 |

If the user gives no parameters, use tasteful defaults and clearly list them as automatic.

## Auto-Matching Defaults

Use these defaults only for blank or `自动` values:

| Field | Default |
|---|---|
| 写真风格 | 清冷私房 or 低饱和写真 |
| 五官方向 | 清冷高级脸 with distinctive East Asian features |
| 场景方向 | 窗边 or 极简房间角落 |
| 服装方向 | 细肩带背心, 修身针织背心, 白衬衫, or 居家棉质套装 |
| 服装颜色 | 米白, 灰色, 浅蓝, or low-saturation cool color |
| 气质标签 | 清冷, 安静, 克制, 松弛 |
| 身形方向 | 柔和曲线 or 自然微肉感 |
| 线条强调 | 中 |
| 身体线条重点 | 锁骨肩颈, 腰腹线条, 侧身轮廓 |
| 姿态方向 | 低头安静, 靠墙站立, 坐在床边, or 自然站姿 |
| 镜头方向 | 半身近景, 半身到大腿, 侧身构图, or 局部裁切 |
| 面部呈现 | 完整脸部 or 头发自然遮挡 |
| 光线方向 | 阴天窗光 or 柔和自然光 |
| 色调方向 | 冷灰蓝, 低饱和米白, or 柔和胶片感 |
| 精修程度 | 高级精修 with natural skin texture |
| 画幅比例 | 9:16 |
| 画质方向 | 真实摄影 or 高级商业写真 |

## Facial Direction Expansion

When expanding 五官方向, avoid generic AI influencer faces. Always include asymmetry, individual facial memory points, and East Asian features.

| 五官方向 | Expansion Guide |
|---|---|
| 清冷高级脸 | elongated or oval face, calm bone structure, narrow expressive eyes, refined nose bridge, restrained lips, cool distant gaze |
| 温柔圆脸型 | soft round face, gentle cheek volume, relaxed eyelids, small rounded nose, natural lips, warm quiet expression |
| 古典鹅蛋脸 | balanced oval face, smooth jawline, elegant brow-eye spacing, refined nose, soft lips, classical calm |
| 自然生活感脸 | slightly imperfect but harmonious features, natural skin texture, relaxed eyes, subtle facial softness, believable daily-life face |
| 东方丹凤眼 | distinct East Asian upturned eye shape, clean eyelid fold or monolid detail, controlled gaze, delicate cheek and jaw structure |
| 明艳浓颜脸 | stronger brow-eye contrast, vivid lips, clearer facial contours, confident gaze, but still tasteful and non-vulgar |
| 甜酷小方脸 | small square jaw, soft cheek volume, alert eyes, slight coolness in expression, not childish |
| 知性长脸型 | longer face, calm forehead and cheek proportions, mature intellectual gaze, understated lips |
| 电影故事脸 | memorable imperfect features, quiet emotional tension, eyes with narrative depth, non-standard beauty |

## Body And Pose Rules

- Keep proportions natural and anatomically plausible.
- Allow clear but restrained emphasis on collarbone, shoulder-neck line, waist, abdomen, waist-hip curve, legs, side silhouette, or overall S curve.
- For `线条强调：强`, increase composition and lighting emphasis, not explicit exposure.
- Avoid exaggerated breasts, impossible waist, distorted hips, pornographic posing, vulgar arching, or fetishized camera angles.
- Posture should feel quiet, composed, and photographic: leaning on wall, seated at bed edge, slight torso turn, lowered head, one hand lifted naturally, side glance, relaxed standing.

## Prompt Construction

Build the complete prompt in this order:

1. subject identity and adult age clarity
2. locked facial direction and facial memory points
3. locked or automatic temperament
4. body shape and line emphasis
5. clothing and color
6. scene and props
7. pose and camera composition
8. light, color grading, retouching, image quality, aspect ratio
9. first-glance visual hook
10. negative restrictions

Write the main prompt as one polished Chinese prompt. Include English photography keywords only when useful for image models, such as `photorealistic`, `soft window light`, `low saturation`, `shallow depth of field`, `film grain`, `high-end editorial portrait`.

## Required Output

Return exactly these sections:

1. `参数锁定复核`
   - `已锁定参数`: list every user-specified non-auto value exactly.
   - `自动补全参数`: list blank or `自动` fields and chosen values.
   - `冲突调和`: state how any tension is harmonized. If none, say `无明显冲突`.
   - `安全复核`: confirm adult, tasteful, non-explicit handling.
2. `完整生成提示词`
   - one complete prompt ready for AI image generation.
3. `本次自动补全部分`
   - concise list of added details.
4. `主要吸睛点`
   - 3-5 visual hooks.
5. `负面限制词`
   - include unsafe-content negatives and quality negatives.

## Negative Restriction Baseline

Always include a negative restriction block adapted to the user input:

`未成年、幼态脸、teen、childlike、school uniform、裸露、色情、低俗姿势、性行为、露骨挑逗、fetish、过度暴露、夸张胸部、畸形腰臀、身体比例失真、AI 网红脸、欧美混血感过强、塑料皮肤、油腻皮肤、重度磨皮、过曝、强闪光、高饱和网红风、廉价棚拍、低清晰度、畸形手指、多余肢体、脸部崩坏、眼睛不对称失控、背景杂乱、文字、水印、logo`

## Examples

Open `references/examples.md` when you need examples for a happy path, robust unsafe-parameter handling, or anti-pattern correction.
