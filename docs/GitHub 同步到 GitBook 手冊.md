---
kind: original
---

# GitHub 同步到 GitBook 手冊

這份筆記庫同時發布到兩個網站，內容來源都是這個 repo 的 `main` 分支：

| 網站 | 網址 | 怎麼更新 |
|---|---|---|
| GitHub Pages（MkDocs） | https://kerryhuang.github.io/Book/ | push 到 `main` 後，GitHub Actions 的「部署文件網站到 GitHub Pages」workflow 自動建置 |
| GitBook | https://kerryhuangs-organization.gitbook.io/kerry-de-bi-ji-ben/ | GitBook 的 Git Sync 監看 `main`，有新 commit 就同步 |

這份手冊只講 GitBook 那條線。GitHub Pages 的建置方式見根目錄 README 的「慣例」段。

## 一、現在的設定長怎樣

以下是 2026-11-27 從 repo 與 GitBook 網站查到的狀況：

- **同步方式**：GitBook 的 GitHub Sync，透過 GitBook 的 GitHub App（`gitbook-com`）連到 `KerryHuang/Book` 的 `main`。
- **啟用時間**：至少從 2023 年就在用。repo 裡有一筆 GitBook 寫回的 commit：2023-08-09，作者 `gitbook-bot`，訊息「GITBOOK-1: change request with no subject merged in GitBook」。
- **repo 裡沒有 `.gitbook.yaml`，也沒有 `SUMMARY.md`**：GitBook 用預設值，以根目錄的 `README.md` 當首頁，目錄依資料夾與 Markdown 檔自動推導。所以 GitBook 側欄除了七個知識領域，也會出現 `scripts/` 和這個 `docs/`。GitHub Pages 那邊由 `.pages` 列出導覽項目，不會出現這兩個資料夾。
- **GitBook 的 space**：在 GitBook 的組織 `kerryhuangs-organization` 底下，space 網址代稱是 `kerry-de-bi-ji-ben`（「Kerry 的筆記本」的拼音）。

## 二、日常寫作流程

### 在本機或 GitHub 寫（建議的主要方式）

1. 寫之前先 `git pull`，把 GitBook 可能寫回的改動拉下來。
2. 照根目錄 README「慣例」段的做法：文章放進對應領域目錄、加上 front matter、執行 `python scripts/gen-readme.py` 重產 README。
3. commit 並 push 到 `main`。
4. 兩個網站各自更新：GitHub Pages 看 Actions 的 workflow 跑完；GitBook 由 Git Sync 自動同步。⚠️ GitBook 官方文件沒寫 push 後多久會反映，實際以 GitBook 網站看到新內容為準。

### 在 GitBook 網頁上改

1. 在 GitBook 開一個 change request 編輯。
2. merge change request 之後，GitBook 會把改動 commit 回 GitHub 的 `main`。作者會是 `gitbook-bot`，訊息格式像上面那筆「GITBOOK-N: …」。
3. 回到本機繼續寫之前，記得先 `git pull`。

### 避免衝突的原則

- **同一篇文章不要兩邊同時改**。挑一邊寫完、同步完，再換另一邊。
- **不要在 GitBook 新增 `README.md`**：GitBook 官方提醒這會造成重複與顯示衝突。各資料夾的 README 由 `scripts/gen-readme.py` 產生。
- **在 GitBook 新增的頁面，檔名由 GitBook 決定**，不一定沿用既有命名習慣。這是 GitBook 的預期行為。在 GitBook 新增後，記得到 repo 補 front matter，再重跑 `gen-readme.py`。
- **GitHub 的 pull request 不會變成 GitBook 的 change request**，只有 merge 進 `main` 之後才會同步。

## 三、從零設定（或重新連線）

GitBook 介面會改版，以下照 GitBook 官方文件的步驟寫，按鈕名稱以實際畫面為準。只有 GitBook 的管理員（administrator）或建立者（creator）能設定。

1. **確認 GitHub App 權限**：到 GitHub 的 Settings → Applications → Installed GitHub Apps，找到 GitBook（`gitbook-com`）→ Configure，確認 Repository access 裡有 `KerryHuang/Book`。沒有安裝的話，設定流程中 GitBook 會引導你安裝。
2. **在 GitBook 開啟 Git Sync**：進入 site 或 space，在側邊欄或 space 標題列找到 Git Sync 的 Set up，選 GitHub Sync。
3. **連結 GitHub 帳號**：用有 `Book` repo 權限的 GitHub 帳號登入授權。
4. **選 repo 與分支**：Source repository 選 `KerryHuang/Book`，branch 選 `main`。
5. **選初次同步方向**（最重要的一步）：
   - 預設是**以 GitBook 內容為準**，會用 GitBook 的內容覆寫 repo。
   - 勾選 **Swap direction** 改成**以 GitHub 內容為準**，會用 repo 的內容取代 GitBook 的內容。
   - 這個 repo 一直以 GitHub 為主，**重新連線時要勾 Swap direction**，否則 GitBook 上較舊的內容可能蓋掉 repo。萬一 GitBook 那邊被蓋掉，可以從 GitBook 的 Version history 還原。
6. **Project directory 留空**：這個 repo 的文章從根目錄開始，不是 monorepo。
7. 按 **Sync** 開始初次同步，等 GitBook 顯示同步完成。

## 四、選用：用 `.gitbook.yaml` 調整 GitBook 的內容

目前沒有這個檔，GitBook 全用預設值。需要調整時，在 repo 根目錄新增 `.gitbook.yaml`：

```yaml
root: ./

structure:
  readme: README.md
  summary: SUMMARY.md

redirects:
  舊路徑/舊頁: 新資料夾/新頁.md
```

- `root`：GitBook 從哪個目錄讀內容，預設 `./`。
- `structure.readme`：首頁檔，預設 `README.md`。
- `structure.summary`：目錄檔，預設 `SUMMARY.md`。
- `redirects`：文章搬家後，把舊網址導到新檔。路徑不加開頭的 `/`；舊頁還存在時 redirect 不會生效。YAML 縮排錯了，redirect 會整個失效。

**想讓 `scripts/`、`docs/` 不出現在 GitBook 側欄**，就要自己維護 `SUMMARY.md`：只有列在 `SUMMARY.md` 裡的檔案才會出現在 GitBook。代價是之後每新增一篇文章，都要記得把它加進 `SUMMARY.md`。GitBook 第一次同步時若沒有 `SUMMARY.md`，會自動建一份，可以拿它當起點刪改。

## 五、疑難排解

| 狀況 | 處理方式 |
|---|---|
| 同步卡住，或 GitBook 顯示 unexpected error | 錯誤發生在 GitBook merge change request 時：在 GitBook 開一個小改動的 change request 再 merge 一次。發生在 GitHub 這邊時：在 repo 推一個小 commit。首次設定就失敗：移除 GitHub 整合後重新設定（見第三節）。 |
| 錯誤訊息「Missing permissions to push to the refs/heads/... protected branch」 | `main` 開了分支保護。到 GitHub 的 branch protection 設定，讓 `gitbook-com` 可以略過「Require a pull request before merging」和「Restrict who can push」。 |
| GitBook 找不到 repo，或授權失敗 | 到 GitHub 的 GitBook App 設定（見第三節第 1 步），把 `Book` 加進 Repository access。 |
| 某篇文章沒出現在 GitBook | 有 `SUMMARY.md` 的話，檢查它有沒有列進去。沒有的話，檢查副檔名是不是 `.md`。 |
| 同步被擋，提到 unsafe 檔案 | GitBook 會擋 `.js` 這類檔案。到 GitBook 的 Files 分頁刪掉那個檔再 merge。 |
| 檔案太大 | GitBook 單檔上限 100MB。這個 repo 的影片（mp4）走 Git LFS，⚠️ GitBook 會不會抓 LFS 實體檔，官方文件沒寫，未驗證。 |

## 六、停用或改連其他 repo／分支

- **改連其他 repo 或分支**：在 GitBook 的 Git Sync 設定裡重新設定連線，等於再做一次初次同步，要重新選同步方向（見第三節第 5 步）。
- **完全停用**：在 GitBook 移除 GitHub 整合；要徹底斷開的話，再到 GitHub 的 Installed GitHub Apps 把 GitBook App 的 `Book` 權限拿掉，或整個解除安裝。⚠️ GitBook 官方文件沒寫停用的完整步驟，按鈕位置以實際畫面為準。
- 停用之後 GitBook 網站還在，只是不再跟著 repo 更新。

## 七、官方文件沒寫、未驗證的事

下面幾項 GitBook 官方文件沒有寫，要到 GitBook 介面實際確認：

- GitHub push 之後，GitBook 多久會更新。
- 手動重新同步（re-sync）的按鈕在哪。
- 免費方案能不能用 Git Sync、有沒有次數或容量限制。
- GitBook 寫回 GitHub 時預設的 commit 訊息格式（目前只看過 2023 年那一筆）。

## 參考資料

- GitBook 官方文件：[Git Sync 概觀](https://gitbook.com/docs/docs-as-code/git-sync)
- [Enabling GitHub Sync](https://gitbook.com/docs/docs-as-code/git-sync/enabling-github-sync)
- [Content configuration（.gitbook.yaml）](https://gitbook.com/docs/getting-started/git-sync/content-configuration)
- [Troubleshooting](https://gitbook.com/docs/docs-as-code/git-sync/troubleshooting)
