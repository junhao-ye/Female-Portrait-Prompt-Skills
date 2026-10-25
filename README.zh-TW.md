# Female Portrait Prompt Skills

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md)

兩個互補的 Codex 成年女性人像技能：一個專注提示詞生成，一個提供更完整的視覺導演流程。本 Repo 提供繁體中文、簡體中文、日文與英文 README 和詳細比較使用手冊。

| 技能 | 適合用途 | 預設結果 |
| --- | --- | --- |
| [female-portrait-prompt-generator](skills/female-portrait-prompt-generator/SKILL.md) | 清冷、克制、低飽和室內寫真，明確鎖定參數 | 完整文字提示詞、參數複核、補充內容、吸睛點與負面詞 |
| [female-portrait-director](skills/female-portrait-director/SKILL.md) | 多風格創作、完整場景設計、優化、診斷與授權參考圖 | 詳細提示詞；只有明確要求時才進入生圖流程 |

## 快速開始

按照[安裝說明](docs/USAGE.zh-TW.md#installation)安裝技能目錄，開啟新的 Codex 對話，選擇一個技能調用：

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

範例保留技能正式定義的中文欄位名稱與模式值，避免使用未定義的別名；補充說明可以使用你偏好的語言。缺失項自動補全，明確填寫的安全參數應當保留。僅提供參數區塊表示請求提示詞，不表示請求生圖。

## 使用手冊

- [繁體中文](docs/USAGE.zh-TW.md)
- [简体中文](docs/USAGE.zh-CN.md)
- [日本語](docs/USAGE.ja.md)
- [English](docs/USAGE.en.md)

每份手冊均包含詳細比較、參數對應、輸出模式、完整範例、參考圖流程、故障排查與來源檔案中的已知不一致。

## 範圍與限制

Generator 只輸出文字。Director 包含 14 條已實作風格路線、7 個氣質增強模組與 6 個任務模組；生圖依賴執行環境提供的能力。兩者都沒有內建圖像模型。提示詞不能保證身份、商品細節、文字或像素尺寸完全準確。人物必須明確成年，並遵守各技能的非露骨範圍；保留身份的參考圖應為本人或已授權成年人物。

## 來源與授權

兩個技能目錄為 2026-10-25 的原樣快照。Director 標示版本 V1.4.1，保留李岳的 MIT 授權及聲明。Generator 未附獨立授權檔，本 Repo 不替它新增授權。公開 Repo 不代表所有元件均已開源。詳見[授權與署名](LICENSES.md)及[來源檔案雜湊](SOURCE_MANIFEST.json)。

## 驗證與貢獻

執行 `python scripts/validate.py`，檢查來源檔案完整性、技能入口、路線與模組檔案、多語言文件、範例結構及集合文件的本機連結。檢查不包含實際生圖測試。貢獻方式見 [CONTRIBUTING.md](CONTRIBUTING.md)。
