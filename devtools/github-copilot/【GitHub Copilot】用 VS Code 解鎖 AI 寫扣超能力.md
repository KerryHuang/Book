---
kind: reprint
source: https://estellacoding.github.io/blog/github-copilot-vscode-ai-coding/
author: Estella (estellacoding)
---

# 【GitHub Copilot】用 VS Code 解鎖 AI 寫扣超能力

 Posted on 2025-03-08 Edited on 2025-04-12 In [GitHub Copilot](https://estellacoding.github.io/blog/categories/GitHub-Copilot/)

一次報名了保哥的 [GitHub Copilot 完整課程（共三堂）](https://learn.duotify.com/courses/gh-copilot-agent/refer/X3YFXL4D)，我把我能吸收的(課程內容太豐富)整理成這篇文章，帶大家一起解鎖 GitHub Copilot 在 VS Code 的各種強大寫扣超功能，從基本程式碼建議，到進階的 Chat 互動、代理指令與語音辨識，並精選常用功能與好用指令，希望能幫助大家提升開發效率🚀！

> 用我的 [連結](https://learn.duotify.com/courses/gh-copilot-agent/refer/X3YFXL4D) 購買保哥 GitHub Copilot 完整課程
> 原本看課有三個月，就可延長至四個月囉~~
> 推薦碼: X3YFXL4D



# 前置作業

## 安裝套件

- [GitHub Copilot](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot)
- [GitHub Copilot Chat](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot-chat)

## 基本設定

| 功能項目                                    | 設定內容 | 功能描述                                 |
| ------------------------------------------- | -------- | ---------------------------------------- |
| github.copilot.enable                       | true     | 設定在所有檔案啟用 GitHub Copilot 功能。 |
| github.copilot.editor.enableAutoCompletions | V        | 啟用程式碼自動補全功能。                 |
| github.copilot.nextEditSuggestions.enabled  | V        | 啟用下一個編輯建議(NES)功能。            |

![github-copilot-nextEditSuggestions-enabled](https://firebasestorage.googleapis.com/v0/b/stellacoding1111.appspot.com/o/article%2Fgithub-copilot-vscode-ai-coding%2Fgithub-copilot-nextEditSuggestions-enabled.jpg?alt=media&token=ec4c9c7d-fcce-4ae6-89c6-7cbaafe63367)

# 程式碼補全

## 建議工具列

根據游標所在的上下文自動生成程式碼建議。例如，當你輸入函式名稱 `days_ago`，並將游標停留在該名稱上，Copilot 會根據現有內容提供最符合邏輯的建議。因此，**若想要獲得準確程式碼建議，那精確命名變數名稱與函式名稱是非常重要的喔!**。

- 點擊 `<` 及 `>` 可以選擇想要的程式碼。
- 確認接受程式碼建議，只需按下 「Tab」鍵即可套用。(AI時代每個人必學的Tab技😂)

![1.code-suggestions](https://firebasestorage.googleapis.com/v0/b/stellacoding1111.appspot.com/o/article%2Fgithub-copilot-vscode-ai-coding%2F1.code-suggestions.jpg?alt=media&token=74351a6f-4f67-48ed-a4a3-b049d0db2620)

## 更多建議

若工具列上的程式碼建議都不想要，還可以工具列上的 或是鍵盤按「Ctrl+Enter」，開啟「Open Completions Panel」，讓 Copilot 提供更多組的程式碼建議。

- 選擇想要的程式碼，若是第1組可以，即可點擊「Accept suggestion 1」套用。

![2.code-suggestions-open-completions-panel-1](https://firebasestorage.googleapis.com/v0/b/stellacoding1111.appspot.com/o/article%2Fgithub-copilot-vscode-ai-coding%2F2.code-suggestions-open-completions-panel-1.jpg?alt=media&token=ae5ca84f-1775-499a-9d53-55ab80b9083b)

![2.code-suggestions-open-completions-panel-2](https://firebasestorage.googleapis.com/v0/b/stellacoding1111.appspot.com/o/article%2Fgithub-copilot-vscode-ai-coding%2F2.code-suggestions-open-completions-panel-2.jpg?alt=media&token=0f5a6765-762f-4a9e-97f3-2403f6861ac1)

# Inline Chat

## 編輯器

鍵盤按「Ctrl/Cmd+I」，開啟「Inline Chat」，可直接從編輯器向 Copilot 詢問問題。

-  可以啟動語音輸入，Copilot會朗讀回應內容。(上班大事把耳機插好😂)

![3.ctrl-i-ask-copilot](https://firebasestorage.googleapis.com/v0/b/stellacoding1111.appspot.com/o/article%2Fgithub-copilot-vscode-ai-coding%2F3.ctrl-i-ask-copilot.jpg?alt=media&token=5bf0b76c-c3d2-46cf-b912-70e0bc49a35b)

## 終端機

鍵盤按「Ctrl/Cmd+I」，開啟「Inline Chat」，可直接從終端機向 Copilot 詢問問題。

![4.ctrl-i-terminal-insert-into-terminal-1](https://firebasestorage.googleapis.com/v0/b/stellacoding1111.appspot.com/o/article%2Fgithub-copilot-vscode-ai-coding%2F4.ctrl-i-terminal-insert-into-terminal-1.jpg?alt=media&token=05680598-f697-4ea4-80a3-01526c90dc94)

也可以直接將指令自動插入終端機。

![4.ctrl-i-terminal-insert-into-terminal-2](https://firebasestorage.googleapis.com/v0/b/stellacoding1111.appspot.com/o/article%2Fgithub-copilot-vscode-ai-coding%2F4.ctrl-i-terminal-insert-into-terminal-2.jpg?alt=media&token=1a44f5c9-3b2c-4973-bf64-91cb8dafb5a9)

設定終端機輸出列印行數為 100000。
`terminal.integrated.scrollback`: `100000`
(預設值為1000行，可以調大一點，因為LLM只能讀到有顯示出來內容。)

# Chat View

鍵盤按「Ctrl+Alt+I(Cmd+Control+I)」，開啟「Chat」，使用自然語言詢問問題。

-  可以建立一個新的聊天。

-  可以存取過往的聊天紀錄。

- 

   

  可以看到更多功能。

  - 在編輯器中開啟Chat。
  - 在新視窗中開啟Chat。

![5.ctrl-alt-i-chat-view-suggest-code](https://firebasestorage.googleapis.com/v0/b/stellacoding1111.appspot.com/o/article%2Fgithub-copilot-vscode-ai-coding%2F5.ctrl-alt-i-chat-view-suggest-code.jpg?alt=media&token=df1fd3b3-a9a0-4571-83a5-2bcc51ae6f97)

(資料來源: [AI Data Science Team)](https://github.com/business-science/ai-data-science-team)

可將 GitHub Copilot Chat 的回應語言設定為繁體中文:
`github.copilot.chat.localeOverride`: `zh-TW`。

可至 [後台設定](https://github.com/settings/copilot) 中啟用「Bing 搜尋」功能:
`Copilot can search the web`: `Enable`。

# Copilot Edits

鍵盤按「Ctrl/Cmd+Shift+I」，開啟「Copilot Edits」，會在多個檔案中直接修改程式碼。

![6.ctrl-shift-i-copilot-edits-modify-code](https://firebasestorage.googleapis.com/v0/b/stellacoding1111.appspot.com/o/article%2Fgithub-copilot-vscode-ai-coding%2F6.ctrl-shift-i-copilot-edits-modify-code.jpg?alt=media&token=aa45481b-ee26-4902-9176-eba1feffac28)

# Quick Chat

鍵盤按「Ctrl+Shift+Alt+L(Cmd+Shift+Opt+L)」，開啟「Quick Chat」。

![7.ctrl-shift-alt+l-quick-chat](https://firebasestorage.googleapis.com/v0/b/stellacoding1111.appspot.com/o/article%2Fgithub-copilot-vscode-ai-coding%2F7.ctrl-shift-alt%2Bl-quick-chat.jpg?alt=media&token=d4cde311-6d26-4476-9ebf-b71ffd085f0b)

# 專業代理

在 Chat 中輸入`@`，可選擇專業代理(Chat Participants)，每個代理都有特定領域的專業知識。

| 指令       | 專家類別     | 功能描述                                                     |
| ---------- | ------------ | ------------------------------------------------------------ |
| @dbcode    | 資料庫專家   | 提供查詢語法、索引優化、資料模型設計等建議。                 |
| @workspace | 專案架構專家 | 瞭解工作區內所有程式碼，可用來查找類別、函式、檔案，或分析程式碼等建議。 |
| @vscode    | VS Code專家  | 提供VS Code功能、設定與API等建議。                           |
| @terminal  | 終端機專家   | 提供Shell命令操作、環境變數設定、腳本執行等建議。            |
| @github    | GitHub專家   | 查詢GitHub倉庫活動，如PR、Issue、合併記錄等。                |

## 設定代理

| 功能項目                           | 設定內容 | 功能描述                                                     |
| ---------------------------------- | -------- | ------------------------------------------------------------ |
| chat.agent.enabled                 | V        | 啟用代理模式。                                               |
| github.copilot.chat.agent.runTasks | V        | 允許代理執行工作區任務。                                     |
| chat.agent.maxRequests             | 50       | 設定代理最大請求次數。代理自動作業預設只有15次，不過對於比較複雜的工作，會需要你不斷的確認是否繼續，所以建議可以調高。 |

## @workspace

| 需求            | 提示詞範例                                                   |
| --------------- | ------------------------------------------------------------ |
| 建立Dockerfile  | 1.@workspace Generate a Dockerfile for this project, ensuring it includes all necessary dependencies and configurations for deployment. 2.@workspace Create a Dockerfile to package this project. Use a Python virtual environment and ensure best practices for containerization are followed. |
| 撰寫`README.md` | @workspace Write a `README.md` file that explains how to set up, run, and use this project. Include installation steps, dependencies, and usage examples for developers. |

## @vscode

| 需求                         | 提示詞範例                                             |
| ---------------------------- | ------------------------------------------------------ |
| 如何啟用自動換行             | @vscode how to enable word wrapping?                   |
| 查找開啟終端機的快捷鍵       | @vscode What is the shortcut for opening the terminal? |
| 搜尋不包含import的Python檔案 | @vscode /search python files without imports           |

## @terminal

| 需求                    | 提示詞範例                                           |
| ----------------------- | ---------------------------------------------------- |
| 列出工作區最大的5個檔案 | @terminal list the 5 largest files in this workspace |
| 解釋top指令的作用       | @terminal /explain top shell command                 |

## @github

| 需求                            | 提示詞範例                                                 |
| ------------------------------- | ---------------------------------------------------------- |
| 查詢指派給我的公開的PR          | @github What are all of the open PRs assigned to me?       |
| 查詢`@dancing-mona`最近合併的PR | @github Show me the recent merged pr’s from @dancing-mona. |
| 實作第一個Issue                 | @github Start working on the first open issue.             |

## @websearch

安裝套件 [Web Search for Copilot](https://marketplace.visualstudio.com/items?itemName=ms-vscode.vscode-websearchforcopilot)，即可在 Chat 視窗中使用 `@websearch` 從網路搜尋最新資訊。

進入設定，找到 `websearch.preferredEngine`，改用 `Bing` 為搜尋引擎。
![github-copilot-websearch](https://firebasestorage.googleapis.com/v0/b/stellacoding1111.appspot.com/o/article%2Fgithub-copilot-vscode-ai-coding%2Fgithub-copilot-websearch.jpg?alt=media&token=666d6c9e-9491-49b8-bad7-6c06fbcb5de5)

## 代理指令

在 Chat 中輸入`/`，可選擇代理執行特定任務，如產生測試、解釋程式碼等。

| 指令            | 功能描述                                                 |
| --------------- | -------------------------------------------------------- |
| /explain        | 解釋當前編輯器內的程式碼或終端機內容。                   |
| /new            | 在工作區建立新檔案或專案架構。                           |
| /newNotebook    | 建立新的Jupyter Notebook。                               |
| /search         | 為工作區的搜尋產生適合的查詢參數。                       |
| /fix            | 為選取的程式碼提供修復建議。                             |
| /startDebugging | 自動產生除錯配置的json檔(實驗性功能)。                   |
| /clear          | 清除所有對話記錄。                                       |
| /docs           | 在編輯器中為程式碼產生程式碼說明註解或文件。             |
| /tests          | 為選取的程式碼產生單元測試。                             |
| /setupTests     | 推薦適合當前專案的測試框架，並配置測試環境(實驗性功能)。 |
| /fixTestFailure | 根據測試錯誤訊息，建議修正方案。                         |

### /explain

| 需求               | 提示詞範例                       |
| ------------------ | -------------------------------- |
| 繁體中文解釋程式碼 | /explain in Traditional Chinese. |

### /new

如果我希望創建一個新專案，可使用`/new` 讓 Copilot 建立整個專案架構的資料夾。

![8.workspace-new-create-workspace](https://firebasestorage.googleapis.com/v0/b/stellacoding1111.appspot.com/o/article%2Fgithub-copilot-vscode-ai-coding%2F8.workspace-new-create-workspace.jpg?alt=media&token=622b0012-0e1d-49dc-a77b-67ccc0a06797)

| 需求 | 提示詞範例                               |
| ---- | ---------------------------------------- |
| /new | Express app using typescript and svelte. |

### /newNotebook

| 需求         | 提示詞範例                                                   |
| ------------ | ------------------------------------------------------------ |
| /newNotebook | Download titanic dataset and display key information using matplotlib. |

### /search

產生正規表示式(regular expression)來搜尋工作區。(regex是人能寫出來的東西嗎😂)

![9.vscode-search-regular-expression](https://firebasestorage.googleapis.com/v0/b/stellacoding1111.appspot.com/o/article%2Fgithub-copilot-vscode-ai-coding%2F9.vscode-search-regular-expression.jpg?alt=media&token=126af932-e1d3-4f62-a3f4-b37bd161b9c7)

| 需求         | 提示詞範例                           |
| ------------ | ------------------------------------ |
| 找出中文字串 | /search Find all Chinese characters. |

# 內建變數

在 Chat 中輸入`#`，可選擇變數，如專案所有程式碼、選擇檔案等。在提示詞中，可以引用變數來當成提問的相關上下文，使得 GitHub Copilot 能夠更準確地理解問題。

| 變數名稱             | 功能描述                            |
| -------------------- | ----------------------------------- |
| #changes             | 版本控制變更的列表。                |
| #codebase            | 工作區中所有程式碼。                |
| #editor              | 當前編輯器中可見的程式碼。          |
| #file                | 從工作區中選擇檔案。                |
| #folder              | 從工作區中選擇資料夾。              |
| #selection           | 當前編輯器中選取的程式碼。          |
| #sym                 | 從工作區中選擇符號(symbol)。        |
| #terminalSelection   | 當前終端機中目前選取的內容。        |
| #terminalLastCommand | 當前終端機的最後執行的指令。        |
| #VSCodeAPI           | VS Code API 及擴展 API 的官方文件。 |

## #changes

| 需求                 | 提示詞範例                             |
| -------------------- | -------------------------------------- |
| 總結工作區的變更內容 | summarize the #changes in my workspace |

## #selection

| 需求               | 提示詞範例                                                   |
| ------------------ | ------------------------------------------------------------ |
| 選取程式碼改成函式 | Refactor #selection into a well-named, reusable function with clear input and output. |

## #codebase

### 設定

| 功能項目                                       | 設定內容 | 功能描述                                     |
| ---------------------------------------------- | -------- | -------------------------------------------- |
| github.copilot.chat.codesearch.enabled         | V        | 啟用`#codebase`原始碼搜尋。                  |
| github.copilot.chat.search.semanticTextResults | V        | 啟用語意搜尋結果(一般搜尋是透過關鍵字比對)。 |

### 範例

將工作區所有程式碼當成提示的上下文。

![10.codebase](https://firebasestorage.googleapis.com/v0/b/stellacoding1111.appspot.com/o/article%2Fgithub-copilot-vscode-ai-coding%2F10.codebase.jpg?alt=media&token=53c3d304-c533-4c98-8be2-03cd39818f8c)

| 需求                   | 提示詞範例                           |
| ---------------------- | ------------------------------------ |
| 找出專案開始執行的位置 | Find out the entry of the #codebase. |

# 語音辨識

## 語音即時轉錄

### 安裝套件

- [VS Code Speech](https://marketplace.visualstudio.com/items?itemName=ms-vscode.vscode-speech)
- [Chinese (Traditional, Taiwan) language support for VS Code Speech](https://marketplace.visualstudio.com/items?itemName=ms-vscode.vscode-speech-language-pack-zh-tw)

### 設定轉錄語言

進入設定，找到 `accessibility.voice.speechLanguage`，選擇 `Chinese (Traditional, Taiwan)`，則語音輸入的語言會設定為繁體中文。

![11.accessibility-voice-speechLanguage-chinese-traditional-taiwan](https://firebasestorage.googleapis.com/v0/b/stellacoding1111.appspot.com/o/article%2Fgithub-copilot-vscode-ai-coding%2F11.accessibility-voice-speechLanguage-chinese-traditional-taiwan.jpg?alt=media&token=55cd1ab8-99f5-43a3-a832-fa082ab6ffc4)

設定完成後，鍵盤按「Ctrl+Alt+V(Cmd+Opt+V)」即開始語音即時轉錄，游標位置會有小麥克風圖示。若想要停止語音即時轉錄點擊「Esc」則可離開語音即時轉錄。

設定語音輸入後可停頓的時間為 1.2 秒:
`accessibility.voice.speechTimeout`: `1200`
(只要語音停頓 1.2 秒，就會送出輸入內容，可以依照自己的語速調整)

## Hey Code

可以啟用 VS Code 隨時監聽「Hey Code」這個關鍵詞，並立即啟動語音輸入功能。

進入設定，找到 `accessibility.voice.keywordActivation`，選擇 `chatInContext`。

- chatInView: 在 Chat View 開始語音輸入。
- quickChat: 在 Quick Chat 開始語音輸入。
- inlineChat: 在 Inline Chat 開始語音輸入。
- chatInContext: 自動判斷在 Inline Chat 或 Chat View 開始語音輸入。

![12.accessibility-voice-keywordActivation-chatInContext](https://firebasestorage.googleapis.com/v0/b/stellacoding1111.appspot.com/o/article%2Fgithub-copilot-vscode-ai-coding%2F12.accessibility-voice-keywordActivation-chatInContext.jpg?alt=media&token=72f53dc4-db94-4dcb-ba92-0e0872c5eada)

# 常用鍵與功能

## 鍵盤快捷鍵

| 快捷鍵                           | 描述                                                         |
| -------------------------------- | ------------------------------------------------------------ |
| Ctrl+I Cmd+I                     | 啟動Inline Chat，從編輯器向 Copilot 詢問問題。               |
| Ctrl+Alt+I Cmd+Control+I         | 啟動Chat，使用自然語言詢問問題。                             |
| Ctrl+Shift+I Cmd+Shift+I         | 啟動Copilot Edits，會在多個檔案中直接修改程式碼。            |
| Ctrl+Shift+Alt+L Cmd+Shift+Opt+L | 啟動Quick Chat。                                             |
| `@`                              | 在Chat中輸入`@`，可選擇代理，這些代理是特定領域的專家，如`@workspace`。 |
| `/`                              | 在Chat中輸入`/`，可選擇代理執行特定任務，如產生測試、解釋程式碼等，如`/explain`。 |
| `#`                              | 在Chat中輸入`#`，可選擇變數，如`#codebase`，將相關的工作區程式碼作為提示的上下文。 |
| Ctrl+Alt+V Cmd+Opt+V             | 開始語音辨識，啟動後會在游標所在位置顯示一個小麥克風圖示，並保持啟用狀態，等待語音輸入。`Esc`則可停止語音辨識。 |

在 GitHut Copilot 圖示的下拉式選單中也有提示鍵盤快捷鍵。
![13.github-copilot-function-keyboard-shortcut](https://firebasestorage.googleapis.com/v0/b/stellacoding1111.appspot.com/o/article%2Fgithub-copilot-vscode-ai-coding%2F13.github-copilot-function-keyboard-shortcut.jpg?alt=media&token=732d7b0c-0adf-4429-bd08-8f9da816e731)

![13.github-copilot-function-keyboard-shortcut-mac](https://firebasestorage.googleapis.com/v0/b/stellacoding1111.appspot.com/o/article%2Fgithub-copilot-vscode-ai-coding%2F13.github-copilot-function-keyboard-shortcut-mac.jpg?alt=media&token=50bf3c9d-668c-4d8e-926f-413c8954bf11)

## 功能圖示

| 圖示 | 描述                                                         |
| ---- | ------------------------------------------------------------ |
|      | 在Chat選擇 可建立一個全新的chat。                            |
|      | 在Chat選擇 可存取過往的聊天紀錄。                            |
|      | 在Chat選擇 可以看到更多功能，如在編輯器或新視窗中開啟Chat等。 |
|      | 語音輸入內容且Copilot會朗讀回應內容。                        |

# 其他好用功能

## Code Review

選取一段程式碼後，右鍵選擇「Review and Comment」，GitHub Copilot 會審查程式碼並提供建議。

![14.github-copilot-review-comment-1](https://firebasestorage.googleapis.com/v0/b/stellacoding1111.appspot.com/o/article%2Fgithub-copilot-vscode-ai-coding%2F14.github-copilot-review-comment-1.jpg?alt=media&token=10fd2e68-2f58-4afa-969d-5e7da6b6a584)

![14.github-copilot-review-comment-2](https://firebasestorage.googleapis.com/v0/b/stellacoding1111.appspot.com/o/article%2Fgithub-copilot-vscode-ai-coding%2F14.github-copilot-review-comment-2.jpg?alt=media&token=41b83a72-5f25-4e53-9aed-ba9b95d24d95)

## 提交訊息

在 VS Code 的 Source Control 面板中，GitHub Copilot 提供自動生成提交訊息的功能，幫助開發者快速撰寫清晰且符合變更內容的提交訊息，大大提升 Git 工作流程的效率。(以後就不會只看到 fix bug 或 update 這種的提交訊息了😂)

![15.generate-commit-message-with-copilot-1](https://firebasestorage.googleapis.com/v0/b/stellacoding1111.appspot.com/o/article%2Fgithub-copilot-vscode-ai-coding%2F15.generate-commit-message-with-copilot-1.jpg?alt=media&token=74d56e86-a828-4b17-bbfe-eda8b240fc2d)

(資料來源: [AI Agents for Beginners)](https://github.com/microsoft/ai-agents-for-beginners)

![15.generate-commit-message-with-copilot-2](https://firebasestorage.googleapis.com/v0/b/stellacoding1111.appspot.com/o/article%2Fgithub-copilot-vscode-ai-coding%2F15.generate-commit-message-with-copilot-2.jpg?alt=media&token=c132098c-08e3-492c-b839-8a0c8617a2b5)

關於如何根據慣例式規範自動生成的提交訊息，請看 [【GitHub Copilot】自動生成慣例式提交訊息](https://estellacoding.github.io/blog/github-copilot-vscode-ai-conventional-commit)。

## Copilot Web

GitHub Copilot Chat 還有提供網頁版。

- 可以在 [GitHub Copilot Chat](https://github.com/copilot) 詢問程式碼的相關問題。
- 也可在 GitHub 倉庫(repo)內使用「Chat with Copilot」詢問該倉庫的問題。

![16.gitHub-copilot-chat-web-1](https://firebasestorage.googleapis.com/v0/b/stellacoding1111.appspot.com/o/article%2Fgithub-copilot-vscode-ai-coding%2F16.gitHub-copilot-chat-web-1.jpg?alt=media&token=3670a825-1efe-4928-878c-02b478ff301d)

(資料來源: [Microsoft Visual Studio Code)](https://github.com/microsoft/vscode)

![16.gitHub-copilot-chat-web-icon](https://firebasestorage.googleapis.com/v0/b/stellacoding1111.appspot.com/o/article%2Fgithub-copilot-vscode-ai-coding%2F16.gitHub-copilot-chat-web-icon.jpg?alt=media&token=c9f1e986-c26b-4fea-ac09-101fab010ac4)

## Mermaid

### Microsoft

安裝套件 [vscode-mermAId](https://marketplace.visualstudio.com/items?itemName=ms-vscode.copilot-mermaid-diagram)，即可在 Chat 視窗中使用 `@mermAId` 繪製流程圖等可視化圖表。

![github-copilot-microsoft-mermaid-example](https://raw.githubusercontent.com/microsoft/vscode-mermAId/refs/heads/main/assets/gifs/01.gif)

(資料來源: [Microsoft vscode-mermAId)](https://github.com/microsoft/vscode-mermAId)

### Mermaid

前往 [Github Marketplace Copilot Extensions](https://github.com/marketplace?type=apps&copilot_app=true)，找到並安裝 Mermaid Chart 擴充套件，即可在 Chat 視窗中使用 `@mermaid-chart` 繪製流程圖等可視化圖表。

![github-copilot-mermaid-chart-example](https://marketplace-screenshots.githubusercontent.com/19169/cd324751-f43d-4bf1-8f64-78b0bc9c6978)

(資料來源: [Github Marketplace Copilot Extensions - Mermaid Chart)](https://github.com/marketplace/mermaid-chart)

## Commander

安裝套件 [VS Code Commander](https://marketplace.visualstudio.com/items?itemName=ms-vscode.vscode-commander)，即可在 Chat 視窗中使用 `@commander` 設定 VS Code 環境。

| 需求         | 提示詞範例                      |
| ------------ | ------------------------------- |
| 設定淺色主題 | @commander Set theme to Light+. |

# 參考文件

[GitHub Copilot in VS Code cheat sheet](https://code.visualstudio.com/docs/copilot/overview)
[GitHub Copilot in VS Code Voice Interactions](https://code.visualstudio.com/docs/editor/voice)
[保哥的最佳 GitHub Copilot 設定🫡](https://github.com/doggy8088/github-copilot-configs)