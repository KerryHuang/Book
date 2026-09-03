---
kind: reprint
---

# C# 中的 HTTPClient — 入門指南

## C# 中的 HTTPClient — 入門指南

當您有多個應用程序並且它們需要相互通信以交換數據時，您可能需要使用一種協議來實現類似的操作。在 C# 中，HTTPClient 類提供了一種強大且靈活的方式來發出 HTTP 請求和處理響應。無論您是構建需要與 API 交互的 Web 應用程序還是僅需要從服務器檢索數據，C# 中的 HTTPClient 都可以提供幫助。

在本教程中，我們將探討如何使用 C# 中的 HTTPClient 類發出 GET 和 POST 請求、處理錯誤等。我們將介紹設置和配置 HTTPClient 的基礎知識以及高級使用場景，例如使用不同的內容類型和處理身份驗證。學完本教程後，您將深入了解如何在自己的 C# 項目中使用 HTTPClient。

在本教程中，我將使用一些您可以在線找到的免費 API。您不需要註冊或生成密鑰。如果將來他們確實發生變化，請告訴我。

## The HTTPClient Explained? HTTPClient 解釋了嗎？

Microsoft 對 C# 中的 HTTPClient 有一個很好且簡短的描述：

> 提供一個類，用於發送 HTTP 請求並從 URI 標識的資源接收 HTTP 響應。

這正是這個類所做的。

HTTP 是 Internet 上數據通信的基礎。每次您訪問頁面、將可愛的狗的照片上傳到社交媒體、檢查電子郵件等等時，都需要通過萬維網發送和接收數據。

如果您使用 C# 並需要從外部在線數據源接收信息或數據，則需要發送 HTTP 請求並需要能夠接收響應。在.NET Framework 4.5之前，我們使用**HttpWebRequest**和**HttpWebResponse**來處理這些請求。從 4.5 版本開始，我們有了 HTTPClient 類。

那麼，為什麼不使用 HttpWebResponse 和 HttpWebRequest 呢？它們與 HTTPClient 之間存在一些差異。以下是一些：

1. HTTPClient 有更好的異步支持。
2. HTTPClient 更易於使用和閱讀
3. HTTPClient自動解壓響應內容
4. HTTPClient 自動重用多個請求的連接以獲得更好的性能。HttpWebRequest 具有_KeepAlive_屬性，但默認情況下它是禁用的。
5. HTTPClient 在每個請求中自動包含一組默認標頭，例如 User-Agent、Accept 和 Connection 標頭。HttpWebRequest 不提供默認標頭。

HTTPWebRequest 在最新版本的 .NET 中仍然可用，並且在某些情況下可能是一個不錯的選擇。新的類和函數並不總是意味著舊的類和函數不好。

這實際上取決於您需要執行 HTTP 請求的情況。以下是一些基本準則：

在以下情況下使用 HTTPClient：

* 您需要一個更簡單、更現代的 API 來發送 HTTP 請求和接收 HTTP 響應。
* 您希望使用 async/await 模式執行異步操作。
* 您需要自動處理解壓縮、連接重用和默認標頭。
* 您想要利用 HTTP/2 支持。

在以下情況下使用 HttpWebRequest：

* 您需要對 HTTP 請求和響應進行更多控制，並願意使用較低級別的 API。
* 您需要支持較舊的 .NET Framework 版本（4.5 之前），因為 HttpWebRequest 自 .NET Framework 1.1 以來就已存在。
* 您需要執行更高級的 HTTP 操作，例如發送分塊請求或使用自定義 HTTP 方法。
* 您正在使用需要使用 HttpWebRequest 的遺留系統。

### Getting The HTTPClient Ready 準備好 HTTPClient

幾種類型的 HTTP 請求描述了您可能想要執行的操作。在本教程中，我將解釋如何執行 GET、POST 和 DELETE 請求。讓我們從最簡單的開始：GET。

在發出 HTTP 請求之前，我們需要設置 HTTPClient。我創建一個控制台應用程序來編寫和測試代碼。我還安裝了 NuGet 包**Newtonsoft.Json**並將在下一個代碼中使用它。

使用和設置 HTTPClient 分為不同的層。我們需要初始化 HTTPClient 類，然後發出請求，並檢查該請求是否成功。如果我們希望發送回數據，我們需要獲取該數據並將其轉換為我們的代碼。

如果我們創建代碼來實現它，它將如下所示：

```c#
using (HttpClient client = new())
{
    HttpResponseMessage response = await client.GetAsync("https://official-joke-api.appspot.com/random_ten");

    if (response.IsSuccessStatusCode)
    {
        string content = await response.Content.ReadAsStringAsync();

        List<Joke>? jokes = JsonConvert.DeserializeObject<List<Joke>>(content);

        if (jokes == null)
            return;

        foreach (Joke joke in jokes)
        {
            Console.WriteLine(joke.Setup);
            Console.WriteLine(joke.Punchline);
            Console.WriteLine();
        }
    }
}

public class Joke
{
    public string Setup { get; set; }
    public string Punchline { get; set; }
}
```

讓我們來看看：

首先，初始化 HTTPClient。我正在使用_using_，因此當我不再需要它時，HTTPClient 初始化將被釋放，同時也會關閉連接。然後我將 GET 請求發送到該 URL。這是一個異步方法，所以我使用了_await_。

接下來，我檢查響應是否成功。這意味著我得到了一個肯定的[HTTP 狀態代碼](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)。如果不成功，我可以拋出異常或其他東西。

但它是成功的，所以我可以從響應中檢索內容。response.Content.ReadAsStringAsync \*()\*以字符串形式檢索響應，非常適合將其轉換為 JSON。

然後我們實際上就完成了 C# 中的 HTTPClient。我瀏覽笑話列表並將其打印在屏幕上。

很簡單，對吧？您所需要做的就是擁有一個 URL、初始化 HTTPClient 類，然後就可以開始了。

### Sending POST Requests 發送 POST 請求

雖然 GET 請求非常簡單，但 POST 需要一些額外的東西。POST 請求允許您將數據從客戶端發送到源，就像 API 一樣。因此，POST 請求需要一個包含數據的正文。

這個實體通常是一個鍵值對的情況。鍵是屬性名稱，值是……。嗯，該屬性的值。除了身體之外，並沒有什麼特別的地方。它甚至開始相同，但我們不期望返回任何數據，因此我們不必抓取和反序列化數據。

```c#
using (HttpClient client = new())
{
    Joke newJoke = new Joke
    {
        Setup = "Why do bees hum?",
        Punchline = "Because they don't know the words."
    };

    StringContent body = new(JsonConvert.SerializeObject(newJoke));
    body.Headers.ContentType = new MediaTypeHeaderValue("aapplication/json");

    HttpResponseMessage response = await client.PostAsync("https://official-joke-api.appspot.com/random_ten", body);
    if (!response.IsSuccessStatusCode)
    {
        var content = await response.Content.ReadAsStringAsync();
        throw new Exception(content);
    }
}

public class Joke
{
    public string Setup { get; set; }
    public string Punchline { get; set; }
}
```

我再次初始化 HTTPClient。然後我創造了一個新的笑話，這裡沒什麼特別的。_但隨後我創建了一個StringContent_類型的新變量，並使用要轉換為 JSON 字符串的_newJoke_對其進行初始化。因為我使用 JSON 作為請求的正文，所以我需要將正文的_ContentType設置為\*\*application/json_。

我需要設置 ContentType 的原因是讓目標知道我將向其發送哪種數據。它也可能是 XML，如果我發送 JSON，目標將無法接收 XML。

PUT 請求的工作原理完全相同，但您不使用_client.PostAsync ，而是使用\*\*client.PutAsync_。

您還可以設置很多其他標頭，但稍後我會告訴您更多相關信息。

好吧！接下來，我對 URL 執行實際的 POST。這次我使用_client.PostAsync_。第一個參數是 URL，我們已經通過 GET 做到了這一點，第二個參數是我們之前創建的正文。

對於 POST 請求或 PUT 和 DELETE，無需檢查響應是否成功。更相反的是；我們想知道什麼時候出了問題。因此，我檢查響應是否不成功。如果這是真的，我會得到請求的內容。大多數時候，這是目標的錯誤，告訴我我做錯了什麼。

我將此信息置於異常中，以便在向目標發布信息時出現問題時我會收到警報。此信息可能是必需的屬性為空，或者端點不正確，等等。

### Sending DELETE Requests 發送刪除請求

DELETE 請求看起來很像 POST 請求，但略有不同：我們不希望從目標接收數據。如果您已經創建了 POST 代碼，則只需複制粘貼該代碼並將其稍微更改為：

```c#
using (HttpClient client = new())
{
    HttpResponseMessage response = await client.DeleteAsync("https://some.api.com/random_ten/12");

    if (!response.IsSuccessStatusCode)
    {
        var content = await response.Content.ReadAsStringAsync();
        throw new Exception(content);
    }
}
```

好吧，當我看它的時候，它看起來根本不一樣。反正…

我再次初始化 HTTPClient。然後我向目標發送 DELETE 請求。DELETE 請求通常需要 URL 中的標識符，因此本示例 URL 中為“12”。

我們只想知道請求何時失敗並發送回帶有返回狀態碼的響應，因此我們只想檢查響應是否不成功。

為了弄清楚出了什麼問題，我們可以通過讀取響應中的內容來提取錯誤並將其放入異常中。

## Advanced HTTPClient 進階 HTTPClient

我想您已經了解如何在 C# 中使用 HTTPClient 了。但它不僅僅是向目標發送簡單的請求並讀取其響應。在擴展 HTTPClient 類時，您可能需要一些高級設置。

### Authorization 授權

某些 API 需要您通過向 API 請求添加令牌來進行授權。這通常是[來自 API 的 JWT](https://kenslearningcurve.com/tutorials/securing-net-6-apis/)。您需要將此令牌添加到請求的**Authorization標頭中。**

這是客戶端的默認請求標頭之一。如果您知道在哪裡添加它，那麼設置它就非常容易：

```c#
using (HttpClient client = new())
{
    client.DefaultRequestHeaders.Add("Authorization", "Bearer Your_Token_Here");

    HttpResponseMessage response = await client.DeleteAsync("https://some.api.com/random_ten/12");

    if (!response.IsSuccessStatusCode)
    {
        var content = await response.Content.ReadAsStringAsync();
        throw new Exception(content);
    }
}
```

雖然看起來很簡單，但請記住，您需要在發送請求之前設置 DefaultRequestHeaders。將所有內容發送到目標後，設置默認請求標頭是沒有意義的。

### Using A Timeout 使用超時

默認情況下，HTTPClient 等待 100000 毫秒（100 秒）才能完成請求。如果在此之前未完成，則會引發異常。這就是我們所說的超時。

如果您覺得有必要，可以將其更改為您想要的任何內容。HTTPClient 類有一個稱為**Timeout**的設置，並使用**TimeSpan**進行設置。

```c#
using (HttpClient client = new())
{
    client.DefaultRequestHeaders.Add("Authorization", "Bearer Your_Token_Here");
    client.Timeout = TimeSpan.FromSeconds(30);

    HttpResponseMessage response = await client.DeleteAsync("https://some.api.com/random_ten/12");

    if (!response.IsSuccessStatusCode)
    {
        var content = await response.Content.ReadAsStringAsync();
        throw new Exception(content);
    }
}
```

在上面的示例中，HTTPClient 的超時設置為 30 秒。這意味著，如果該初始化客戶端的請求花費超過 30 秒，則會引發異常。

### Multiple Requests With One Client 一個客戶的多個請求

如果您需要在同一方法內或同時發送不同的請求，則不必關閉並打開 HTTPClient。只需重複使用它即可。下面是一個例子。_只有在使用_結束後，客戶端才會被關閉。

```c#
string baseUrl = "https://official-joke-api.appspot.com/jokes/{0}";

using (HttpClient client = new())
{
    for(int i = 0; i < 10; i++)
    {
        HttpResponseMessage response = await client.GetAsync(string.Format(baseUrl, i + 1));

        if (response.IsSuccessStatusCode)
        {
            string content = await response.Content.ReadAsStringAsync();
            Joke? joke = Newtonsoft.Json.JsonConvert.DeserializeObject<Joke>(content);

            if (joke == null)
                return;

            Console.WriteLine(joke.Setup);
            Console.WriteLine(joke.Punchline);
            Console.WriteLine();
        }
        else
        {
            var currentColor = Console.ForegroundColor;

            string content = await response.Content.ReadAsStringAsync();
            Console.ForegroundColor = ConsoleColor.Red;
            Console.WriteLine(content);

            Console.ForegroundColor = currentColor;        
        }
    }
}

public class Joke
{
    public string Setup { get; set; }
    public string Punchline { get; set; }
}
```

### Proxies 代理

如果您想使用代理到達目標，C# 中的 HTTPClient 將幫助您。它有一個特殊的_處理程序_，您可以將其配置為使用代理。

以下示例有一個代理，該代理是\***虛構的\***。

```c#
HttpClientHandler handler = new()
{
    Proxy = new WebProxy(new Uri($"socks5://123.45.678.90:12345")),
    UseProxy = true,
};

using (HttpClient client = new(handler))
{
    client.Timeout = TimeSpan.FromSeconds(10);

    HttpResponseMessage response = await client.GetAsync("https://official-joke-api.appspot.com/random_ten");

    if (response.IsSuccessStatusCode)
    {
        string content = await response.Content.ReadAsStringAsync();

        List<Joke>? jokes = JsonConvert.DeserializeObject<List<Joke>>(content);

        if (jokes == null)
            return;

        foreach (Joke joke in jokes)
        {
            Console.WriteLine(joke.Setup);
            Console.WriteLine(joke.Punchline);
            Console.WriteLine();
        }
    }
}

public record Joke(string Setup, string Punchline);
```

### Download An Image 下載圖片

您可以使用 HTTPClient 從 Web 下載圖像，將其存儲在字節數組中，然後將其另存為文件。為此，我們使用**GetByteArrayAsync(** uri \*\*)\*\*方法。

```c#
using (HttpClient httpClient = new())
{
    byte[] imageBytes = await httpClient.GetByteArrayAsync("https://i.imgur.com/OVFxdJy.jpg");

    string desktopPath = Environment.GetFolderPath(Environment.SpecialFolder.Desktop);
    string localPath = Path.Combine(desktopPath, "this_makes_your_day.jpg");

    File.WriteAllBytes(localPath, imageBytes);
}
```

## 結論

C# 中的 HTTPClient 主要在向外部目標（通常是 API）請求或發送數據時使用。它有不同的選項和設置，您可以使用它來提出您的請求。

它比 HttpWebRequest 有很大的優勢，但是 HttpWebRequest 仍在新老項目中使用。了解 HttpWebRequest 的工作原理是個好主意，儘管這對 HTTPClient 來說意義重大。
