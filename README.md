# Female Portrait Prompt Skills

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md)

Two complementary Codex skills for clearly adult female portrait prompts: a focused prompt generator and a broader portrait direction workflow. Includes READMEs and practical comparison/usage manuals in English, Simplified Chinese, Traditional Chinese, and Japanese.

| Skill | Best fit | Default result |
| --- | --- | --- |
| [female-portrait-prompt-generator](skills/female-portrait-prompt-generator/SKILL.md) | Cool, restrained, low-saturation indoor portraits; explicit parameter locking | A complete text prompt, lock review, additions, visual hooks, and negatives |
| [female-portrait-director](skills/female-portrait-director/SKILL.md) | Multiple styles, coherent scene direction, optimization, diagnosis, and authorized reference images | Detailed prompt output; image generation only when explicitly requested |

## Quick start

Install the skill directories using the [installation guide](docs/USAGE.en.md#installation), start a new Codex conversation, and invoke one skill:

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

Examples retain canonical Chinese field names and mode values to avoid undocumented aliases; write additional directions in your preferred language. Missing values are completed automatically. Safe explicit values must be preserved. A parameter block alone requests text, not an image.

## Documentation

- [English manual](docs/USAGE.en.md)
- [简体中文使用说明](docs/USAGE.zh-CN.md)
- [繁體中文使用說明](docs/USAGE.zh-TW.md)
- [日本語利用ガイド](docs/USAGE.ja.md)

Each manual includes the detailed comparison, parameter mapping, output modes, full examples, reference-image workflow, troubleshooting, and known source inconsistencies.

## Scope and limits

Generator is text-only. Director supplies 14 implemented style routes, 7 temperament overlays, and 6 task modules; its image workflows require capabilities provided by the host. Neither skill bundles an image model. Identity, product details, lettering, and pixel dimensions are not guaranteed by prompt wording. Subjects must be clearly adult and requests must follow each skill's non-explicit scope; identity-preserving references must be your own or authorized adult images.

## Source and licensing

The supplied skill directories are unmodified snapshots dated 2026-10-25. Director identifies itself as V1.4.1 and retains 李岳's MIT license and notice. Generator includes no standalone license; this repository does not add one. Public visibility does not make every component open source. See [licensing and attribution](LICENSES.md) and [source hashes](SOURCE_MANIFEST.json).

## Validation and contributions

Run `python scripts/validate.py`. Checks cover source integrity, skill entry points, route/module files, multilingual documentation, runnable example structure, and local links in collection documentation. They do not test generated images. See [contributing](CONTRIBUTING.md).
