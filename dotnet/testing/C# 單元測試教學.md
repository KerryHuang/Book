---
kind: original
---

# C#單元測試教學

**前言**

本人在公司負責導入單元測試框架，這是寫給公司內部的教學文件，稍微編修後分享給各位

本篇文章內容包含：

- 單元測試介紹
- 為什麼要寫測試？如何寫測試？
- 單元測試框架 MSTest、NUnit、xUnit
- 可讀性更佳的 Fluent Assertions
- 程式碼覆蓋率 (Code Coverage)
- 免費程式碼覆蓋率分析工具 dotCover
- E2E 測試工具 Selenium

**什麼是測試？**

模擬程式碼的執行行為，來進行正確性檢驗的測試工作。

**單元測試 (Unit testing)**

單元測試指的是最小單元的測試，一個單元就是單個程式、函式、過程等。對於物件導向程式設計，最小單元就是方法，包括基礎類別、抽象類別、或者衍生類別中的方法。

這種測試由開發人員自行撰寫。

**整合測試 (Integration testing)**

整合測試是指將 2 個以上的類別整合一起測試，以確保它們之間的連動是否正常。例如：單元測試分別測試了購物車、轉帳的功能。而整合測試就一口氣將 2 步驟一次跑完，所以整合測試一定是跨類別的。

這種測試通常由專門的測試團隊撰寫，但大部份情況由某模組的負責人寫。

**端對端測試 (End-to-end testing) (E2E testing)**

使用者（一端）對真實系統（另一端）進行測試。從用戶的角度、環境出發，實際操作系統服務，看結果是否符合預期，這部份就屬於人工測試的範圍。

更詳細的介紹請看 [一次搞懂單元測試、整合測試、端對端測試之間的差異](https://blog.miniasp.com/post/2019/02/18/Unit-testing-Integration-testing-e2e-testing)

**為什麼要寫測試？**

1. 確保程式碼品質。每次改動某個功能、模組，時常會忽略、擔心會不會導致別的呼叫端錯誤，只要有單元測試就可以避免這個問題，每次改版完都只要跑一次測試並且都通過，就可以確保改動後的邏輯是沒問題的、不會牽連到其他模組。
2. 省去人工測試麻煩。雖然寫單元測試需要額外花時間，但只要寫完一次就可以不斷重複使用，也省去自己 Debug 跑模擬的過程。
3. 彈性高。可以一上班就測試、中午測試、下班測試、上版時搭配 CI/CD 自動測試，想什麼時候測試都可以。
4. 速度快。單元測試的執行速度應該要非常快，所以跑測試也就不需要太多時間。

**如何建立測試專案**

建議將測試程式碼獨立開一個專案來存放，避免混亂。

在 Visual Studio 中，直接新增專案就有範本了，可以看到包含 .NET Core 與 .NET Framework。其中.NET Core 已經有 MSTest、NUnit、xUnit 的範本。

![img](https://miro.medium.com/v2/resize:fit:1138/1*nOeOJYLm58LJttBZ5BYiyw.png)

**檔名規範**

可自訂。若沒有想法的話可在要測試的 cs 檔後面加上 Tests

**路徑規範**

與原本專案一致即可

*e.g.*

*專案/Service/Service.cs*

*測試專案/Service/ServiceTests.cs*

**MSTest**

[MSTest 官方介紹](https://docs.microsoft.com/zh-tw/dotnet/core/testing/unit-testing-with-mstest)

這是微軟官方自己出的測試框架，但有鑑於我在網路上查資料用這套的人好像不多，因此就不特別介紹語法怎麼寫。

**NUnit**

[NUnit 官方網站](https://nunit.org/)

**寫測試程式**

在測試專案安裝 NuGet 套件 NUnit，於測試專案底下加入一個測試檔案 Tests.cs

![img](https://miro.medium.com/v2/resize:fit:1400/1*nZBlTomdZKbNGjse3sjEqQ.png)

其中 [TestFixture] 指出這個 Class 是測試用的 Class

而 [Test] 則代表此 Method 是測試 Method，如果不寫 [Test] 則測試時就不會跑。

**執行測試**

開啟 Test Explorer ：上方工具列 > 測試 > Test Explorer （或是快捷鍵 Ctrl + E, T）

因為沒有任何程式碼，所以執行測試後通過。

![img](https://miro.medium.com/v2/resize:fit:816/1*u_j9nxkqEHH-ZZEgMMb-CA.png)

**驗證 (Assert)**

Assert 語法就是寫單元測試中的關鍵了，用以判斷實際得到的結果與預期的結果是否相符。若 Assert 是 True，則測試會通過。

![img](https://miro.medium.com/v2/resize:fit:1400/1*9VGuKFMFZDKz-cbmfGL_xQ.png)

**改善程式碼**

**Method命名方式**

這點其實沒有一定，選用適合自己團隊都能接受的方法就好。如果沒有想法，可以參考微軟的 Best Practice

[單元測試最佳做法](https://docs.microsoft.com/zh-tw/dotnet/core/testing/unit-testing-best-practices)

這裡就以這篇文章的原則來介紹。

測試的名稱應該包含三個部分

- 所測試的方法名稱
- 用以測試的案例
- 叫用案例時的預期行為

測試方法名稱_測試案例_預期行為

將 MyTest 更名為 Add_InputTwoInteger_ReturnSum

**以 3A 原則改善程式碼**

Arrange: 初始化

Act: 執行方法、行為、操作並取得結果

Assert: 驗證

這三個步驟會讓測試更明確，同時也應該加入註解中。

![img](https://miro.medium.com/v2/resize:fit:1400/1*atst2Fg0ioU1hwOPtWlQsA.png)

**測試多筆資料**

使測資放在傳入參數中，用 [TestCase] 即可

![img](https://miro.medium.com/v2/resize:fit:1400/1*SrOSIqHsJTOlRVv7GpYOww.png)

![img](https://miro.medium.com/v2/resize:fit:1022/1*ZYCVZMtWpBQ3zCW71uN4EQ.png)

也可以使用 TestCaseSource 的方式，從外部代入測試資料，這樣的話就可以將測試資料額外放一個檔案

*e.g.*

*TestCases\TestCases.cs*

![img](https://miro.medium.com/v2/resize:fit:1400/1*DK9EHEks5rdJvrN9np1nEQ.png)

其中回傳的測試資料型態為 TestCaseData 的集合，這種方式可以輕易代入參數、並且設定測試的名稱。

![img](https://miro.medium.com/v2/resize:fit:820/1*mT9Iveg9EqWi0jHV78-8wg.png)

**SetUp 與 TearDown**

SetUp: 每個測試案例開始前，會執行此方法。通常用來還原測試案例初始化狀態，確保測試案例不互相干擾。

TearDown: 每個測試案例完成後，會執行此方法。通常用來清除測試案例的狀態，確保測試案例不互相干擾。

![img](https://miro.medium.com/v2/resize:fit:1400/1*nXKSePEfTdOZYrDLXtaGaw.png)

執行順序如下：

SetUp

Test1

TearDown

SetUp

Test2

TearDown

**xUnit**

[xUnit 官方網站](https://xunit.net/)

**標記測試方法**

與 NUnit 不同，需標記為 [Fact]

xUnit 沒有標記為測試 Class 的方法，它會自動搜尋測試專案內的測試方法。實際上 NUnit 也可以省略標記測試 Class，至於這樣會不會為了搜尋而拖慢速度？這不清楚。

![img](https://miro.medium.com/v2/resize:fit:1400/1*czBzzcM2wBUku2BM4dXVMg.png)

**測試多筆資料**

使用 [Theory] 與 [InlineData] 達成

![img](https://miro.medium.com/v2/resize:fit:1400/1*SbR7ZITE9Zj6U5iMhuUK_w.png)

若要將測試資料額外分開，則使用 [MemberData] （另外也有 [ClassData] 的方法）

![img](https://miro.medium.com/v2/resize:fit:1400/1*WqpFyDe9E6IHkOJYHgZOYA.png)

TestData 內提供 2 種給予測資的方式 AddData 與 AddData2

目前查不到個別設定測試名稱的方式，只可統一使用 DisplayName 放在 [Theory]

![img](https://miro.medium.com/v2/resize:fit:738/1*iM407AJ8hYz01xCoZwGw3A.png)

**Fact 與 Theory**

為什麼 xUnit 不使用像是 [Test] 這樣的標記？以下節錄自 [官方說明](https://xunit.net/docs/getting-started/netfx/visual-studio#write-first-theory)：

> ***Facts\*** *are tests which are always true. They test invariant conditions.*
>
> ***Theories\*** *are tests which are only true for a particular set of data.*

Fact 只用於測試單一情況，不會有外在影響，因此也不可有傳入參數

Theory 用於測試特定資料，可有傳入參數

**Constructor 與 Dispose**

xUnit 沒有 NUnit 那樣的 SetUp 與 TearDown。

xUnit 認為這兩個方法是糟糕的方法，取而代之的 xUnit 是使用建構、解構的概念去實作。

![img](https://miro.medium.com/v2/resize:fit:1400/1*51HjCT8E2aAJo_zkPw-L5A.png)

**Analyzers**

xUnit 有 Analyzers 套件，可以自動分析測試程式碼的好壞。

去 NuGet 安裝 xunit.analyzers

![img](https://miro.medium.com/v2/resize:fit:1400/1*GpYShMNWU0DZr6LeC3_m7g.png)

**範例 1**

用 Assert.True 與 string.StartsWith 判斷某 string 開頭是否為 “AB”，但 xUnit 有可讀性更佳的 Assert.StartsWith

![img](https://miro.medium.com/v2/resize:fit:1400/1*ka4V2-U894t0U7uFTiRcNQ.png)

![img](https://miro.medium.com/v2/resize:fit:1400/1*wECye9E3QPLAhFZ69YReLQ.png)

**範例 2**

[Fact] 不可傳入參數，需用 [Theory] 或者刪除傳入參數

![img](https://miro.medium.com/v2/resize:fit:1400/1*4EDOf5r8mId-0E9UMbXn6g.png)

![img](https://miro.medium.com/v2/resize:fit:1400/1*-54kFZK6DzCjbeyYG5gY9w.png)

**NUnit 與 xUnit 簡易比較**

其實所有的測試框架都差不多，差異僅有一些特別功能，但感覺這些功能的使用時機也不多。

**功能比較**

太多了，請直接看這篇文章 [MSTest,NUnit 3,xUnit.net 2.0 比較](https://blog.yowko.com/mstest-nunit-xunit/#mstest-nunit-3-xunit-net-2-0-比較)

**語法差異**

1. xUnit 在 Assert 上捨去了 be 動詞 is, are

- xUnit: Assert.Equal() Assert.Null()
- NUnit: Assert.AreEqual() Assert.IsNull()
- Exception 的處理

- xUnit: Assert.Throws<Exception>(() => Add(0, 1));
- NUnit: Throws.TypeOf<Exception>

xUnit 的 Assert.Throws<> 內部是接收一個 delegate，Assert.Throws<Exception>(() => 物件.方法);

代表某物件的某方法應該要會 Throw 指定的 Exception

**SetUp / TearDown 與 Constructor / Dispose**

xUnit 認為 SetUp 與 TearDown 是不好的方法。雖然 SetUp 與 TearDown 可以協助初始化、清除狀態，但是每個測試執行前後都會分別呼叫一次 SetUp 與 TearDown，如果在 SetUp 中不只是 new 出一個物件，甚至還賦值。在特殊案例的測試中又需要視情況賦值，如此一來特殊案例就重複賦值，且每一個測試都會需要一次掌管 3 個 Method：SetUp、自己、TearDown，這違反了 [SOLID](https://zh.wikipedia.org/wiki/SOLID_(面向对象设计)) 中的 [單一職責原則](http://glj8989332.blogspot.com/2018/02/design-pattern-single-responsibility.html)。

範例如下：

![img](https://miro.medium.com/v2/resize:fit:1400/1*a38QPgiRcSl_-In2YjT-Ig.png)

與其這樣寫，不如在每個測試都 new 出一個物件、賦予這個情境下的數值。雖然多了些重複的 code，但至少確保每個測試都是獨立且封閉的。

而 xUnit 則使用建構、解構的方式實作該功能，每個測試都會建立新的 Instance。

也就是 建構式 (初始化) -> 跑該筆測試 -> Dispose (清除狀態)

不過 NUnit 也沒有強制要寫 SetUp 與 TearDown。使用 NUnit 可以考慮避開 SetUp 與 TearDown

**相依性**

xUnit 在每個測試中分別使用新的 Instance，強迫每個測試都獨立、封閉，且相依性為 0，請看以下範例

**NUnit**

![img](https://miro.medium.com/v2/resize:fit:1400/1*JLxDCmrDqsI-a5ogj4XD2A.png)

**xUnit**

![img](https://miro.medium.com/v2/resize:fit:1400/1*N_DjdMhiFRTt-fS7OYvQ2A.png)

![img](https://miro.medium.com/v2/resize:fit:920/1*hudZ_uDVkhdQYiUQgKb-NQ.png)

**擴展性**

xUnit 可自定義 Attributes ，這是其他測試框架都沒有的功能。

可參考 [Creating a custom xUnit theory test DataAttribute to load data from JSON files](https://andrewlock.net/creating-a-custom-xunit-theory-test-dataattribute-to-load-data-from-json-files/)

**文件**

NUnit 較齊全，xUnit 連 Attributes 的說明文件都沒有。

**Fluent Assertions**

[Fluent Assertions 官方網站](https://fluentassertions.com/)

**什麼是 Fluent Assertions**

一種口語化的 Assert，讓程式碼更有可讀性，且跨測試框架，若有多種測試框架並行的情況，仍可用同一種 Assert 寫法。

基本上把測試結果講出來，Code 差不多就是那樣子寫。

**安裝**

去 NuGet 安裝 Fluent Assertions

![img](https://miro.medium.com/v2/resize:fit:1400/1*815RnBINyn2khJsZ9TFtnQ.png)

**範例**

以 xUnit 為例，某 string 需要一次判斷 4 個條件

![img](https://miro.medium.com/v2/resize:fit:1400/1*YW-O30Gk9KBC2T4w1cKp5A.png)

改成 Fluent Assertions

![img](https://miro.medium.com/v2/resize:fit:1400/1*FBFgBG28dp0WjmqwIiupAA.png)

就是這麼簡單。

**判斷物件是否相等**

自定義物件是 Reference type，要比對裡面的值是否一樣需要自訂比較方法或是 Override Equal 方法，但 Fluent Assertions 只要一個方法即可搞定。

![img](https://miro.medium.com/v2/resize:fit:1400/1*2tTM8tRyBqbaKRsM2FXyPA.png)

**程式碼覆蓋率 (Code Coverage)**

**概述**

代表程式碼被測試的比例。

以下要被測試的 Class 只有一個方法 Test，輸入什麼數字就回傳什麼數字。

![img](https://miro.medium.com/v2/resize:fit:1400/1*gKB401Ly2GeFwMu196ddVg.png)

測試方法這樣會傳入 1, 2, 3 ，共 3 個整數

*註：Assert 與 Fluent Assertions 只要擇一來寫就好。這邊多寫是範例。*

![img](https://miro.medium.com/v2/resize:fit:1400/1*JhCrX0w4-VFWLWfNT-H9GQ.png)

這樣子程式碼覆蓋率 (Code Coverage) 就是 75%，因為 5 個 case 中只測試了 3 個 case

**分析工具**

**Visual Studio Enterprise (企業版)**

Visual Studio Enterprise 內建就有程式碼覆蓋率的工具，且有 UI，讓操作與閱讀都十分方便。但只有企業版有這個功能。

教學請看官方文件 [使用程式碼涵蓋範圍來決定所測試的程式碼數量](https://docs.microsoft.com/zh-tw/visualstudio/test/using-code-coverage-to-determine-how-much-code-is-being-tested?view=vs-2019)

**dotCover**

JetBrains 出品的工具，也是有 UI 的。但是是付費工具，有 30 天免費試用，或者該公司產品的 ReSharper 也有附贈。

那免費仔該怎麼辦呢？幸好他們有開放 Command line tools 免費使用，太棒啦

去 [官方網站](https://www.jetbrains.com/dotcover/download/#section=commandline) 下載 dotCover Command Line Tools

**.NET Core**

打開 CMD 視窗 > cd 到 dotCover 的目錄 > 輸入以下指令 （MSTest、NUnit、xUnit 都是同一個指令）

> *dotCover.exe dotnet --output=AppCoverageReport.html --reportType=HTML --test "C:\MyProject\MainTests.csproj"*

**參數說明**

output: 輸出覆蓋率報告的位置、名字。若不指定輸出路徑，則輸出在 dotCover 目錄底下

> *--output=C:\Users\Hao\Report\AppCoverageReport.html 指定路徑*

reportType: 輸出覆蓋率報告的類型，這邊用 HTML

test: 要分析覆蓋率的測試專案，需指到 csproj 檔

![img](https://miro.medium.com/v2/resize:fit:1400/1*cdDeZk0mFq7M39yJOqdQ7A.png)

如此一來就會在 dotCover 的目錄底下輸出一個 AppCoverageReport.html 檔，把它打開就可以看到覆蓋率的分析了。其中綠色代表有被測試到、紅色代表沒有被測試到。

分析包含了：該檔案的覆蓋率、檔案內的方法的覆蓋率等等……

![img](https://miro.medium.com/v2/resize:fit:1400/1*Fu2OHkVUIaJ7SWn4HWoGWQ.png)

**.NET Framework**

打開 CMD 視窗 -> cd 到 dotCover 的目錄 -> 輸入以下指令 （根據不同測試框架，參數值會不同）

> *dotcover cover /TargetExecutable="TestRunner\TestRunner.exe" /TargetArguments="C:\MyProject\bin\Debug\MyTest.dll" /Output="AppCoverageReport.html" /ReportType="HTML"*

**參數說明**

TargetExecutable: 要執行的測試框架的 Runner

TargetArguments: 要被分析覆蓋率的測試專案，編譯後產出的 dll

Output: 輸出覆蓋率報告的位置、名字。若不指定輸出路徑，則輸出在 dotCover 目錄底下

ReportType: 輸出覆蓋率報告的類型，這邊用 HTML

**MSTest**

若顯示錯誤訊息，請嘗試使用「以系統管理員身分執行」來執行 CMD

> *dotcover cover /TargetExecutable="C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\Common7\IDE\Extensions\TestPlatform\vstest.console.exe" /TargetArguments="C:\MyProject\bin\Debug\MyTest.dll" /Output="AppCoverageReport.html" /ReportType="HTML"*

如果要用 vstest.console 去執行測試，指令如下

> *vstest.console.exe myTestProject.dll*

**NUnit**

先去 NuGet 安裝 NUnit.ConsoleRunner，然後 TargetExecutable 參數指定該套件底下的 nunit3-console.exe

![img](https://miro.medium.com/v2/resize:fit:1400/1*B3K1CY58HtdcXReG_OWH-w.png)

> dotcover cover /TargetExecutable="~\nunit.consolerunner\3.11.1\tools\nunit3-console.exe" /TargetArguments="C:\MyProject\bin\Debug\MyTest.dll" /Output="AppCoverageReport.html" /ReportType="HTML"

**xUnit**

先去 NuGet 安裝 xunit.runner.console，然後 TargetExecutable 參數指定該套件底下的 xunit.console.exe

目錄底下有很多資料夾細分對應的 .NET 版本

![img](https://miro.medium.com/v2/resize:fit:1400/1*jnpSUaXdRvJvUd4I0frGLQ.png)

> dotcover cover /TargetExecutable="~\xunit.runner.console\2.4.1\tools\net472\xunit.console.exe" /TargetArguments="C:\MyProject\bin\Debug\MyTest.dll" /Output="AppCoverageReport.html" /ReportType="HTML"

**其他**

其他還有 [OpenCover](https://github.com/OpenCover/opencover)、[Coverlet](https://github.com/tonerdo/coverlet) 等，但似乎都只針對 .NET Core 使用。且這兩個工具產出的覆蓋率報告是 XML 格式，需透過 [ReportGenerator](https://github.com/danielpalme/ReportGenerator) 來將報告轉為 HTML 格式。

**Selenium**

[Selenium 官方網站](https://www.selenium.dev/)

**什麼是 Selenium**

Selenium 是 E2E 測試工具，可執行開啟瀏覽器、操作功能等行為，可模擬使用者操作系統的真實情況。

**安裝**

去 NuGet 安裝 Selenium.WebDriver

![img](https://miro.medium.com/v2/resize:fit:1400/1*SRE8m1qzozBsXTd1zLnXmw.png)

若要測試某瀏覽器，需要額外安裝該瀏覽器的 WebDriver，以 Chrome 為例

![img](https://miro.medium.com/v2/resize:fit:1400/1*JPOMHpUIFkL9-hfrttY5SA.png)

**範例**

![img](https://miro.medium.com/v2/resize:fit:1400/1*JAWOXJWdefXTYFJwMOqjzQ.png)

這是模擬使用 Google 搜尋引擎搜尋關鍵字 "Google" 是否成功

打開瀏覽器，並且測試結束時關閉

```
using (IWebDriver driver = new ChromeDriver())
```

設定一個監聽事件

```
WebDriverWait wait = new WebDriverWait(driver, TimeSpan.FromSeconds(10));
```

前往 Google 搜尋引擎網址

```
driver.Navigate().GoToUrl("https://www.google.com/");
```

根據 Name 找到填入關鍵字的欄位，並且使用 SendKeys() 填入關鍵字 "Google"

最後透過 Name 找到搜尋按鈕呼叫 Click() 按下。

```
driver.FindElement(By.Name("q")).SendKeys("Google");
driver.FindElement(By.Name("btnK")).Click();         
```

搜尋成功後，右方會出現關於 Google 的介紹，我以介紹上方的圖片（紅框處）有出現來當作搜尋已經完成。

![img](https://miro.medium.com/v2/resize:fit:1002/1*RK1GpGUJ-h-GCHTHN4UWDA.png)

而這張圖片資訊如下，找到能辨識它的資訊即可（紅框處）

![img](https://miro.medium.com/v2/resize:fit:1400/1*11bRjnSulnIbpJnCZ0qxUQ.png)

```
wait.Until(ExpectedConditions.ElementExists(By.Id("wp_thbn_13")));
```

圖片出現後視為搜尋已完畢，我透過 Fluent Assertions 驗證網頁標題

```
driver.Title.Should().Be("Google - Google 搜尋");
```

跑這個測試 Selenium 會打開 Chrome 瀏覽器來實際做這些操作並且測試。

我以這一套流程以及 UI 的出現，來判定搜尋功能是正常可以運作的。

**如何不實際開啟瀏覽器測試？**

我們跑測試時剛開始也許需要實際看瀏覽器的操作來確保自己的程式碼正確。當確認完畢後，我們不希望每次測試都要打開瀏覽器，耗時又佔記憶體。

Chrome 有個 headless 模式，只要將這個參數傳入建構子，跑測試時就不會真的開啟瀏覽器測試。

```
ChromeOptions chromeOptions = new ChromeOptions();
chromeOptions.AddArguments("headless");
using (IWebDriver driver = new ChromeDriver(chromeOptions))
{
}
```

**Selenium IDE**

Selenium IDE 可以直接錄製你對網頁的操作、甚至轉成程式碼，在不懂程式的情況下仍可完成人工測試腳本。

以 Chrome 為例：

去擴充功能搜尋 Selenium IDE

![img](https://miro.medium.com/v2/resize:fit:1400/1*Z7P9g5CDS8taTjNNYLk1xw.png)

打開 Selenium IDE

![img](https://miro.medium.com/v2/resize:fit:1300/1*X46ZCqcQF2o93vysxbsSkA.png)

點選 Record a new test in a new project

輸入測試專案名稱，這可以協助你分類測試腳本

![img](https://miro.medium.com/v2/resize:fit:1300/1*lpsoJEVmvph_3BFWwCPPHA.png)

輸入想要錄製腳本的網址，按下 START RECORDING

![img](https://miro.medium.com/v2/resize:fit:1300/1*DtO3goNtlzeqWR3u_JDcGA.png)

Selenium IDE 會打開你輸入的網址，打開後就已經在錄製了，可以執行自己想測試的操作。

搜尋完畢後，我選擇依照網頁的標題來判斷是否搜尋成功，在頁面 右鍵 > Selenium IDE > Assert > Title

![img](https://miro.medium.com/v2/resize:fit:1400/1*3-vhHa02iCa0pB0ZFYj5_w.png)

點開 Selenium IDE，按下停止錄製就完成了。

![img](https://miro.medium.com/v2/resize:fit:1400/1*VMTYj-hNcrSLtVljQ66Iyg.png)

左邊就是你所有的測試，右邊是該測試執行的動作，最後一個動作是 Assert Title 是否為 “Google — Google 搜尋”

執行測試後綠色代表成功。

![img](https://miro.medium.com/v2/resize:fit:1400/1*xTcTiL-0Ee79MUGU-j_jBg.png)

**如何匯出成程式碼**

滑鼠移到測試名稱上，最右邊應該會顯示 3 個點

![img](https://miro.medium.com/v2/resize:fit:362/1*xi1sFYIkdOi4O7hDen2mUg.png)

按下 Export

![img](https://miro.medium.com/v2/resize:fit:360/1*igdn4ilAZmQR_jOFAXx41w.png)

就可以將剛剛錄製的腳本轉成程式碼

![img](https://miro.medium.com/v2/resize:fit:1400/1*e0r77JAYnnvTI_Iq_tPBDw.png)

**參考資料**

[一次搞懂單元測試、整合測試、端對端測試之間的差異](https://blog.miniasp.com/post/2019/02/18/Unit-testing-Integration-testing-e2e-testing)

[NUnit — 測試案例 TestCaseSourceAttribute](https://blog.johnwu.cc/article/nunit-test-case-source-attribute.html)

[.NET Core 和 .NET Standard 的單元測試最佳做法](https://docs.microsoft.com/zh-tw/dotnet/core/testing/unit-testing-best-practices)

[Creating parameterised tests in xUnit with [InlineData\], [ClassData], and [MemberData]](https://andrewlock.net/creating-parameterised-tests-in-xunit-with-inlinedata-classdata-and-memberdata/)

[xUnit Theory: Working With InlineData, MemberData, ClassData](https://hamidmosalla.com/2017/02/25/xunit-theory-working-with-inlinedata-memberdata-classdata/)

[MSTest,NUnit 3,xUnit.net 2.0 比較](https://blog.yowko.com/mstest-nunit-xunit/#mstest-nunit-3-xunit-net-2-0-比較)

[Comparing xUnit.net to other frameworks](https://xunit.net/docs/comparisons)

[Why you should not use SetUp and TearDown in NUnit](https://jamesnewkirk.typepad.com/posts/2007/09/why-you-should-.html)

[使用程式碼涵蓋範圍來決定所測試的程式碼數量](https://docs.microsoft.com/zh-tw/visualstudio/test/using-code-coverage-to-determine-how-much-code-is-being-tested?view=vs-2019)

[Coverage Analysis from the Command Line](https://www.jetbrains.com/help/dotcover/Running_Coverage_Analysis_from_the_Command_LIne.html#)

[VSTest.Console.exe 命令列選項](https://docs.microsoft.com/zh-tw/visualstudio/test/vstest-console-options?view=vs-2019)

[Why Should You Use xUnit? A Unit Testing Framework For .Net](https://www.clariontech.com/blog/why-should-you-use-xunit-a-unit-testing-framework-for-.net)

[Creating a custom xUnit theory test DataAttribute to load data from JSON files](https://andrewlock.net/creating-a-custom-xunit-theory-test-dataattribute-to-load-data-from-json-files/)