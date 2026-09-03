---
kind: original
---

# LinePay  支付完成後返回 LINE 應用而不跳出外部瀏覽器

.NET 開發 LINE LIFF 和 LINE Pay 整合的應用，並希望支付完成後返回 LINE 應用而不跳出外部瀏覽器，可以根據以下步驟進行調整：

### 1. 使用內嵌結帳模式

在 .NET 中使用 LINE Pay API 時，可以通過設置 API 請求的參數來控制支付流程。內嵌結帳模式允許用戶在 LINE 應用內完成支付，而無需跳出到外部瀏覽器。

#### 1.1 設定支付請求中的 `capture` 參數

在呼叫 LINE Pay API 的 `.NET` 程式碼中，設置 `capture` 或 `confirm` 為 `false`，然後進行後續支付流程控制。這樣可以啟用「內嵌結帳」模式：

```csharp
var requestBody = new
{
    amount = 1000,
    currency = "JPY",
    orderId = "order12345",
    packages = new[]
    {
        new
        {
            id = "package123",
            amount = 1000,
            name = "Sample Package",
            products = new[]
            {
                new { id = "product123", name = "Sample Product", quantity = 1, price = 1000 }
            }
        }
    },
    redirectUrls = new
    {
        confirmUrl = "https://yourdomain.com/linepay/confirm",
        cancelUrl = "https://yourdomain.com/linepay/cancel"
    },
    options = new
    {
        payment = new { capture = false } // 開啟內嵌結帳模式
    }
};

// 呼叫 LINE Pay API（假設已經建立 HttpClient）
var content = new StringContent(JsonConvert.SerializeObject(requestBody), Encoding.UTF8, "application/json");
var response = await httpClient.PostAsync("https://api-pay.line.me/v3/payments/request", content);
```

### 2. 設置回調 URL 回到 LIFF 應用

支付完成後，可以使用 LIFF 協議 `liff://app/{LIFF_ID}` 作為 `confirmUrl`，這樣用戶在支付完成後會返回到 LIFF 頁面而不是啟動外部瀏覽器。

#### 2.1 設置 `confirmUrl` 參數

當建立支付請求時，將 `redirectUrls.confirmUrl` 設置為 LIFF 應用的 URL：

```csharp
var requestBody = new
{
    amount = 1000,
    currency = "JPY",
    orderId = "order12345",
    packages = new[]
    {
        new
        {
            id = "package123",
            amount = 1000,
            name = "Sample Package",
            products = new[]
            {
                new { id = "product123", name = "Sample Product", quantity = 1, price = 1000 }
            }
        }
    },
    redirectUrls = new
    {
        confirmUrl = "liff://app/YOUR_LIFF_ID", // 導回 LIFF 應用的 URL
        cancelUrl = "https://yourdomain.com/linepay/cancel"
    }
};
```

這樣，當用戶完成支付後會直接返回到 LIFF 頁面而不會啟動外部瀏覽器。

### 3. 使用 .NET API 來確認支付

支付完成後，可以在您的 .NET 應用中確認支付結果並返回支付狀態給 LIFF 應用。可以設置一個 API 端點來接收支付狀態，並在 LIFF 中用 JavaScript 呼叫此端點檢查支付狀態。

```csharp
[ApiController]
[Route("linepay")]
public class LinePayController : ControllerBase
{
    [HttpGet("confirm")]
    public async Task<IActionResult> ConfirmPayment([FromQuery] string transactionId)
    {
        // 確認支付狀態的邏輯
        var requestBody = new
        {
            amount = 1000,
            currency = "JPY"
        };
        
        var content = new StringContent(JsonConvert.SerializeObject(requestBody), Encoding.UTF8, "application/json");
        var response = await httpClient.PostAsync($"https://api-pay.line.me/v3/payments/{transactionId}/confirm", content);
        
        if (response.IsSuccessStatusCode)
        {
            return Ok(new { status = "success" });
        }
        return BadRequest(new { status = "failed" });
    }
}
```

### 4. 在 LIFF 中自動檢查支付結果

支付完成返回到 LIFF 頁面後，可以使用 JavaScript 自動檢查支付狀態並顯示結果。

```javascript
// 確認付款狀態的 API URL
const confirmUrl = 'https://yourdomain.com/linepay/confirm';

async function checkPaymentStatus(transactionId) {
  try {
    const response = await fetch(`${confirmUrl}?transactionId=${transactionId}`);
    const data = await response.json();
    if (data.status === 'success') {
      alert('付款成功');
    } else {
      alert('付款失敗');
    }
  } catch (error) {
    console.error('檢查付款狀態時發生錯誤', error);
  }
}

// 在頁面加載完成後檢查付款狀態
document.addEventListener('DOMContentLoaded', () => {
  const transactionId = getTransactionIdFromUrl(); // 從 URL 中取得 transactionId
  if (transactionId) {
    checkPaymentStatus(transactionId);
  }
});
```

這樣可以在支付完成後，讓用戶自動回到 LINE 應用中的 LIFF 畫面並檢查支付結果。