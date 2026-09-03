---
kind: original
---

# MediatR Notification (Publish) 與 Behaviors 範例

## 專案設定

bash

```bash
dotnet add package MediatR
dotnet add package MediatR.Extensions.Microsoft.DependencyInjection  # MediatR 11 以下需要
```

csharp

```csharp
// Program.cs (.NET 8)
builder.Services.AddMediatR(cfg => {
    cfg.RegisterServicesFromAssembly(Assembly.GetExecutingAssembly());
    
    // 註冊 Pipeline Behaviors（順序很重要）
    cfg.AddBehavior(typeof(IPipelineBehavior<,>), typeof(LoggingBehavior<,>));
    cfg.AddBehavior(typeof(IPipelineBehavior<,>), typeof(ValidationBehavior<,>));
    cfg.AddBehavior(typeof(IPipelineBehavior<,>), typeof(PerformanceBehavior<,>));
});
```

------

## 1. Notification (發布/訂閱模式)

Notification 是「一對多」的事件通知，一個事件可以有多個 Handler。

### 定義 Notification

csharp

```csharp
// 訂單建立事件
public record OrderCreatedNotification(
    int OrderId,
    string CustomerName,
    decimal TotalAmount,
    DateTime CreatedAt
) : INotification;
```

### 定義多個 Handler

csharp

```csharp
// Handler 1：發送電子郵件
public class SendOrderConfirmationEmailHandler 
    : INotificationHandler<OrderCreatedNotification>
{
    private readonly ILogger<SendOrderConfirmationEmailHandler> _logger;
    private readonly IEmailService _emailService;

    public SendOrderConfirmationEmailHandler(
        ILogger<SendOrderConfirmationEmailHandler> logger,
        IEmailService emailService)
    {
        _logger = logger;
        _emailService = emailService;
    }

    public async Task Handle(OrderCreatedNotification notification, CancellationToken cancellationToken)
    {
        _logger.LogInformation("發送訂單確認信給 {Customer}", notification.CustomerName);
        
        await _emailService.SendAsync(
            to: $"{notification.CustomerName}@example.com",
            subject: $"訂單 #{notification.OrderId} 已建立",
            body: $"您的訂單金額為 {notification.TotalAmount:C}"
        );
    }
}

// Handler 2：更新庫存
public class UpdateInventoryHandler 
    : INotificationHandler<OrderCreatedNotification>
{
    private readonly ILogger<UpdateInventoryHandler> _logger;
    private readonly IInventoryService _inventoryService;

    public UpdateInventoryHandler(
        ILogger<UpdateInventoryHandler> logger,
        IInventoryService inventoryService)
    {
        _logger = logger;
        _inventoryService = inventoryService;
    }

    public async Task Handle(OrderCreatedNotification notification, CancellationToken cancellationToken)
    {
        _logger.LogInformation("更新訂單 {OrderId} 的庫存", notification.OrderId);
        await _inventoryService.DeductStockAsync(notification.OrderId, cancellationToken);
    }
}

// Handler 3：寫入審計日誌
public class AuditOrderCreatedHandler 
    : INotificationHandler<OrderCreatedNotification>
{
    private readonly IAuditService _auditService;

    public AuditOrderCreatedHandler(IAuditService auditService)
    {
        _auditService = auditService;
    }

    public async Task Handle(OrderCreatedNotification notification, CancellationToken cancellationToken)
    {
        await _auditService.LogAsync(new AuditEntry
        {
            Action = "OrderCreated",
            EntityId = notification.OrderId.ToString(),
            Timestamp = notification.CreatedAt
        });
    }
}
```

### Command + 發布 Notification

csharp

```csharp
// Command
public record CreateOrderCommand(
    string CustomerName,
    List<OrderItem> Items
) : IRequest<int>;

// Command Handler：處理完業務邏輯後發布 Notification
public class CreateOrderCommandHandler : IRequestHandler<CreateOrderCommand, int>
{
    private readonly IOrderRepository _repository;
    private readonly IMediator _mediator;

    public CreateOrderCommandHandler(IOrderRepository repository, IMediator mediator)
    {
        _repository = repository;
        _mediator = mediator;
    }

    public async Task<int> Handle(CreateOrderCommand request, CancellationToken cancellationToken)
    {
        // 1. 建立訂單
        var order = new Order
        {
            CustomerName = request.CustomerName,
            Items = request.Items,
            TotalAmount = request.Items.Sum(i => i.Price * i.Quantity),
            CreatedAt = DateTime.UtcNow
        };

        await _repository.AddAsync(order, cancellationToken);
        await _repository.SaveChangesAsync(cancellationToken);

        // 2. 發布事件，通知所有訂閱者（非同步並行執行）
        await _mediator.Publish(new OrderCreatedNotification(
            order.Id,
            order.CustomerName,
            order.TotalAmount,
            order.CreatedAt
        ), cancellationToken);

        return order.Id;
    }
}
```

------

## 2. Pipeline Behaviors

Behaviors 是 MediatR 的中介層，在 Handler 前後插入邏輯（類似 ASP.NET Core Middleware）。

### Behavior 1：日誌記錄

csharp

```csharp
public class LoggingBehavior<TRequest, TResponse> 
    : IPipelineBehavior<TRequest, TResponse>
    where TRequest : notnull
{
    private readonly ILogger<LoggingBehavior<TRequest, TResponse>> _logger;

    public LoggingBehavior(ILogger<LoggingBehavior<TRequest, TResponse>> logger)
    {
        _logger = logger;
    }

    public async Task<TResponse> Handle(
        TRequest request,
        RequestHandlerDelegate<TResponse> next,
        CancellationToken cancellationToken)
    {
        var requestName = typeof(TRequest).Name;
        
        _logger.LogInformation(">>> 開始處理 {RequestName}: {@Request}", requestName, request);

        var response = await next(); // 呼叫下一個 Behavior 或 Handler

        _logger.LogInformation("<<< 完成處理 {RequestName}", requestName);

        return response;
    }
}
```

### Behavior 2：驗證 (FluentValidation)

bash

```bash
dotnet add package FluentValidation
dotnet add package FluentValidation.DependencyInjectionExtensions
```

csharp

```csharp
// 定義驗證規則
public class CreateOrderCommandValidator : AbstractValidator<CreateOrderCommand>
{
    public CreateOrderCommandValidator()
    {
        RuleFor(x => x.CustomerName)
            .NotEmpty().WithMessage("客戶名稱不能為空")
            .MaximumLength(100).WithMessage("客戶名稱不能超過 100 字");

        RuleFor(x => x.Items)
            .NotEmpty().WithMessage("訂單至少需要一個品項");

        RuleForEach(x => x.Items).ChildRules(item =>
        {
            item.RuleFor(i => i.Quantity).GreaterThan(0);
            item.RuleFor(i => i.Price).GreaterThan(0);
        });
    }
}

// 驗證 Behavior
public class ValidationBehavior<TRequest, TResponse> 
    : IPipelineBehavior<TRequest, TResponse>
    where TRequest : notnull
{
    private readonly IEnumerable<IValidator<TRequest>> _validators;

    public ValidationBehavior(IEnumerable<IValidator<TRequest>> validators)
    {
        _validators = validators;
    }

    public async Task<TResponse> Handle(
        TRequest request,
        RequestHandlerDelegate<TResponse> next,
        CancellationToken cancellationToken)
    {
        if (!_validators.Any())
            return await next();

        var context = new ValidationContext<TRequest>(request);
        
        var failures = _validators
            .Select(v => v.Validate(context))
            .SelectMany(r => r.Errors)
            .Where(f => f != null)
            .ToList();

        if (failures.Any())
            throw new ValidationException(failures);

        return await next();
    }
}
```

### Behavior 3：效能監控

csharp

```csharp
public class PerformanceBehavior<TRequest, TResponse> 
    : IPipelineBehavior<TRequest, TResponse>
    where TRequest : notnull
{
    private const int SlowRequestThresholdMs = 500;
    private readonly ILogger<PerformanceBehavior<TRequest, TResponse>> _logger;

    public PerformanceBehavior(ILogger<PerformanceBehavior<TRequest, TResponse>> logger)
    {
        _logger = logger;
    }

    public async Task<TResponse> Handle(
        TRequest request,
        RequestHandlerDelegate<TResponse> next,
        CancellationToken cancellationToken)
    {
        var sw = Stopwatch.StartNew();
        
        var response = await next();
        
        sw.Stop();

        if (sw.ElapsedMilliseconds > SlowRequestThresholdMs)
        {
            _logger.LogWarning(
                "⚠️ 慢請求警告 [{ElapsedMs}ms] {RequestName}: {@Request}",
                sw.ElapsedMilliseconds,
                typeof(TRequest).Name,
                request);
        }

        return response;
    }
}
```

### Behavior 4：交易管理（Transaction）

csharp

~~~csharp
public class TransactionBehavior<TRequest, TResponse> 
    : IPipelineBehavior<TRequest, TResponse>
    where TRequest : ITransactionalRequest  // 自訂 marker interface
{
    private readonly AppDbContext _dbContext;
    private readonly ILogger<TransactionBehavior<TRequest, TResponse>> _logger;

    public TransactionBehavior(AppDbContext dbContext, ILogger<TransactionBehavior<TRequest, TResponse>> logger)
    {
        _dbContext = dbContext;
        _logger = logger;
    }

    public async Task<TResponse> Handle(
        TRequest request,
        RequestHandlerDelegate<TResponse> next,
        CancellationToken cancellationToken)
    {
        await using var transaction = await _dbContext.Database.BeginTransactionAsync(cancellationToken);
        
        try
        {
            _logger.LogDebug("開始交易 {RequestName}", typeof(TRequest).Name);
            
            var response = await next();
            
            await transaction.CommitAsync(cancellationToken);
            _logger.LogDebug("提交交易成功");
            
            return response;
        }
        catch (Exception ex)
        {
            await transaction.RollbackAsync(cancellationToken);
            _logger.LogError(ex, "交易回滾 {RequestName}", typeof(TRequest).Name);
            throw;
        }
    }
}

// Marker interface
public interface ITransactionalRequest { }

// 套用到 Command
public record CreateOrderCommand(...) : IRequest<int>, ITransactionalRequest;
```

---

## 3. 完整 Pipeline 執行流程圖
```
HTTP Request
    │
    ▼
Controller.CreateOrder()
    │
    ▼ mediator.Send(CreateOrderCommand)
    │
    ├──► LoggingBehavior.Before        ← 記錄進入
    │       ├──► ValidationBehavior    ← 驗證資料
    │       │       ├──► PerformanceBehavior.Start  ← 開始計時
    │       │       │       ├──► TransactionBehavior.Begin  ← 開啟交易
    │       │       │       │       └──► CreateOrderCommandHandler.Handle()
    │       │       │       │               └── mediator.Publish(OrderCreatedNotification)
    │       │       │       │                       ├── SendEmailHandler
    │       │       │       │                       ├── UpdateInventoryHandler
    │       │       │       │                       └── AuditOrderCreatedHandler
    │       │       │       └──► TransactionBehavior.Commit
    │       │       └──► PerformanceBehavior.Stop   ← 計算耗時
    │       └──► (驗證失敗則 throw)
    └──► LoggingBehavior.After         ← 記錄完成
~~~

------

## 4. 在 Controller 使用

csharp

```csharp
[ApiController]
[Route("api/[controller]")]
public class OrdersController : ControllerBase
{
    private readonly IMediator _mediator;

    public OrdersController(IMediator mediator) => _mediator = mediator;

    [HttpPost]
    public async Task<IActionResult> Create([FromBody] CreateOrderCommand command)
    {
        var orderId = await _mediator.Send(command);
        return CreatedAtAction(nameof(GetById), new { id = orderId }, new { orderId });
    }
}
```

------

## 重點整理

| 概念                | 說明                     | 適用場景                       |
| ------------------- | ------------------------ | ------------------------------ |
| `IRequest<T>`       | 一對一，有回傳值         | Query / Command                |
| `INotification`     | 一對多，無回傳值         | 事件通知（Email、Log、庫存）   |
| `IPipelineBehavior` | 包裹所有 Request         | 跨切面邏輯（驗證、日誌、交易） |
| Publish 順序        | 預設循序執行，可自訂並行 | 多個 Handler 時注意相依性      |

若需要 **並行執行** Notification Handlers，可自訂 `IMediator` 實作或使用 `ParallelNoWaitPublishStrategy`。