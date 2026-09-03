---
kind: reprint
source: https://blog.hungwin.com.tw/cshart-server-monitoring/
author: Hungwin
---

# [C#] 伺服器監控常用語法 (事件檢視器、CPU 硬碟使用率、程式執行狀況)


如果你有在管理 Windows 伺服器的話，你可能會常常看一下伺服器的狀況，檢查「事件檢視器」是否有異常，檢查 CPU 及硬碟使用率，還有檢查某個程式是否有在執行。

這些都是我平常檢查伺服器會做的事情，其實這些工作都可以讓程式來幫我們執行就好，這樣就可以省下一些遠端登入檢查時間。

我們可以寫一些監控程式放在伺服器上執行，當程式發現有異常時，再立即主動通知我們，讓維護工作更有效率。

要開發這樣的程式，我建議使用 .Net Framework 的架構來寫就好，因為 .Net Framework 與 Windows 的結合較多，可以直接使用 Windows 內建的函式庫來執行工作。

以下我會提供幾個程式範例，這些程式碼可以替我們執行檢查的工作，一起來看看吧。

目錄 [[hide](https://blog.hungwin.com.tw/cshart-server-monitoring/?fbclid=IwAR3jqNBJeTbz3EF8quS90infZMXneQLG641vHTJyV0pAFUVtzsWOzkuRLnE#)]

- [1 讀取「事件檢視器」](https://blog.hungwin.com.tw/cshart-server-monitoring/?fbclid=IwAR3jqNBJeTbz3EF8quS90infZMXneQLG641vHTJyV0pAFUVtzsWOzkuRLnE#i)
- [2 讀取 CPU 使用率](https://blog.hungwin.com.tw/cshart-server-monitoring/?fbclid=IwAR3jqNBJeTbz3EF8quS90infZMXneQLG641vHTJyV0pAFUVtzsWOzkuRLnE#_CPU)
- [3 讀取硬碟可用容量](https://blog.hungwin.com.tw/cshart-server-monitoring/?fbclid=IwAR3jqNBJeTbz3EF8quS90infZMXneQLG641vHTJyV0pAFUVtzsWOzkuRLnE#i-2)
- [4 檢查程式執行狀況](https://blog.hungwin.com.tw/cshart-server-monitoring/?fbclid=IwAR3jqNBJeTbz3EF8quS90infZMXneQLG641vHTJyV0pAFUVtzsWOzkuRLnE#i-3)
- 5 即時回傳 Line 通知
  - [5.1 範例下載](https://blog.hungwin.com.tw/cshart-server-monitoring/?fbclid=IwAR3jqNBJeTbz3EF8quS90infZMXneQLG641vHTJyV0pAFUVtzsWOzkuRLnE#i-4)

## 讀取「事件檢視器」

事件檢視器是 Windows 內建記錄各種訊息的小工具，我們可以在「開始」裡面搜尋「事件檢視器」就會找到這工具了。

通常我會打開「Windows 記錄 > 應用程式」的內容，而裡面我只會看一下「錯誤」的訊息內容，檢查一下這個錯誤訊息，是否有問題要排除，可能有些「錯誤」的內容是可以忽略的，這個要自己判斷了。

[![事件檢視器](https://blog.hungwin.com.tw/wp-content/uploads/2022/08/cshart-server-monitoring-1.png)](https://blog.hungwin.com.tw/wp-content/uploads/2022/08/cshart-server-monitoring-1.png)

這樣的工作，我們可以寫程式，讓程式直接幫我們讀取出有「錯誤」的資料就好了，其他狀態的資料就可以忽略掉。

接著我們回到程式開發環境，我在 Visual Studio 2022 建立一個範例程式，選擇「Windows Forms App (.NET Framework)」，建立新專案。

[![Windows Forms App (.NET Framework)](https://blog.hungwin.com.tw/wp-content/uploads/2022/08/cshart-server-monitoring-2.png)](https://blog.hungwin.com.tw/wp-content/uploads/2022/08/cshart-server-monitoring-2.png)

輸入專案名稱與路徑就可以建立專案了，在文章最下面我會分享今天所建立的範例原始檔。

簡單設計一個介面來執行語法，

[![簡單設計一個介面](https://blog.hungwin.com.tw/wp-content/uploads/2022/08/cshart-server-monitoring-3.png)](https://blog.hungwin.com.tw/wp-content/uploads/2022/08/cshart-server-monitoring-3.png)

在讀取事件檢視器按鈕的語法，可以輸入以下語法：



```c#
//讀取事件檢視器
EventLog evLog = new EventLog();

//選取Application 類的 Log
evLog.Log = "Application";

//選出 Type 為 Error，且時間為一天內的 Log
var AppLogEntries =
from EventLogEntry ev in evLog.Entries
where ev.EntryType == EventLogEntryType.Error && ev.TimeGenerated > DateTime.Now.AddDays(-1) 
orderby ev.TimeGenerated descending
select new
{
	ev.Source,
	ev.InstanceId,
	ev.Message,
	ev.TimeGenerated,
	ev.UserName,
	ev.EntryType,
};

//放到DataSource上
dataGridView1.DataSource = AppLogEntries.ToList();
```

在最上面會用到 `using System.Diagnostics;`

當執行之後，就可以看到以下的結果，從 DataGridView 顯示的都是一天內的錯誤訊息，因為我通常一天檢查一次就行了，如果有資料，我再把資料回傳出來檢查內容就行了。

[![讀取「事件檢視器」](https://blog.hungwin.com.tw/wp-content/uploads/2022/08/cshart-server-monitoring-4.png)](https://blog.hungwin.com.tw/wp-content/uploads/2022/08/cshart-server-monitoring-4.png)

## 讀取 CPU 使用率

讀取 CPU 使用率是為了檢查 CPU 是否過於忙碌，如果太忙碌時，就要檢查一下忙碌的原因，可能是正常的狀況，也可能是中毒或木馬執行的問題，所以值得觀察。

接著簡單設計一個介面來執行

![接著簡單設計一個介面來執行](https://blog.hungwin.com.tw/wp-content/uploads/2022/08/cshart-server-monitoring-5.png)

讀取 CPU 使用率的語法：



C#
```c#
// 取得cpu 效能
PerformanceCounter cpu = new PerformanceCounter(
"Processor", "% Processor Time", "_Total");

// 取得近 5 秒的平均值
double cpuAvg = 0;
for (int i = 0; i < 5; i++)
{
	cpuAvg += cpu.NextValue();
	Thread.Sleep(1000);
}
cpuAvg = Math.Round(cpuAvg / 5, 0);
txtCPU.Text = "CPU 使用率 = " + cpuAvg + " %";
```

這個做法我會取近 5 秒的平均值，你也可以改成 10 秒之類的，因為 CPU 會因為一時的執行而衝高使用率，所以不要單抓一個數值，我會取平均值這樣比較準。

執行後的畫面：

![讀取 CPU 使用率](https://blog.hungwin.com.tw/wp-content/uploads/2022/08/cshart-server-monitoring-6.png)

## 讀取硬碟可用容量

讀取硬碟可用容量是觀察硬碟空間是否足夠，如果硬碟容量不夠時，電腦就會當機無法使用，有時候伺服器會因為一些儲存資料太多或是 Log 成長太快，導致容量不夠，所以也值得定時檢查。

接著簡單設計一個介面來執行

![接著簡單設計一個介面來執行](https://blog.hungwin.com.tw/wp-content/uploads/2022/08/cshart-server-monitoring-7.png)



讀取硬碟容量的語法：



C#

```c#
//硬碟可用容量
StringBuilder sb = new StringBuilder();
DriveInfo[] allDrives = DriveInfo.GetDrives();

foreach (DriveInfo d in allDrives)
{
	sb.Append($"裝置 {d.Name}: ");
	if (d.IsReady == true)
	{
		// 可用容量 MB
		string FreeSpace = (d.TotalFreeSpace / (1024 * 1024)).ToString("N0");
		int FreeSpacePercent = Convert.ToInt32(Convert.ToDouble(d.TotalFreeSpace) / Convert.ToDouble(d.TotalSize) * 100);
		sb.AppendLine($"可用容量: {FreeSpace} MB 使用率: ({FreeSpacePercent} %)");
	}
}
txtHD.Text = sb.ToString();
```

此段語法會用到 `using System.IO;`

我們可以直接使用 C# 內建函式庫，來取得硬碟的狀態。
執行後的畫面：

![讀取硬碟可用容量](https://blog.hungwin.com.tw/wp-content/uploads/2022/08/cshart-server-monitoring-8.png)

## 檢查程式執行狀況

接著我會檢查幾個重要程式是否有在執行中，通常是一些系統服務，或是自己寫的批次程式，確保伺服器繼續提供服務。

一樣簡單設計介面：

![一樣簡單設計介面](https://blog.hungwin.com.tw/wp-content/uploads/2022/08/cshart-server-monitoring-9.png)

使用的語法如下：



C#
```c#
//檢查某程式執行
string[] ProgName = { "w3wp" , "sqlserver", "Batch1" }; //執行程式名稱
StringBuilder sb = new StringBuilder();
foreach (string name in ProgName)
{
	Process[] myProcess = Process.GetProcessesByName(name);
	if (myProcess.Length == 0)
	{
		sb.AppendLine("程式: " + name + " 未執行");
	}
	else
	{
		sb.AppendLine("程式: " + name + " 執行中");
	}
}
txtProg.Text = sb.ToString();
```

執行結果：

![檢查程式執行狀況](https://blog.hungwin.com.tw/wp-content/uploads/2022/08/cshart-server-monitoring-10.png)

## 即時回傳 Line 通知

我已經分享了 4 種我常用的方法，接著分享當監控程式檢查完之後，要即時回報訊息的做法，通常我會立即回傳文字訊息到我的 Line 通知，這樣比較能即時掌握。

要使用 Line 通知，要先去官網 [Line Notify 個人頁面](https://notify-bot.line.me/my/) 申請一組「發行存取權杖」，請使用電腦瀏覽器開啟。

![發行存取權杖](https://blog.hungwin.com.tw/wp-content/uploads/2022/06/csharp-line-notify-1.png)

接著選擇要通知的對象，可以選個人或是群組，個人的話會在第一順位，下面的都是群組。
輸入權杖名稱後就可以按「發行」。

![發行存取權杖](https://blog.hungwin.com.tw/wp-content/uploads/2022/06/csharp-line-notify-2.png)

發行後會得到權杖金鑰，先自行儲存此權杖，之後寫程式會用到。
此權杖金鑰關閉後，就查不到了，記得先存起來。

![權杖金鑰](https://blog.hungwin.com.tw/wp-content/uploads/2022/06/csharp-line-notify-3.png)

按發行後，這時候個人的 Line 通知也會出現訊息。
如果沒有的話，就是還沒加入官方「LINE Notify」為好友，在好友搜尋欄位輸入「LINE Notify」再加入好友即可。

![加入官方「LINE Notify」為好友](https://blog.hungwin.com.tw/wp-content/uploads/2022/06/csharp-line-notify-5.png)

如果推播對象是群組的話，那就在群組內按「邀請」，將「LINE Notify」加入到群組內就行了。

接著我建立一按鈕來寫程式碼：

![接著我建立一按鈕來寫程式碼](https://blog.hungwin.com.tw/wp-content/uploads/2022/08/cshart-server-monitoring-11.png)

發送 Line 通知語法如下：



C#

```c#
//發送 Line  通知
string message = "測試訊息1\n測試訊息2\n測試訊息3";

HttpClient httpClient = new HttpClient();
httpClient.DefaultRequestHeaders.Accept.Add(new MediaTypeWithQualityHeaderValue("application/x-www-form-urlencoded"));
httpClient.DefaultRequestHeaders.Authorization = new AuthenticationHeaderValue("Bearer", "{取代你的 Token}");
var content = new Dictionary<string, string>();
content.Add("message", message);
httpClient.PostAsync("https://notify-api.line.me/api/notify", new FormUrlEncodedContent(content));
```

此語法會引用

```c#
using System.Net.Http;using System.Net.Http.Headers;
```

發送前準備好要傳送的訊息，將語法中 `{取代你的 Token}` 換成你剛剛申請的 Token 就可以了。
執行之後，在 Line 上就會收到此通知了。

![發送 Line 通知](https://blog.hungwin.com.tw/wp-content/uploads/2022/08/cshart-server-monitoring-12.png)

以上就是我監控伺服器常用的做法，分享給你，有任何問題都可以與我討論。

### 範例下載

[連結 GitHub 下載範例](https://github.com/eermagic/cshart-server-monitoring)