---
kind: reprint
source: https://github.com/CI-YU/2022-ITHelp/tree/main/MailKitExample
author: CI-YU
---

# .NET 6 MailKit範例

### 目的

使用gmail寄信

### 建立新專案

選擇ASP.NET Core Web API專案範本，並執行下一步
![步驟1](https://user-images.githubusercontent.com/19286751/143255617-9964a993-becd-414b-aba2-632e99dd985d.png)

### 設定新的專案

命名你的專案名稱，並選擇專案要存放的位置。
![步驟2](https://user-images.githubusercontent.com/19286751/163670709-0989cdef-de26-44d5-b2f8-1e68d70767d6.png)

### 其他資訊

直接進行下一步
![步驟3](https://user-images.githubusercontent.com/19286751/148767425-ef0c8469-3d95-4f86-87ca-1c47c5cd0791.png)

### NuGet加入套件

- Google.Apis.Auth(使用google信箱時需要做oauth驗證才可以使用)
- MailKit(寄信)

![步驟4](https://user-images.githubusercontent.com/19286751/167292013-1a27880d-da28-4124-abf6-105c67e4144c.png)

### 編輯WeatherForecastController檔案

將預設的API註解
![步驟5-1](https://user-images.githubusercontent.com/19286751/154978191-e218edc4-5df3-49ad-9b7b-c4ddfa9fcdb1.png)

```c#
[HttpGet("SendEmail")]
    public async Task<IActionResult> Get() {
      #region OAuth驗證
      const string GMailAccount = "前置作業文章打上去的測試帳號";

      var clientSecrets = new ClientSecrets {
        ClientId = "前置作業文章最後給的用戶ID",
        ClientSecret = "前置作業文章最後給的用戶端密碼"
      };

      var codeFlow = new GoogleAuthorizationCodeFlow(new GoogleAuthorizationCodeFlow.Initializer  {
        DataStore = new FileDataStore("CredentialCacheFolder", false),
        Scopes = new[] { "https://mail.google.com/" },
        ClientSecrets = clientSecrets
      });

      var codeReceiver = new LocalServerCodeReceiver();
      var authCode = new AuthorizationCodeInstalledApp(codeFlow, codeReceiver);

      var credential = await authCode.AuthorizeAsync(GMailAccount, CancellationToken.None);

      if (credential.Token.IsExpired(SystemClock.Default))
        await credential.RefreshTokenAsync(CancellationToken.None);

      var oauth2 = new SaslMechanismOAuth2(credential.UserId, credential.Token.AccessToken);
      #endregion

      #region 信件內容
      var message = new MimeMessage();
      //寄件者名稱及信箱(信箱是測試帳號)
      message.From.Add(new MailboxAddress("bill", "xxxx@gmail.com"));
      //收件者名稱，收件者信箱
      message.To.Add(new MailboxAddress("billhuang", "xxxx@gmail.com"));
      //信件標題
      message.Subject = "How you doing'?";
      //信件內容
      message.Body = new TextPart("plain") {
        Text = @"This is test"
      };
      using (var client = new SmtpClient()) {
        await client.ConnectAsync("smtp.gmail.com", 587);
        await client.AuthenticateAsync(oauth2);
        await client.SendAsync(message);
        await client.DisconnectAsync(true);
      } 
      #endregion

      return Ok("OK");
    }
```

![步驟5-2](https://user-images.githubusercontent.com/19286751/167293076-92e833cd-c1a3-44fa-bb14-ae24ee3a3923.png)

### 執行結果

F5執行後，依照下列步驟操作，最後看到OK後，就可以去信箱確認有沒有收到信了。
![步驟6-1](https://user-images.githubusercontent.com/19286751/167293129-4e335003-0428-4795-af8d-fc7f17d7d0cf.png)

![步驟6-2](https://user-images.githubusercontent.com/19286751/167293158-388d7e9a-980d-4a56-95c8-9bb2cf9d8e5a.png)

![步驟6-3](https://user-images.githubusercontent.com/19286751/167293189-e1c4a5b6-130c-4126-925a-cc2c348e5119.png)

MailKit為基於MimeKit解析器的客戶端函式庫 MimeKit為解析器，用於解析電子郵件格式

### 參考

[官方網站](https://github.com/jstedfast/MailKit) [官方GmailOauth2範例](https://github.com/jstedfast/MailKit/blob/master/GMailOAuth2.md) [Gmail教學](https://www.796t.com/post/MWg2NWc=.html)

### 範例檔

[GitHub](https://github.com/CI-YU/2022-ITHelp/tree/main/MailKitExample)