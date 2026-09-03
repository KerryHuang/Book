---
kind: reprint
source: site:ithelp.ithome.com.tw
---

# 第6章 - [Redmine]自行建立及維護表單

------

### 本篇預期成果畫面

![https://ithelp.ithome.com.tw/upload/images/20220913/20151950oK457O0AgA.png](https://ithelp.ithome.com.tw/upload/images/20220913/20151950oK457O0AgA.png)

------

對專案管理系統的新手而言，Redmine設定功能感覺非常複雜，所以我們先不談各種設定的細節，先用最簡單最快速的方式建立表單。

開始前我們必須擬定建立一個表單計畫。

> [註]：在Redmine系統中，本篇寫的「表單」正確名稱叫「Issue」，或有人叫Ticket，就是一個議題或一則任務。本系列文章一開始幾篇會以「表單」稱呼只是為了符合一般人的常識名稱，讓這分享內容顯得平易近人能讓大家比較能理解的說明而已。

------

### 案例表單情境

【表單名稱】：AR 管理 (Action Required)
【適用情境】：主管會議、各專案會議、老闆口頭交辦
【追蹤標籤】：研發、生產、廠務、品保、資訊、人事、行政

【欄位需求】：

- AR提出人員：董事長、總經理、部門主管 (使用下拉式選單)
- 其他資訊紀錄：使用Redmine預設欄位
  - AR狀態 ：(新建立、進行中、已完成、延後、取消結案)
  - AR來源及描述：主管會議、專案會議、口頭要求 (寫在[概述]欄位)

------

### 本篇將學習到Redmine的功能重點

- 建立新專案及新專案的基本資料設定
- 追蹤標籤的修改與使用
- 自訂欄位清單(下拉選單)
- 匿名者(未登入)的系統權限設定
- 建立新議題(白話說，就是新的表單及任務資料)

------

### Redmine設計邏輯

1. 把AR管理定義成專案(Project)，每一個AR就是一個專案內的新議題(Issue)。
2. [建立專案]：先建立專案資料
3. [建立議題]：再建立議題內容。
4. [專案及議題相關設定]：可以指派人員、專案版本、自訂議題追蹤標籤、建立議題分類等設定。
5. [編輯及確認表單欄位]：建立及編輯議題設定，就是我們需要建立及編輯的表單。
6. [使用者視野]：完成後User可以在專案中，使用[建立新議題]，建立表單紀錄。

------

### 建立專案

【步驟一】：建立新專案

- 在[專案清單 ]/[建立新專案]

【步驟二】：建立專案基本資料

- 填寫專案基本資料，代碼必填(預設會產生)，公開打勾，按[建立] (圖01)
  ![https://ithelp.ithome.com.tw/upload/images/20220913/201519500TZlnGBHwU.png](https://ithelp.ithome.com.tw/upload/images/20220913/201519500TZlnGBHwU.png)

【步驟三】：進入專案設定

- 點選[專案清單]會看到您建立的專案
- 點進去就會進入專案設定頁面
- 按[設定]，就會看到專案的相關設定
  (圖02、03、04)
  ![https://ithelp.ithome.com.tw/upload/images/20220913/20151950NvdN1Yb2bD.png](https://ithelp.ithome.com.tw/upload/images/20220913/20151950NvdN1Yb2bD.png)

![https://ithelp.ithome.com.tw/upload/images/20220913/20151950keZxp5mI7A.png](https://ithelp.ithome.com.tw/upload/images/20220913/20151950keZxp5mI7A.png)

![https://ithelp.ithome.com.tw/upload/images/20220913/20151950mUIdajC1JT.png](https://ithelp.ithome.com.tw/upload/images/20220913/20151950mUIdajC1JT.png)

------

### 建立議題

【步驟四】：議題清單

- 點選[議題清單]，我們先來看看預設的議題版面
- 按[建立新議題]，看到預設的議題版面
- 其實若只想簡單用，可以直接用「概述」的備註欄位的方式，說明此議題的相關資訊，就不需要再新增欄位了
  (圖05、06)

![https://ithelp.ithome.com.tw/upload/images/20220913/20151950APfgt0uyp6.png](https://ithelp.ithome.com.tw/upload/images/20220913/20151950APfgt0uyp6.png)
![https://ithelp.ithome.com.tw/upload/images/20220913/20151950Yah7IhCaNO.png](https://ithelp.ithome.com.tw/upload/images/20220913/20151950Yah7IhCaNO.png)

------

### 專案及議題相關設定

【步驟五】：修改議題欄位_修改[追蹤標籤]

- 在點進本專案的第一個畫面是在[概觀]，如下圖。你會看到[議題追蹤]，出現Bug、Feature、Support項目的二維表，欄位是進行中、已結束。這是預設沒修改過的狀態。
- 在[建立新議題]時，追蹤標籤也是出現Bug、Feature、Support三個選項。
- 我們來修改這個標籤符合本專案的需求
  (圖07、08)
  ![https://ithelp.ithome.com.tw/upload/images/20220913/201519504NnL74juKn.png](https://ithelp.ithome.com.tw/upload/images/20220913/201519504NnL74juKn.png)
  ![https://ithelp.ithome.com.tw/upload/images/20220913/20151950PXHoYy1OrN.png](https://ithelp.ithome.com.tw/upload/images/20220913/20151950PXHoYy1OrN.png)
- 點[議題清單]/[追蹤標籤清單]/[網站管理]/[建立新的追蹤標籤] (圖09、10、11)
  ![https://ithelp.ithome.com.tw/upload/images/20220913/20151950gTYEV7erCC.png](https://ithelp.ithome.com.tw/upload/images/20220913/20151950gTYEV7erCC.png)

![https://ithelp.ithome.com.tw/upload/images/20220913/20151950C8g0Wfbv13.png](https://ithelp.ithome.com.tw/upload/images/20220913/20151950C8g0Wfbv13.png)

![https://ithelp.ithome.com.tw/upload/images/20220913/20151950RcciAqB1RU.png](https://ithelp.ithome.com.tw/upload/images/20220913/20151950RcciAqB1RU.png)

- 注意：[從以下追蹤標籤複製工作流程]要設定，請先設定為bug，專案要選定，輸入完標籤資料後，按[建立]
- 陸續同上設定其他標籤
- 設定完成後請點回[專案清單]中的本專案，會看到剛剛設定的議題標籤 (圖12)
  ![https://ithelp.ithome.com.tw/upload/images/20220913/20151950hwhrNijSxf.png](https://ithelp.ithome.com.tw/upload/images/20220913/20151950hwhrNijSxf.png)
- 把不要的標籤取消出現：[設定]/[議題追蹤]，按[儲存] (圖13)
  ![https://ithelp.ithome.com.tw/upload/images/20220913/20151950rLt8g1Ce5Z.png](https://ithelp.ithome.com.tw/upload/images/20220913/20151950rLt8g1Ce5Z.png)
- 完成議題標籤修改了!可以到[概觀]及[建立新議題]看一下成果。(圖14、15)
  ![https://ithelp.ithome.com.tw/upload/images/20220913/20151950dwJhfzBKdT.png](https://ithelp.ithome.com.tw/upload/images/20220913/20151950dwJhfzBKdT.png)

![https://ithelp.ithome.com.tw/upload/images/20220913/20151950fpeWr4rOHm.png](https://ithelp.ithome.com.tw/upload/images/20220913/20151950fpeWr4rOHm.png)

------

### 編輯及確認表單欄位

【步驟六】：新增及修改欄位資料

- 點[議題清單]/[自訂欄位清單]/[網站管理]/[建立新自訂欄位]
- (或[網站管理]/[自訂欄位清單]/[建立新自訂欄位])
  (圖16、17)
  ![https://ithelp.ithome.com.tw/upload/images/20220913/20151950lZuDBKkbXJ.png](https://ithelp.ithome.com.tw/upload/images/20220913/20151950lZuDBKkbXJ.png)

![https://ithelp.ithome.com.tw/upload/images/20220913/20151950T6foEeMc8Y.png](https://ithelp.ithome.com.tw/upload/images/20220913/20151950T6foEeMc8Y.png)

- 選[議題清單]。按[下一步] (圖18)

![https://ithelp.ithome.com.tw/upload/images/20220913/201519506OW9vWxNhw.png](https://ithelp.ithome.com.tw/upload/images/20220913/201519506OW9vWxNhw.png)

- 點[議題清單]/[自訂欄位清單]/[網站管理]/[建立新自訂欄位]
- 請記得右邊的[追蹤標籤清單]及[專案清單]也要勾選對應
- 此處以格式為[值/清單]為例，建立完後按[儲存]
  (圖19)
  ![https://ithelp.ithome.com.tw/upload/images/20220913/201519503WF5EGHFBJ.png](https://ithelp.ithome.com.tw/upload/images/20220913/201519503WF5EGHFBJ.png)
- 再點進去剛剛設定的欄位進行進一步設定 (圖20)
  ![https://ithelp.ithome.com.tw/upload/images/20220913/20151950AGxdvcsdzK.png](https://ithelp.ithome.com.tw/upload/images/20220913/20151950AGxdvcsdzK.png)
- 在[可能值]/[編輯]，新增你要在表單出現的選擇清單。 (圖21、22)
  ![https://ithelp.ithome.com.tw/upload/images/20220913/20151950hNIRkd8iUI.png](https://ithelp.ithome.com.tw/upload/images/20220913/20151950hNIRkd8iUI.png)

![https://ithelp.ithome.com.tw/upload/images/20220913/20151950RAW7Qgvd6u.png](https://ithelp.ithome.com.tw/upload/images/20220913/20151950RAW7Qgvd6u.png)

- 完成後按[儲存]，新增自訂欄位完成了
- 到[建立新議題]看建立的欄位是否正確出現
  (圖23)
  ![https://ithelp.ithome.com.tw/upload/images/20220913/20151950ZeLkApKRKF.png](https://ithelp.ithome.com.tw/upload/images/20220913/20151950ZeLkApKRKF.png)
- 使用者視野：新增議題(輸入表單紀錄)
- 系統安裝後，[新增議題]的權限必須登入，匿名者預設只有瀏覽的權限。
- 若要允許不登入也可以新增議題，請先設定匿名者的權限
- [網站管理]/[角色與權限]/[匿名者]/[議題追蹤]，[新增議題]必須勾選
  (圖24)
  ![https://ithelp.ithome.com.tw/upload/images/20220913/20151950MOwPcCdDIS.png](https://ithelp.ithome.com.tw/upload/images/20220913/20151950MOwPcCdDIS.png)
- User要建立資料要先到[專案清單]。進入專案 (圖25、26)
  ![https://ithelp.ithome.com.tw/upload/images/20220913/20151950GCcawLNqpN.png](https://ithelp.ithome.com.tw/upload/images/20220913/20151950GCcawLNqpN.png)

![https://ithelp.ithome.com.tw/upload/images/20220913/20151950sXYRhWb9jX.png](https://ithelp.ithome.com.tw/upload/images/20220913/20151950sXYRhWb9jX.png)

- [議題清單]/[建立新議題] (圖27)
  ![https://ithelp.ithome.com.tw/upload/images/20220913/20151950zPCxZgPcLH.png](https://ithelp.ithome.com.tw/upload/images/20220913/20151950zPCxZgPcLH.png)
- 輸入本次AR資料 (圖28、29、30、31)

![https://ithelp.ithome.com.tw/upload/images/20220913/20151950McOegML91k.png](https://ithelp.ithome.com.tw/upload/images/20220913/20151950McOegML91k.png)

![https://ithelp.ithome.com.tw/upload/images/20220913/20151950Q7llyq6JqA.png](https://ithelp.ithome.com.tw/upload/images/20220913/20151950Q7llyq6JqA.png)

![https://ithelp.ithome.com.tw/upload/images/20220913/20151950sBi5uqRvTa.png](https://ithelp.ithome.com.tw/upload/images/20220913/20151950sBi5uqRvTa.png)

![https://ithelp.ithome.com.tw/upload/images/20220913/201519508VbwtZMBLT.png](https://ithelp.ithome.com.tw/upload/images/20220913/201519508VbwtZMBLT.png)

------

沒寫任何一個程式，我們就可以用Redmine強大的專案及議題模組，建立我們需要的表單及進行記錄管理及追蹤。
是不是很簡單又厲害!