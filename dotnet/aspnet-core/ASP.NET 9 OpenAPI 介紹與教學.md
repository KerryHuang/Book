---
kind: original
---

# .NET 9 OpenAPI 介紹與教學

## 目錄

1. [OpenAPI 簡介](#openapi-簡介)
2. [環境與套件清單](#環境與套件清單)
3. [設定 API 版本管理](#設定-api-版本管理)
4. [產生多版本 OpenAPI 文件](#產生-多版本-openapi-文件)
5. [整合 Swagger UI](#整合-swagger-ui)
6. [整合 ReDoc](#整合-redoc)
7. [整合 Scalar UI](#整合-scalar-ui)
8. [自訂與進階功能](#自訂與進階功能)
9. [測試與驗證](#測試與驗證)
10. [結語](#結語)

------

## OpenAPI 簡介

OpenAPI（前稱 Swagger）是一種用於描述 RESTful API 的開放標準（Open Specification）。其核心價值在於：

- **機器可讀**：以 JSON 或 YAML 格式描述 API，包括路由（paths）、請求/回應模型（components）、安全機制（securitySchemes）等。
- **工具生態**：可自動生成互動式文件（Swagger UI、ReDoc、Scalar），自動產生 Client SDK，甚至可結合測試／模擬伺服器。
- **清晰規範**：統一規範能讓前後端、跨團隊協作時都依同一份文件開發。

一份典型的 OpenAPI 文件包含：

```yaml
openapi: 3.0.3
info:
  title: My API
  version: v1
  description: 這是範例 API
servers:
  - url: https://api.example.com
paths:
  /weather:
    get:
      summary: 取得天氣列表
      responses:
        '200':
          description: 成功
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/Weather'
components:
  schemas:
    Weather:
      type: object
      properties:
        date:
          type: string
          format: date
        temperatureC:
          type: integer
```

------

## 環境與套件清單

- **.NET 9 SDK**
- **IDE**：Visual Studio 2022 (17.7+) 或 VS Code

透過 CLI 安裝以下 NuGet 套件：

```bash
dotnet add package Asp.Versioning.Http                   # API 版本管理
dotnet add package Asp.Versioning.Mvc.ApiExplorer        # 版本化的 ApiExplorer
dotnet add package Microsoft.AspNetCore.OpenApi          # 內建 OpenAPI 支援
dotnet add package Swashbuckle.AspNetCore               # Swagger UI
dotnet add package Swashbuckle.AspNetCore.ReDoc         # ReDoc 支援
dotnet add package Scalar.AspNetCore --version 2.1.0    # Scalar UI（含多文件支援）
```

------

## 設定 API 版本管理

在 `Program.cs`（Minimal API 範例）中加入：

```csharp
var builder = WebApplication.CreateBuilder(args);

// 1. 最小化 API 探索 (EndpointsApiExplorer)
builder.Services.AddEndpointsApiExplorer();

// 2. 設定 API 版本管理
builder.Services.AddApiVersioning(options =>
{
    options.DefaultApiVersion             = new ApiVersion(1, 0);
    options.AssumeDefaultVersionWhenUnspecified = true;
    options.ReportApiVersions             = true;  // 回應 header 中顯示 supported versions
})
// 3. 版本化 Explorer，供後續產生多份 OpenAPI 文件
.AddApiExplorer(options =>
{
    options.GroupNameFormat       = "'v'VVV";    // 版本群組格式，例如 v1、v2.1
    options.SubstituteApiVersionInUrl = true;     // 將版本字串注入路由
});
```

> **注意**：若使用 Controller API，還需 `builder.Services.AddControllers();` 並在 `app.MapControllers()` 前註冊版本化路由。

------

## 產生 多版本 OpenAPI 文件

緊接著，在建置完 `builder` 之後、呼叫 `Build()` 之前，動態為每個版本產生描述檔：

```csharp
var app = builder.Build();

// 取得版本描述清單
var provider = app.Services.GetRequiredService<IApiVersionDescriptionProvider>();

// 透過 Microsoft.AspNetCore.OpenApi 為每個版本註冊 OpenAPI 生成器
foreach (var desc in provider.ApiVersionDescriptions)
{
    builder.Services.AddOpenApiDocument(desc.GroupName, options =>
    {
        options.DocumentName = desc.GroupName; 
        options.PostProcess = doc =>
        {
            doc.Info.Version     = desc.ApiVersion.ToString();
            doc.Info.Title       = $"My API {desc.GroupName}";
            doc.Info.Description = "多版本 OpenAPI 範例";
        };
    });
}
```

上面會在執行時為每個版本（如 `v1`、`v2`）生成相對應的 JSON：

```bash
/openapi/v1.json
/openapi/v2.json
...
```

------

## 整合 Swagger UI

在 `app.Environment.IsDevelopment()` 中加入：

```csharp
if (app.Environment.IsDevelopment())
{
    // 1. 將所有 /openapi/{name}.json 映射成路由
    app.MapOpenApi();

    // 2. 啟用 Swagger UI
    app.UseSwaggerUI(options =>
    {
        // 對所有文件逐一註冊在下拉選單
        foreach (var desc in provider.ApiVersionDescriptions)
        {
            var url  = $"/openapi/{desc.GroupName}.json";
            var name = $"My API {desc.GroupName}";
            options.SwaggerEndpoint(url, name);
        }
        options.RoutePrefix = "swagger";  // UI 路徑 /swagger
    });
}
```

開啟瀏覽器至 `https://<host>/swagger`，即可在 UI 下拉選單中切換不同版本。

------

## 整合 ReDoc

在同一區塊中，繼續啟用 ReDoc：

```csharp
if (app.Environment.IsDevelopment())
{
    app.UseReDoc(options =>
    {
        foreach (var desc in provider.ApiVersionDescriptions)
        {
            options.SpecUrl = $"/openapi/{desc.GroupName}.json";
        }
        options.RoutePrefix = "redoc";     // UI 路徑 /redoc
        options.DocumentTitle = "ReDoc API Docs";
    });
}
```

開啟 `https://<host>/redoc` 可看到由 ReDoc 生成的文件。

------

## 整合 Scalar UI

最後，以 Scalar 提供更現代化的互動介面：

```csharp
if (app.Environment.IsDevelopment())
{
    // 映射 OpenAPI JSON
    app.MapOpenApi();

    // 啟用 Scalar，多版本支援
    app.MapScalarApiReference(options =>
    {
        // 逐一加入版本
        foreach (var desc in provider.ApiVersionDescriptions)
        {
            options.AddDocument(desc.GroupName, $"My API {desc.GroupName}");
        }
        // 靜態檔案根路徑 (若有自訂 CSS/JS)
        options.RoutePrefix = "scalar";
    });
}
```

瀏覽 `https://<host>/scalar`，側邊欄或下拉即可切換 `v1`、`v2`……等文件。

------

## 自訂與進階功能

- **XML 註解**：在 `.csproj` 中啟用 `<GenerateDocumentationFile>true</...>`，並於 `AddOpenApiDocument` 加入 `IncludeXmlComments(...)`。
- **安全機制**：在 OpenAPI 描述中新增 `components.securitySchemes` 與 `security`，並透過 `options.AddSecurity(...)` 注入。
- **OAuth2／API Key**：Swagger/UI、ReDoc、Scalar 都支援注入授權設定，方便互動測試。
- **UI 客製**：調整路由前綴（`RoutePrefix`）、標題（`DocumentTitle`）、注入自訂 CSS/JS（`InjectStylesheet`、`InjectJavascript`）等。

------

## 測試與驗證

1. **執行專案**

   ```bash
   dotnet run
   ```

2. **Swagger UI**：`https://localhost:5001/swagger`

3. **ReDoc**：`https://localhost:5001/redoc`

4. **Scalar UI**：`https://localhost:5001/scalar`

三者皆應呈現對應版本的互動式 API 文件；可透過下拉或側邊切換版本。

------

## 結語

這份教學示範了如何在 .NET 9 中，**一步一步**：

1. 啟用 **API 版本管理**
2. 產生 **多版本 OpenAPI** JSON
3. 整合三種主流程式文件前端：
   - **Swagger UI**
   - **ReDoc**
   - **Scalar UI**