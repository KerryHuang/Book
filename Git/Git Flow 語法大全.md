# **Git Flow 指令大全（完整指令整理）** 🚀

Git Flow 是 Git 的一種分支管理策略，它透過 `git-flow` 命令來簡化 **開發 (Feature)**、**發佈 (Release)**、**熱修復 (Hotfix)** 等流程。

------

## **📌 1. 安裝 Git Flow**

### **🔹 Windows**

使用 **Scoop** (推薦)：

```sh
scoop install git-flow-avh
```

使用 **Chocolatey**：

```sh
choco install gitflow-avh -y
```

使用 **Git Bash (手動安裝)**：

```sh
git clone --depth=1 https://github.com/petervanderdoes/gitflow-avh.git
cd gitflow-avh
make install
```

### **🔹 macOS**

使用 **Homebrew (推薦)**

```sh
brew install git-flow-avh
```

使用 **MacPorts**

```sh
sudo port install git-flow
```

### **🔹 Linux (Ubuntu/Debian)**

```sh
sudo apt install git-flow
```

確認安裝成功：

```sh
git flow version
```

------

## **📌 2. 初始化 Git Flow**

Git Flow 需要在 **每個 Git 專案中初始化一次**：

```sh
git flow init
```

你會被問到以下問題，通常可以直接按 **Enter** 接受預設值：

```mathematica
Which branch should be used for production releases?
- main

Which branch should be used for integration of the "next release"?
- develop

Feature branches? (feature/)
Release branches? (release/)
Hotfix branches? (hotfix/)
```

✅ **初始化完成後，會建立 `develop` 分支**，用於日常開發。

------

## **📌 3. 開發新功能 (Feature Branch)**

當你要開發新功能時：

```sh
git flow feature start <feature-name>
```

例如：

```sh
git flow feature start login-page
```

這會： ✅ 建立 `feature/login-page` 分支
 ✅ 自動切換到該分支

🔹 **提交變更**

```sh
git add .
git commit -m "完成登入頁面"
```

🔹 **分享 Feature 分支到遠端**

```sh
git flow feature publish <feature-name>
```

🔹 **其他開發者拉取這個 Feature 分支**

```sh
git flow feature pull origin <feature-name>
```

🔹 **完成功能開發，合併回 `develop`**

```sh
git flow feature finish <feature-name>
```

這會： ✅ 合併 `feature` 到 `develop`
 ✅ 切換回 `develop` 分支
 ✅ **刪除本地 `feature` 分支**

🔹 **推送最新的 `develop` 分支**

```sh
git push origin develop
```

------

## **📌 4. 發佈新版本 (Release Branch)**

當 `develop` 分支的功能準備發佈時：

```sh
git flow release start <version>
```

例如：

```sh
git flow release start v1.0
```

這會： ✅ 建立 `release/v1.0` 分支
 ✅ 讓你可以修正最後的 Bug 或新增說明文件

🔹 **如果需要修正錯誤**

```sh
git add .
git commit -m "修正錯誤"
```

🔹 **完成發佈**

```sh
git flow release finish <version>
```

這會： ✅ 合併 `release/v1.0` 到 `main`
 ✅ **建立 Tag `v1.0`**
 ✅ **合併 `release/v1.0` 到 `develop`** (確保最新的 `develop` 包含這些變更)
 ✅ **刪除 `release/v1.0` 分支**

🔹 **推送更新到遠端**

```sh
git push origin main develop --tags
```

------

## **📌 5. 修復緊急 Bug (Hotfix Branch)**

如果 `main` 分支的正式版本有 **重大 Bug**，請使用 **Hotfix** 分支：

```sh
git flow hotfix start <hotfix-name>
```

例如：

```sh
git flow hotfix start fix-login-bug
```

這會： ✅ **從 `main` 建立 `hotfix/fix-login-bug` 分支**

🔹 **修正錯誤後，提交變更**

```sh
git add .
git commit -m "修正登入 Bug"
```

🔹 **完成修正**

```sh
git flow hotfix finish <hotfix-name>
```

這會： ✅ **合併 `hotfix` 到 `main`**
 ✅ **建立 Tag (標記修正版本)**
 ✅ **合併 `hotfix` 到 `develop`** (讓 `develop` 也包含修正)
 ✅ **刪除 `hotfix` 分支**

🔹 **推送更新**

```sh
git push origin main develop --tags
```

------

## **📌 6. 列出當前 Git Flow 分支**

🔹 **查看所有 Feature 分支**

```sh
git flow feature list
```

🔹 **查看所有 Release 分支**

```sh
git flow release list
```

🔹 **查看所有 Hotfix 分支**

```sh
git flow hotfix list
```

------

## **📌 7. 刪除 Git Flow 分支**

🔹 **刪除本地 `feature` 分支**

```sh
git branch -D feature/<feature-name>
```

🔹 **刪除遠端 `feature` 分支**

```sh
git push origin --delete feature/<feature-name>
```

🔹 **刪除本地 `release` 分支**

```sh
git branch -D release/<release-name>
```

🔹 **刪除遠端 `release` 分支**

```sh
git push origin --delete release/<release-name>
```

🔹 **刪除本地 `hotfix` 分支**

```sh
git branch -D hotfix/<hotfix-name>
```

🔹 **刪除遠端 `hotfix` 分支**

```sh
git push origin --delete hotfix/<hotfix-name>
```

------

## **📌 8. 其他實用指令**

🔹 **切換分支**

```sh
git flow feature checkout <feature-name>
git flow release checkout <release-name>
git flow hotfix checkout <hotfix-name>
```

🔹 **檢查 Git Flow 設定**

```sh
git config --list | grep gitflow
```

🔹 **查看 Git Flow 工作流程**

```sh
git log --oneline --decorate --graph --all
```

🔹 **變更 Git Flow 預設編輯器**

```sh
git config --global core.editor "nano"  # 使用 nano
git config --global core.editor "code --wait"  # 使用 VS Code
```

------

## **📌 9. 停止使用 Git Flow**

如果你不想再使用 Git Flow：

```sh
git flow init -d
```

或手動刪除 Git Flow 設定：

```sh
git config --remove-section gitflow
```

------

### **🎯 總結**

- **新功能開發** → `git flow feature start/finish`
- **準備發佈** → `git flow release start/finish`
- **修復緊急 Bug** → `git flow hotfix start/finish`
- **查看目前流程** → `git flow feature/release/hotfix list`
- **刪除 Git Flow 分支** → `git branch -D` 或 `git push origin --delete`

這份 **Git Flow 指令大全** 可以幫助你更有效率地管理專案！🚀
 如果有任何問題，歡迎隨時問我 😊