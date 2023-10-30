# 第27章 - [ISMS管理]ISMS文管中心

---

## 本篇預期成果畫面

![https://ithelp.ithome.com.tw/upload/images/20220924/20151950PLs3HL3nnl.png](https://ithelp.ithome.com.tw/upload/images/20220924/20151950PLs3HL3nnl.png)

------

### 管理議題

多數公司的ISMS是遵循ISO27001的管理架構去建立，近年來因為資通安全法及國際大廠對供應商資安制度的要求，依據ISO27001建立ISMS之後有很高比例都會請第三方認證公司認證(例如BSI、SGS、TUV等機構)，基於驗證需求，文件及紀錄的管理就變得非常重要，因為ISO27001的驗證就是依據公司所建立的管理制度，確認程序書規定要的執行的管理表單有沒有依規定執行? 整個管理系統是否依循PDCA循環有效運作? 而驗證公司稽核的方法就是抽查表單管理紀錄的執行狀況。

ISO的認證是3年一個循環，第1年重新審查，2、3年會定期複審，所以為了維持證書的有效性，驗證ISO的公司每年都會有稽核活動。

很多中大型公司有文管中心，文件由品保單位中負責公司管理系統(如ISO9001、ISO 14001、IATF16949等)的專人統一管理。

有些公司的文管有一套專門系統在管理，或採用BPM的簽核去建立文管中心。

那為什麼我會在本系列文章把ISMS的文管中心獨立來談? 因為在筆者的經驗中，ISO27001由於驗證的是資訊部門、機房和核心系統，加上資訊有專業的獨特性其他單位不熟悉，現實狀況是，有更多公司的ISO27001是由MIS自行管理，最多就是文件簽核及保存走公司的文管中心機制，但MIS要自行管理ISMS的文件和紀錄。

本系列文的初衷是建構中小企業的MIS的管理平台，採用了Redmine，當然就用Redmine來建立ISMS的文管中心。

ISMS管理文件有些需要簽核，例如四階文件的發行需要資安長及資訊主管簽核發佈後才算生效，不過四階程序文件的簽核不在本文的討論範圍，多數公司有自己的文件核准流程、方法和工具，依循即可。

本篇在分享的是利用Redmin平台的功能來建立適合ISMS的文管中心。

------

### 建立文件分類

- 文件分類是Redmine平台的共同設定，所以要先到[網站管理]/[列舉值清單]/[文件分類]/[建立新列舉值]建立需要的分類
- Redmine建立文件分類的方法在本系列前文已有說明，此不再詳述。
- 以筆者的經驗，若要管理ISMS文件，可將文件分為幾類：
  - 一階政策
  - 二階程序
  - 三階SOP
  - 四階表單
  - 操作手冊
  - 技術文件
  - 文件範本
  - 資安手冊

圖01
![https://ithelp.ithome.com.tw/upload/images/20220924/20151950BQ2j2l8r5n.png](https://ithelp.ithome.com.tw/upload/images/20220924/20151950BQ2j2l8r5n.png)

------

### 管理資訊需求：

- 【議題名稱】：文管中心
- 【權限需求】：未登入者可瀏覽及下載
- 【適用場合】：ISMS文件管理
- 【追蹤標籤】：不需要
- 【模組需求】：
  - (X)議題追蹤
  - (X)工時追蹤
  - (O)新聞
  - (O)文件
  - (O)檔案
  - (O)Wiki
  - (O)版本控管
  - (O)討論區
  - (X)日曆
  - (O)甘特圖
- 【欄位需求】：使用標準預設

------

### 建立文管中心

- 就是用專案的方式，建立文管中心
- 因為是文管中心，不需要的模組就不需要進來。

圖02、03
![https://ithelp.ithome.com.tw/upload/images/20220924/201519506fR6nFPWoF.png](https://ithelp.ithome.com.tw/upload/images/20220924/201519506fR6nFPWoF.png)

圖03
![https://ithelp.ithome.com.tw/upload/images/20220924/20151950FKI9byIScT.png](https://ithelp.ithome.com.tw/upload/images/20220924/20151950FKI9byIScT.png)

- 這邊要注意的是，如果你的文管中心可能會給其他部門查閱，就不建議放在MIS部門的子專案下，建議成立第一階的【文管中心】
  圖04

![https://ithelp.ithome.com.tw/upload/images/20220924/20151950dZEiKbe5T0.png](https://ithelp.ithome.com.tw/upload/images/20220924/20151950dZEiKbe5T0.png)

- 建立ISMS的文件
  圖05、06、07
  ![https://ithelp.ithome.com.tw/upload/images/20220924/20151950OaFU1jPtgN.png](https://ithelp.ithome.com.tw/upload/images/20220924/20151950OaFU1jPtgN.png)

圖06
![https://ithelp.ithome.com.tw/upload/images/20220924/20151950HfDVt7mnEq.png](https://ithelp.ithome.com.tw/upload/images/20220924/20151950HfDVt7mnEq.png)

圖07
![https://ithelp.ithome.com.tw/upload/images/20220924/20151950z4FQF0NiZR.png](https://ithelp.ithome.com.tw/upload/images/20220924/20151950z4FQF0NiZR.png)

- 利用Wiki管理程序書的發行及修改歷程
  圖08
  ![https://ithelp.ithome.com.tw/upload/images/20220924/20151950PLs3HL3nnl.png](https://ithelp.ithome.com.tw/upload/images/20220924/20151950PLs3HL3nnl.png)

------

### 檔案清單

檔案清單比較像是非正式管理的常用文件下載，可以當作常用檔案下載的分享區。
圖09

![https://ithelp.ithome.com.tw/upload/images/20220924/20151950RT7meQAo0L.png](https://ithelp.ithome.com.tw/upload/images/20220924/20151950RT7meQAo0L.png)