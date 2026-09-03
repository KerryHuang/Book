---
kind: original
---

# Azure App Configuration 使用教學

Azure App Configuration 是一個服務，用來集中管理應用程式的設定，尤其是在雲端、多環境或微服務架構下非常實用。它能幫助你有效地分離設定與程式碼，並且支援動態更新設定。以下是一個詳細的 Azure App Configuration 使用教學。

### Azure App Configuration 的基本步驟

#### 1. **建立 Azure App Configuration 資源**

首先，您需要在 Azure 內建立一個 App Configuration 資源。

1. 登入 [Azure 入口網站](https://portal.azure.com/)。
2. 點擊「**Create a resource**」。
3. 搜索「**App Configuration**」，然後點擊「**Create**」。
4. 在建立頁面中，選擇訂閱、資源群組並命名資源（例如：`my-app-config`）。
5. 點擊「**Review + Create**」，檢查設定無誤後，點擊「**Create**」來完成建立。

#### 2. **新增設定到 Azure App Configuration**

一旦 App Configuration 資源建立完成，您可以新增應用程式的設定。

1. 在 Azure 入口網站中進入您建立的 App Configuration 資源。
2. 點擊「**Configuration Explorer**」來進行設定管理。
3. 點擊「**+ Create**」來新增一個設定。
   - **Key**: 設定的名稱（例如：`AppSettings:MySetting`）。
   - **Value**: 設定的值（例如：`Hello, Azure!`）。
   - **Label**: 標籤，用於區分不同環境或版本（可以留空或設定為環境標籤如 `Production` 或 `Development`）。
4. 新增完畢後，點擊「**Apply**」來保存設定。

#### 3. **在 .NET 應用中使用 Azure App Configuration**

接下來，您可以將 Azure App Configuration 整合到 .NET 應用中。首先，需要安裝必要的 NuGet 套件。

##### 安裝 NuGet 套件

使用以下指令安裝 `Microsoft.Azure.AppConfiguration.AspNetCore` NuGet 套件：

```bash
dotnet add package Microsoft.Azure.AppConfiguration.AspNetCore
```

#### 4. **設定 .NET 應用以連接 Azure App Configuration**

在您的 `.NET` 應用程式（例如 ASP.NET Core）中，您需要在 `Program.cs` 或 `Startup.cs` 檔案中進行設定，讓應用程式從 Azure App Configuration 中載入設定。

##### 在 `Program.cs` 中設定 Azure App Configuration

打開 `Program.cs` 檔案，並將以下程式碼新增到設定部分：

```csharp
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;

var builder = WebApplication.CreateBuilder(args);

// 加入 Azure App Configuration 支援
builder.Configuration.AddAzureAppConfiguration(options =>
{
    options.Connect("<Your-App-Configuration-Connection-String>")
           .Select(KeyFilter.Any, LabelFilter.Null);
});

// 設置服務和應用
builder.Services.AddRazorPages();
var app = builder.Build();

app.UseHttpsRedirection();
app.UseStaticFiles();
app.UseRouting();
app.UseAuthorization();
app.MapRazorPages();
app.Run();
```

要取得 Azure App Configuration 的連接字串 (`Your-App-Configuration-Connection-String`)，您需要進入 Azure 入口網站並找到您建立的 Azure App Configuration 資源。以下是具體步驟：

#### 5. **設定連接字串**

從 Azure 入口網站中取得 App Configuration 的連接字串，並將其應用到程式碼中。

1. 在 Azure 入口網站中進入您建立的 App Configuration 資源。
2. 點擊「**Access keys**」來查看連接字串。
3. 將連接字串複製，然後在 `Program.cs` 檔案中替換 `<Your-App-Configuration-Connection-String>` 為實際的連接字串。

#### 6. **使用 Azure App Configuration 的設定**

您可以在應用程式的程式碼中直接存取設定。假設您在 Azure App Configuration 中新增了一個 `AppSettings:MySetting` 鍵，您可以通過以下方式讀取它：

```csharp
var mySetting = builder.Configuration["AppSettings:MySetting"];
Console.WriteLine($"My setting value: {mySetting}");
```

這將從 Azure App Configuration 中讀取該設定並將其顯示在控制台中。

#### 7. **動態設定刷新**

Azure App Configuration 支援動態設定更新，您可以啟用即時設定刷新。這可以確保應用程式在設定發生變更時自動更新，而無需重新部署應用程式。

##### 新增動態刷新支援

首先，在 `Program.cs` 中更新設定程式碼，加入動態刷新支援：

```csharp
builder.Services.AddAzureAppConfiguration();
builder.Configuration.AddAzureAppConfiguration(options =>
{
    options.Connect("<Your-App-Configuration-Connection-String>")
           .Select(KeyFilter.Any, LabelFilter.Null)
           .ConfigureRefresh(refresh =>
           {
               refresh.Register("AppSettings:MySetting", refreshAll: true)
                      .SetCacheExpiration(TimeSpan.FromSeconds(30));
           });
});

// 使用 Azure App Configuration 中間件
app.UseAzureAppConfiguration();
```

這段程式碼會每 30 秒自動檢查 `AppSettings:MySetting` 是否有更新，並自動應用更新到應用程式中。

#### 8. **不同環境的設定**

您可以使用 **Label** 來區分不同環境的設定。例如，您可以為「Production」和「Development」設定新增不同的標籤，並在應用程式中根據當前環境選擇載入正確的設定。

在 `Program.cs` 中可以根據環境來載入帶有相應標籤的設定：

```csharp
var environment = builder.Environment.EnvironmentName;

builder.Configuration.AddAzureAppConfiguration(options =>
{
    options.Connect("<Your-App-Configuration-Connection-String>")
           .Select(KeyFilter.Any, environment);
});
```

這樣，應用程式會自動載入相應環境標籤的設定。

### 總結

Azure App Configuration 提供了一個靈活且集中化的方式來管理應用程式設定，特別是在分散式系統或多環境部署中非常有用。它不僅簡化了設定管理，還支援動態設定更新，從而提高了應用程式的可維護性和靈活性。使用以上步驟，您可以輕鬆地將 Azure App Configuration 整合到您的 .NET 應用中，並在多個環境中管理您的應用設定。



---

## 如何取得"<Your-App-Configuration-Connection-String>"

### 1. 登入 Azure 入口網站

前往 [Azure 入口網站](https://portal.azure.com)，並使用您的帳戶進行登入。

### 2. 尋找 Azure App Configuration 資源

1. 在 Azure 入口網站中，點擊左側的「**所有資源**」（All Resources）或在搜索欄中輸入 `App Configuration`，然後選擇您建立的 App Configuration 資源。
2. 進入資源頁面。

### 3. 取得連接字串

1. 在 App Configuration 資源的概覽頁面中，找到左側菜單中的「**Access keys**」（存取金鑰）。
2. 點擊「**Access keys**」，您會看到多個連接字串，包括「**Primary connection string**」（主連接字串）和「**Secondary connection string**」（次連接字串）。
3. 複製「**Primary connection string**」或「**Secondary connection string**」——它們兩個都可以使用。

這就是您應該用在應用程式中的 `Your-App-Configuration-Connection-String`。

### 4. 使用連接字串

將這個連接字串貼上到您的應用程式中，比如：

```csharp
builder.Configuration.AddAzureAppConfiguration(options =>
{
    options.Connect("<Your-App-Configuration-Connection-String>");
});
```

或者將它作為環境變數、密鑰管理等方式來安全儲存。