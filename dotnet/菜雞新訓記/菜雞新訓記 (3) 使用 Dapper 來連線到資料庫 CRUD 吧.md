---
kind: reprint
source: https://igouist.github.io/post/2021/05/newbie-3-dapper
author: igouist
---

# 菜雞新訓記 (3): 使用 Dapper 來連線到資料庫 CRUD 吧



![Image](https://i.imgur.com/aIHQL5Z.png)

這是俺整理公司新訓內容的第三篇文章，目標是在 .NET Core 簡單地使用 Dapper 連線到資料庫並完成 CRUD 的功能。

接續 [上一篇](https://igouist.github.io/post/2021/05/newbie-2-webapi) 的進度，我們接著要來連線到資料庫中完成我們的 Web Api 的 CRUD 範例。因為從新訓時期到現在工作團隊作業上主要都是使用 Dapper 來做連線資料庫的工作，這邊就直接用 Dapper 來推進吧！

Dapper 有多好用呢？它輕量、它簡單、它快速。總之先把大神們的介紹文直接拿來鎮樓：

- [短小精悍的.NET ORM神器 – Dapper - 黑暗執行緒](https://blog.darkthread.net/blog/dapper/)
- [另一種資料存取對映處理方式的選擇 - Dapper - mrkt 的程式學習筆記](https://dotblogs.com.tw/mrkt/2016/06/10/153606)
- [好用的微型 ORM：Dapper - Huanlin 學習筆記](https://www.huanlintalk.com/2014/03/a-micro-orm-dapper.html)

那麼按照慣例，我們先來 ~~吹捧今天的主角~~ 說明一點簡單的前因後果吧。想直接實作的朋友，可以跳到[正式開工](https://igouist.github.io/post/2021/05/newbie-3-dapper/#正式開工)的小節呦。

## 前言、基本觀念

### 弱型別與強型別

在很久很久以前，從資料庫裏面撈資料會使用 `DataTable`、`DataSet` 的做法去取，但有一個小小的問題，就是這些做法並不是強型別的。當我們在從 `Rows[0]["ID"]` 取值的時候，其實我們不知道 Key 對不對，也不知道取不取得到值，更不知道取出來的值是哪個型別。

當強型別的語法寫慣了之後，再回到上面的這種弱型別環境，就常常會遇到一些令人抓狂的狀況。像是編譯的時候沒出錯，執行的時候才炸掉；因為沒有指定型別，也就無法進行某些操作，必須額外再轉型；轉了型也不知道跑起來是不是和想的一樣等等……內心充滿了不安感。戰戰慄慄，汗不敢出。

> 當然，強型別與弱型別各有優缺點，會按照語言環境、個人喜好等等有適用的場合。這邊就不再贅述，對這部分有興趣的朋友可以參照：
>
> - [何謂「強型別」(Strong Type) - The Will Will Web](https://blog.miniasp.com/post/2008/01/21/What-is-Strong-Type)
> - [你不可不知的 JavaScript 二三事#Day3：資料型態的夢魘——動態型別加弱型別](https://ithelp.ithome.com.tw/articles/10202260)
>
> 至於我們上面提到的，像使用 `DataTable` 會掉的坑，可以參考 coreychen71 的這篇 [強型別與弱型別](https://coreychen71.github.io/posts/2019-06/strongtypeweaktype/) 的範例，有使用過（踩過）的朋友可能會比較眼熟。
>
> 說到底，想要編譯時期就發現錯誤？或是不想耗費心力在轉型過程？本來就會有相對應的代價。
>
> 不過就我個人認為，既然都在 C# 這個環境了，又是嘗試向已知的資料表取值，取出來的值通常都還會進行進一步的操作，最後還是要指定型別做轉型囧…
>
> 既然你遲早要用強型別的，為什麼不一開始就用強型別呢？還能少一堆坑。
>
> 順便感謝微軟拔拔讓我有 `var` 可以用，自動幫我檢查型別又讓我可以爽寫，還不耗效能，讚啦。

------

### 物件關係對映（ORM）

因為前述的型別問題，大多數人就投向了 ORM 的懷抱。

ORM 的全名是物件關係對映（Object Relational Mapping），核心理念是將資料庫的資料映射到物件裡，這樣就可以在我們的程式語言中像直接操作物件一樣地去操作資料。

例如說在之前的這篇 [Asp.net MVC: Entity Framework 連線資料庫](https://igouist.github.io/post/2019/12/aspnet-connect-db-ef)，就利用了 Entity Framework 這個工具去把資料表和類別對接起來，進而直接在程式碼中對資料進行操作。

> 關於 ORM 的更多介紹，例如優點和缺點等等，可以參照這兩篇：
>
> - [資料庫設計概念 - ORM - johnliutw](https://ithelp.ithome.com.tw/articles/10207752)
> - [ORM 实例教程 - 阮一峰](http://www.ruanyifeng.com/blog/2019/02/orm-tutorial.html)

雖然 ORM 帶來了很多方便的好處，例如說：

- 可以自動產生 SQL 語法不用自己寫
- 包裝之後的語法讓可讀性變好了，操作也變方便了
- 資料操作放在專案裡容易維護
- 通常都已經做了一些必要的處理，例如用參數的方式幫忙擋了 SQL Injection 啦，使用交易、避免更新衝突等等。

但畢竟自動產生語法是有極限的，因此 ORM 同時也有著一些問題：

- 肥大、前置作業太多
- 當語句複雜時轉換成 SQL 的效能可能會變差
- 對於較特別或客製化的場景可能會較難處理

最常被提到的坑就是前面提到的「複雜場景產生的 SQL 效能可能會變差」這點；而較難處理的部分，最常見的就是遇到翻寫古老 SQL 程式時，難以將原本的 T-SQL 語法順利轉換成 ORM 語法的狀況，又或者是原本的資料表設計並沒有好好弄好關聯和正規化、早已變得一團亂，導致對已經運行一段時間的專案引入 ORM 就會變得相當困難。

因此，在使用上需要根據狀況，再決定是否要用 ORM 來進行開發。像是如果對資料表的操作語句單純（例如經典傳統百年不變的 CRUD），或是不需要對 SQL 有太深的認識也要能夠開發，那使用 ORM 就是上上之選。

> 關於各個狀況的比較，這邊推薦黑大的 [閒聊：用 LINQ 還是自己寫 SQL？](https://blog.darkthread.net/blog/linq-or-direct-sql/)，整理了在 Dotnet 執行 SQL 邏輯的策略和優缺點，建議可以先看過會比較有概念。
>
> 另外，關於一些 ORM 的問題點，除了上面 ORM 介紹文章中提到的缺點以外，也可以閱讀這篇 [你不需要 ORM](https://gordon.hk/blog/2019/10/22/You-Dont-need-ORM/) 有實際的程式碼例子可能會比較有感覺。

------

### Dapper

那既然這樣，我們能不能在上面兩者之間取得一個平衡呢？

讓一個工具來協助我們處理和資料庫的溝通，幫忙我們把資料表對應到類別，把資料轉換成物件，讓我們可以使用強型別去開發；同時我們又可以保留大部分的彈性，像是讓我們自己撰寫 SQL 語法或一些細微的設定，讓我們可以主動去調整效能？

如果又比起 ORM 更輕量，又能快速方便好用就好了。

這種工具真的存在嗎？

有，就是今天的主角 －－ Dapper！

Dapper 是一個輕量的 ORM 工具，[效能好](https://noamlewis.wordpress.com/2012/07/18/net-4-5-improves-orm-performance-across-the-chart/)，使用簡單，自由度高。

它的特色就是快速、輕便、效能好，使用方式也相當簡單，因為它只幫你處理資料轉物件的部份，剩下的像是 SQL 語法和連線，你還是要自己負責。

不過，我們有讚讚的物件就行了唄，畢竟是物件導向嘛，能當成物件使用最重要了。而且換個方向想，至少我們奪回了 SQL 語法的自主權（？）

> 補充一下：如果你用了 Dapper 但還是很不想寫 SQL，場景又是簡單的 CRUD。呃，~~為什麼不去用隔壁棚的 EF~~，你可以試試加裝 [DapperExtensions](https://github.com/tmsmith/Dapper-Extensions) 或 [Dapper.Contrib](https://dotblogs.com.tw/yc421206/2019/03/07/dapper_contrib_insert_update_get)

當我們有了 Dapper 之後…

把 Dapper 交給那些 認真到會去 SSMS 跑一次 SQL 語法看執行效能的那些朋友，你們可以盡量發揮你們的 SQL 能力取得更好的效能。

把 Dapper 交給那些 覺得 Entity Framework 效能地雷太多（或只是像我一樣不太熟）的朋友，神秘的事故發生率會少很多。

把 Dapper 交給那些 覺得還要先建一堆東西做一堆事才能拿資料很麻煩的朋友，快速簡單 Model 開下去 SQL 砸下去就可以爽拿 DB 資料。

把 Dapper 交給那些 翻寫古老屎山的朋友，移植又臭又長 SQL 語法到新框架的時候，終於可以整個拉過來先跑，再步步為營去重構。

所以說，Dapper 好！Dapper 妙！Dapper 嚇嚇叫！

## 正式開工

### 環境準備（建立資料表、安裝 Dapper）

到這邊已經用了兩千字來吹捧 Dapper 了，差不多讓我們把鏡頭轉回到 Web Api 服務上，邊推進邊說明一些簡單的用法吧！

接續我們 [上一篇](https://igouist.github.io/post/2021/05/newbie-2-webapi) 的進度，在上一篇裡，我們對外開了一組簡單 CRUD 的 API，用來查增修刪我們的卡片資訊。

但當時只是開了簡單的服務，資料也是暫存的而已。所以這篇的目標是將我們的 API 服務連到資料庫，真正實現對卡片資料的操作。

先讓我們說明一下本篇的示範環境，假設在 Local 的 SQL Server 裡，有著一個 `Newbie` 資料庫，其中有一張 `Card` 的資料表。其結構如下：

![img](https://i.imgur.com/Gec9WeQ.png)

```sql
CREATE TABLE [dbo].[Card](
	[Id] [int] IDENTITY(1,1) NOT NULL,
	[Name] [nvarchar](50) NULL,
	[Description] [nvarchar](50) NULL,
	[Attack] [int] NOT NULL,
	[Health] [int] NOT NULL,
	[Cost] [int] NOT NULL
) ON [PRIMARY]
GO
```

該表用來存放基本的卡牌資訊，包含該卡牌的 ID（主鍵）、卡牌名稱、卡牌描述、攻擊力、血量、花費值。

> 小提示：使用其他結構的資料表，例如用自己建立的資料表，或是經典的北風資料表，甚至是公司內的資料表來練習開發的朋友，要記得後續的處理都要改成你使用的資料表的內容呦！

現在我們有了一張資料表，鏡頭轉回到我們的 .net Core Web API 服務。

既然今天的主角是 Dapper，當然要先打開 NuGet 把 Dapper 給安裝下來。

![img](https://i.imgur.com/rT0Nop6.png)

![img](https://i.imgur.com/66GtKJA.png)

![img](https://i.imgur.com/0fuLbQC.png)

恭喜你，你已經完成本篇文章實作的一半了。

------

### 建立對應資料表的類別

使用 Dapper 的時候，我們要先準備好把資料從拉回來時，用來轉換成物件的類別。

我們在上次已經有在 `Models` 資料夾裡建立好 `Card.cs`，現在我們就來修改它。（不是從上一期開始跟的朋友，請製作一個和資料表欄位相對應的 Class）

```csharp
/// <summary>
/// 卡片
/// </summary>
public class Card
{
    /// <summary>
    /// 卡片編號
    /// </summary>
    public int Id { get; set; }

    /// <summary>
    /// 卡片名稱
    /// </summary>
    public string Name { get; set; }

    /// <summary>
    /// 卡片描述
    /// </summary>
    public string Description { get; set; }

    /// <summary>
    /// 攻擊力
    /// </summary>
    public int Attack { get; set; }

    /// <summary>
    /// 血量
    /// </summary>
    public int Health { get; set; }

    /// <summary>
    /// 花費
    /// </summary>
    public int Cost { get; set; }
}
```

> 小提示：如果資料表的欄位數量很多很龐大，手刻會刻到死的朋友，可以試試用 Linqpad 去產生對應的類別。請參閱 mrkt 的這篇 [Dapper - 使用 LINQPad 快速產生相對映 SQL Command 查詢結果的類別](https://dotblogs.com.tw/mrkt/2016/06/14/190618)。
>
> 用 Linqpad 直接從資料表產生類別，和 Dapper 搭配起來，開發上那可真是一個快啊！這邊推薦給大家。

> 補充：如果建立類別的時候，對於把 SQL Server 裡面的型別對應到 C# 裡有困難的話，可以參閱 [SQL Server 資料類型對應](https://docs.microsoft.com/zh-tw/dotnet/framework/data/adonet/sql-server-data-type-mappings)（感謝 [Sian](https://sunnyday0932.github.io/2020/dotnet-core-webapi實作使用dapper-1/) 的補充）。至於其他家的 DB，呃，還請大家自己查一下囉。

建立類別的時候要注意，這個類別是用來接收你最後拉回來的資料的。要是你最後打算 Join 兩張表然後各取兩個欄位，這裡的類別就是那兩個欄位；要是你查詢之後只打算返回其中的幾個欄位，這裡的類別就是那幾個欄位。

在工作上就見識過同事在查詢一張數百欄位的大型表時，針對該表建立了少數欄位、一半欄位、全部欄位三種情況的類別，搭配了泛型和 Dapper 的轉換來接收不同數量的值，藉此控制不同查詢場景時的傳輸成本。因此，建立類別的時候還是要依照你想要拿到哪些資料下去調整比較好。

刻好要用來接資料的類別之後，接著就讓我們來實作 CRUD 的銜接部分吧！

------

### 使用 Dapper 實作 CRUD

> 小提示：你可能需要對 SQL 有基本的認識，至少需要知道對應 CRUD 的 SELECT, INSERT, UPDATE 和 DELETE。不太熟悉的朋友可以參考 [SQL語法教學](https://www.1keydata.com/tw/sql/sql.html)

> 小提示：這個章節會實際操作 Dapper 去資料表取得資料，如果過程中對 Dapper 的各個 Function 使用上有疑惑的話，可以參閱尼克人生的這篇 [輕量級ORM - Dapper 使用](https://dotblogs.com.tw/OldNick/2018/01/15/Dapper#Dapper - Query)，對各方法都有範例，相當好懂，推薦給大家。

在這個步驟，我打算在方案中新增一個 `Repository` 資料夾，並在裡面新增 `CardRepository.cs` 檔案，用來放我們接下來對資料表的操作。

這邊的資料夾和檔案命名是因為在公司分層習慣了，所以原本使用 MVC 的朋友，可以把檔案或是以下實作的部分新增在代表資料處理的 `Models` 裡就好了，例如加到 `Models/Card.cs`，或是放在任何你用來放資料庫連線處理的位置即可，位置並不是本篇記錄的重點。

現在我們應該會有個空的 Class：

```csharp
/// <summary>
/// 卡片資料操作
/// </summary>
public class CardRepository
{

}
```

然後讓我們加上連線字串，我的範例直接使用 Localhost 的 DB，所以如果你也有按照步驟來測試的話，這邊請改成你的連線字串。

連線字串放好之後，回到我們的 `CardRepository`，加上放置連線字串的私有常數和建構式：

```csharp
/// <summary>
/// 連線字串
/// </summary>
private readonly string _connectString = @"Server=(LocalDB)\MSSQLLocalDB;Database=Newbie;Trusted_Connection=True;";
```

這邊採用直接放私有成員的做法，如果你有多個類別需要用到資料庫連線，可以考慮集中管理連線字串到 `appsettings.json` 或是 `web.config` 之類的地方。這邊之所以直接放到私有成員裡寫死，是因為這邊的範例情景相對簡單，先不打算挪出去而模糊焦點 ~~，而且我之後要改成依賴注入的時候也比較好改。~~

接著就讓我們從查詢全部卡片的方法開始加入吧！我們應該要有一個回傳 卡片串列 的方法（我這邊習慣使用 IEnumerable，比較不熟的朋友用 List 也沒關係）

準備好了嗎？深呼吸！我們要對資料表進行查詢囉：

```csharp
/// <summary>
/// 查詢卡片列表
/// </summary>
/// <returns></returns>
public IEnumerable<Card> GetList()
{
    using (var conn = new SqlConnection(_connectString))
    {
        var result = conn.Query<Card>("SELECT * FROM Card");
        return result;
    }
}
```

就是這麼簡單！

Dapper 會替實作 IDbConnection 的類別們，也就是我們平常用的連線小幫手們加上擴充方法，讓我們可以方便簡單地使用。

> 小提示：過程中看到紅線請不要慌，如果有需要 using 的就請順手 using 一下，例如 `Card` 的類別、等等會用到的 `Dapper` 等等。或是像 `SqlConnection` 沒抓到套件，就 Alt Enter 安裝一下即可。

> 補充：因為 Dapper 對每個資料庫系統所產生的語法會不一樣，所以假如你是使用 MySql 的朋友，這邊的連線請改成使用 `MySqlConnection`

如果你的 C# 版本大於 8.0 ，using 語句甚至不需要大括弧，如果又不像我喜歡把每一小段都宣告成變數來加減表達意圖的話，整體就更簡潔了：

```csharp
/// <summary>
/// 查詢卡片列表
/// </summary>
/// <returns></returns>
public IEnumerable<Card> GetList()
{
    using (var conn = new SqlConnection(_connectString))
    return conn.Query<Card>("SELECT * FROM Card");
}
```

這邊也能看到 Dapper 最常見的使用方式：當我們查詢的時候，可以使用 `Query<T>` 方法，並將我們要接收資料的類別放入泛型，再將我們的 SQL 語法做為參數傳入。Dapper 會執行 SQL 並嘗試把查詢結果轉換成我們指定的類別。

> 補充：Dapper 會去對照資料表的欄位名稱和類別中的欄位名稱，名稱一樣且型別能對應的就會把資料放進去。
>
> 如果遇到兩者有不一樣的，例如資料表欄位開成 `card_name` 但是類別中的欄位是 `Name` 這種時候，比較簡單暴力的做法是在 `SELECT` 的時候用 `AS` 替欄位命名，或是告訴 Dapper 指定的欄位對照，有這個需求的朋友請參照軟體主廚的這篇 [料理佳餚 - Dapper 自定義欄位對應的三種方式](https://dotblogs.com.tw/supershowwei/2016/08/16/175753)

> 補充：如果有好奇的朋友也可以嘗試不給 `Query<T>` 指定型別，這樣回來的就會是 `dynamic`，但是不太建議這樣用啦，畢竟我們就是打算要享受強型別的好處才這樣做的嘛！何必又回到方法不能用、執行才報錯的時代呢？乖乖建立類別還比較實在。這部分請參見 [每個查詢的結果都要定義並對映一個類別嗎？（使用 dynamic）](https://dotblogs.com.tw/mrkt/2016/06/12/170411)

------

事不宜遲，我們接著建立查詢單筆的方法吧：

```csharp
/// <summary>
/// 查詢卡片
/// </summary>
/// <returns></returns>
public Card Get(int id)
{
    using (var conn = new SqlConnection(_connectString))
    {
        var result = conn.QueryFirstOrDefault<Card>(
            "SELECT TOP 1 * FROM Card Where Id = @id",
            new 
            { 
                Id = id,
            });
        return result;
    }
}
```

從這段我們可以知道兩件事情：

除了 `Query` 之外，Dapper 還準備了一些針對不同查詢的 `Query` 方法給大家使用，例如：

- `QueryFirst` 只取第一筆，如果找不到就報錯
- `QueryFirstOrDefault` 只取第一筆，如果找不到就丟回預設值
- `QuerySingle`，只取一筆，如果找不到或是找到多筆符合的就報錯
- `QuerySingleOrDefault` 只取一筆，如果找不到就丟回預設值，找到多筆符合的就報錯

除此之外，如果你的架構已經大量使用非同步，Dapper 也都有提供非同步版本的方法使用，例如 `QueryAsync`，這邊的示範專案還在黑暗時代，就不贅述。

至於 `Query` 系列裡面比較特別的應該就是 `QueryMultiple` 了，它能允許同時執行多段 SQL，例如 `SELECT * FROM Card; SELECT TOP 1 * FROM Card;` 之類的，並取回一串結果。

取得之後再逐一用 `Read<T>()` 的方式來把結果轉換成物件，但由於平常開 Function 會需要考慮 [單一職責原則](https://igouist.github.io/post/2020/10/oo-10-single-responsibility-principle) 的關係，很少接觸到有需要在同個方法執行兩段 SQL 並回傳兩個甚至多個不同物件的狀況，這邊就留給有需要的朋友自己嘗試囉。

------

回到我們剛剛開好的查詢卡片方法，第二件事就是我們知道了 `Query<T>` 系列可以傳入第二個參數，用來告訴 Dapper 這次 SQL 語法會用到的變數。

只要丟個物件進去，就算是匿名物件，Dapper 也會幫忙做成 SQL 的參數。有些朋友可能會問：為什麼不直接用 `+` 的方式或是直接 [字串插值](https://igouist.github.io/post/2020/08/csharp-string-interpolation) 組到 SQL 裡面就好了呢？

如果真的有這個問題的話，呃，`SQL Injection` 先了解一下。

> 給那些想瞭解又懶得跳出去查的朋友：
>
> - [網站安全🔒 一次看懂 SQL Injection 的攻擊原理 — 「雍正繼位之謎」](https://medium.com/程式猿吃香蕉/淺談駭客攻擊-網站安全-一次看懂-sql-injection-的攻擊原理-b1994fd2392a)
> - [攻擊行為－SQL 資料隱碼攻擊 SQL injection](https://ithelp.ithome.com.tw/articles/10189201)

簡單來說，為了防範不良分子在 SQL 上「自由發揮」，通常都不會允許直接把傳進來的參數等等直接丟到 SQL 裡面去串起來。

所以現在比較常見也被認為是最有效的作法是，把參數另外宣告成 SQL 提供的變數，例如 Sql Server 的 [變數](https://docs.microsoft.com/zh-tw/sql/t-sql/language-elements/variables-transact-sql?view=sql-server-ver15)。

如此一來，資料庫就會先解析完 SQL 語法，才嘗試把變數「作為字串」塞進去指定的位置。藉此來防範 SQL Injection 的問題。

同樣是 `SELECT * FROM Card WHERE id = {id};`，然後傳入一樣是 `1; DROP TABLE Card`;

- 直接銜接：`SELECT * FROM Card WHERE id = 1; DROP TABLE Card;`
- 作為字串：`SELECT * FROM Card WHERE id = "1; DROP TABLE Card";`

這樣子的差異應該就能理解為什麼參數化查詢能夠防範 SQL Injection 了，因為通通給你包起來。除此之外，參數化查詢還有能夠重複使用執行計畫提升效能、好維護等等好處，真的是屌打字串拼接黨。

回到我們剛剛開好的查詢卡片方法，在這邊我們必須用卡片 ID 來查詢卡片，所以必須將 ID 丟進去。那就可以看到我們的 SQL 條件有加上 `Where Id = @Id`，告訴 SQL 我們有一個 `@Id` 變數，接著我們再把 ID 包成物件丟給 Dapper 請他幫忙處理一下。

不過我個人比較不喜歡把東西都集中一坨在方法的呼叫上，所以我會把 SQL 和參數都拆分出來，並使用 DynamicParameters 來建立參數，如下：

```csharp
/// <summary>
/// 查詢卡片
/// </summary>
/// <returns></returns>
public Card Get(int id)
{
    var sql =
    @"
        SELECT * 
        FROM Card 
        Where Id = @id
    ";

    var parameters = new DynamicParameters();
    parameters.Add("Id", id);

    using (var conn = new SqlConnection(_connectString))
    {
        var result = conn.QueryFirstOrDefault<Card>(sql, parameters);
        return result;
    }
}
```

這樣切出來做成變數也比較整潔美觀好清理，如果有需要按照狀況增加 SQL 語法或參數的時候，也比較方便。例如：

```csharp
// 假設查詢卡片列表的時候，為了知道這回合能用的卡片有哪些
// 需要指定卡片的「花費值」必須低於多少，所以多了一個參數 int? cost 的場合：
if (cost != null && cost > 0)
{
    sql += " And Cost <= @Cost ";
    parameters.Add("Cost", cost);
}
```

當然上面這段只是示範，實務上在附加條件和參數的時候也會遇到…

- 因為不想判斷前面有沒有 `WHERE` 語句，所以把所有條件先放到陣列中，最後再用 `String.Join` 以 `AND` 連接起來的
- 同上，但比較古老的時代會使用 `WHERE 1 = 1` 然後再接 `AND` 串條件
- 由於參數太多，因為效能上的考量，所以不用 `+=` 來連接 SQL 語句，而是使用 `StringBuilder` 的
- 把 SQL 語法內共用的部分拆出去做成 Private 以提高程式碼共用程度，減少重複贅詞的
- 直接把整個 SQL 語法拆出去放別的地方的

等等各種因應狀況所採取的手段，各位在處理這部分的時候，如果不是自己新建的專案，還請觀察一下團隊的用法再自行調整。

------

除此之外，這邊還有一個小細節需要補充：當我們在使用 `DynamicParameters`，把變數丟進去時，Dapper 會自動幫我們做型別上的轉換。

BUT！就是這個 BUT！對於一些 `int` 啦、`bool` 的是不會有什麼問題，但一些比較難對應得到的型別，Dapper 就會嘗試用比較穩的打法，例如 `String` 就會變成 `nvarchar(4000)` 之類的。

但是，型別不同對 SQL 的執行計畫也會造成影響，甚至會造成效能變差。針對這個問題，我們可以在加入參數的時候，一併告訴 Dapper 我們指定的型別。

例如前述的 `parameters.Add("Id", id)`，可以給第三個參數告訴它 DBType，變成 `parameters.Add("Id", id, System.Data.DbType.Int32);`

關於這個型別調整的部分，有興趣的朋友可以閱讀軟體主廚的這篇：[Dapper 用起來很友善，但是預設的參數型別對執行計劃不太友善](https://dotblogs.com.tw/supershowwei/2019/08/12/232213)

裡面針對型別影響執行計畫有進行測試，並且提供了針對 DbString 更方便使用的 String 擴充方法，我們團隊也有將其應用在專案上，推薦大家可以瞭解一下。

------

現在我們已經解決了查詢，接著讓我們來處理一下新增卡片和修改卡片的部分吧！

首先先讓我們回到上篇的 `CardParameter`，把這次多的欄位也給補上。如果是這篇才加入的朋友，請自己捏一個 `CardParameter.cs` 出來，我們在新增和修改的時候會拿來當作參數使用。

```csharp
/// <summary>
/// 卡片參數
/// </summary>
public class CardParameter
{
    /// <summary>
    /// 卡片名稱
    /// </summary>
    public string Name { get; set; }

    /// <summary>
    /// 卡片描述
    /// </summary>
    public string Description { get; set; }

    /// <summary>
    /// 攻擊力
    /// </summary>
    public int Attack { get; set; }

    /// <summary>
    /// 血量
    /// </summary>
    public int Health { get; set; }

    /// <summary>
    /// 花費
    /// </summary>
    public int Cost { get; set; }
}
```

如果在業務上有些需求導致新增和修改的參數不一樣的朋友（例如有些欄位不開放修改），也可以考慮拆分成兩個 Parameter 去面對不同的場景。

補上之後讓我們回到 `CardRepository`，利用 SQL 的 `INSERT` 和 `UPDATE` 語法來把 `Parameter` 的內容給塞進去吧：

```csharp
/// <summary>
/// 新增卡片
/// </summary>
/// <param name="parameter">參數</param>
/// <returns></returns>
public int Create(CardParameter parameter)
{
    var sql =
    @"
        INSERT INTO Card 
        (
            [Name]
           ,[Description]
           ,[Attack]
           ,[Health]
           ,[Cost]
        ) 
        VALUES 
        (
            @Name
           ,@Description
           ,@Attack
           ,@Health
           ,@Cost
        );
        
        SELECT @@IDENTITY;
    ";

    using (var conn = new SqlConnection(_connectString))
    {
        var result = conn.QueryFirstOrDefault<int>(sql, parameter);
        return result;
    }
}

/// <summary>
/// 修改卡片
/// </summary>
/// <param name="id">卡片編號</param>
/// <param name="parameter">參數</param>
/// <returns></returns>
public bool Update(int id, CardParameter parameter)
{
    var sql =
    @"
        UPDATE Card
        SET 
             [Name] = @Name
            ,[Description] = @Description
            ,[Attack] = @Attack
            ,[Health] = @Health
            ,[Cost] = @Cost
        WHERE 
            Id = @id
    ";

    var parameters = new DynamicParameters(parameter);
    parameters.Add("Id", id, System.Data.DbType.Int32);

    using (var conn = new SqlConnection(_connectString))
    {
        var result = conn.Execute(sql, parameters);
        return result > 0;
    }
}
```

這邊可以注意到，除了查詢用的 `Query` 以外，Dapper 也提供了執行指令用的 `Execute`。在一些不需要回傳東西的時候，例如更新和刪除，又或是單純呼叫預存程序（SP, Stored Procedure）的時候相當方便，而且當然也有提供非同步的版本可以使用。

而最強大的地方是，Dapper 支援多筆新增和更新。例如前面我們的新增卡片 `Create(CardParameter parameter)` 裡面：

如果我們是直接改成丟一整串的新卡片進來，也就是 `Create(IEnumerable<CardParameter> parameters)` 然後呼叫 Dapper 來跑 `conn.Execute(sql, parameters)` 是可以新增多筆卡片的，更新也是同樣的道理。

同時也因為可以執行多個 SQL 語句、新增多筆資料，Dapper 也提供了交易（Transaction），只需要 `using(var transaction = conn.BeginTransaction())`，完成後 `transaction.Commit()` 就可以囉。不過這些部份我們暫時不會用到，有興趣的朋友可以再自己嘗試看看。

> 補充：由於我個人習慣新增資料之後，用 `@@IDENTITY` 或 `LAST_INSERT_ID()` 這類語法把該筆資料的 ID 拉回來方便後續檢查和使用，所以在 `Create()` 是使用 `Query<int>` 的方式來取得 ID。沒有這類需求的朋友，也可以像 `Update()` 的部分一樣用 `Execute` 就可以了。

到這邊大家應該已經大致了解 Dapper 的使用方式了，讓我們把最後的刪除卡片補上去吧：

```csharp
/// <summary>
/// 刪除卡片
/// </summary>
/// <param name="id">卡片編號</param>
/// <returns></returns>
public void Delete(int id)
{
    var sql =
    @"
        DELETE FROM Card
        WHERE Id = @Id
    ";

    var parameters = new DynamicParameters();
    parameters.Add("Id", id, System.Data.DbType.Int32);

    using (var conn = new SqlConnection(_connectString))
    {
        var result = conn.Execute(sql, parameters);
    }
}
```

到這邊我們就做完 CRUD 一套囉！現在的 `CardRepository` 應該會長得像這樣：

```csharp
public class CardRepository
{
    /// <summary>
    /// 連線字串
    /// </summary>
    private readonly string _connectString = 
    @"Server=(LocalDB)\MSSQLLocalDB;Database=Newbie;Trusted_Connection=True;";

    /// <summary>
    /// 查詢卡片列表
    /// </summary>
    /// <returns></returns>
    public IEnumerable<Card> GetList()
    {
        var sql = "SELECT * FROM Card";

        using (var conn = new SqlConnection(_connectString))
        {
            var result = conn.Query<Card>(sql);
            return result;
        }
    }

    /// <summary>
    /// 查詢卡片
    /// </summary>
    /// <returns></returns>
    public Card Get(int id)
    {
        var sql =
        @"
            SELECT * 
            FROM Card 
            Where Id = @id
        ";

        var parameters = new DynamicParameters();
        parameters.Add("Id", id, System.Data.DbType.Int32);

        using (var conn = new SqlConnection(_connectString))
        {
            var result = conn.QueryFirstOrDefault<Card>(sql, parameters);
            return result;
        }
    }

    /// <summary>
    /// 新增卡片
    /// </summary>
    /// <param name="parameter">參數</param>
    /// <returns></returns>
    public int Create(CardParameter parameter)
    {
        var sql =
        @"
            INSERT INTO Card 
            (
               [Name]
              ,[Description]
              ,[Attack]
              ,[Health]
              ,[Cost]
            ) 
            VALUES 
            (
                 @Name
                ,@Description
                ,@Attack
                ,@Health
                ,@Cost
            );
            
            SELECT @@IDENTITY;
        ";

        using (var conn = new SqlConnection(_connectString))
        {
            var result = conn.QueryFirstOrDefault<int>(sql, parameter);
            return result;
        }
    }

    /// <summary>
    /// 修改卡片
    /// </summary>
    /// <param name="id">卡片編號</param>
    /// <param name="parameter">參數</param>
    /// <returns></returns>
    public bool Update(int id, CardParameter parameter)
    {
        var sql =
        @"
            UPDATE Card
            SET 
                 [Name] = @Name
                ,[Description] = @Description
                ,[Attack] = @Attack
                ,[Health] = @Health
                ,[Cost] = @Cost
            WHERE 
                Id = @id
        ";

        var parameters = new DynamicParameters(parameter);
        parameters.Add("Id", id, System.Data.DbType.Int32);

        using (var conn = new SqlConnection(_connectString))
        {
            var result = conn.Execute(sql, parameters);
            return result > 0;
        }
    }

    /// <summary>
    /// 刪除卡片
    /// </summary>
    /// <param name="id">卡片編號</param>
    /// <returns></returns>
    public void Delete(int id)
    {
        var sql =
        @"
            DELETE FROM Card
            WHERE Id = @Id
        ";

        var parameters = new DynamicParameters();
        parameters.Add("Id", id, System.Data.DbType.Int32);

        using (var conn = new SqlConnection(_connectString))
        {
            var result = conn.Execute(sql, parameters);
        }
    }
}
```

------

### 對接與測試

接著就讓我們回到 `CardController` 把這邊的操作和 API 對外的開口給銜接起來。

首先先把 `CardRepository` 宣告成私有成員，取代掉我們原本用來暫存卡片資料的 `private static List<Card> _cards`。並且在建構式進行賦值（~~一樣是打算讓之後改成注入的時候比較好改XD~~）

```csharp
/// <summary>
/// 卡片資料操作
/// </summary>
private readonly CardRepository _cardRepository;

/// <summary>
/// 建構式
/// </summary>
public CardController()
{
    this._cardRepository = new CardRepository();
}
```

後續其實就是把 `_cards` 給砍掉後，並且把各個操作改成呼叫 `CardRepository` 對應的方法，如果是這篇才加入的朋友，也就直接建立各個方法去對接 `CardRepository` 即可。

過程就不再贅述。修改後應該會長這個樣子：

```csharp
[ApiController]
[Route("[controller]")]
public class CardController : ControllerBase
{
    /// <summary>
    /// 卡片資料操作
    /// </summary>
    private readonly CardRepository _cardRepository;

    /// <summary>
    /// 建構式
    /// </summary>
    public CardController()
    {
        this._cardRepository = new CardRepository();
    }

    /// <summary>
    /// 查詢卡片列表
    /// </summary>
    /// <returns></returns>
    [HttpGet]
    public IEnumerable<Card> GetList()
    {
        return this._cardRepository.GetList();
    }

    /// <summary>
    /// 查詢卡片
    /// </summary>
    /// <param name="id">卡片編號</param>
    /// <returns></returns>
    [HttpGet]
    [Route("{id}")]
    public Card Get([FromRoute] int id)
    {
        var result = this._cardRepository.Get(id);
        if (result is null)
        {
            Response.StatusCode = 404;
            return null;
        }
        return result;
    }

    /// <summary>
    /// 新增卡片
    /// </summary>
    /// <param name="parameter">卡片參數</param>
    /// <returns></returns>
    [HttpPost]
    public IActionResult Insert([FromBody] CardParameter parameter)
    {
        var result = this._cardRepository.Create(parameter);
        if (result > 0)
        {
            return Ok();
        }
        return StatusCode(500);
    }

    /// <summary>
    /// 更新卡片
    /// </summary>
    /// <param name="id">卡片編號</param>
    /// <param name="parameter">卡片參數</param>
    /// <returns></returns>
    [HttpPut]
    [Route("{id}")]
    public IActionResult Update(
        [FromRoute] int id,
        [FromBody] CardParameter parameter)
    {
        var targetCard = this._cardRepository.Get(id);
        if (targetCard is null)
        {
            return NotFound();
        }

        var isUpdateSuccess = this._cardRepository.Update(id, parameter);
        if (isUpdateSuccess)
        {
            return Ok();
        }
        return StatusCode(500);
    }

    /// <summary>
    /// 刪除卡片
    /// </summary>
    /// <param name="id">卡片編號</param>
    /// <returns></returns>
    [HttpDelete]
    [Route("{id}")]
    public IActionResult Delete([FromRoute] int id)
    {
        this._cardRepository.Delete(id);
        return Ok();
    }
}
```

接著就和上一篇一樣，讓我們按照 新增 → 查詢列表 → 修改 → 查詢單筆 → 刪除 的順序來跑一次看看吧！

> 備註：因為這邊還沒說明到 Postman 等測試軟體，所以直接使用 Powershell 呼叫 API 進行示範。已經有慣用軟體的朋友，請用自己方便順手的測試方法去呼叫就好囉。

首先讓我們新增一張卡片（記得 URL 和 Port 要改成你啟動的版本呦）：

```
Invoke-RestMethod https://localhost:44304/card `
 -Method 'POST' `
 -Headers @{ "Content-Type" = "application/json"; } `
 -Body "{`"name`": `"mycard`",`"description`": `"sample card`", `"attack`": 3, `"health`": 4, `"cost`": 2 }"
```

![img](https://i.imgur.com/oQOv7VN.png)

然後讓我們在 SSMS（SQL Server Management Studio）確認一下：

![img](https://i.imgur.com/CuxT7jB.png)

接著讓我們試試查詢：

```
Invoke-RestMethod https://localhost:44304/card | ConvertTo-Json
```

![img](https://i.imgur.com/XmKRKsm.png)

既然查詢成功了，就針對這筆來試試看修改：

```
Invoke-RestMethod https://localhost:44304/card/1 `
 -Method 'PUT' `
 -Headers @{ "Content-Type" = "application/json"; } `
 -Body "{`"name`": `"ourcard`",`"description`": `"sample card`", `"attack`": 4, `"health`": 5, `"cost`": 3}"
```

![img](https://i.imgur.com/Xo5JFyP.png)

一樣在 SSMS 確認一下：

![img](https://i.imgur.com/SxsQdc2.png)

看來我們有成功更新到，讓我們針對這筆來查詢看看：

```
Invoke-RestMethod https://localhost:44304/card/1 | ConvertTo-Json
```

![img](https://i.imgur.com/iieIxee.png)

查詢出來的也的確是變動過的結果了。最後，讓我們把這張卡片刪除，回歸乾淨吧！

```
Invoke-RestMethod https://localhost:44304/card/1 `
 -Method 'DELETE'
```

![img](https://i.imgur.com/WcNVRKA.png)

確認資料表的卡片已經消失：

![img](https://i.imgur.com/a5toUnV.png)

到這邊我們就宣告完工啦！

## 小結

我們把前篇的 Web API 服務利用 Dapper 連接到 SQL Server，並成功完成了基本的 CRUD 功能。

這邊總結一下這篇的一些小要點：

- `DataTable` 等弱型別在使用上會有偵錯困難、必須額外轉型等問題；而直接對映的 `ORM` 又常有過於肥大、自動產生的語法效能可能不佳的問題

- `Dapper` 是一款輕量級的 ORM

  ，它具有以下特色：

  - 簡單：能幫我們將資料表欄位對應到類別欄位，讓我們查詢的資料能簡單直接地轉換成物件，享受強型別的好處
  - 輕便：比起其他 ORM，相當輕便，引入套件後就能快速開始使用，效能也相當不錯
  - 彈性：可以自己撰寫 SQL 語法，自己進行效能的優化與調整，相對 ORM 提升了自由度和彈性，但也要自己對語法負責

- 使用

   

  `Query` 系列的方法來進行資料的查詢

  - 提供了 `QueryFirstOrDefault` 等方法來進一步調整查詢方式（[參閱](https://dotblogs.com.tw/OldNick/2018/01/15/Dapper#Dapper - Query)）
  - 提供了 `Async` 結尾的非同步方法
  - 在 `Query<T>` 中指定對應資料表欄位的類別來讓 Dapper 進行轉換
  - 建立對應資料表欄位的類別時，可以用 Linqpad 來節省時間（[參閱](https://dotblogs.com.tw/mrkt/2016/06/14/190618)）

- 使用

   

  `Execute` 系列的方法來進行語法的執行

  - 同樣提供了 `Async` 結尾的非同步方法

- 使用

   

  `DynamicParameters` 來建立參數集合

  - 藉由參數化查詢迴避 SQL Injection 攻擊
  - 預設的型別轉換可能會有效能問題，在使用 DBString 等難以對應的型別時，可以自訂型別轉換來提升效能（[參閱](https://dotblogs.com.tw/supershowwei/2019/08/12/232213)）
  - 允許傳遞多組參數來執行同一段 SQL 語法，藉此可以做到多筆新增、多筆更新的效果

- 提供了 `BeginTransaction` 來開啟一段 SQL Transaction

- 針對不同的查詢場景、邏輯的複雜程度等等，我們應該評估後再決定使用傳統 ORM 或是 Dapper 或其他方式來操作資料庫（[參閱](https://blog.darkthread.net/blog/linq-or-direct-sql/)）

今天就到這邊告一段落。現在這組 Web API 已經是常見的「連接到資料庫進行基本操作」的範本了，接下來我們會針對這組 Web API 服務進行各式各樣的 ~~擺弄~~ 改造。

那麼，我們下次見～

> 本系列下一篇：[菜雞新訓記 (4): 使用 Swagger 來自動產生簡單好看可測試的 API 文件吧](https://igouist.github.io/post/2021/05/newbie-4-swagger)

## 本系列文章

- [菜雞新訓記 (0): 目錄](https://igouist.github.io/post/2021/04/newbie-0-menu)
- [菜雞新訓記 (1): 使用 Git 來進行版本控制吧](https://igouist.github.io/post/2021/04/newbie-1-hello-git)
- [菜雞新訓記 (2): 認識 Api & 使用 .net Core 來建立簡單的 Web Api 服務吧](https://igouist.github.io/post/2021/05/newbie-2-webapi)
- [菜雞新訓記 (3): 使用 Dapper 來連線到資料庫 CRUD 吧](https://igouist.github.io/post/2021/05/newbie-3-dapper)
- [菜雞新訓記 (4): 使用 Swagger 來自動產生可互動的 API 文件吧](https://igouist.github.io/post/2021/05/newbie-4-swagger)
- [菜雞新訓記 (5): 使用 三層式架構 來切分服務的關注點和職責吧](https://igouist.github.io/post/2021/10/newbie-5-3-layer-architecture)
- [菜雞新訓記 (6): 使用 依賴注入 (Dependency Injection) 來解除強耦合吧](https://igouist.github.io/post/2021/11/newbie-6-dependency-injection)
- [菜雞新訓記 (7): 使用 FluentValidation 來驗證傳入參數吧](https://igouist.github.io/post/2022/03/newbie-7-fluent-validation)

## 其他文章

- [菜雞新訓記 (2): 認識 Api & 使用 .net Core 來建立簡單的 Web Api 服務吧](https://igouist.github.io/post/2021/05/newbie-2-webapi/)
- [菜雞抓蟲: 在 Amazon Linux AMI 安裝 .net Core 時卡在 Requires: openssl-libs](https://igouist.github.io/post/2020/11/bugs-install-dotnet-core-on-amazon-ami-requires-openssl/)
- [EPPlus —— 輕鬆處理 Excel](https://igouist.github.io/post/2020/04/epplus/)
- [Asp.net MVC: Entity Framework 連線資料庫](https://igouist.github.io/post/2019/12/aspnet-connect-db-ef/)
- [菜雞新訓記 (1): 使用 Git 來進行版本控制吧](https://igouist.github.io/post/2021/04/newbie-1-hello-git/)