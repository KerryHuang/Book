---
kind: reprint
source: site:dotblogs.com.tw
author: 余小章
---

# ASP.NET 使用 MassTransit 與 RabbitMQ，實現事件發佈、訂閱

MassTransit 的架構是一個基於事件驅動和 Message 傳遞的分佈式系統架構，主要是要解耦服務之間的通訊。它使用 Message Broker（如 RabbitMQ、ActiveMQ、Kafka、Azure Service Bus、Amazon SQS 等）來傳遞不同服務之間的訊息，它大大的簡化事件驅動的開發門檻

![img](https://dotblogsfile.blob.core.windows.net/user/%E4%BD%99%E5%B0%8F%E7%AB%A0/62d0d5d0-d5fb-4798-9707-d06ff60e336a/1728792113.png.png)




## MassTransit 與 RabbitMQ 架構圖

下圖出自：[MassTransit 知多少 | .NET 分布式应用框架 - 「圣杰」 - 博客园 (cnblogs.com)](https://www.cnblogs.com/sheng-jie/p/MassTransit-NET-Distributed-Application-Framework.html#autoid-3-2-0)

[![img](https://dotblogsfile.blob.core.windows.net/user/%E4%BD%99%E5%B0%8F%E7%AB%A0/62d0d5d0-d5fb-4798-9707-d06ff60e336a/1728837295.png.png)](https://dotblogsfile.blob.core.windows.net/user/余小章/62d0d5d0-d5fb-4798-9707-d06ff60e336a/1728837295.png.png)

### 消息流動過程

Producer，發布消息：

- 生產者向 RabbitMQ 發布一個消息（如事件或命令）。
  - 通過 IPublishEndpoint.Publish：將事件廣播給所有訂閱了該事件類型的消費者。
  - 通過 ISendEndpoint.Send：將訊息發送到指定的佇列，通常用於點對點模式，確保只有一個消費者處理該訊息。

Message Broker (RabbitMQ)：

- 消息到達 RabbitMQ 的 Exchange，Exchange 根據配置的路由規則將消息轉發到一個或多個 Queue。這些規則可以根據消息類型、路由鍵等來進行配置。
- Transport：跟 Message Broker 通訊的角色，負責發送和接收消息。
- 支援多個 Message Broker 例如：RabbitMQ、Azure Service Bus 或 Kafka。

Consumer，處理消息：

- 消費者從 RabbitMQ 的 Queue 中取出消息，並通過實作 IConsumer<T> 的方式來處理收到的消息。
  - IConsumer<T>：處理從 Queue 接收到的事件或命令的消費者。
  - IReceiveEndpoint：接收端點，從 Transport 接收訊息反序列化後傳給消費者。

Message：消息合約，定義消息生產者和消息消費者之間的內容規範。

###  

## 開發環境

- Windows 11 Home
- Rider 2024.2.6
- .NET 8
- rabbitmq:3-management

## 建立 RabbitMQ

docker-compose 內容如下

```plaintext
version: '3.8'
services:
  rabbitmq:
    container_name: rabbitmq.3
    image: "rabbitmq:3-management"
    ports:
      - "5672:5672"   # RabbitMQ 主要連接埠
      - "15672:15672" # 管理介面連接埠
    environment:
      RABBITMQ_DEFAULT_USER: guest
      RABBITMQ_DEFAULT_PASS: guest
```

 

GUI 頁面如下所示

[![img](https://dotblogsfile.blob.core.windows.net/user/%E4%BD%99%E5%B0%8F%E7%AB%A0/62d0d5d0-d5fb-4798-9707-d06ff60e336a/1728881382.png.png)](https://dotblogsfile.blob.core.windows.net/user/余小章/62d0d5d0-d5fb-4798-9707-d06ff60e336a/1728881382.png.png)

## 快速開始

建立一個  .NET 8 的 Web API 專案，

安裝套件

```plaintext
dotnet add package MassTransit.RabbitMQ --version 8.2.5
dotnet add package Microsoft.Extensions.Hosting --version 8.0.1
```

 

### 生產者發佈訊息

新增一個端點，使用 IPublishEndpoint.Publish 發佈事件

```cs
public class OrderCreated
{
    public Guid OrderId { get; set; }

    public DateTime CreatedAt { get; set; }

    public decimal TotalAmount { get; set; }
}

public class CreateOrderRequest
{
    public decimal TotalAmount { get; set; }
}

[ApiController]
[Route("api/[controller]")]
public class OrdersController : ControllerBase
{
    private readonly IPublishEndpoint _publishEndpoint;
    public OrdersController(IPublishEndpoint publishEndpoint)
    {
        this._publishEndpoint = publishEndpoint;
    }

    [HttpPost]
    public async Task<ActionResult> CreateOrder([FromBody] CreateOrderRequest request)
    {
        if (request == null)
        {
            return this.BadRequest("Invalid order data");
        }

        var orderCreatedEvent = new OrderCreated
        {
            OrderId = Guid.NewGuid(),
            CreatedAt = DateTime.UtcNow,
            TotalAmount = request.TotalAmount
        };
        
        // 生產者，發布 OrderCreated 事件
        await this._publishEndpoint.Publish(orderCreatedEvent);

        return this.Ok($"Order created with ID: {orderCreatedEvent.OrderId}");
    }
}
```

 

### 消費者處理訊息

消費者實作 IConsumer<OrderCreated>，並用 ConsumeContext<OrderCreated> 處理訊息

```cs
public class OrderCreatedConsumer : IConsumer<OrderCreated>
{
    public Task Consume(ConsumeContext<OrderCreated> context)
    {
        Console.WriteLine($"Order created: {context.Message.OrderId}, Total Amount: {context.Message.TotalAmount}");
        return Task.CompletedTask;
    }
}
```

 

經中斷得知 ConsumeContext 內容如下

[![img](https://dotblogsfile.blob.core.windows.net/user/%E4%BD%99%E5%B0%8F%E7%AB%A0/62d0d5d0-d5fb-4798-9707-d06ff60e336a/1728882601.png.png)](https://dotblogsfile.blob.core.windows.net/user/余小章/62d0d5d0-d5fb-4798-9707-d06ff60e336a/1728882601.png.png)

 

在 DI Container 配置 MassTransit⁠⁠ 的 Message Broker

```cs
builder.Services.AddMassTransit(x =>
{
    // 註冊消費者
    x.AddConsumer<OrderCreatedConsumer>();

    // 配置 MassTransit 使用 RabbitMQ
    x.UsingRabbitMq((context, config) =>
    {
        config.Host("localhost", "/", h =>
        {
            h.Username("guest");
            h.Password("guest");
        });
        
        // 註冊消費者
        config.ReceiveEndpoint("order-created-event", e =>
        {
            e.ConfigureConsumer<OrderCreatedConsumer>(context);
        });
    });
});
builder.Services.AddControllers();
```

 

完成之後應該就可以，試著尻 API 

```plaintext
curl -X 'POST' `
 'https://localhost:7293/api/Orders' `
 -H 'Content-Type: application/json' `
 -d '{
 "totalAmount": 2
}'
```

 

結果如下

```plaintext
PS C:\Users\yao> curl -X 'POST' `
>>   'https://localhost:7293/api/Orders' `
>>   -H 'Content-Type: application/json' `
>>   -d '{
>>   "totalAmount": 2
>> }'
Order created with ID: edc992db-3e78-4d79-8d17-5ac42f46a758
```

 

## 生產者與消費者分開

上一個簡單的例子是把生產者跟消費者放在同一個專案，沒意外的話，真實的案場，兩者應該都是分開的

### 生產者(Producer)

ISendEndpoint：提供了 Send 方法，用於發送命令，由特定的消費者接收。
IPublishEndpoint：提供了 Publish 方法，用事件廣播，有訂閱的消費者都可以接收。

 

發送命令有幾種寫法

透過 DI Container 註冊後，建構子開一個洞讓它依賴以下

- IBus
- ISendEndpointProvider

#### ISendEndpointProvider

```cs
public class MessageSenderService : IHostedService
{
    private readonly ISendEndpointProvider _sendEndpointProvider;

    public MessageSenderService(ISendEndpointProvider sendEndpointProvider)
    {
        this._sendEndpointProvider = sendEndpointProvider;
    }

    public async Task StartAsync(CancellationToken cancellationToken)
    {
        // 取得 SendEndpoint 並發送訊息到指定佇列
        // var address = new Uri("queue:order-submitted-queue");
        var address = new Uri("rabbitmq://localhost/order-submitted-queue");
        var sendEndpoint =
            await this._sendEndpointProvider.GetSendEndpoint(address);

        var message = new OrderSubmitted
        {
            OrderId = Guid.NewGuid(),
            Timestamp = DateTime.UtcNow
        };
        await sendEndpoint.Send(message, cancellationToken);

        Console.WriteLine("OrderSubmitted event sent to order-submitted-queue.");
    }

    public Task StopAsync(CancellationToken cancellationToken)
    {
        return Task.CompletedTask;
    }
}
```

 

#### IBus

```cs
public class MessageSenderService2 : IHostedService
{
    private readonly IBus _bus;

    public MessageSenderService2(IBus bus)
    {
        this._bus = bus;
    }

    public async Task StartAsync(CancellationToken cancellationToken)
    {
        // 使用 Publish 發佈事件，所有訂閱者都能接收此事件
        var orderSubmitted = new OrderSubmitted
        {
            OrderId = Guid.NewGuid(),
            Timestamp = DateTime.UtcNow
        };

        // ===Publish===
        // await this._bus.Publish(orderSubmitted, cancellationToken);
        // Console.WriteLine("OrderSubmitted event published.");

        // ===Send===
        // EndpointConvention.Map<OrderSubmitted>(new Uri("queue:order-submitted-queue"));
        EndpointConvention.Map<OrderSubmitted>(new Uri("rabbitmq://localhost/order-submitted-queue"));

        await this._bus.Send(orderSubmitted, cancellationToken);
        Console.WriteLine("OrderSubmitted event sent.");
    }

    public Task StopAsync(CancellationToken cancellationToken)
    {
        return Task.CompletedTask;
    }
}
```

 

#### IBusControl

IBusControl 實作 IBus，除了可以透過 DI Container 之外，也可以自行建立執行個體

```cs
public class MessagePublishService4 : IHostedService
{
    public async Task StartAsync(CancellationToken cancellationToken)
    {
        var busControl = Bus.Factory.CreateUsingRabbitMq(config =>
        {
            config.Host("rabbitmq://localhost", h =>
            {
                h.Username("guest");
                h.Password("guest");
            });
        });
        await busControl.StartAsync(cancellationToken);
        
        var orderSubmitted = new OrderSubmitted
        {
            OrderId = Guid.NewGuid(),
            Timestamp = DateTime.UtcNow
        };

        // 發佈事件
        await busControl.Publish(new OrderSubmitted
        {
            OrderId = Guid.NewGuid(),
            Timestamp = DateTime.UtcNow
        }, cancellationToken); 

        // ===Publish===
        // 使用 Publish 發佈事件，所有訂閱者都能接收此事件
        await busControl.Publish(orderSubmitted, cancellationToken);
        Console.WriteLine("OrderSubmitted event published.");

        // ===Send===
        EndpointConvention.Map<OrderSubmitted>(new Uri("rabbitmq://localhost/order-submitted-queue"));
        await busControl.Send(orderSubmitted, cancellationToken);
        Console.WriteLine("OrderSubmitted event sent.");
    }

    public Task StopAsync(CancellationToken cancellationToken)
    {
        return Task.CompletedTask;
    }
}
```

 

#### ConsumeContext

或者是在消費者端再次發送訊息，ConsumeContext 可以 Send 也可以 Publish

```cs
public class OrderSubmittedConsumer : IConsumer<OrderSubmitted>
{
    public async Task Consume(ConsumeContext<OrderSubmitted> context)
    {
        var destinationAddress = new Uri("rabbitmq://localhost/order-submitted-queue");
        var command = new OrderSubmitted()
        {
            OrderId = context.Message.OrderId,
            Timestamp = context.Message.Timestamp
        };
       
        await context.Send(destinationAddress, command);
        // var endpoint = await context.GetSendEndpoint(destinationAddress);
        // await endpoint.Send(command);

        Console.WriteLine($"Order received: {context.Message.OrderId} at {context.Message.Timestamp}");
    }
}
```

注意：上面這個例子，會造成無窮迴圈

 

### 消費者(Consumer)

Consumer，消費者用來消化消息，消費者可以訂閱某一個生產者的命令 queue，也可以訂閱生產者的廣播訊息，在  Hosting 配置好接收路徑，以及收到訊息要做甚麼事，基本上就設定好了。

```cs
public static async Task Main(string[] args)
{
    var host = Host.CreateDefaultBuilder(args)
        .ConfigureServices((hostContext, services) =>
        {
            services.AddMassTransit(x =>
            {
                x.AddConsumer<OrderSubmittedConsumer>();

                x.UsingRabbitMq((context, config) =>
                {
                    config.Host("rabbitmq://localhost", h =>
                    {
                        h.Username("guest");
                        h.Password("guest");
                    });

                    // 設置接收端點，並消費 `OrderSubmitted`
                    config.ReceiveEndpoint("order-submitted-queue", endpoint =>
                    {
                        endpoint.ConfigureConsumer<OrderSubmittedConsumer>(context);
                    });
                });
            });
        })
        .Build();
    try
    {
        Console.WriteLine("Listening for OrderSubmitted events...");
        await host.RunAsync();
    }
    finally
    {
        await host.StopAsync();
    }
}
```

 

```cs
public class OrderSubmittedConsumer : IConsumer<OrderSubmitted>
{
    public async Task Consume(ConsumeContext<OrderSubmitted> context)
    {

        Console.WriteLine($"Order received: {context.Message.OrderId} at {context.Message.Timestamp}");
    }
}
```

 

## 案例位置

[sample.dotblog/Event Bus/MassTransit/Lab.MassTransit at 4549713ed44b723b6d68111a947b0a83d4bae9e0 · yaochangyu/sample.dotblog](https://github.com/yaochangyu/sample.dotblog/tree/4549713ed44b723b6d68111a947b0a83d4bae9e0/Event%20Bus/MassTransit/Lab.MassTransit)

---

---

## 健康檢查

配置 RabbitMQ 健康檢查的參數，以確保你的應用程序能夠正確地連接到 RabbitMQ

安裝套件

```plaintext
dotnet add package AspNetCore.HealthChecks.Rabbitmq
dotnet add package AspNetCore.HealthChecks.UI.Client
```

在 `Program.cs` 中添加 Health Check

```cs
// Health Check
builder.Services.AddHealthChecks()
    .AddRabbitMQ(rabbitConnectionString: "amqp://guest:guest@localhost:5672",
                 name: "rabbitmq",
                 failureStatus: Microsoft.Extensions.Diagnostics.HealthChecks.HealthStatus.Degraded,
                 tags: new string[] { "ready", "live" });
```


```cs
// Health Check
app.MapHealthChecks("/health", new HealthCheckOptions()
{
    // 設定格式
    ResponseWriter = UIResponseWriter.WriteHealthCheckUIResponse
});
```

啟動應用程序，然後在瀏覽器中訪問 `https://localhost:7016/health`，應該可以看到類似下面的畫面

```json
{
    "status": "Healthy",
    "totalDuration": "00:00:00.0490208",
    "entries": {
        "masstransit-bus": {
            "data": {
                "Endpoints": {
                    "rabbitmq://localhost/order-created-event": {
                        "status": "Healthy",
                        "description": "ready"
                    },
                    "rabbitmq://localhost/DESKTOPD81FR0E_KHLabMassTransitLab_bus_ztkoyynje91qxehkbdqxtp9jri?temporary=true": {
                        "status": "Healthy",
                        "description": "ready (not started)"
                    }
                }
            },
            "description": "Ready",
            "duration": "00:00:00.0428675",
            "status": "Healthy",
            "tags": [
                "ready",
                "masstransit"
            ]
        },
        "rabbitmq": {
            "data": {},
            "duration": "00:00:00.0420492",
            "status": "Healthy",
            "tags": [
                "ready",
                "live"
            ]
        }
    }
}
```