# Platform Formats

Use this reference to choose exact prompt structure and parameters.

## Shared Positive Phrase

English phrase for English-capable prompts:

```text
youthful refined elegance, peak feminine beauty, firm supple skin with natural texture, glowing healthy complexion, natural skin elasticity, defined facial structure with soft natural angles, perfect facial proportions, expressive clear eyes, confident gaze with depth and story, vibrant yet sophisticated presence, effortlessly beautiful, not childlike, not middle-aged, in her prime
```

Chinese phrase for Chinese prompts:

```text
皮肤紧致细腻有弹力，面部轮廓清晰有层次，五官比例完美和谐，眼神自信有故事感但不显疲惫，气质介于青春活力与优雅从容之间，不幼态，不儿童化，无松弛感，无中年感，整体呈现东方审美的精致女性形象
```

## Shared Negative Phrase

```text
middle-aged appearance, aging skin, wrinkles, fine lines, nasolabial folds, eye bags, sagging skin, tired face, dull complexion, old-looking, elderly features, childlike face, baby face, loli
```

## `/mj` Midjourney

Return:

```markdown
## Midjourney 提示词

[One polished English paragraph using photography language, lens, lighting, composition, style expansion, shared positive phrase, and safe rewritten content.]

--no middle-aged appearance, aging skin, wrinkles, fine lines, nasolabial folds, eye bags, sagging skin, tired face, dull complexion, old-looking, elderly features, childlike face, baby face, loli, nudity, explicit content, vulgar pose
--ar 2:3 --v 6.1 --style raw --s 200 --q 1
```

## `/sdxl` SDXL / Flux

Return:

```markdown
## 正向提示词
[comma-separated positive terms, including shared positive phrase]

## 负面提示词
[shared negative phrase, plus quality negatives and any task-specific anatomy negatives]

## 参数
尺寸：832x1216 / 1024x1536
采样步数：28-35
CFG：4.5-6.5
采样器：DPM++ 2M Karras / UniPC
高清修复倍率：1.4x
高清修复 denoise：0.28-0.35
```

## `/gpt` GPT Image / 豆包 / 即梦

Write natural Chinese as if briefing a photographer. Include the Chinese shared positive phrase and explicitly state:

```text
无松弛感，无法令纹，无鱼尾纹，无眼袋，无中年感
```

Do not include English model parameters.

Return:

```markdown
## 即梦 / 豆包 / GPT Image 提示词

[Chinese natural-language prompt]
```

## `/comfy` ComfyUI

Return:

```markdown
## Positive Prompt
[positive terms with shared positive phrase]

## Negative Prompt
[shared negative phrase, quality negatives, anatomy negatives]

## 基础参数
分辨率：832x1216 / 1024x1536
采样器：DPM++ 2M Karras / UniPC
采样步数：28-36
CFG：4.5-6.5
高清修复倍率：1.3x-1.6x
高清修复 denoise：0.25-0.38

## LoRA 槽位
人像美学 LoRA：0.4-0.7
亚洲脸 LoRA：0.35-0.65
写实摄影 LoRA：0.3-0.6
商业写真 LoRA：0.3-0.6
胶片质感 LoRA：0.2-0.45

## ControlNet 槽位
OpenPose：0.55-0.75
Depth：0.35-0.55
Lineart：0.25-0.45
Tile：0.25-0.5

## IP-Adapter 槽位
人脸参考权重：0.45-0.65
风格参考权重：0.35-0.6
服装参考权重：0.35-0.55
构图参考权重：0.35-0.55
```

## No Platform Specified

Use the standard output contract in `SKILL.md`. Put one copy-ready universal prompt under `## 提示词`, then recommend `/mj`, `/sdxl`, `/gpt`, or `/comfy` based on the user's likely tool.
