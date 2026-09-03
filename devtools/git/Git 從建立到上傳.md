---
kind: original
---

# Git 建立到上傳

將現有的 .NET 專案上傳到 GitLab 的步驟如下：

1. **創建 GitLab 專案：**

   - 登入 GitLab，點擊「New Project」按鈕，選擇「Create blank project」。
   - 設定專案名稱、訪問權限等，並完成專案創建。
   - 建立後會看到一個「HTTPS」或「SSH」的 URL，稍後會用到。

2. **初始化本地 Git 儲存庫：**

   - 開啟命令提示字元或終端機，導航至專案的根目錄。

   - 如果還沒有初始化 Git 儲存庫，請執行以下命令：

     ```bash
     git init
     ```

3. **將檔案加入 Git：**

   - 執行以下指令將所有檔案加入 Git 的追蹤列表：

     ```bash
     git add .
     ```

   - 接著提交初始版本：

     ```bash
     git commit -m "Initial commit"
     ```

4. **連結遠端儲存庫 (GitLab)：**

   - 使用專案創建時的 URL（HTTPS 或 SSH）將本地儲存庫連結到 GitLab 遠端儲存庫。

     ```bash
     git remote add origin <your-gitlab-repo-url>
     ```

5. **檢查並切換到 `main` 分支  (選擇性)**

   **檢查目前分支名稱**
   使用以下指令查看目前的分支名稱：

   ```bash
   git branch
   ```

   如果目前的分支是 `master` 而不是 `main`，則需要創建並切換到 `main` 分支。

   **創建並切換到 `main` 分支**
   執行以下指令以將當前分支改名為 `main` 並推送到遠端：

   ```bash
   git branch -M main
   ```

6. **將遠端更改合併到本地 (選擇性)**

   **拉取（pull）遠端的更改並合併**
   執行以下指令，將遠端儲存庫的更改拉取到本地並進行合併：

   ```bash
   git pull origin main --rebase
   ```

   此指令會使用 `rebase` 的方式將遠端的提交紀錄放在你的本地提交紀錄之前，確保紀錄順序更整齊。

   **解決合併衝突（如果有的話）**
   如果拉取過程中出現合併衝突，Git 會提示你手動解決。打開衝突檔案，解決完衝突後，提交這些變更：

   ```bash
   git add .
   git commit -m "Resolve merge conflicts"
   ```

7. **推送專案到 GitLab：**

   - 將本地專案推送到 GitLab，並設定`origin`

     作為默認的上傳位置：

     ```bash
     git push -u origin master
     ```
     
   - 如果 GitLab 的默認分支是`main`

     ，可改成以下指令：

     ```bash
     git push -u origin main
     ```
   
8. **確認上傳成功：**

   - 回到 GitLab 頁面並刷新，應該能看到剛剛上傳的專案內容。