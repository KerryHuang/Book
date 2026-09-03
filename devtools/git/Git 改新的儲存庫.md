---
kind: original
---

# 將現有專案的遠端儲存庫直接更改為新的儲存庫

如果您已經在本地有現有專案並且已經初始化 Git，可以將遠端儲存庫 URL 更改為新的儲存庫，並推送現有的內容。

1. **進入專案目錄**

   ```bash
   cd <existing-project-directory>
   ```

2. **更新遠端儲存庫的 URL**

   ```bash
   git remote set-url origin <new-repository-url>
   ```

3. **將所有分支和標籤推送到新的儲存庫**

   ```bash
   git push -u origin --all
   git push origin --tags
   ```

這樣可以將現有專案的所有內容複製到新的儲存庫中，而無需重新克隆。