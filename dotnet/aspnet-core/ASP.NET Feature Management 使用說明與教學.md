---
kind: original
---

# ASP.NET Feature Management 使用說明與教學

`.NET` 的 `AddFeatureManagement` 是由 Microsoft 提供的功能管理 (Feature Management) 庫，用於啟用或停用應用程式中的功能。這個庫支援動態開啟或關閉功能，尤其在微服務架構或 DevOps 流程中非常實用。通過 `AddFeatureManagement`，您可以集中管理功能標誌 (Feature Flags) 並在應用程式中輕鬆地檢查和控制功能的啟用狀態。

### 步驟 1：安裝 Feature Management 套件

首先，在您的 .NET 應用程式中安裝 `Microsoft.FeatureManagement.AspNetCore` 套件：

```bash
dotnet add package Microsoft.FeatureManagement.AspNetCore
```

### 步驟 2：在 `Program.cs` 中新增 Feature Management

要在應用中啟用 Feature Management，請在 `Program.cs` 中進行設定：

```csharp
using Microsoft.FeatureManagement;

var builder = WebApplication.CreateBuilder(args);

// 設置 Feature Management
builder.Services.AddFeatureManagement();

builder.Services.AddControllersWithViews();
var app = builder.Build();

app.UseHttpsRedirection();
app.UseStaticFiles();
app.UseRouting();
app.UseAuthorization();
app.MapControllers();
app.Run();
```

在上面的程式碼中，`AddFeatureManagement()` 方法會將 Feature Management 新增到服務容器，並允許應用在執行時檢查功能標誌的狀態。

### 步驟 3：定義功能標誌 (Feature Flags)

在 `appsettings.json` 中定義功能標誌。您可以將標誌設定為 `true` 或 `false`，以控制功能的啟用狀態。

#### appsettings.json 範例

```json
{
  "FeatureManagement": {
    "NewFeature": true,
    "ExperimentalFeature": false
  }
}
```

這段設定會定義兩個功能標誌 `NewFeature` 和 `ExperimentalFeature`，其中 `NewFeature` 是啟用狀態，`ExperimentalFeature` 是停用狀態。

### 步驟 4：在程式碼中使用功能標誌

一旦定義了功能標誌，您就可以在程式碼中檢查這些標誌的狀態，以控制功能的啟用或停用。

#### 4.1. 在控制器中使用功能標誌

在控制器或其他服務中，注入 `IFeatureManager` 來檢查功能標誌的狀態：

```csharp
using Microsoft.AspNetCore.Mvc;
using Microsoft.FeatureManagement;

public class HomeController : Controller
{
    private readonly IFeatureManager _featureManager;

    public HomeController(IFeatureManager featureManager)
    {
        _featureManager = featureManager;
    }

    public async Task<IActionResult> Index()
    {
        if (await _featureManager.IsEnabledAsync("NewFeature"))
        {
            ViewData["Message"] = "New Feature is enabled!";
        }
        else
        {
            ViewData["Message"] = "New Feature is disabled.";
        }

        return View();
    }
}
```

在這段程式碼中，`IsEnabledAsync("NewFeature")` 會檢查 `NewFeature` 是否啟用，並根據結果決定顯示不同的訊息。

#### 4.2. 使用特性 (Attribute) 控制功能存取

您還可以使用 `FeatureGate` 特性來保護控制器或操作方法，當功能標誌被停用時，請求將回傳 `404 Not Found`：

```csharp
using Microsoft.AspNetCore.Mvc;
using Microsoft.FeatureManagement.Mvc;

[FeatureGate("NewFeature")]
public class NewFeatureController : Controller
{
    public IActionResult Index()
    {
        return View();
    }
}
```

這段程式碼使用 `FeatureGate("NewFeature")`，當 `NewFeature` 標誌被停用時，所有請求都會自動被阻止並回傳 `404`。

### 步驟 5：使用條件 Feature Filters

`Feature Filters` 提供了基於條件啟用或停用功能標誌的能力，例如基於使用者角色、百分比或自訂條件。

#### 在 `appsettings.json` 中設定條件過濾器

下面的範例展示了如何設定基於百分比的 Feature Filter：

```json
{
  "FeatureManagement": {
    "BetaFeature": {
      "EnabledFor": [
        {
          "Name": "Percentage",
          "Parameters": {
            "Value": 50
          }
        }
      ]
    }
  }
}
```

在這裡，`BetaFeature` 標誌會以 50% 的概率被啟用。這意味著每次請求有一半的機率會啟用此功能。

#### 使用條件 Feature Filters

要使用 Feature Filter，您需要在 `Program.cs` 中新增相應的過濾器支援：

```csharp
builder.Services.AddFeatureManagement()
    .AddFeatureFilter<Microsoft.FeatureManagement.FeatureFilters.PercentageFilter>();
```

### 步驟 6：自訂 Feature Filter

如果您需要基於自訂邏輯來控制功能標誌，則可以建立自訂 Feature Filter。

#### 建立自訂 Feature Filter

以下是一個基於使用者角色的自訂 Feature Filter：

```csharp
using Microsoft.FeatureManagement;
using System.Threading.Tasks;

public class RoleFeatureFilter : IFeatureFilter
{
    public Task<bool> EvaluateAsync(FeatureFilterEvaluationContext context)
    {
        // 自定義邏輯判斷，這裡可以基於角色或其他條件
        bool isAdmin = false; // 自定義判斷邏輯...
        return Task.FromResult(isAdmin);
    }
}
```

#### 註冊自訂 Feature Filter

在 `Program.cs` 中註冊自訂過濾器：

```csharp
builder.Services.AddFeatureManagement()
    .AddFeatureFilter<RoleFeatureFilter>();
```

### 使用總結

1. **定義功能標誌**：在 `appsettings.json` 中定義功能標誌。
2. **設定 Feature Management**：在 `Program.cs` 中使用 `AddFeatureManagement` 新增支援。
3. **檢查功能標誌**：在程式碼中使用 `IFeatureManager` 或 `FeatureGate` 特性來檢查和控制功能的啟用。
4. **使用 Feature Filters**：基於條件設定 Feature Filters（如百分比或自訂條件），控制功能的動態啟用。

這樣，您就可以靈活地管理應用中的功能標誌，並根據條件動態控制功能啟用。


---

##  ASP.NET Core Web API 應用中實作

以下是使用 `AddFeatureManagement` 在 ASP.NET Core Web API 應用中實作功能標誌 (Feature Flags) 的範例，包括基本功能標誌的設定、檢查和使用條件 Feature Filter。

### 步驟 1：安裝 Feature Management 套件

首先，在您的 Web API 專案中安裝 `Microsoft.FeatureManagement.AspNetCore` 套件：

```bash
dotnet add package Microsoft.FeatureManagement.AspNetCore
```

### 步驟 2：在 `Program.cs` 中設定 Feature Management

要在 Web API 中啟用 Feature Management，請在 `Program.cs` 中設定 `AddFeatureManagement()`。

```csharp
using Microsoft.FeatureManagement;

var builder = WebApplication.CreateBuilder(args);

// 設定 Feature Management
builder.Services.AddFeatureManagement();

// 設定控制器
builder.Services.AddControllers();

var app = builder.Build();

app.UseHttpsRedirection();
app.UseAuthorization();
app.MapControllers();
app.Run();
```

在上面的程式碼中，`AddFeatureManagement()` 方法會將 Feature Management 新增到服務容器中，使應用可以在執行時檢查功能標誌的狀態。

### 步驟 3：定義功能標誌

在 `appsettings.json` 中定義功能標誌，設定啟用或停用的狀態。

#### appsettings.json 範例

```json
{
  "FeatureManagement": {
    "NewFeature": true,
    "ExperimentalFeature": false
  }
}
```

在這裡定義了兩個功能標誌 `NewFeature` 和 `ExperimentalFeature`，分別設定為 `true` 和 `false`。

### 步驟 4：在 API 控制器中使用功能標誌

接下來，我們在控制器中使用 `IFeatureManager` 檢查功能標誌的狀態，並根據標誌狀態執行不同的邏輯。

#### 使用 `IFeatureManager` 檢查功能標誌

建立一個控制器，並注入 `IFeatureManager` 來控制功能標誌：

```csharp
using Microsoft.AspNetCore.Mvc;
using Microsoft.FeatureManagement;

[ApiController]
[Route("api/[controller]")]
public class FeatureController : ControllerBase
{
    private readonly IFeatureManager _featureManager;

    public FeatureController(IFeatureManager featureManager)
    {
        _featureManager = featureManager;
    }

    [HttpGet("check-new-feature")]
    public async Task<IActionResult> CheckNewFeature()
    {
        if (await _featureManager.IsEnabledAsync("NewFeature"))
        {
            return Ok("New Feature is enabled!");
        }
        else
        {
            return Ok("New Feature is disabled.");
        }
    }
}
```

這段程式碼會根據 `NewFeature` 功能標誌的狀態回傳不同的回應。

### 步驟 5：使用 `FeatureGate` 屬性控制 API 端點存取

您可以使用 `FeatureGate` 屬性來限制 API 端點的存取。如果功能標誌被停用，該端點會回傳 `404 Not Found`。

```csharp
[ApiController]
[Route("api/[controller]")]
public class FeatureController : ControllerBase
{
    private readonly IFeatureManager _featureManager;

    public FeatureController(IFeatureManager featureManager)
    {
        _featureManager = featureManager;
    }

    // 使用 FeatureGate 限制端點訪問
    [FeatureGate("NewFeature")]
    [HttpGet("new-feature-endpoint")]
    public IActionResult NewFeatureEndpoint()
    {
        return Ok("New Feature Endpoint is accessible!");
    }
}
```

在這裡，`FeatureGate("NewFeature")` 屬性將 `NewFeature` 端點限制在 `NewFeature` 標誌啟用時才能存取。當 `NewFeature` 標誌被停用時，這個端點將回傳 `404`。

### 步驟 6：新增條件 Feature Filters

`Feature Filters` 允許您基於條件控制功能的啟用。以下是基於百分比的 Feature Filter 設定範例。

#### appsettings.json 設定

可以在 `appsettings.json` 中設定基於百分比的 Feature Filter：

```json
{
  "FeatureManagement": {
    "BetaFeature": {
      "EnabledFor": [
        {
          "Name": "Percentage",
          "Parameters": {
            "Value": 50
          }
        }
      ]
    }
  }
}
```

在這裡，`BetaFeature` 標誌會以 50% 的概率被啟用，這意味著每次請求有一半的機率會啟用該功能。

#### 在 `Program.cs` 中新增 Feature Filter 支援

您需要在 `Program.cs` 中將 `PercentageFilter` 新增到 Feature Management 中：

```csharp
builder.Services.AddFeatureManagement()
    .AddFeatureFilter<Microsoft.FeatureManagement.FeatureFilters.PercentageFilter>();
```

### 步驟 7：自訂 Feature Filter（可選）

如果您需要根據自訂邏輯控制功能標誌，可以建立自訂的 Feature Filter，例如基於使用者角色。

#### 自訂 Feature Filter 類別

建立一個基於角色的自訂 Feature Filter：

```csharp
using Microsoft.FeatureManagement;
using System.Threading.Tasks;

public class RoleFeatureFilter : IFeatureFilter
{
    public Task<bool> EvaluateAsync(FeatureFilterEvaluationContext context)
    {
        // 自定義邏輯判斷，例如根據角色控制啟用
        bool isAdmin = false; // 自定義邏輯
        return Task.FromResult(isAdmin);
    }
}
```

#### 註冊自訂 Feature Filter

在 `Program.cs` 中註冊自訂 Feature Filter：

```csharp
builder.Services.AddFeatureManagement()
    .AddFeatureFilter<RoleFeatureFilter>();
```

### 使用總結

1. **設定功能標誌**：在 `appsettings.json` 中定義功能標誌。
2. **設定 Feature Management**：在 `Program.cs` 中新增 `AddFeatureManagement`。
3. **檢查功能標誌狀態**：在 Web API 控制器中使用 `IFeatureManager` 或 `FeatureGate` 屬性來檢查並控制功能啟用。
4. **使用 Feature Filters**：通過 `PercentageFilter` 或自訂的 `RoleFeatureFilter` 來基於條件控制功能標誌的啟用。

這樣，您可以在 ASP.NET Core Web API 中靈活地管理和使用功能標誌，並根據條件動態控制 API 端點的啟用。

---

## 在 ASP.NET Core Web API 中結合 **Azure App Configuration** 的 Feature Management

在 ASP.NET Core Web API 中結合 **Azure App Configuration** 的 Feature Management，可以集中管理功能標誌並實作應用內的動態功能控制。Azure App Configuration 讓您可以直接管理功能標誌，而不需要修改 `appsettings.json`。以下是一個整合 Azure Feature Management 和 .NET Web API 的完整範例。

### 步驟 1：在 Azure 上設定 App Configuration 和 Feature Flags

1. **建立 Azure App Configuration 資源**
   - 登入到 [Azure 入口網站](https://portal.azure.com)。
   - 搜索 `App Configuration`，點擊「**Create**」來建立資源。
   - 填寫必要資訊，並建立 App Configuration 資源。
2. **設定 Feature Flags**
   - 在 App Configuration 資源中，選擇「**Feature Manager**」。
   - 點擊「**+ Add**」，為每個功能標誌新增標識（如 `NewFeature`）。
   - 可以設定每個功能標誌的啟用狀態以及其他條件（如標籤、百分比等）。
3. **取得連接字串**
   - 在 Azure App Configuration 資源中，選擇「**Access keys**」。
   - 複製連接字串，稍後需要在應用程式中使用它。

### 步驟 2：在 Web API 中安裝必要的 NuGet 套件

您需要安裝 `Microsoft.Azure.AppConfiguration.AspNetCore` 和 `Microsoft.FeatureManagement.AspNetCore` 兩個套件來實作 Azure App Configuration 與 Feature Management。

```bash
dotnet add package Microsoft.Azure.AppConfiguration.AspNetCore
dotnet add package Microsoft.FeatureManagement.AspNetCore
```

### 步驟 3：設定 `Program.cs` 使用 Azure App Configuration 和 Feature Management

在 `Program.cs` 中，新增 Azure App Configuration 連接字串並設定 Feature Management。確保 Feature Management 可以動態刷新。

```csharp
using Microsoft.FeatureManagement;
using Microsoft.Extensions.Configuration.AzureAppConfiguration;

var builder = WebApplication.CreateBuilder(args);

// 從環境變數或密碼管理器獲取 Azure App Configuration 連接字串
string appConfigConnectionString = builder.Configuration["AppConfig:ConnectionString"];

// 添加 Azure App Configuration 並啟用動態設定刷新
builder.Configuration.AddAzureAppConfiguration(options =>
{
    options.Connect(appConfigConnectionString)
           .UseFeatureFlags(featureOptions =>
           {
               featureOptions.CacheExpirationInterval = TimeSpan.FromSeconds(30); // 每 30 秒刷新一次功能標誌狀態
           });
});

// 設定 Feature Management
builder.Services.AddFeatureManagement();

// 添加控制器
builder.Services.AddControllers();

var app = builder.Build();

app.UseHttpsRedirection();
app.UseAuthorization();
app.MapControllers();

app.Run();
```

### 步驟 4：在 Web API 控制器中使用功能標誌

您可以通過 `IFeatureManager` 來檢查功能標誌的狀態，並根據不同狀態控制 API 的回應。

#### 在 API 控制器中檢查功能標誌

```csharp
using Microsoft.AspNetCore.Mvc;
using Microsoft.FeatureManagement;

[ApiController]
[Route("api/[controller]")]
public class FeatureController : ControllerBase
{
    private readonly IFeatureManager _featureManager;

    public FeatureController(IFeatureManager featureManager)
    {
        _featureManager = featureManager;
    }

    [HttpGet("check-new-feature")]
    public async Task<IActionResult> CheckNewFeature()
    {
        if (await _featureManager.IsEnabledAsync("NewFeature"))
        {
            return Ok("New Feature is enabled!");
        }
        else
        {
            return Ok("New Feature is disabled.");
        }
    }
}
```

在這段程式碼中，`IsEnabledAsync("NewFeature")` 會從 Azure App Configuration 檢查 `NewFeature` 的狀態。根據狀態，API 回傳不同的回應。

#### 使用 `FeatureGate` 屬性控制 API 端點存取

可以使用 `FeatureGate` 屬性直接控制端點的存取。當功能標誌被停用時，端點將回傳 `404 Not Found`。

```csharp
[ApiController]
[Route("api/[controller]")]
public class FeatureController : ControllerBase
{
    private readonly IFeatureManager _featureManager;

    public FeatureController(IFeatureManager featureManager)
    {
        _featureManager = featureManager;
    }

    [FeatureGate("NewFeature")]
    [HttpGet("new-feature-endpoint")]
    public IActionResult NewFeatureEndpoint()
    {
        return Ok("New Feature Endpoint is accessible!");
    }
}
```

當 `NewFeature` 功能標誌被停用時，對 `new-feature-endpoint` 的存取將回傳 `404`。

### 步驟 5：使用條件 Feature Filters（例如百分比）

您可以在 Azure App Configuration 中設定基於條件的功能標誌過濾器，例如百分比控制。在 Azure App Configuration 內，為功能標誌（如 `BetaFeature`）設定一個百分比過濾器：

1. 回到 Azure App Configuration 的「**Feature Manager**」。
2. 點擊 `BetaFeature`，然後新增 `Percentage` 過濾器。
3. 設定「Parameters」中的「Value」為 50（即 50% 的請求會啟用此功能）。

#### 在 `Program.cs` 中註冊 PercentageFilter 支援

在 `Program.cs` 中新增 `PercentageFilter` 支援，以便應用可以正確處理這一過濾器：

```csharp
builder.Services.AddFeatureManagement()
    .AddFeatureFilter<Microsoft.FeatureManagement.FeatureFilters.PercentageFilter>();
```

這樣設定後，應用會根據設定的百分比控制功能標誌的啟用。

### 步驟 6：測試與偵錯

1. **啟動應用程式**，然後存取 `/api/feature/check-new-feature` 或 `/api/feature/new-feature-endpoint`。
2. **在 Azure App Configuration 中更新功能標誌狀態**，並觀察 Web API 中的變化。
3. **使用條件過濾器**進行測試，比如修改百分比並觀察 API 回應。

### 使用總結

1. **Azure App Configuration 設定功能標誌**：在 Azure App Configuration 中設定功能標誌及過濾器。
2. **整合 .NET Web API**：在 `Program.cs` 中設定 Azure App Configuration 和 Feature Management。
3. **檢查功能標誌狀態**：在 API 控制器中使用 `IFeatureManager` 或 `FeatureGate` 屬性檢查和控制功能。
4. **使用條件過濾器**：根據條件（如百分比）動態控制功能標誌。

這樣，您就能在 Azure 中集中管理功能標誌，並將其整合到 .NET Web API 應用中，以實作更靈活的功能控制。

---

## 自訂回傳的錯誤格式與訊息

`FeatureNotEnabledHandler` 用於自訂當功能標誌 (Feature Flag) 被停用時的錯誤回應格式。在 ASP.NET Core Web API 中，您可以通過實作 `IDisabledFeaturesHandler` 介面來定義自訂的錯誤處理邏輯。這樣，當使用 `FeatureGate` 屬性控制的功能標誌被停用時，就可以回傳自訂的錯誤訊息和狀態碼。

以下是如何使用 `FeatureNotEnabledHandler` 自訂錯誤回應的完整教學。

### 步驟 1：建立自訂的 `FeatureNotEnabledHandler`

首先，建立一個類來實作 `IDisabledFeaturesHandler`，並在其中定義當功能被停用時應回傳的錯誤訊息和格式。

#### 自訂 FeatureNotEnabledHandler 類別

```csharp
using Microsoft.AspNetCore.Mvc.Filters;
using Microsoft.FeatureManagement.Mvc;
using System.Text.Json;

// 建立自定義的 FeatureNotEnabledHandler
public class FeatureNotEnabledHandler : IDisabledFeaturesHandler
{
    public Task HandleDisabledFeatures(IEnumerable<string> features, ActionExecutingContext context)
    {
        var response = context.HttpContext.Response;
        response.StatusCode = StatusCodes.Status403Forbidden;  // 可改為所需的狀態碼
        response.ContentType = "application/json";

        var errorResponse = new
        {
            Status = response.StatusCode,
            Message = "This feature is currently disabled.",
            Feature = context.ActionDescriptor.DisplayName // 可以包含更多上下文資訊
        };

        // 將自定義錯誤訊息轉為 JSON
        var json = JsonSerializer.Serialize(errorResponse);

        return response.WriteAsync(json);
    }
}
```

在此程式碼中，我們自訂了 `HandleDisabledFeatures` 方法，以回傳 `403 Forbidden` 狀態碼和自訂 JSON 格式的錯誤訊息。您可以根據需求調整狀態碼和錯誤內容。

### 步驟 2：註冊自訂的 `FeatureNotEnabledHandler`

在 `Program.cs` 中註冊自訂的 `FeatureNotEnabledHandler`，以便當功能標誌被停用時，ASP.NET Core Web API 使用我們自訂的處理邏輯。

#### 在 `Program.cs` 中新增註冊

```csharp
using Microsoft.FeatureManagement;
using Microsoft.FeatureManagement.Mvc;

var builder = WebApplication.CreateBuilder(args);

// 添加 Feature Management 和自定義的 FeatureNotEnabledHandler
builder.Services.AddFeatureManagement();
builder.Services.AddSingleton<IDisabledFeaturesHandler, FeatureNotEnabledHandler>();

// 添加控制器
builder.Services.AddControllers();

var app = builder.Build();

app.UseHttpsRedirection();
app.UseAuthorization();
app.MapControllers();
app.Run();
```

在上面的程式碼中，`AddSingleton<IDisabledFeaturesHandler, FeatureNotEnabledHandler>()` 註冊了自訂的 `FeatureNotEnabledHandler`，這樣當使用 `FeatureGate` 檢查到功能標誌被停用時，就會呼叫自訂的錯誤處理邏輯。

### 步驟 3：在控制器中使用 `FeatureGate` 屬性

在控制器的 API 端點上應用 `FeatureGate` 屬性來控制存取。當功能標誌被停用時，應用程式將回傳自訂的錯誤回應。

#### API 控制器範例

```csharp
using Microsoft.AspNetCore.Mvc;
using Microsoft.FeatureManagement.Mvc;

[ApiController]
[Route("api/[controller]")]
public class FeatureController : ControllerBase
{
    [FeatureGate("NewFeature")]
    [HttpGet("new-feature-endpoint")]
    public IActionResult NewFeatureEndpoint()
    {
        return Ok("New Feature Endpoint is accessible!");
    }
}
```

這段程式碼使用 `FeatureGate("NewFeature")` 來控制 `/api/feature/new-feature-endpoint` 的存取。當 `NewFeature` 被停用時，`FeatureNotEnabledHandler` 會攔截請求並回傳自訂的錯誤回應。

### 驗證效果

當 `NewFeature` 標誌被停用時，存取 `/api/feature/new-feature-endpoint` 將回傳自訂的錯誤訊息：

```json
{
    "Status": 403,
    "Message": "This feature is currently disabled.",
    "Feature": "new-feature-endpoint"
}
```

### 調整錯誤回應內容

您可以根據需要在 `FeatureNotEnabledHandler` 中自訂錯誤訊息的格式和內容，例如新增更多的上下文資訊（如使用者身分、請求 ID 等），或更改狀態碼。

這樣，您就能使用 `FeatureNotEnabledHandler` 自訂 `FeatureGate` 屬性控制的功能標誌被停用時的錯誤回應格式，從而提升使用者體驗並便於進行錯誤排查。