# Log Paser Studio 分析 IIS W3C Log

在工作上剛好遇到要查詢IIS Log 的情況

第一次碰到決定整理成一整篇比較完整步驟的筆記

在IIS 的 Log 中可以看到很多資訊但是格式很不方便

所以我們要使用 Log Parser 這套微軟官方工具整理

但是這套軟體只有提供指令列的方式

所以我選擇再下載 Log Parser Studio 提供圖形介面的工具

整套下載跟使用的速度其實很快 而且很簡單 不用寫Code喔

馬上開始操作

> 步驟

1. 在IIS 開啟Log 紀錄
2. 補充說明Log 檔案資訊
3. 下載 並操作Log Parser 及 Log Parser Studio

> 在IIS 開啟 Log 紀錄

1. 開啟 IIS 並選擇站台- 記錄

![img](https://miro.medium.com/v2/resize:fit:875/1*wUinVU1KrbHc6fpKxVMHFg.png)

2. 我們可以得知 Log 存放的位置及格式

![img](https://miro.medium.com/v2/resize:fit:570/1*3bDA8sP_I_VBxcKWtQTn1A.png)

3. 開啟該資料夾即可查看Log檔案

![img](https://miro.medium.com/v2/resize:fit:483/1*7ITsj6vyLGK8ufC-Lcnb4A.png)

這時候你會很疑惑 哪一個才是你要查詢的?

其實在IIS站台的列表 就有寫 ID

W3SVC 後面的數字就是對應的 ID

4. 開啟資料夾就會有超多Log檔案

> 補充說明Log檔案資訊

Log 記錄的時間是格林威治時間不是主機時間

所以以台灣要 +8小時才會是發生當下的時間

那Log 裡面到底有甚麼資訊呢?

內容我不要誤人子弟比較好 因為我也不懂 僅附上對照參考

![img](https://miro.medium.com/v2/resize:fit:686/1*nObCcHXo8xOb-LsBoDayNg.png)

> 下載 Log Parser 及 Log Parser Studio

皆只有提供英文及日文版

[Log Parser 載點](https://www.microsoft.com/en-us/download/details.aspx?id=24659)

[Log Parser Studio 載點( 一定要下載Log Parser 才可使用)](https://techcommunity.microsoft.com/gxcuf89792/attachments/gxcuf89792/Exchange/16744/1/LPSV2.D2.zip)

下載完成後執行並開啟程式

Log Parser Studio 請開啟下載的資料夾選擇LPS.exe

![img](https://miro.medium.com/v2/resize:fit:838/1*H3AM9bcvRstCVNYLfyCA3Q.png)

就會跳出這個操作畫面

![img](https://miro.medium.com/v2/resize:fit:875/1*trvO8fut3MYnPFqjLLXO2g.png)

接下來我們要操作的步驟是

1. 新增一個查詢
2. 選擇Log檔案
3. 選擇資料類型
4. 匯出Excel檔案

1.先來新增一個新的查詢

![img](https://miro.medium.com/v2/resize:fit:875/1*BDRYwb0xiGmzF4xJJe_ryw.png)

2.選擇Log檔案

這邊我示範的是查詢單一Log檔案

如果要查詢多個Log檔案 可以查看[這邊的說明](https://hackmd.io/@Not/LogParserStudio_with_IISLog)

先點選上方黃色按鈕 - 並Add Files 選擇Log檔案 - 最後按下OK

![img](https://miro.medium.com/v2/resize:fit:875/1*m_EmWtx6HL90heDO9-aXUw.png)

3. 選擇資料類型

先按下右下角的Log Type 並選擇 W3CLOG

再按下左上角的驚嘆號

![img](https://miro.medium.com/v2/resize:fit:875/1*ZY181mUYqhSOuYmsd9yfxQ.png)

結果就跑出來了

你也可以修改下方query

預設是搜尋前10個

如果你想要搜尋前 100個 就改成 SELECT TOP 100 …(後面不變)

如果你要全部搜尋 那就改成 SELECT * FROM …(後面不變)

![img](https://miro.medium.com/v2/resize:fit:875/1*PFlIYE5FkVpHA8puxZALlg.png)

4.匯出Excel

把資料匯出Excel 比較方便整理查看

![img](https://miro.medium.com/v2/resize:fit:875/1*-SksbWU7EZQIbE66hnWvvw.png)

只摸了一點點皮毛

但因為我在看網路上有些文章省略了一些步驟

所以花了一點時間 寫下比較詳細的操作步驟

資料參考來源:

1. https://hackmd.io/@Not/LogParserStudio_with_IISLog