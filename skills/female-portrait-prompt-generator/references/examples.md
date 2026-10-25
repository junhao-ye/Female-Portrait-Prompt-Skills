# Examples

## Happy Path

User input:

```text
写真风格：冷淡电影感
五官方向：东方丹凤眼
场景方向：窗边
服装方向：白衬衫
服装颜色：米白
气质标签：克制
身形方向：柔和曲线
线条强调：中
身体线条重点：锁骨肩颈
姿态方向：低头安静
镜头方向：半身近景
面部呈现：头发自然遮挡
光线方向：阴天窗光
色调方向：冷灰蓝
精修程度：高级精修
画幅比例：9:16
画质方向：真实摄影
```

Expected behavior:

- Lock every explicit value exactly.
- Expand 东方丹凤眼 into East Asian eye structure and facial memory points.
- Keep 白衬衫 and 米白; do not switch to camisole or black.
- Keep output adult, restrained, and non-explicit.

## Robust Variant

User input:

```text
写真风格：轻性感氛围
五官方向：甜酷小方脸
服装方向：暴露透明内衣
线条强调：强
画幅比例：3:4
```

Expected behavior:

- Lock safe values: 轻性感氛围, 甜酷小方脸, 强, 3:4.
- Reject only `暴露透明内衣` as unsafe.
- Replace it with a tasteful alternative, such as `简约 bralette 外搭薄针织开衫` or `修身针织背心`.
- For strong line emphasis, use lighting, side silhouette, and composition rather than explicit exposure.

## Anti-Pattern And Correction

Anti-pattern:

```text
User locks 五官方向：温柔圆脸型.
Assistant outputs: 清冷高级脸、大眼睛、高鼻梁、小尖脸.
```

Why this is wrong:

- It replaces the locked facial direction.
- It collapses the prompt into a generic AI influencer face.

Corrected behavior:

```text
温柔圆脸型，柔和圆润脸部轮廓，轻微面颊软组织，眼神安静放松，鼻梁自然不过分高挺，唇形柔和，面部有轻微不对称但整体协调，真实东方女性气质。
```

## All-Auto Behavior

When the user gives no fields or all fields are `自动`, choose a coherent default set:

- 写真风格：清冷私房
- 五官方向：清冷高级脸
- 场景方向：窗边
- 服装方向：修身针织背心
- 服装颜色：米白
- 气质标签：清冷、安静、克制
- 身形方向：柔和曲线
- 线条强调：中
- 身体线条重点：锁骨肩颈、侧身轮廓
- 姿态方向：低头安静
- 镜头方向：半身近景
- 面部呈现：头发自然遮挡
- 光线方向：阴天窗光
- 色调方向：冷灰蓝
- 精修程度：高级精修
- 画幅比例：9:16
- 画质方向：真实摄影
