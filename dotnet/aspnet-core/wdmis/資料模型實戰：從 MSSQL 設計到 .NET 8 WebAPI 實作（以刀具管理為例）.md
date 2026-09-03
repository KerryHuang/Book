---
kind: original
---

# 資料模型實戰：從 MSSQL 設計到 .NET 8 WebAPI 實作（以刀具管理為例）

## 前言

在現代製造業或工廠數位化轉型中，「刀具管理」是一個具代表性的應用場景。透過資料庫模型設計、Entity Framework Core 整合與 API 建置，我們能快速打造一套具備 CRUD、保養紀錄與歷史查詢的完整系統。

本書將以 30 分鐘教學課程為藍本，帶領讀者從 MSSQL 資料庫設計開始，一步一步進入 .NET 8 的 WebAPI 開發世界，使用 EF Core Power Tools 自動產生模型，並實作實用的 API。

------

## 第 1 章：資料模型設計概論

### 1.1 資料模型的角色

資料模型是連結業務需求與資料結構的橋樑。它幫助我們：

- 定義資料如何儲存（資料表設計）
- 理解資料之間的關係（ERD 設計）
- 支援系統的資料存取與驗證需求

### 1.2 資料模型分類

- **概念性模型（Conceptual Model）**：業務角度的抽象定義實體與關聯，例如「一把刀具可有多筆保養紀錄」。
- **邏輯模型（Logical Model）**：資料表結構、欄位類型、關聯關係（ERD）。
- **實體模型（Physical Model）**：實際在資料庫中的實作，例如實際的資料表定義、索引、資料型別。

```text
[使用者需求訪談]
        ↓
[概念性模型]（Entities: 刀具、入庫、保養、使用紀錄）
        ↓
[邏輯模型 ERD]
（關聯關係：一對多、多對多）
        ↓
[實體模型]
（欄位設計、資料型別、主外鍵）
        ↓
[MSSQL 資料表實作]
（CREATE TABLE）
        ↓
[.NET 實體類別]
（EF Core Entity / DbContext）
        ↓
[DTO + 驗證 + API + 測試 + 觀察性]
```



### 1.3 資料模型設計原則

設計資料模型時應遵守以下原則：

- **正規化（Normalization）**：消除資料冗餘，確保一致性（如第三正規化）
- **關聯一致性（Referential Integrity）**：透過外鍵約束維持資料關聯的正確性
- **可擴展性（Scalability）**：模型設計應容許未來擴充欄位或新關聯
- **命名一致性（Naming Consistency）**：欄位名稱具描述性，資料型別合理

### 1.4 資料模型設計流程（步驟）

1. **需求蒐集**：訪談使用者或主管，瞭解業務流程與資料項目
2. **定義實體與屬性**：找出資料實體（如 Tool）、每個實體的屬性（如 Name, PurchaseDate）
3. **設計關聯**：定義實體之間的關聯類型（如一對多）
4. **畫出 ERD**：使用圖形工具（如 dbdiagram.io）呈現模型
5. **驗證與調整**：與業務方對焦確認，是否符合實際應用
6. **轉換為資料表設計**：將 ERD 對應至 MSSQL 資料表與欄位型別

### 1.5 刀具管理系統概念性模型

實體：

- **Tool（刀具）**：刀具的基本資料。
- **ToolInbound（刀具入庫）**：刀具何時入庫、來源、數量。
- **ToolUsage（刀具使用紀錄）**：紀錄使用時間、機台、人員。
- **ToolMaintenance（刀具保養紀錄）**：紀錄保養項目、保養人員與時間。

關聯：

- 一個 Tool 對應多個 Inbound、Usage、Maintenance

ERD 示意：

```
Tool
├── ToolInbound
├── ToolUsage
└── ToolMaintenance
```

## 

#### 關聯設計：

- 一把 `Tool` 可有多筆 `ToolUsage` → 一對多
- 一把 `Tool` 可有多筆 `ToolMaintenance` → 一對多
- 使用 `ToolId` 作為外鍵連結

#### ERD 示意圖（文字版）：

```
Tool (1) -------- (∞) ToolUsage
Tool (1) -------- (∞) ToolMaintenance
```

透過這樣的設計，我們可以：

- 快速查詢某把刀具的使用與保養紀錄
- 保證每筆紀錄都有對應的刀具資料（外鍵保護）
- 容許未來擴充屬性，例如刀具狀態、壽命指標等

### 1.6 工具與設計建議

- ERD 設計：使用 dbdiagram.io、draw.io、SSMS Diagram Tool
- 命名建議：實體用單數命名（Tool）、主鍵為實體名 + Id
- 優先定義核心資料表，次要資料表視需求擴充

------

## 第 2 章：MSSQL 資料表設計與關聯

### 2.1 資料表設計

```sql
CREATE TABLE Tool (
    ToolId INT PRIMARY KEY IDENTITY,
    ToolCode NVARCHAR(50) NOT NULL,
    ToolName NVARCHAR(100) NOT NULL,
    Spec NVARCHAR(200),
    CreatedAt DATETIME NOT NULL DEFAULT GETDATE()
);

CREATE TABLE ToolInbound (
    InboundId INT PRIMARY KEY IDENTITY,
    ToolId INT FOREIGN KEY REFERENCES Tool(ToolId),
    Quantity INT NOT NULL,
    InboundDate DATETIME NOT NULL,
    Source NVARCHAR(100)
);

CREATE TABLE ToolUsage (
    UsageId INT PRIMARY KEY IDENTITY,
    ToolId INT FOREIGN KEY REFERENCES Tool(ToolId),
    Machine NVARCHAR(50),
    Operator NVARCHAR(50),
    UsedHours DECIMAL(5,2),
    UsageDate DATETIME NOT NULL
);

CREATE TABLE ToolMaintenance (
    MaintenanceId INT PRIMARY KEY IDENTITY,
    ToolId INT FOREIGN KEY REFERENCES Tool(ToolId),
    MaintenanceDate DATETIME NOT NULL,
    Description NVARCHAR(200),
    Maintainer NVARCHAR(50)
);
```

### 2.2 關聯解釋

- 一把刀具 `Tool` 會有多筆使用紀錄與保養紀錄 → 一對多關係
- 使用外鍵約束確保資料完整性
- 可為 ToolUsage.Date、Tool.Name 建立索引加速查詢

### 2.3 資料表命名原則（Table Naming）

#### ✅ 原則說明

| 原則                          | 說明                                                         |
| ----------------------------- | ------------------------------------------------------------ |
| 使用單數名詞                  | 如：`Tool` 而非 `Tools`，對應物件導向設計（Entity）概念      |
| 使用 PascalCase 或 Snake_Case | 根據團隊慣例選擇一致風格，例如 `ToolMaintenance` 或 `tool_maintenance` |
| 命名具備業務語意              | 使用業務語言描述（如 `PurchaseOrder`、`ToolUsage`）          |
| 不使用縮寫或語焉不詳詞        | 避免 `TMP`, `VAL1`, `DATA2` 等無意義命名                     |



#### 🔍 範例命名

| 業務對象 | 表名建議          |
| -------- | ----------------- |
| 刀具主檔 | `Tool`            |
| 使用紀錄 | `ToolUsage`       |
| 保養紀錄 | `ToolMaintenance` |
| 採購訂單 | `PurchaseOrder`   |
| 工作單   | `WorkOrder`       |



------

### 2.4 資料欄位命名原則（Column Naming）

#### ✅ 原則說明

| 原則                                      | 說明                                                      |
| ----------------------------------------- | --------------------------------------------------------- |
| 使用 PascalCase（C#）或 snake_case（SQL） | 保持一致性，例如：`ToolId` / `tool_id`                    |
| 主鍵命名為 TableName + Id                 | 如 `ToolId`、`OrderId`，避免單一 `Id` 帶來混淆            |
| 外鍵應具備來源實體語意                    | 如：`ToolId`（來自 `Tool`）                               |
| 避免使用保留字                            | 如 `Date`, `User`, `Name` 等，應改為具體如 `PurchaseDate` |
| 布林欄位建議用 Is/Has 開頭                | 例如：`IsActive`, `HasWarranty`                           |
| 時間類欄位建議用 Time/Date 結尾           | 例如：`CreatedDate`, `LastModifiedTime`                   |



#### 🔍 範例命名

| 欄位目的 | 命名建議                          |
| -------- | --------------------------------- |
| 主鍵     | `ToolId`                          |
| 外鍵     | `ToolId`, `OrderId`               |
| 名稱     | `Name`                            |
| 狀態     | `IsActive`, `Status`              |
| 建立時間 | `CreatedDate`                     |
| 負責人員 | `MaintainedBy`, `Operator`        |
| 數值欄位 | `UsageHours`, `Price`, `Quantity` |



------

### 2.6 命名一致性對 EF Core 的重要性

| 類型     | 建議命名格式            | EF Core 行為      |
| -------- | ----------------------- | ----------------- |
| 主鍵     | `EntityNameId`          | 自動辨識為主鍵    |
| 導覽屬性 | 複數命名如 `ToolUsages` | 對應一對多集合    |
| 外鍵欄位 | `EntityNameId`          | 自動建立關聯與 FK |

------

## 第 3 章：使用 EF Core Power Tools 映射資料模型

### 3.1 安裝 EF Core Power Tools

- Visual Studio → Extensions → Manage Extensions
- 搜尋 "EF Core Power Tools" 並安裝
- 重啟 Visual Studio

### 3.2 使用 Reverse Engineer 功能

1. 右鍵專案 → `EF Core Power Tools` → `Reverse Engineer`
2. 選擇資料庫連線 → 選擇 `Tool`, `ToolUsage`, `ToolMaintenance`
3. 設定輸出目錄（如 `/Models/Entities`）
4. 命名 DbContext 為 `ToolDbContext`
5. 選擇適合的選項（如使用 Fluent API、自動包含導覽屬性）

### 3.3 產出結果說明

- 自動產生三個 Entity 類別與一個 DbContext：

```csharp
public partial class Tool
{
    public int ToolId { get; set; }
    public string Name { get; set; }
    public string ToolType { get; set; }
    public DateTime? PurchaseDate { get; set; }
    public bool IsActive { get; set; }

    public virtual ICollection<ToolUsage> ToolUsages { get; set; }
    public virtual ICollection<ToolMaintenance> ToolMaintenances { get; set; }
}
```

### 3.4 測試查詢

```csharp
using var db = new ToolDbContext();
var tool = db.Tools.Include(t => t.ToolUsages).FirstOrDefault(t => t.ToolId == 1);
```

------

## 第 4 章：建立 WebAPI 並整合資料模型

### 4.1 建立 ASP.NET Core Web API 專案

```bash
dotnet new webapi -n ToolManagement.Api
```

### 4.2 設定 DI 與資料庫連線

在 `Program.cs` 註冊 DbContext：

```csharp
builder.Services.AddDbContext<ToolDbContext>(options =>
    options.UseSqlServer(builder.Configuration.GetConnectionString("DefaultConnection")));
```

### 4.3 實作 Controller

以 `ToolController` 為例：

```csharp
[ApiController]
[Route("api/[controller]")]
public class ToolController : ControllerBase
{
    private readonly ToolDbContext _context;
    public ToolController(ToolDbContext context) => _context = context;

    [HttpGet]
    public async Task<IEnumerable<Tool>> GetAll() => await _context.Tools.ToListAsync();

    [HttpPost]
    public async Task<IActionResult> Create(Tool tool)
    {
        _context.Tools.Add(tool);
        await _context.SaveChangesAsync();
        return Ok(tool);
    }
}
```

### 4.4 測試 API

- 使用 Swagger 自動產生測試介面
- 或用 Postman 測試 GET/POST 呼叫

------

## 第 5 章：進階開發實務補充

### 5.1 使用 DTO 與 AutoMapper 抽離資料模型

在實際開發中，我們不建議直接將 EF Core 的實體類別（Entities）公開給前端使用，原因包括資料洩漏風險、耦合性過高、不易維護等。

**Data Transfer Object (DTO)** 是一種介於資料層與展示層之間的中介結構，用於：

- 隱藏不必要欄位
- 控制資料流向（防止 over-posting）
- 提供多樣化輸出格式（如列表頁與詳情頁不同格式）

AutoMapper 可自動將 Entity 與 DTO 相互對應，簡化轉換程式碼：

```csharp
public class ToolDto
{
    public string Name { get; set; }
    public string ToolType { get; set; }
    public bool IsActive { get; set; }
}

public class MappingProfile : Profile
{
    public MappingProfile()
    {
        CreateMap<Tool, ToolDto>();
        CreateMap<ToolDto, Tool>();
    }
}
```

在 `Program.cs` 中註冊 AutoMapper：

```csharp
builder.Services.AddAutoMapper(typeof(Program));
```

### 5.2 驗證機制：FluentValidation 整合

FluentValidation 是一套用於建構強型別驗證規則的 .NET 套件，相較於 Data Annotations 更具彈性與可讀性。

安裝方式：

```
dotnet add package FluentValidation.AspNetCore
```

定義驗證規則：

```csharp
public class ToolDtoValidator : AbstractValidator<ToolDto>
{
    public ToolDtoValidator()
    {
        RuleFor(x => x.Name).NotEmpty().WithMessage("名稱不可空白");
        RuleFor(x => x.ToolType).MaximumLength(50);
    }
}
```

在 `Program.cs` 註冊：

```csharp
builder.Services.AddValidatorsFromAssemblyContaining<ToolDtoValidator>();
```

### 5.3 單元測試與整合測試（xUnit）

良好的系統需具備測試能力，包括：

- 單元測試（Unit Test）：測試個別邏輯，例如驗證規則、資料轉換
- 整合測試（Integration Test）：模擬 API 呼叫流程，測試資料庫互動

安裝必要套件：

```
dotnet add package xunit
```

範例測試類別：

```csharp
public class ToolTests
{
    [Fact]
    public void Should_Create_Valid_Tool()
    {
        var tool = new Tool { Name = "Cutter", ToolType = "Drill", IsActive = true };
        Assert.Equal("Cutter", tool.Name);
    }
}
```

整合測試可使用 `WebApplicationFactory` 或 TestServer 建立 API 測試情境。

### 5.4 加入觀察性：OpenTelemetry + Serilog

現代應用應具備觀察性能力，包括追蹤、日誌與指標收集。

#### Serilog 紀錄日誌

```
dotnet add package Serilog.AspNetCore
```

設定 Serilog：

```csharp
Log.Logger = new LoggerConfiguration()
    .WriteTo.Console()
    .CreateLogger();

builder.Host.UseSerilog();
```

#### OpenTelemetry 分散式追蹤

```
dotnet add package OpenTelemetry.Exporter.Zipkin
```

設定追蹤：

```csharp
builder.Services.AddOpenTelemetryTracing(builder => builder
    .AddAspNetCoreInstrumentation()
    .AddEntityFrameworkCoreInstrumentation()
    .AddZipkinExporter(opt => opt.Endpoint = new Uri("http://localhost:9411/api/v2/spans")));
```

搭配 Zipkin/Grafana/Jaeger 可視覺化整個請求鏈路，有助除錯與效能監控。

---

## 結語

透過本書範例，我們實作了 MSSQL → EF Core → ASP.NET Core API 的資料模型整合流程。這不僅可套用於刀具管理，也適用於大多數的商業資料管理系統。
