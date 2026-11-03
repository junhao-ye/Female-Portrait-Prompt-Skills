# Examples

Use these examples to match output quality, robust handling, and anti-pattern correction.

## Happy Path: `/mj /cyber /tasteful 霓虹街头女主`

```markdown
## 快捷指令
平台：/mj
风格：/cyber
分级：/tasteful
模式：生成

## 风险词处理
无风险词。

## 中文创意描述
赛博朋克雨夜街头的东方审美女主，霓虹与雨水反射塑造电影感，人物气质冷静、自信、有吸引力但克制。

## 提示词
## Midjourney 提示词

A breathtaking refined Asian female cyberpunk portrait on a rainy neon city street, youthful refined elegance, peak feminine beauty, firm supple skin with natural texture, glowing healthy complexion, natural skin elasticity, defined facial structure with soft natural angles, perfect facial proportions, expressive clear eyes, confident gaze with depth and story, vibrant yet sophisticated presence, futuristic tailored outfit with reflective fabric, cinematic rain reflections, holographic signs, dramatic rim light outlining hair and outfit, 85mm portrait lens, shallow depth of field, fashion editorial composition, alluring yet refined presence, not childlike, not middle-aged, in her prime

--no middle-aged appearance, aging skin, wrinkles, fine lines, nasolabial folds, eye bags, sagging skin, tired face, dull complexion, old-looking, elderly features, childlike face, baby face, loli, nudity, explicit content, vulgar pose
--ar 2:3 --v 6.1 --style raw --s 200 --q 1

## 参数建议
Midjourney 默认参数已附在提示词末尾。

## 可替换变量
脸型 / 发型发色 / 妆容 / 气质 / 姿态 / 服装 / 场景 / 光影 / 镜头 / 色调
```

## Robust Variant: Unsafe Wording Rewritten

User: `/gpt /boudoir 性感床上亚洲美女`

```markdown
## 快捷指令
平台：/gpt
风格：默认商业人像
分级：/boudoir
模式：生成

## 风险词处理
性感 → 天然吸引力，眼神有故事，克制而迷人的气质
床上 → 高级精品酒店卧室，丝绸床品，柔和窗光，慵懒而优雅的氛围

## 中文创意描述
高级内衣品牌广告感的精品酒店卧室人像，重点放在面部美感、精致面料、柔和窗光和优雅姿态上。

## 提示词
## 即梦 / 豆包 / GPT Image 提示词

生成一张符合东方审美的女性商业写真。人物皮肤紧致细腻有弹力，轻微自然毛孔可见，面部轮廓清晰有层次，五官比例完美和谐，眼神自信有故事感但不显疲惫，气质介于青春活力与优雅从容之间，不幼态，不儿童化，无松弛感，无法令纹，无鱼尾纹，无眼袋，无中年感。场景为高级精品酒店卧室，丝绸床品和柔和窗光营造精致氛围，服装为高级内衣品牌广告质感的精致面料造型，整体优雅克制，不暴露，不低俗。人物姿态自然放松，镜头以半身或七分身构图突出脸部、气质、服装质感和光影层次。风格接近高端商业写真与时尚杂志大片。

## 参数建议
使用竖构图 2:3 或 3:4，强调自然肤质、柔和窗光、商业写真质感。

## 可替换变量
脸型 / 发型发色 / 妆容 / 气质 / 姿态 / 服装 / 场景 / 光影 / 镜头 / 色调
```

## Anti-Pattern And Correction

Bad prompt:

```text
mature sexy Asian woman, loli face, low-angle body close-up, explicit seductive pose
```

Problems:

- `mature` pushes older output.
- `loli face` is disallowed minor-coded language.
- body close-up and explicit pose are unsafe and unstable.

Corrected prompt:

```text
refined Asian female portrait, youthful refined elegance, firm supple skin with natural texture, defined facial structure, perfect facial proportions, expressive clear eyes, confident gaze with depth, tasteful high-fashion outfit, graceful editorial pose, soft cinematic lighting, not childlike, not middle-aged, no nudity, no explicit content
```
