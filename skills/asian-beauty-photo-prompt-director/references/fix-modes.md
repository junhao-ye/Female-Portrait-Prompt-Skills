# Fix Modes

Use this reference when the user invokes `/fix ...` or describes a failed generation.

## Output Contract

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

## `/fix 生成太老`

Delete:

```text
mature, mature woman, mature lady, adult woman, 成熟女性, 成熟, 有阅历, 岁月感, 沧桑
```

Add positive:

```text
youthful refined elegance, peak feminine beauty, firm supple skin, natural skin elasticity, glowing healthy complexion, defined facial structure, clear expressive eyes, vibrant yet sophisticated presence, in her prime, not childlike, not middle-aged
```

Add negative:

```text
middle-aged appearance, aging skin, wrinkles, fine lines, nasolabial folds, eye bags, sagging skin, tired face, dull complexion, old-looking
```

## `/fix 被拒`

Delete or rewrite:

```text
性感, 挑逗, 魅惑, 裸露, 低机位, 湿身, 暧昧, 诱惑, 擦边, 幼态, 情趣, sexy, seductive, erotic, nude, explicit, provocative
```

Replace with:

```text
refined Asian beauty, elegant portrait, tasteful outfit, graceful posture, fashion editorial, magnetic gaze, soft cinematic lighting
```

If the original request is red-line unsafe, refuse that part and provide a safe commercial portrait alternative.

## `/fix 太幼`

Add:

```text
defined facial structure, non-childlike face, clear jawline, confident story-rich gaze, elegant refined presence, not childlike, not baby-faced
```

Avoid:

```text
baby face, loli, innocent childlike, schoolgirl, teen
```

## `/fix 脸崩`

Add positive:

```text
detailed face, detailed eyes, perfect facial symmetry, sharp facial features, realistic skin, natural pores, clear eye structure
```

Add negative:

```text
bad face, asymmetrical eyes, distorted face, deformed face, dead eyes, waxy skin, over-smoothed skin
```

## `/fix 手崩`

Add positive:

```text
anatomically correct hands, correct number of fingers, natural hand gesture, relaxed fingers
```

Add negative:

```text
bad hands, extra fingers, missing fingers, fused fingers, deformed hands, twisted fingers
```
