---
kind: reprint
source: site:ithelp.ithome.com.tw
---

# 第5章 - [Redmine]Redmine系統邏輯說明

------

使用Redmine基本邏輯及順序是這樣子的：

1. 要設計好組織與專案人員架構。
2. 根據你的架構設定適當的使用者、角色，並設定好相對應的權限。
3. 設定好各式Tracker，也就是你要追蹤管理的標的以及它的狀態與流程。
4. 做好教育訓練， 讓你的團隊成員充分了解你所定義的流程與角色。
5. 督促專案成員/使用者詳實紀錄各自的工作狀況與結果。
6. 定時檢討流程與改善

------

### 本篇將學習到Redmine的功能重點

- 【使用者視野-基本流程】
- 【專案管理員視野-基本流程】
- 【Redmine系統功能說明】
  - 專案管理
  - 議題(Issue)管理
  - 角色與權限
  - 流程
  - 用戶清單
  - 群組清單
  - 追蹤標籤清單
  - 議題狀態清單

------

### 【使用者視野-基本流程】

1. 開啟專案
2. 開啟議題
3. 建立新議題
4. 查看議題的狀態

以下為在系統頁面功能操作的簡單介紹。

**[網站首頁]**

- 網站首頁只會看到網站簡介(圖1)
  ![https://ithelp.ithome.com.tw/upload/images/20220913/20151950y93wcowFCJ.png](https://ithelp.ithome.com.tw/upload/images/20220913/20151950y93wcowFCJ.png)

**[專案清單]**

- 點選[專案清單]，才會看到有授權的專案清單。
- 若要跳過網站首頁直接取得這一頁的連結，系統預設是：`http://網站IP/redmine/projects` (圖2)
  ![https://ithelp.ithome.com.tw/upload/images/20220913/20151950HqAqTQ6rwd.png](https://ithelp.ithome.com.tw/upload/images/20220913/20151950HqAqTQ6rwd.png)
- 要特別注意的是，若未登入，一般User看到的只有"公開"的專案。
- 若專案的設定[公開]未打勾，只有該專案的成員在登入後才能看到未公開的專案(圖3)
  ![https://ithelp.ithome.com.tw/upload/images/20220913/20151950AVmTNnb17t.png](https://ithelp.ithome.com.tw/upload/images/20220913/20151950AVmTNnb17t.png)
- 使用者[登入] (圖4)
  ![https://ithelp.ithome.com.tw/upload/images/20220913/20151950VfJBzj0vYk.png](https://ithelp.ithome.com.tw/upload/images/20220913/20151950VfJBzj0vYk.png)
- 點選要進入的專案 (圖5)
  ![https://ithelp.ithome.com.tw/upload/images/20220913/20151950qs7SRIlx1W.png](https://ithelp.ithome.com.tw/upload/images/20220913/20151950qs7SRIlx1W.png)
- 看到該專案已經建立的Issue進度概況 (圖6)
  ![https://ithelp.ithome.com.tw/upload/images/20220913/20151950PwZMKBSfXV.png](https://ithelp.ithome.com.tw/upload/images/20220913/20151950PwZMKBSfXV.png)
- 若要建立新議題(Issue)，[議題清單]/[建立新議題]
  - 註：若你沒登入(匿名者)，可以看到此專案卻在這一頁沒看到[建立新議題]的連結功能，代表匿名者(未登入者)只有瀏覽沒有建立新Issue的權限。(圖7、8)

![https://ithelp.ithome.com.tw/upload/images/20220913/201519509BHQqI4QZp.png](https://ithelp.ithome.com.tw/upload/images/20220913/201519509BHQqI4QZp.png)
![https://ithelp.ithome.com.tw/upload/images/20220913/20151950XNmqJ5mjuU.png](https://ithelp.ithome.com.tw/upload/images/20220913/20151950XNmqJ5mjuU.png)

------

### 【專案管理員視野-基本流程】

**1. 建立專案**

- (1)建立專案基本資料設定
- (2)需要的模組設定
- (3)專案成員及權限設定

**2. 議題設定**

- (1)議題基本資料設定
- (2)議題追蹤標籤設定
- (3)議題需求欄位設定(自訂欄位)

**3. 專案平台開始使用**

- (1)專案成員/一般User 建立議題
- (2)被指定/被授權之專案成員編輯、更新議題之欄位資訊(例如完成進度、狀態)
- (3)專案議題追蹤狀態、分析統計

#### 操作畫面如下：

**1. 建立新專案**

- [專案清單]/[建立新專案] (圖9、10)
  ![https://ithelp.ithome.com.tw/upload/images/20220913/20151950aYgWFwy6WF.png](https://ithelp.ithome.com.tw/upload/images/20220913/20151950aYgWFwy6WF.png)
  ![https://ithelp.ithome.com.tw/upload/images/20220913/20151950rtY38oz4Tj.png](https://ithelp.ithome.com.tw/upload/images/20220913/20151950rtY38oz4Tj.png)

**2. 議題設定**

- 進入專案後，[設定]/[議題追蹤]，設定[追蹤標籤清單]及[自訂欄位清單] (圖11)
  ![https://ithelp.ithome.com.tw/upload/images/20220913/20151950aY8fMCrJQb.png](https://ithelp.ithome.com.tw/upload/images/20220913/20151950aY8fMCrJQb.png)

**3. 專案平台開始使用**

- 完成後，如本篇一開始的【使用者視野-基本流程】的說明，就可以看到設定的專案和自訂的議題欄位，並建立新的Issue。

------

### 【Redmine系統功能說明】

#### -- [Redmine系統]_專案管理

- 概觀 – 快速總覽 (Bug、進度… 等)
- 活動 – 最近相關異動
- 議題清單 – Ticket List, Issue tracking.
- 甘特圖 – 議題的狀態以甘特圖方式顯示
- 日曆 – 以日曆的方式顯示議題的狀態
- 新聞 – 發布/顯示專案的消息
- 文件 – 提供文件存放區域.
- Wiki – 多人協同寫作的系統
- 檔案清單 – 提供檔案上傳或下載的區域.
  (圖12)
  ![https://ithelp.ithome.com.tw/upload/images/20220913/20151950jQJvTMFWPq.png](https://ithelp.ithome.com.tw/upload/images/20220913/20151950jQJvTMFWPq.png)

#### -- [Redmine系統]_議題(Issue)管理

- 在Redmine系統中, 發現的錯誤、新提的要求、對工作的安排等都可以被當作問題/議題(Issue)來處理
- Issue是一個過程性的概念, 從提出問題到解決問題、關閉問題是一個完整的過程,表示了對錯誤的處理、對新需求的響應或對工作安排的完成情況正處於什麼階段
- 系統預設的議題狀態有6種：
  - New：表示錯誤剛被發現、新需求剛被提出、或者工作任務剛被下達
  - In Progress：表示已經安排了人來處理該問題
  - Resolved：表示此問題已經被解決
  - Feedback：表示有人對問題的解決效果提出了反饋意見
  - Closed：表示問題已經徹底解決並通過稽核, 可以告一段落. 預設情況下問題列表中將不再顯示已經關閉的問題
  - Rejected：認為該問題提出的錯誤不存在、工作任務不合理等, 拒絕執行此問題
- 被分派者:
  - 表示已將此問題安排給某人負責解決
  - 被指派人應全權負責處理此問題
- 問題的狀態變化
  - 問題負責人應及時更新問題狀態, 並填寫說明
  - 其他相關人員通過其狀態和說明來了解問題的進度
- 處理進度
  - 開始日期
  - 完成日期
  - 完成百分比
- 郵件通知
  - 問題的提出人（新建問題）和負責人（被分派者）都可以自動收到有關此問題的郵件通知
  - 問題狀態每次變化都會傳送通知郵件
  - 其他使用者可以通過‘觀察’選項來收取某個問題的通知
  - 問題建立人可以將相關人員加入跟蹤者列表
    (圖13)
    ![https://ithelp.ithome.com.tw/upload/images/20220913/20151950izSG4e5pX6.png](https://ithelp.ithome.com.tw/upload/images/20220913/20151950izSG4e5pX6.png)

#### --[Redmine系統]_角色與權限 ：[網站管理]/[角色與權限]

- Manager
  - 管理人員
  - 專案經理人, 負責決策/分派.
- Developer
  - 開發人員
  - 負責問題之分析/處理/解決.
- Reporter
  - 報告人員
  - 回報問題, 確認問題是否解決.
- 自定義角色
  - 自行定義出更符合現況的角色
  - 例如: Project Leader, DT Manager, CIM Manager, Employee, Marketing, Sales…etc
    (圖14、15)
    ![https://ithelp.ithome.com.tw/upload/images/20220913/201519505CMl90VEtz.png](https://ithelp.ithome.com.tw/upload/images/20220913/201519505CMl90VEtz.png)
    ![https://ithelp.ithome.com.tw/upload/images/20220913/20151950NITi55nv8k.png](https://ithelp.ithome.com.tw/upload/images/20220913/20151950NITi55nv8k.png)

#### -- [Redmine系統]_流程 ：[網站管理]/[流程]

- Redmine系統中，專案管理的核心部分就是工作流程了，涉及到問題跟蹤標籤、問題狀態、角色權限等，工作流直接影響系統正常運行和專案管理。
- 系統中工作流程是以角色和跟蹤標籤來定義整個問題的流轉過程。定義好後，不同用戶在不同角色下，才能順利的對所分配的任務進行操作和狀態變更，達到專案管理的目的，實現不同業務需求。(圖16)
  ![https://ithelp.ithome.com.tw/upload/images/20220913/20151950BcDnkdsv9J.png](https://ithelp.ithome.com.tw/upload/images/20220913/20151950BcDnkdsv9J.png)

#### --[Redmine系統]_用戶清單 ：[網站管理]/[用戶清單]

- 就是User管理，非常清楚，此不多述。

#### --[Redmine系統]_群組清單 ：[網站管理]/[群組清單]

- 就是將User組成群組，例如MIS部門群組。非常清楚，此不多述。

#### --[Redmine系統]_追蹤標籤清單 ：[網站管理]/[追蹤標籤清單]

- 議題的追蹤標籤設定。會在後續的建立範例中詳細說明，先不多述。

#### --[Redmine系統]_議題狀態清單：[網站管理]/[議題狀態清單]

- 議題的狀態清單設定，如 New、In Progress、Resolved、Feedback、Closed、Rejected。會在後續的建立範例中詳細說明，先不多述。