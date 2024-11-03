# ASP.NET Core Consul 教學

Cunsul 架構圖

![Cunsul 架構圖](https://godleon.github.io/blog/images/service-mesh/consul-arch.png)

[官方網站](https://www.consul.io)

Consul 是 HashiCorp 提供的一個分布式服務網格解決方案，專為微服務架構設計，具有服務發現、配置管理和健康檢查等功能。它能夠幫助不同服務在分布式系統中相互發現並進行通訊，同時提供配置管理和自動化功能，以便在雲端、混合雲和本地環境中高效運行。

### Consul 的核心功能

1. **服務發現（Service Discovery）**
   - Consul 能夠自動識別和記錄已註冊的服務，使得每個服務都能根據需要找到其他服務。服務可以通過 Consul 的 API 註冊和查詢，使得它們能動態更新並相互發現。
2. **健康檢查（Health Checks）**
   - Consul 支持針對服務和節點的健康檢查。健康檢查確保只有健康的服務和節點才會被記錄並使用，這樣能提高服務的穩定性，並防止服務調用到無法使用的實例。
3. **分布式鍵值存儲（Key-Value Store）**
   - Consul 提供一個簡單的鍵值存儲，可以用來保存配置、標記和元數據等信息。這個功能可以支援配置管理和動態設置變數，使得配置更靈活。
4. **服務網格（Service Mesh）**
   - Consul 提供了完整的服務網格功能，包括服務之間的安全通訊、流量管理和監控。它支持自動注入代理，從而實現透明的服務通訊、安全策略管理和監控等功能。
5. **多數據中心支持（Multi-Datacenter Support）**
   - Consul 的架構支持多數據中心，並能在跨數據中心的情況下實現一致性和容錯機制，適合在大型分布式系統和全球範圍內的部署。

### Consul 的工作原理

Consul 使用一種稱為「代理（Agent）」的架構，並且每個服務器或節點上都會運行一個 Consul 代理。代理可以在以下兩種模式之一下運行：

1. **Client 模式**：該模式下的代理僅負責轉發查詢和服務註冊請求，無需存儲數據。
2. **Server 模式**：該模式下的代理負責存儲數據和處理查詢。Consul 使用 Raft 共識算法來保證一致性，一般需要至少三到五個 Server 節點來維持高可用性和故障恢復。

### Consul 的應用場景

- **微服務架構中的服務發現**：隨著服務數量的增多，手動管理服務間的連接變得困難，Consul 的服務發現功能能幫助解決這個問題。
- **動態配置管理**：透過 Consul 的鍵值存儲，可以進行分布式的配置管理，適合需要動態更新配置的場景。
- **服務健康檢查**：在分布式系統中進行健康檢查，能確保流量不會路由到失效的服務或節點。
- **跨數據中心的高可用架構**：使用 Consul 構建跨數據中心的部署，可以實現全球範圍內的服務冗餘和一致性。

---

## 範例教學

### 1. 在 Docker 中安裝 Consul

首先，在 Docker 上啟動 Consul：

```bash
docker run -d --name=consul -p 8500:8500 consul
```

這將啟動 Consul 並將管理界面開放於 `http://localhost:8500`。

### 2. 建立 .NET WebAPI 專案

創建一個新的 .NET WebAPI 專案：

```bash
dotnet new webapi -n ConsulDemoAPI
cd ConsulDemoAPI
```

### 3. 添加 Consul 套件

使用 NuGet 安裝 `Consul` 套件：

```bash
dotnet add package Consul
```

### 4. 設定 Consul 客戶端並註冊服務

在 `Program.cs` 中設定 Consul 註冊服務的邏輯：

```csharp
using Consul;

var builder = WebApplication.CreateBuilder(args);

// 註冊 Consul 客戶端
builder.Services.AddSingleton<IConsulClient, ConsulClient>(p => new ConsulClient(consulConfig =>
{
    // 設定 Consul 位址
    consulConfig.Address = new Uri("http://localhost:8500");
}));

// 註冊 WebAPI 服務
var app = builder.Build();

app.Lifetime.ApplicationStarted.Register(() =>
{
    var consulClient = app.Services.GetRequiredService<IConsulClient>();

    // 註冊服務到 Consul
    var registration = new AgentServiceRegistration
    {
        ID = "ConsulDemoAPI",
        Name = "ConsulDemoAPI",
        Address = "localhost",
        Port = 7240, // 設定 WebAPI 埠號
        Check = new AgentServiceCheck
        {
            HTTP = "http://localhost:7240/api/health", // 健康檢查的 URL
            Interval = TimeSpan.FromSeconds(10),       // 檢查間隔
            Timeout = TimeSpan.FromSeconds(5)          // 超時設定
        }
    };

    // 註冊服務
    consulClient.Agent.ServiceRegister(registration).GetAwaiter().GetResult();
});

app.Lifetime.ApplicationStopping.Register(() =>
{
    var consulClient = app.Services.GetRequiredService<IConsulClient>();
    // 取消註冊服務
    consulClient.Agent.ServiceDeregister("ConsulDemoAPI").GetAwaiter().GetResult();
});

app.MapControllers();
app.Run();
```

這段程式碼會在應用程式啟動時向 Consul 註冊服務，並在停止時自動註銷。

### 5. 從 Consul 中查詢服務資訊

在控制器中建立一個方法，用於從 Consul 中查詢特定服務的資訊。以下是查詢的範例程式碼：

```csharp
using Consul;
using Microsoft.AspNetCore.Mvc;

namespace ConsulDemoAPI.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class ConsulServiceController : ControllerBase
    {
        private readonly IConsulClient _consulClient;

        public ConsulServiceController(IConsulClient consulClient)
        {
            _consulClient = consulClient;
        }

        [HttpGet("services/{serviceName}")]
        public async Task<IActionResult> GetService(string serviceName)
        {
            // 從 Consul 中取得指定服務的所有實例
            var queryResult = await _consulClient.Health.Service(serviceName, null, true);
            if (queryResult.Response.Length == 0)
            {
                return NotFound("Service not found");
            }

            // 範例：顯示每個服務實例的 ID、地址和埠號
            var services = queryResult.Response.Select(s => new
            {
                ServiceID = s.Service.ID,
                ServiceName = s.Service.Service,
                Address = s.Service.Address,
                Port = s.Service.Port
            });

            return Ok(services);
        }
    }
}
```

### 6. 測試查詢服務

啟動 WebAPI 並使用以下 API 路徑來查詢已註冊在 Consul 中的服務：

```bash
GET http://localhost:7240/api/consulservice/services/{serviceName}
```

將 `{serviceName}` 替換為要查詢的服務名稱。例如，如果服務名稱是 `ConsulDemoAPI`，則 URL 會是：

```bash
GET http://localhost:7240/api/consulservice/services/ConsulDemoAPI
```

這個 API 將返回服務的所有實例及其詳細資訊，包括每個實例的 ID、地址和埠號。

### 7. 設定健康檢查端點

在 WebAPI 中添加一個健康檢查端點，用來返回服務健康狀態。可以在 `Controllers` 資料夾中添加一個 `HealthController`：

```csharp
using Microsoft.AspNetCore.Mvc;

namespace ConsulDemoAPI.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class HealthController : ControllerBase
    {
        [HttpGet]
        public IActionResult HealthCheck()
        {
            // 健康檢查的簡單回應
            return Ok("Service is healthy");
        }
    }
}
```

這個 `HealthCheck` 方法將作為健康檢查的端點，返回服務狀態。

### 8. 執行和測試健康檢查

啟動 WebAPI，然後訪問 Consul 的 UI（`http://localhost:8500`）。在 Consul 管理介面中可以看到 `ConsulDemoAPI` 服務已註冊，並且會定期檢查 `http://localhost:5000/api/health` 的狀態。如果此端點返回成功狀態（如 200 OK），則 Consul 將該服務標記為健康狀態。