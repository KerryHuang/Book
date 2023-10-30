# 第23章 - [變革管理]MIS的新專案管理：監控階段

---

### 監控階段(Monitoring and Controlling)

- 【輸入與輸出】
  - 輸入資訊：專案計畫
  - 產出文件紀錄：專案文件及檔案、專案溝通文件、專案會議文件
- 【主要目的】：在確保專案的所有進度狀況及問題被有效地追蹤記錄、分析評估、及檢討處理。
- 【主要活動】：包含控管現況、解決問題及管理溝通與文件等。
- 【成員任務】：監控的工作由專案經理及專案團隊成員來負責。專案贊助者及專案委員會則負責指導及審核的工作。

------

### 範例專案

![https://ithelp.ithome.com.tw/upload/images/20220923/201519505UvbdEOdPp.png](https://ithelp.ithome.com.tw/upload/images/20220923/201519505UvbdEOdPp.png)

------

監控階段貫穿其他階段，如下圖，所以並不在廠商計劃書中規劃(上圖)的5個階段內。正確地說，我們是用專案管理工具去監督廠商規劃的這5個專案階段有沒有依計畫執行?有沒有偏差?有沒有需要矯正措施?
![https://ithelp.ithome.com.tw/upload/images/20220923/20151950XuVYEwKSsH.png](https://ithelp.ithome.com.tw/upload/images/20220923/20151950XuVYEwKSsH.png)
專案生命週期，資料來源：PMBOK

------

### 監督階段在系統上的3個角色

- (1)被分配者
  - 被分配者就是被指派負責這項工作的人
  - 分配的類別有對應到成員，調整分類就會自動填入被分派者，能幫助不熟悉用戶職權的人輕鬆的做議題分配
  - 「被分配者」和「分類」的設定細節，在本系列文章分享之前的範例有介紹及應用過，這裡就不再贅述。(圖01)
    ![https://ithelp.ithome.com.tw/upload/images/20220924/20151950VcVWnLDv0J.png](https://ithelp.ithome.com.tw/upload/images/20220924/20151950VcVWnLDv0J.png)
- (2)監看者(watcher)
  這個欄位有人把主管設定為主管，有人設定為協辦。反正除了[被分配者]外，新增新議題單時，需要收到mail通知的都可列為監看者。(圖02)
  ![https://ithelp.ithome.com.tw/upload/images/20220924/20151950VWoWkcr4te.png](https://ithelp.ithome.com.tw/upload/images/20220924/20151950VWoWkcr4te.png)
- (3)提及(memtion)：
  在撰寫議題概述的時候常常會提到其他同事(ex:這項決議是哪位長官決定、這塊功能會由誰負責…)，可以用 @ 來操作設定，系統也會發送Mail通知給Memtion。如下圖 (圖03)
  ![https://ithelp.ithome.com.tw/upload/images/20220924/20151950GUiyJEYvKg.png](https://ithelp.ithome.com.tw/upload/images/20220924/20151950GUiyJEYvKg.png)

------

### 議題狀態變更Mail通知

被分配者、監看者、提及的人會收到Mail通知。但要看Mail通知的類型是哪幾類。可在[網站管理]/[設定]/[電子郵件提醒選項] (圖04)
![https://ithelp.ithome.com.tw/upload/images/20220924/2015195030qZAezhKI.png](https://ithelp.ithome.com.tw/upload/images/20220924/2015195030qZAezhKI.png)

- Mail通知在專案執行實務上的運用
  - 過多的通知就是沒有通知，實務上很多人對專案管理系統發出的Mail通知不讀不回(根本是當作垃圾郵件對待)，尤其是被設定為監看者更是常見的現象。原因是，系統發出太多不重要的異動細節，收件人已麻痺而直接忽略系統發的通知。
  - 解決此問題的其中一個方法是：不設定【監看者】，就不會有人每天都收到一堆Redmine發出的通知信件。若真有需要發通知給特定人士，再用【提及】的方式指定收mail人員。

------

### 專案監督-甘特圖

- 專案計畫進度與實際實施進度比較與檢討
- 在Redmine提供的甘特圖，灰色代表計畫
  - 灰色：[開始日期]-[完成日期] (就是計畫日期)
  - 綠色：完成百分比
  - 粉紅色：逾期囉 (包含當天已過了[完成日期]但進度還未100%，或今天已過了[開始日期，但進度為0%或不符[完成百分比]的日期]) (圖05、06)
    ![https://ithelp.ithome.com.tw/upload/images/20220924/20151950c75Dg4N2x9.png](https://ithelp.ithome.com.tw/upload/images/20220924/20151950c75Dg4N2x9.png)

![https://ithelp.ithome.com.tw/upload/images/20220924/20151950w0agjPvtyC.png](https://ithelp.ithome.com.tw/upload/images/20220924/20151950w0agjPvtyC.png)

------

### 專案監督-議題清單詳細資料

下圖此張單子，已逾期1天，但完成進度只有70%，專案經理應該進行此項工作項目的檢討 (圖07)
![https://ithelp.ithome.com.tw/upload/images/20220924/20151950VDWFOi3ma9.png](https://ithelp.ithome.com.tw/upload/images/20220924/20151950VDWFOi3ma9.png)

------

### 專案監督-議題清單查詢

Redmine提供非常彈性且有用的查詢工具，可依管理需求過濾查詢條件，此處不贅述，由需要的人自行依管理需求決定條件進行查詢。(圖8)
![https://ithelp.ithome.com.tw/upload/images/20220924/20151950QDBruex7xy.png](https://ithelp.ithome.com.tw/upload/images/20220924/20151950QDBruex7xy.png)

------

### 專案監督-耗用工時

成本的估算很重要，Redmine提供了[工時預估]及[耗用工時]的資料維護。此本系列文之前有介紹過，不再贅述。只要到[耗用工時]依條件進行過濾及查詢。(圖9)
![https://ithelp.ithome.com.tw/upload/images/20220924/20151950z5RvuUpW4c.png](https://ithelp.ithome.com.tw/upload/images/20220924/20151950z5RvuUpW4c.png)

------

### 實際行動

系統工具只能做到提供異常資訊的主動警訊通知給相關人員，但有效的監督工作還是要靠人的敏感度去發掘、面對及提出矯正措施來修正已發生/可能發生的問題，以確保專案在預期內達到目標。

最後整理一下【監控階段】實際要做的工作內容：

- 專案的實際績效與專案管理計畫書進行比較。
- 評估專案績效，決定是否採取矯正措施或預防行動，並提出建議。
- 辨識新風險，分析、追蹤及監視現有風險，確保風險被辨識，報告風險現況，並適當的執行風險回應計畫。
- 維護準確且及時的專案產品、相關文件的資料庫。
- 提供資訊，支援現況報告、進度衡量及預測。
- 提供預測，更新目前成本及時程資訊。
- 對已獲准的變更，監控其執行情況。
- 向計畫管理階層報告專案進度與現況。