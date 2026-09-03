---
kind: reprint
source: site:ithelp.ithome.com.tw
---

# 第28章 - [ISMS管理]ISMS表單紀錄的管理

---

## 本篇預期成果畫面

![https://ithelp.ithome.com.tw/upload/images/20220924/20151950hxIpYBHloY.png](https://ithelp.ithome.com.tw/upload/images/20220924/20151950hxIpYBHloY.png)

![https://ithelp.ithome.com.tw/upload/images/20220924/20151950N8kCC32FND.png](https://ithelp.ithome.com.tw/upload/images/20220924/20151950N8kCC32FND.png)

------

### 管理議題

1. 管理表單能不紙本就不紙本，盡量線上填單，記錄盡量變成資料庫內容，而不只是掃描紙本的的PDF檔的管理。
2. 能以線上簽核方式處理就不要列印紙本簽核。
3. 無論線上表單或紙本申請單，全部記錄都在單一平台被分類及歸檔。
4. 平日易於管理，用最簡單明瞭且能輕易找到的分類方式。
5. 稽核前的準備能簡單建立Check List，為稽核做準備。
6. ISO 27001驗證稽核時，無論誰受稽，都能輕易找到稽核員要查核的管理紀錄。
7. 若ISMS承辦異動，能最短時間清楚交接完畢。
8. ISMS KPI的統計所需數據資料盡可能由這個平台自動統計。

------

### 本文範例的規劃思維

雖然企業導入ISMS的目的不是為了要驗證，但不可否認的驗證ISO 27001已經是多數企業執行ISMS固定的年度最重要活的活動。

ISO 27001的稽核有2個重要活動：

- 文件審查：每3年一個循環一次，除了驗證範圍的確認外，主要是審查程序書是否符合要驗證版本的ISO27001的框架和要求，以及控制項的適用性聲明。
- 實地審查：每年執行一次，第2、3年屬於複查，確認管理系統有效地在執行。主要審查的是紀錄文件是否依照程序書的要求執行。

所以本篇規劃的角度，以驗證稽核的觀點進行管理表單和紀錄分類。最後決定規劃方向如下：

1. 以ISO 27001管理系統的條文及附錄A控制項的要求進行表單及紀錄的歸類。
2. 為便於操作及管理，將所有管理表單以專案/議題的方式建立管理。
3. 表單及紀錄的管理：思考及設計：
   (1) 那些能以線上表單的方式建立紀錄資料?
   (2) 那些需要紙本簽後，事後紀錄以掃描文件的方式歸檔?
   (3) 那些需要同時考量線上及紙本二種方式並存?
   (4) 目標是：稽核老師在進行審查稽核時，所有相關紀錄都可以在**對應的本文或控制項**分類中找到紀錄。
4. 如果需要線上簽核，可以以[筆記]的方式請主管簽核

> 關於紀錄簽核使用Redmine [筆記] 功能設計的議題，可參閱[[日常管理\]機房工作日誌](https://ithelp.ithome.com.tw/articles/10292454)的範例。

------

### 表單紀錄的分類

ISO27001的驗證條文要求是本文的4-10章，以及附錄A的14項(A.5-A.18)：

- 4-10章是管理系統的要求：從關注者議題、目標規劃、風險評鑑的實作，到內外部稽核、持續改善的矯正措施都在本文的範圍內。
- 附錄A的控制項是資安管理實作的要求，對應的是各控制項表單紀錄及相關實作紀錄。
- 部分紀錄或過程可能不屬於ISMS正式的四階表單，他屬於紀錄佐證或過程，也將其歸類在對應的條紋或附錄。
- 紀錄分類舉例：
  - 例1：關注者議題的蒐集可以建立用小[專案]/[議題]的方案日常建立資料，在稽核上它屬於[04_組織全景]那一類。
  - 例2：[全景分析作業表]是ISMS正式的四階表單，每年要做一次，它屬於[04_組織全景]那一類。
  - 例3：「人員機房進出表」是紙本，每個月審核後歸檔一次，它屬於[A.11 實體與環境安全]的類別。
  - 例4：網路圖、拓樸圖示稽核必要的檢查項目，但不是正式的ISMS表單紀錄，所以我們將這些圖的檔案做好版本控制，放在[A.13 通訊安全的類別]。

依照上述原則，在Redmine以專案進行各項設定後，完成如下2圖： (圖1、圖2)

![https://ithelp.ithome.com.tw/upload/images/20220924/20151950VAKI1xzt63.png](https://ithelp.ithome.com.tw/upload/images/20220924/20151950VAKI1xzt63.png)

![https://ithelp.ithome.com.tw/upload/images/20220924/20151950nnQfufkxDy.png](https://ithelp.ithome.com.tw/upload/images/20220924/20151950nnQfufkxDy.png)

------

### 紀錄的必要執行頻率

在多數公司的ISMS中，有部分的紀錄產出是每年有固定頻率，常見的程序書規定及頻率如下：(不是標準答案，要看公司的程序書如何規定)

- 資訊資產清單每年都要清查一次，而且必須完成簽核。
- 一般User的帳號每年都要請各部門主管Review一次。
- 特權帳號及VPN帳號每半年要清查一次。
- 有些網管紀錄的審查有可能規定每季或每月，例如機房的進出管制可能就是1個月主管要審核一次並每月歸檔。

所以在規劃上為了管理上的便利將這些產出紀錄的重要資訊直接呈現在表單名稱之下，可使用平台的[專案]/[概述]去進行設定。

- 在[設定]/[專案]/[概述]中， (圖03、04)

![https://ithelp.ithome.com.tw/upload/images/20220924/20151950hxIpYBHloY.png](https://ithelp.ithome.com.tw/upload/images/20220924/20151950hxIpYBHloY.png)

![https://ithelp.ithome.com.tw/upload/images/20220924/20151950ynqmthZaAc.png](https://ithelp.ithome.com.tw/upload/images/20220924/20151950ynqmthZaAc.png)

------

### 線上、紙本檔案、線上+紙本

- 線上：就是使用Redmine的 【建立新議題】 的方式去建立表單紀錄。例如帳號權限申請(線上)。此方式在本系列文章已多次用不同的範例示範 (可參考這2個範例的設計：[機房工作日誌](https://ithelp.ithome.com.tw/articles/10292454)、[資通安全事件通報/處理記錄單](https://ithelp.ithome.com.tw/articles/10294990) )，將不再贅述。
- 紙本檔案：就是不適合線上填寫的方式，只能紙本完成後掃描變成檔案，我們再以檔案管理的方式管理。例如**機房進出登記表**的每月歸檔
- 線上+紙本：紀錄以線上填寫，但實際執行部分必須以紙本或檔案的方式進行，就是在線上紀錄該筆紀錄時，以檔案夾帶的方式歸檔。例如**系統一般帳號權限審查**，實際執行是各部門主管，且MIS必須先整理該部門權限給部門主管審核，並不適合直接使用線上簽核的方式。

------

### 外部稽核報告管理

第三方驗證公司的稽核是ISMS年度最重要的活動，無論有沒有缺失稽核員都會產出正式的稽核報告，而且若有缺失還必須在5天內有檔案回覆矯正計畫(業界普遍簡稱CAR單)。

不過這一部分比較特殊，所以除了稽核報告的上傳管理外，我們也將稽核的每一項稽核發現用議題的方式記錄，以做為改善追蹤的依據。

外部稽核報告的管理，我將其獨立在紀錄表單的分類之外。(圖05、06)
![https://ithelp.ithome.com.tw/upload/images/20220924/201519502nbMaM1p5V.png](https://ithelp.ithome.com.tw/upload/images/20220924/201519502nbMaM1p5V.png)

![https://ithelp.ithome.com.tw/upload/images/20220924/20151950gXxAA5m8aT.png](https://ithelp.ithome.com.tw/upload/images/20220924/20151950gXxAA5m8aT.png)

外部稽核報告的上傳及管理 (圖07)

![https://ithelp.ithome.com.tw/upload/images/20220924/20151950OzVDpOxRaB.png](https://ithelp.ithome.com.tw/upload/images/20220924/20151950OzVDpOxRaB.png)
外部稽核發現的維護及管理 (圖08、09)

![https://ithelp.ithome.com.tw/upload/images/20220924/20151950N8kCC32FND.png](https://ithelp.ithome.com.tw/upload/images/20220924/20151950N8kCC32FND.png)

![https://ithelp.ithome.com.tw/upload/images/20220924/20151950AREF5J5s1C.png](https://ithelp.ithome.com.tw/upload/images/20220924/20151950AREF5J5s1C.png)

------

### 矯正處理單

普遍簡稱CAR單(Corrective Action Request)。

很多製造業的管理系統會以8D Report的方式撰寫。不過老實說，8D Report比較適合在品質系統，對於ISO 27001的資安不大適用，所以多數會另外設計表單。以下這張是網路上Google來的，最常見的表單範本： (圖10)

![https://ithelp.ithome.com.tw/upload/images/20220924/20151950v27Gq8NqhT.png](https://ithelp.ithome.com.tw/upload/images/20220924/20151950v27Gq8NqhT.png)

矯正處理單一定適合用線上紀錄的方式建立資料及管理，不過因為CAR單有簽核的問題，要走紙本還是線上，還是要視企業管理現實環境做出最適合的選擇。

- 歸類：10 改善
- 追蹤議題：以事件來源定義
  - 內部稽核
  - 外部稽核
  - 資訊安全事件
  - 自行提出
    圖11、12、13

![https://ithelp.ithome.com.tw/upload/images/20220924/20151950RAAZdHDgkx.png](https://ithelp.ithome.com.tw/upload/images/20220924/20151950RAAZdHDgkx.png)

![https://ithelp.ithome.com.tw/upload/images/20220924/20151950EScad0xYHl.png](https://ithelp.ithome.com.tw/upload/images/20220924/20151950EScad0xYHl.png)

![https://ithelp.ithome.com.tw/upload/images/20220924/201519506yxhZFFmev.png](https://ithelp.ithome.com.tw/upload/images/20220924/201519506yxhZFFmev.png)