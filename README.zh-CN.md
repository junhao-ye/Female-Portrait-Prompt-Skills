# Female Portrait Prompt Skills

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md)

两个互补的 Codex 成年女性人像技能：一个专注提示词生成，一个提供更完整的视觉导演流程。本仓库提供简体中文、繁体中文、日文与英文 README 和详细比较使用手册。

| 技能 | 适合用途 | 默认结果 |
| --- | --- | --- |
| [female-portrait-prompt-generator](skills/female-portrait-prompt-generator/SKILL.md) | 清冷、克制、低饱和室内写真，明确锁定参数 | 完整文字提示词、参数复核、补充内容、吸睛点与负面词 |
| [female-portrait-director](skills/female-portrait-director/SKILL.md) | 多风格创作、完整场景设计、优化、诊断与授权参考图 | 详细提示词；只有明确要求时才进入生图流程 |

## 快速开始

按照[安装说明](docs/USAGE.zh-CN.md#installation)安装技能目录，打开新的 Codex 对话，选择一个技能调用：

```text
$female-portrait-prompt-generator
写真风格：清冷私房
五官方向：温柔圆脸型
场景方向：窗边
服装方向：米白色白衬衫
画幅比例：3:4
```

```text
$female-portrait-director
风格：都市时尚写真
场景：雨后咖啡馆外
服装：深灰西装与米白内搭
气质：知性、安静
画幅：3:4
输出模式：简洁
```

示例保留技能正式定义的中文字段名与模式值，避免使用未经定义的别名；补充说明可以使用你偏好的语言。缺失项自动补全，明确填写的安全参数应当保留。仅提供参数块表示请求提示词，不表示请求生图。

## 使用手册

- [简体中文](docs/USAGE.zh-CN.md)
- [繁體中文](docs/USAGE.zh-TW.md)
- [日本語](docs/USAGE.ja.md)
- [English](docs/USAGE.en.md)

每份手册均包含详细比较、参数对应、输出模式、完整示例、参考图流程、故障排查与源文件中的已知不一致。

## 范围与限制

Generator 只输出文字。Director 包含 14 条已实现风格路线、7 个气质增强模块与 6 个任务模块；生图依赖运行环境提供的能力。两者都没有内置图像模型。提示词不能保证身份、商品细节、文字或像素尺寸完全准确。人物必须明确成年，并遵守各技能的非露骨范围；保留身份的参考图应为本人或已授权成年人物。

## 来源与授权

两个技能目录为 2026-10-25 的原样快照。Director 标注版本 V1.4.1，保留李岳的 MIT 授权及声明。Generator 未附独立授权文件，本仓库不替它新增授权。公开仓库不意味着所有组件均已开源。详见[授权与署名](LICENSES.md)及[源文件哈希](SOURCE_MANIFEST.json)。

## 验证与贡献

运行 `python scripts/validate.py`，检查源文件完整性、技能入口、路线与模块文件、多语言文档、示例结构及集合文档的本地链接。检查不包含实际生图测试。贡献方式见 [CONTRIBUTING.md](CONTRIBUTING.md)。
