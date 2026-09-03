---
kind: reprint
source: https://estellacoding.github.io/blog/github-copilot-vscode-ai-conventional-commit
author: Estella (estellacoding)
---

# 【GitHub Copilot】自動生成約定式提交訊息

 Posted on 2025-03-08 Edited on 2025-04-15 In [GitHub Copilot](https://estellacoding.github.io/blog/categories/GitHub-Copilot/)

本教學將介紹如何使用 GitHub Copilot 在 VS Code 中自動產生符合約定式提交規範的提交訊息。



# 約定式提交

常會看到團隊成員的提交訊息，像是 `fix bug`、`update`、`fix another`、`oh yeah` 等，但這樣的提交訊息對於其他人來說是不容易理解的，因此約定式提交就是為了解決這個問題而生的。

約定式提交是一種對提交說明的規範，提供簡單的條件集合用於建立明確的提交歷史。

```
<類型 type>[可選的作用範圍 scope]: <描述 description>

[可選的正文 body]

[可選的頁腳 footer]
```

# 自動生成

看完約定式提交官方說明後，還是沒有記下來(我到底看了什麼)，沒關係，讓AI來記就好。

## 設定

進入設定，找到 `github.copilot.chat.commitMessageGeneration.instructions`，點擊「Edit in settings.json」，新增以下內容。

```
"github.copilot.chat.commitMessageGeneration.instructions": [
    {
        "file": ".github/prompts/copilot-commit-message-instructions.md"
    }
],
```

## 建立md檔

在專案根目錄建立 `.github\prompts\copilot-commit-message-instructions.md` 檔案。

![github-prompts-copilot-commit-message-instructions-md-path](https://firebasestorage.googleapis.com/v0/b/stellacoding1111.appspot.com/o/article%2Fgithub-copilot-vscode-ai-conventional-commit%2Fgithub-prompts-copilot-commit-message-instructions-md-path.jpg?alt=media&token=1e2ee167-8122-4592-9f2b-4cb49265b005)

### 官方md檔

下載 [約定式提交md檔](https://github.com/conventional-commits/conventionalcommits.org/blob/master/content/v1.0.0/index.zh-hant.md) 後，將內容複製貼到 `copilot-commit-message-instructions.md` 檔案中。

### 手動複製

複製 [約定式提交](https://www.conventionalcommits.org/zh-hant/v1.0.0/) 說明內容，到 [Paste to Markdown](https://p2m.gh.miniasp.com/) 轉成 Markdown 格式，貼到 `copilot-commit-message-instructions.md` 檔案中。

## 提交訊息

我簡單更改 `README.md` 的內容後，進入 VS Code 的 Source Control 面板中，讓 GitHub Copilot 根據約定式提交格式來生成我的提交訊息。

![github-copilot-vscode-ai-conventional-commit-auto-generate-message](https://firebasestorage.googleapis.com/v0/b/stellacoding1111.appspot.com/o/article%2Fgithub-copilot-vscode-ai-conventional-commit%2Fgithub-copilot-vscode-ai-conventional-commit-auto-generate-message.jpg?alt=media&token=678827ce-86b8-47a7-9816-39673b86aef4)

# 加入工作區

進一步還可以將 VS Code 設定加入工作區，就可以將 VS Code 設定也提交至 GitHub 中，而團隊成員就能一起共用相同設定及 `copilot-commit-message-instructions.md` 所使用的提示詞。

進入設定，點擊「Workspace」標籤，找到 `github.copilot.chat.commitMessageGeneration.instructions`，點擊「Edit in settings.json」，VS Code 自動產生 `.vscode/settings.json` 檔案，並新增以下內容。

```
{
    "github.copilot.chat.commitMessageGeneration.instructions": [
        {
            "file": ".github/prompts/copilot-commit-message-instructions.md"
        }
    ]
}
```

![vscode-settings-json-path](https://firebasestorage.googleapis.com/v0/b/stellacoding1111.appspot.com/o/article%2Fgithub-copilot-vscode-ai-conventional-commit%2Fvscode-settings-json-path.jpg?alt=media&token=8a54e021-3933-4843-8b42-6a4afe5b7959)

# 結論

讓 AI 根據約定式提交規範自動生成的提交訊息，會嚴格遵守 `<type>[scope]: <description>` 結構，統一格式讓團隊成員能快速理解提交內容，也因此能提高整體團隊協作效率喔。

# 參考文件

- [約定式提交文檔](https://www.conventionalcommits.org/zh-hant/v1.0.0/)
- [約定式提交md檔](https://github.com/conventional-commits/conventionalcommits.org/blob/master/content/v1.0.0/index.zh-hant.md)