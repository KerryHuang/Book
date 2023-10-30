# 第11章 - [日常管理]MIS部門主管月會報告管理

---

## 本篇預期成果畫面

![https://ithelp.ithome.com.tw/upload/images/20220917/20151950C8oi0Zqp1s.png](https://ithelp.ithome.com.tw/upload/images/20220917/20151950C8oi0Zqp1s.png)

------

### 管理議題

蒐集、產生、歸檔、查詢MIS在主管會議的簡報，這一定是「日常」，而且定期每月在固定時間發生的工作。

很多公司主管會議的報告是簡報檔。

很多公司主管會議的報告必須仰賴同仁每月固定時間mail提供的資料，再由主管彙整成做成簡報。

主管會議簡報的內容有時需要查閱。但檔案多數恐怕是存放在MIS主管的PC或NB。

都說了要用Redmine管理MIS的大事小事及鳥事，所以例行性工作的MIS部門主管月會報告當然也要設計在平台上管理。

------

### 本篇將學習到Redmine的功能重點

- 檔案上傳：用Redmine管理每月一次的主管會議簡報及相關檔案
- 專案成員的協同作業：MIS同仁在每月主管會議報告的該筆Ticket，提供相關資訊和檔案讓該月的主管會議資料明細及紀錄更完整。
- 舊的Redmine知識回顧
  - 模組的設定：請參考系列文Day 7-[[Redmine\]專案版面的規劃](https://ithelp.ithome.com.tw/articles/10290131)
  - 自訂欄位清單：請參考系列文Day 6-[[Redmine\]自行建立及維護表單](https://ithelp.ithome.com.tw/articles/10289889)
  - 專案建立基本邏輯：請參考系列文Day 5-[[Redmine\]Redime系統邏輯說明](https://ithelp.ithome.com.tw/articles/10289859)
  - 其餘本文有完成功能但沒做進行詳細畫面說明的：請參考系列Day 8開始的每篇文章的「本篇將學習到Redmine的功能重點」。每篇分享文都有當篇文章要新學習的Redmine某項功能的應用及設定方法的示範重點。

------

### 管理資訊需求

- 【議題名稱】：主管月會報告管理
- 【權限需求】：MIS部門權限
- 【適用場合】：每月的主管會議報告管理
- 【追蹤標籤】：一般
- 【模組需求】：
  - (O)議題追蹤
  - (X)工時追蹤
  - (X)新聞
  - (X)文件
  - (X)檔案
  - (X)Wiki
  - (X)版本控管
  - (X)討論區
  - (X)日曆
  - (X)甘特圖
- 【欄位需求】：
  - (1)備註說明
  - (2)簡報檔案
- 【系統可使用之預設欄位】
  - 概述：(1)備註說明
  - 狀態：X
  - 優先權：X
  - 被分派者：X
  - 開始日期：X
  - 完成日期：X
  - 預估工時：X
  - 完成百分比：X
  - 檔案：(2)簡報檔案
- 【自訂欄位需求】
  - 無

------

### 專案設定

- [設定]/[專案]-[公開]：請不勾選
- [設定]/[成員]：請指定成員(或直接設定[群組清單]：MIS)

------

### 議題管理

- 完成設定後[建立新議題]資料建立畫面如下：(圖1、2)
  ![https://ithelp.ithome.com.tw/upload/images/20220917/20151950cBrig956Za.png](https://ithelp.ithome.com.tw/upload/images/20220917/20151950cBrig956Za.png)
  ![https://ithelp.ithome.com.tw/upload/images/20220917/201519501ODk4YYOxo.png](https://ithelp.ithome.com.tw/upload/images/20220917/201519501ODk4YYOxo.png)
- 以每月一筆新的Issue建立主管會議簡報的管理，MIS同仁也可以協助用編輯該筆紀錄的方式，協助該月主管會議資料的補充，以及相關訊息處理的紀錄(圖03、04、05)

![https://ithelp.ithome.com.tw/upload/images/20220917/20151950zy4h8nFyot.png](https://ithelp.ithome.com.tw/upload/images/20220917/20151950zy4h8nFyot.png)

![https://ithelp.ithome.com.tw/upload/images/20220917/20151950YeRcqiUq5O.png](https://ithelp.ithome.com.tw/upload/images/20220917/20151950YeRcqiUq5O.png)

![https://ithelp.ithome.com.tw/upload/images/20220917/20151950C8oi0Zqp1s.png](https://ithelp.ithome.com.tw/upload/images/20220917/20151950C8oi0Zqp1s.png)

------

### 就這樣?

- Allan：沒有錯，今天的分享就這樣!
- You ：這不就是檔案上傳及管理的功能嗎?
- Allan：沒錯，是的!
- You ：幹嘛大費周章，把主管月會的簡報檔案放到X槽就好了啊?
- Allan：X槽能知道誰更新、刪除、新增了檔案嗎? X槽有版本控制嗎? X槽可以分享/討論相關資訊的地方嗎? X槽能有回饋紀錄嗎? X槽有比有權限控管的網頁平台安全嗎?
- You ：...@@..沒有。X槽只有建資料夾和放檔案而已!
- Allan：你需要一個MIS檔案文件管理的Portal，建立一個找資料的知識庫嗎?
- You ：.....從管理面，長期來說，是需要...

嗯，以上，本篇「就這樣」的藉口...喔，不是啦，是理由!