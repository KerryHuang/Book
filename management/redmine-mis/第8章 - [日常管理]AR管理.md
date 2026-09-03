---
kind: reprint
source: site:ithelp.ithome.com.tw
---

# 第8章 - [日常管理]AR管理

------

## 本篇預期成果畫面

![https://ithelp.ithome.com.tw/upload/images/20220916/20151950wa0BSFQzL2.png](https://ithelp.ithome.com.tw/upload/images/20220916/20151950wa0BSFQzL2.png)

![https://ithelp.ithome.com.tw/upload/images/20220913/20151950mcR6V1fQFt.png](https://ithelp.ithome.com.tw/upload/images/20220913/20151950mcR6V1fQFt.png)

------

### 管理議題：

在某些科技產業，工程師最怕highlight和AR。

所謂「highlight」，其實就是「某人做錯事，被點名出來負責或被責怪」的意思。被highlight的目標對象可大可小，可以從產品品質有問題，到桌面不乾淨。被highlight的人，必須將事情解釋清楚，提出改善方針。

而AR，中文是「待完成任務」（action required），指的是長官對部屬的行動要求。待檢討、改進的事項，待解決的問題，解決問題之後的效益評估事項，都可以成為AR。

在會議上被主管問到的問題，如果當下沒有好答案，事後會一一被列AR。所以，常聽到的「押AR」，就是要你在報告或會議紀錄上簽名，代表同意日後不能反悔。

如果老闆有一天跟MIS說，AR別再用Excel mail來mail去，把AR上系統管理吧?

你說：那還不簡單，用Share point吧?! 市面上有些EIP Portal的套裝產品就有了啊?!

孩子，醒醒吧，你是中小企業的MIS，錢要花在刀口上，老闆只說別用Excel了，可沒答應給你花大錢。要用商業軟體先把O.S.、DB及AP等連線人數授權費用估算一下給老闆看他點頭了再說。

如果如你預期這筆費用不屬於刀口，那就另外想其他方案囉! 老闆請你是來解決問題，不是來說問題，只會搖頭老闆就會把你當問題來處理。

不過你也別自怨自艾，這個問題也不大，能解決此問題的免費工具其實並不少。不過既然我們選擇Redmine當作MIS的管理平台，我們就用Redmine快速解決老闆交付的這個任務。

------

### 本篇將學習到Redmine的功能重點：

- 專案成員對Ticket的進度的維護
- 被指派者的任務訊息
- 舊的Redmine知識回顧
  - 模組的設定：請參考系列文Day 7-[[Redmine\]專案版面的規劃](https://ithelp.ithome.com.tw/articles/10290131)
  - 自訂欄位清單：請參考系列文Day 6-[[Redmine\]自行建立及維護表單](https://ithelp.ithome.com.tw/articles/10289889)
  - 專案建立基本邏輯：請參考系列文Day 5-[[Redmine\]Redmine系統邏輯說明](https://ithelp.ithome.com.tw/articles/10289859)

------

### 管理資訊需求：

- 【議題名稱】：AR 管理 (Action Required)
- 【權限需求】：未登入者可瀏覽，由執行長秘書建立AR相關資訊，被指派的AR負責人必須登入維護AR的狀態。
- 【適用場合】：主管會議、各專案會議、老闆口頭交辦
- 【追蹤標籤】：研發、生產、廠務、品保、資訊、人事、行政
- 【模組需求】：(O)開啟使用-設定勾選；(X)不使用-設定不勾選
  - (O)議題追蹤
  - (X)工時追蹤
  - (X)新聞
  - (X)文件
  - (X)檔案
  - (X)Wiki
  - (X)版本控管
  - (X)討論區
  - (O)日曆
  - (O)甘特圖
- 【欄位需求】
  - (1)AR提出人員
  - (2)AR來源
  - (3)AR建立日期
  - (4)要求AR進度報告日期
  - (5)AR負責人
  - (6)急迫性
  - (7)進度摘要說明
  - (8)相關檔案資料
  - (9)AR狀態
- 【系統可使用之預設欄位】
  - 概述：(7)進度摘要說明
  - 狀態：(9)AR狀態
  - 優先權：(6)急迫性
  - 被分派者：(5)AR負責人
  - 開始日期：(3)AR建立日期
  - 完成日期：(4)要求AR進度報告日期
  - 預估工時：X (因為，AR通常工時不重要耶)
  - 完成百分比：User選填
  - 檔案：(8)相關檔案資料
- 【自訂欄位需求】
  - (1)AR提出人員：董事長、總經理、副總、部門主管 (選單)
  - (2)AR來源：主管會議、專案會議、口頭要求(文字)

------

### 專案設定：

- [設定]/[專案]-[公開]：請勾選
- [設定]/[成員]：請指定成員 (有設定成員才能被指派AR)
- [設定]/[議題追蹤]/[自訂欄位清單]：請新增2個新欄位
  - AR提出人員
  - AR來源

------

### 議題管理：

- 完成設定後[建立新議題]資料建立畫面如下。

(圖01)
![https://ithelp.ithome.com.tw/upload/images/20220913/201519504r4yr6kfp8.png](https://ithelp.ithome.com.tw/upload/images/20220913/201519504r4yr6kfp8.png)

- AR的管理追蹤畫面如下：(圖02、03、04)
  ![https://ithelp.ithome.com.tw/upload/images/20220913/201519503NH9lts176.png](https://ithelp.ithome.com.tw/upload/images/20220913/201519503NH9lts176.png)

![https://ithelp.ithome.com.tw/upload/images/20220913/20151950FlqjYaqCkl.png](https://ithelp.ithome.com.tw/upload/images/20220913/20151950FlqjYaqCkl.png)

![https://ithelp.ithome.com.tw/upload/images/20220913/20151950CKYc8GFFMM.png](https://ithelp.ithome.com.tw/upload/images/20220913/20151950CKYc8GFFMM.png)

------

### 進度維護

- 專案成員只要登入該筆議題資料，按[編輯]，即可更新議題進度資訊。
- 另外也可以使用[筆記]，作為這個AR的相關處理回應及記錄 (圖05、06、07)
  ![https://ithelp.ithome.com.tw/upload/images/20220913/20151950JPgJs2KsgJ.png](https://ithelp.ithome.com.tw/upload/images/20220913/20151950JPgJs2KsgJ.png)

![https://ithelp.ithome.com.tw/upload/images/20220913/20151950n14zCR9Hxx.png](https://ithelp.ithome.com.tw/upload/images/20220913/20151950n14zCR9Hxx.png)

![https://ithelp.ithome.com.tw/upload/images/20220913/20151950386jHog5Lt.png](https://ithelp.ithome.com.tw/upload/images/20220913/20151950386jHog5Lt.png)

### 被指派者的資訊

在[帳戶首頁]，可以看到自己被指派的工作及議題清單 (圖08)

![https://ithelp.ithome.com.tw/upload/images/20220913/20151950mcR6V1fQFt.png](https://ithelp.ithome.com.tw/upload/images/20220913/20151950mcR6V1fQFt.png)

------

### 「被分派者」與「AR提出人」

- 請注意.. 「被分派者」..
  - 就是，就是這張AR的苦主..
  - 就是，傳說中被押AR的負責人
- 請再注意.. 「AR提出人」..
  - 就是在會議中下令這張AR的那位大長官
- 因為2個欄位很重要，所以要再三強調!!

(圖09)
![https://ithelp.ithome.com.tw/upload/images/20220916/20151950wa0BSFQzL2.png](https://ithelp.ithome.com.tw/upload/images/20220916/20151950wa0BSFQzL2.png)

看清了AR提出人，請再眼睜睜大看他說了甚麼...(圖10)
![https://ithelp.ithome.com.tw/upload/images/20220916/201519504KmXfXRgEP.png](https://ithelp.ithome.com.tw/upload/images/20220916/201519504KmXfXRgEP.png)

------

### AR上了系統，然後呢?

當然以後就是用這個在Redmine建立的AR管理系統檢討AR執行狀況啊!

- 被押AR的人要自己上平台更新進度
- 被押AR的人要自己上傳相關簡報和相關檔案
- 被押AR的人在會議中要打開這張AR跟老闆報告AR狀態，老闆聽完滿意狀態才可以改成"已完成"
- AR會議的秘書或助理以後就靠這個平台幫老闆管好所有AR，管好所有主管、所有工程師、所有阻礙公司前進不長進的員工!

## 完美!!

### 好吧...這個完美是Allan自己的想像而已啦..哈哈!

#### 老話一句：工具沒有好壞，只有管理和執行力而已。完美的關鍵才不是平台，而是解決問題的思維和決心!