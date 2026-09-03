---
kind: original
---

# Git 語法大全

### 1. 基本指令

- `git init`：初始化一個空的 Git 儲存庫。
- `git status`：顯示工作目錄和暫存區的狀態。
- `git add <file>`：將檔案新增到暫存區。
- `git rm <file>`：從工作目錄和索引中移除檔案。
- `git commit -m "message"`：將暫存區的更改提交到儲存庫，並附上提交訊息。
- `git log`：顯示提交歷史紀錄。
- `git config`：git 設定。

### 2. 檢視和比較

- `git diff`：顯示未暫存的更改。
- `git diff --staged`：顯示已暫存但尚未提交的更改。
- `git show <commit>`：顯示指定提交的詳細內容。

### 3. 分支（Branch）操作

- `git branch`：列出所有分支。
- `git branch <branch_name>`：建立新分支。
- `git branch -d <branch_name>`：刪除已合併的分支。
- `git checkout <branch_name>`：切換到指定分支。
- `git checkout -b <branch_name>`：建立並切換到新分支。
- `git merge <branch_name>`：將指定分支的更改合併到當前分支。

### 4. 暫存和回復

- `git stash`：將未提交的更改暫時儲存起來。
- `git stash pop`：恢復暫存的更改並將其從暫存區移除。
- `git reset <file>`：取消指定檔案的暫存狀態。
- `git reset --hard <commit>`：將工作目錄和暫存區重置到指定的提交版本。

### 5. 遠端（Remote）操作

- `git remote add <name> <url>`：新增遠端儲存庫。
- `git remote -v`：顯示遠端儲存庫的名稱和 URL。
- `git fetch <remote>`：從遠端儲存庫下載資料但不合併。
- `git pull <remote> <branch>`：從遠端儲存庫下載並合併分支。
- `git push <remote> <branch>`：將本地分支推送到遠端儲存庫。

### 6. 標籤（Tag）操作

- `git tag <tag_name>`：建立輕量標籤。
- `git tag -a <tag_name> -m "message"`：建立帶訊息的註釋標籤。
- `git tag -d <tag_name>`：刪除本地標籤。
- `git push origin <tag_name>`：將標籤推送到遠端。
- `git push origin --tags`：將所有標籤推送到遠端。

### 7. 進階指令

- `git rebase <branch>`：將一個分支的提交應用到另一個分支之上。
- `git cherry-pick <commit>`：應用指定提交的更改到當前分支。
- `git revert <commit>`：建立新提交，撤銷指定提交的更改。
- `git blame <file>`：顯示每行程式碼的最後更改記錄（誰在何時修改）。

### 8. 低階指令

- `git cat-file -p <SHA1>`：顯示 Git 物件內容。
- `git ls-files`：顯示目前在索引中的檔案。
- `git rev-parse <revision>`：解析修訂版本名稱或其他參數。

---

### 監看

```
watch -n 1 -d find .
```

