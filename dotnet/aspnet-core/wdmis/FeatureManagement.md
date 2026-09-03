---
kind: original
---

# FeatureManagement

在 .NET 8 中使用 `builder.Services.AddFeatureManagement()` 來啟用功能管理（Feature Management），您需要安裝 `Microsoft.FeatureManagement.AspNetCore` 套件。

### 安裝套件

可以通過 NuGet 安裝 `Microsoft.FeatureManagement.AspNetCore`：

```shell
dotnet add package Microsoft.FeatureManagement
```

### 使用範例

安裝套件後，您可以在 `Program.cs` 中使用 `AddFeatureManagement()` 來啟用功能管理，這樣可以方便地在應用程式中控制特性或功能的啟用狀態。

```csharp
using Microsoft.FeatureManagement;

var builder = WebApplication.CreateBuilder(args);

// 啟用功能管理
builder.Services.AddFeatureManagement();

var app = builder.Build();

// 使用功能管理進行特性判斷
app.MapGet("/", async (IFeatureManager featureManager) =>
{
    if (await featureManager.IsEnabledAsync("MyFeature"))
    {
        return Results.Ok("Feature is enabled");
    }
    return Results.Ok("Feature is disabled");
});

app.Run();
```

### 設定功能標誌

在 `appsettings.json` 中可以定義功能標誌（feature flags）：

```json
{
  "FeatureManagement": {
    "MyFeature": true
  }
}
```

這樣，您就可以使用 `IFeatureManager` 來動態檢查和管理應用程式中的功能啟用情況，非常適合用於 A/B 測試、分階段發布和其他場景的功能控制。