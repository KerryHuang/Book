---
kind: reprint
source: site:ithelp.ithome.com.tw
---

# 第10章 - [日常管理]MIS部門週會工作進度追蹤

---

## 本篇預期成果畫面

![https://ithelp.ithome.com.tw/upload/images/20220916/20151950l3ck6Knldk.png](https://ithelp.ithome.com.tw/upload/images/20220916/20151950l3ck6Knldk.png)

![https://ithelp.ithome.com.tw/upload/images/20220916/20151950qZzTNX7WqP.png](https://ithelp.ithome.com.tw/upload/images/20220916/20151950qZzTNX7WqP.png)

------

### 管理議題：

MIS的工作來源通常有幾類：

- (一) 來自User提出的需求
  - 表單解決方案：【資訊服務申請】
- (二) 來自主管交辦的事項(含AR)
  - 表單解決方案：【MIS工作進度追蹤】
- (三) 來自參與的專案工作
  - 【各專案平台】
- (四) 日常例行性工作：
  - 表單解決方案1：【工作日誌】
  - 表單解決方案2：【Time sheet】

本篇管理需求是要建立上述第(二)項【MIS工作進度追蹤】的表單解決方案。

其實這個管理需求和本系列文章前二篇介紹的【AR管理】、【資訊服務申請】很類似，連需求欄位資訊都只有少數差異，且都是從Issue 的角度去設計管理需求。但除了「進度追蹤」一樣是管理重點外，【MIS工作進度追蹤】和上述2個最大的不同是：

1. 【MIS工作進度追蹤】是MIS部門內部的管理使用
2. 需求上更著重在MIS人員的投入工時和實際績效的統計分析。

- 由於此專案成員是全部MIS的同仁，所以我們也將在此專案建立MIS內部的技術討論區。

------

### 本篇將學習到Redmine的功能重點

- 使用「複製」現有專案來建立新的專案
- 專案不公開，僅限專案成員
- 指派專案成員工作
- 被指派的成員更新及維護該筆Kicket(表單紀錄)
- 群組的設定與使用
- 討論區的建立
- 進度追蹤：[開始日期]、[完成日期]、[完成百分比]、[狀態]的系統及管理意義
- 紀錄時間(填報工時)
- 舊的Redmine知識回顧
  - 模組的設定：請參考系列文Day 7-[[Redmine\]專案版面的規劃](https://ithelp.ithome.com.tw/articles/10290131)
  - 自訂欄位清單：請參考系列文Day 6-[[Redmine\]自行建立及維護表單](https://ithelp.ithome.com.tw/articles/10289889)
  - 專案建立基本邏輯：請參考系列文Day 5-[[Redmine\]Redime系統邏輯說明](https://ithelp.ithome.com.tw/articles/10289859)
  - 其餘本文有完成功能但沒做進行詳細畫面說明的：請參考系列Day 8開始的每篇文章的「本篇將學習到Redmine的功能重點」。每篇分享文都有當篇文章要新學習的Redmine某項功能的應用及設定方法的示範重點。

------

### 管理資訊需求

- 【議題名稱】：MIS工作進度追蹤
- 【權限需求】：
  - 專案不公開，限MIS內部使用
  - MIS主管可指派MIS處理人員
  - 被指派的人可以更新申請的表單和狀態
- 【適用場合】：MIS內部工作清單及進度紀錄
- 【追蹤標籤】：系統及報表開發、系統軟硬體維護、網路機房維護、User問題處理、其他
- 【分類】：ERP、BPM、Help Desk
- 【模組需求】：
  - (O)議題追蹤
  - (O)工時追蹤
  - (X)新聞
  - (X)文件
  - (X)檔案
  - (X)Wiki
  - (X)版本控管
  - (O)討論區
  - (O)日曆
  - (O)甘特圖
- 【欄位需求】：(同【資訊服務申請】，可參考上一篇)
  - (1)需求人員
  - (2)需求部門單位
  - (3)聯絡人分機/手機
  - (4)聯絡人e-mail
  - (5)希望完成日期
  - (6)實際提出日期
  - (7)實際完成日期
  - (8)MIS負責人
  - (9)急迫性
  - (10)需求摘要說明、
  - (11)相關檔案資料
  - (12)進度狀態
  - (13)MIS預估工時
- 【系統可使用之預設欄位】
  - 概述：(10)需求摘要說明
  - 狀態：(12)進度狀態
  - 優先權：(9)急迫性
  - 被分派者：(8)MIS負責人
  - 開始日期：(6)實際提出日期
  - 完成日期：(7)實際完成日期
  - 預估工時：(13)MIS預估工時
  - 完成百分比：由MIS維護
  - 檔案：(11)相關檔案資料
- 【自訂欄位需求】
  - (1)需求人員 (文字)
  - (2)需求部門單位(文字)
  - (3)聯絡人分機/手機(文字)
  - (4)聯絡人e-mail(文字)
  - (5)希望完成日期 (日期)

------

### 專案設定

- 複製【資訊服務申請】：因內容類似，可以複製專案再進行修改
- [網站管理]/[專案清單]-->[複製]
- 請注意：本次需求增加[討論區]、[日曆]、[甘特圖]模組 (圖：01、02)
  ![https://ithelp.ithome.com.tw/upload/images/20220916/20151950FKAeDsM6Vn.png](https://ithelp.ithome.com.tw/upload/images/20220916/20151950FKAeDsM6Vn.png)

![https://ithelp.ithome.com.tw/upload/images/20220916/20151950iAtUXcXZg1.png](https://ithelp.ithome.com.tw/upload/images/20220916/20151950iAtUXcXZg1.png)

- [設定]/[專案]-[公開]：請不勾選
- [設定]/[成員]：請指定成員(或直接設定[群組清單]：MIS) (圖：03、04、05、06)

![https://ithelp.ithome.com.tw/upload/images/20220916/20151950GRpgWTmgA5.png](https://ithelp.ithome.com.tw/upload/images/20220916/20151950GRpgWTmgA5.png)

![https://ithelp.ithome.com.tw/upload/images/20220916/20151950BTcmobiUbm.png](https://ithelp.ithome.com.tw/upload/images/20220916/20151950BTcmobiUbm.png)

![https://ithelp.ithome.com.tw/upload/images/20220916/20151950dhQRGDVCOZ.png](https://ithelp.ithome.com.tw/upload/images/20220916/20151950dhQRGDVCOZ.png)

![https://ithelp.ithome.com.tw/upload/images/20220916/20151950tCW3y0AX77.png](https://ithelp.ithome.com.tw/upload/images/20220916/20151950tCW3y0AX77.png)

- [設定]/[議題追蹤]/[自訂欄位清單]：新增4個，並加入已有的[其他]
  - 系統及報表開發
  - 系統軟硬體維護
  - 網路機房維護
  - User問題處理
  - 其他(已有，勾選即可)
- [設定]/[議題分類清單] [建立新分類] ：同【資訊服務申請】
- [設定]/[論壇]/[建立新論壇]：我們建立2個MIS內部的論壇
  - MIS開發技術及議題交流
  - 網管硬體議題交流 (圖07)
    ![https://ithelp.ithome.com.tw/upload/images/20220916/20151950i2pqkXUOze.png](https://ithelp.ithome.com.tw/upload/images/20220916/20151950i2pqkXUOze.png)

------

### 議題管理

- 完成設定後[建立新議題]資料建立畫面如下：(圖08、09)

![https://ithelp.ithome.com.tw/upload/images/20220916/20151950gp1IEht4Gn.png](https://ithelp.ithome.com.tw/upload/images/20220916/20151950gp1IEht4Gn.png)

![https://ithelp.ithome.com.tw/upload/images/20220916/20151950vCa8iSr8FD.png](https://ithelp.ithome.com.tw/upload/images/20220916/20151950vCa8iSr8FD.png)

------

### 論壇

- 完成設定的論壇可作為MIS內部討論的交流平台：(圖10)

![https://ithelp.ithome.com.tw/upload/images/20220916/20151950vkINpQABX7.png](https://ithelp.ithome.com.tw/upload/images/20220916/20151950vkINpQABX7.png)

------

### 專案清單首頁(登入前登入後)

本此管理需求限MIS內部成員使用，所以我們將本專案設定成[不公開]，只有專案成員才有權限看到專案資訊。

- 登入前(匿名者) (圖11)

![https://ithelp.ithome.com.tw/upload/images/20220916/20151950bfZSFfXe3S.png](https://ithelp.ithome.com.tw/upload/images/20220916/20151950bfZSFfXe3S.png)

- 登入前後(MIS群組) (圖12)

![https://ithelp.ithome.com.tw/upload/images/20220916/20151950QRqRNdbRz3.png](https://ithelp.ithome.com.tw/upload/images/20220916/20151950QRqRNdbRz3.png)

------

### 追蹤進度管理

- 完成後[議題清單]，可作為MIS部門之後檢討同仁工作進度的依據。(圖13、14)

![https://ithelp.ithome.com.tw/upload/images/20220916/20151950l3ck6Knldk.png](https://ithelp.ithome.com.tw/upload/images/20220916/20151950l3ck6Knldk.png)

![https://ithelp.ithome.com.tw/upload/images/20220916/20151950qZzTNX7WqP.png](https://ithelp.ithome.com.tw/upload/images/20220916/20151950qZzTNX7WqP.png)

這邊先說明幾個欄位的資訊在Redmine設計的意義

- 開始日期：就是這一張單子的有效開始日期
- 完成日期：正確的說法是，預計完成日期，而非實際完成日期
- 完成百分比：工作的完成進度
- 狀態：目前是處理中，或已結案

所以如果這張單子已經完成，最重要要更新的是[狀態]設為Close。其他完成百分比設100%。

再強調一次，**[完成日期】在系統預設並不是實際完成日期喔**。

當然，很多人把這個欄位當作實際完成日期在用，也OK，如果你不在乎預計完成日期資訊在甘特圖呈現的話。
所以理論上你若需要實際完成日期資訊，是需要自己[自訂欄位]的。

下圖的例子，你已經設了[完成日期]，[完成百分比]設100%，但因為[狀態]是"處理中"，所以仍然會出現逾期6天
(圖15)

![https://ithelp.ithome.com.tw/upload/images/20220916/20151950Nk1OdSsFmo.png](https://ithelp.ithome.com.tw/upload/images/20220916/20151950Nk1OdSsFmo.png)

------

### 紀錄時間(填報工時)

被指定的同仁近來編輯此筆Ticket時，若完成後可以[記錄時間]，有就是處理這張單子所花費的實際工時。

- 一筆Ticket可以記錄一次以上的「紀錄時間」。
- 可以按[編輯]來輸入紀錄這張Ticket的實際工時，也可以開啟這張Ticket直接按[紀錄工時]。
- 議題我們留在後續的案例進行更深入的應用探討 (圖16、17、18)

![https://ithelp.ithome.com.tw/upload/images/20220916/201519503PED6BuUhJ.png](https://ithelp.ithome.com.tw/upload/images/20220916/201519503PED6BuUhJ.png)

![https://ithelp.ithome.com.tw/upload/images/20220919/20151950M3MXWBBKx3.png](https://ithelp.ithome.com.tw/upload/images/20220919/20151950M3MXWBBKx3.png)

## ![https://ithelp.ithome.com.tw/upload/images/20220919/20151950gbfwW0ZrWF.png](https://ithelp.ithome.com.tw/upload/images/20220919/20151950gbfwW0ZrWF.png)

### 然後呢?

別然後了!

- 當然是每週MIS工作進度用今天建構的「MIS工作進度追蹤」平台來檢討手中的工作進度!
- 當然是用「MIS工作進度追蹤」當作MIS員工績效的指標量化依據，讓主動優秀又有效率的員工出頭、讓打混摸魚沒效率的員工被看見、
- 當然是用「MIS工作進度追蹤」來檢討人力的配置是否不當
- 當然是用「MIS工作進度追蹤」的數字告訴老闆MIS的雜事已經多到影響你想做的AI智慧製造專案
- 當然是用「MIS工作進度追蹤」的管理統計告訴老闆，Help desk應該外包或找工讀生，讓網管人員專注在網管資安的監控和ISMS的執行

以上這些前提是執行力，在「MIS工作進度追蹤」平台的資料正確性及即時更新的執行力。要不然久了沒管理者看資料、MIS就開始沒更新、大家覺得那個平台的資訊荒廢已久與現實落差太大，所以又開始用Excel和Powerpoint石器時代的方式管理MIS，然後又走回每天處理**MIS鳥事**的惡性循!