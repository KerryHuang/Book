---
kind: reprint
source: https://github.com/CI-YU/2022-ITHelp/tree/main/TelegramBotExample
author: CI-YU
---

# .NET 6 Telegram.Bot範例

### 目的

使用telegram做聊天機器人

### 建立新專案

選擇ASP.NET Core Web API專案範本，並執行下一步
![步驟1](https://user-images.githubusercontent.com/19286751/143255617-9964a993-becd-414b-aba2-632e99dd985d.png)

### 設定新的專案

命名你的專案名稱，並選擇專案要存放的位置。
![步驟2](https://user-images.githubusercontent.com/19286751/185736387-f949c425-98e2-4da5-9074-44680824fdcb.png)

### 其他資訊

直接進行下一步
![步驟3](https://user-images.githubusercontent.com/19286751/148767425-ef0c8469-3d95-4f86-87ca-1c47c5cd0791.png)

### NuGet加入套件

- Telegram.Bot
- ![步驟4](https://user-images.githubusercontent.com/19286751/185736688-0a078210-5460-44c1-8238-657811f83b20.png)

### 編輯WeatherForecastController檔案

- 將預設的API註解
![步驟5-1](https://user-images.githubusercontent.com/19286751/154978191-e218edc4-5df3-49ad-9b7b-c4ddfa9fcdb1.png)

- 寫新的對外API

```c#
    [HttpGet("Test")]
    public async Task<string> Test() {
      var botClient = new TelegramBotClient("前置作業給的機器人ID");
      //取得機器人基本資訊
      var me = await botClient.GetMeAsync();
      //發送訊息到指定頻道
      Message message = await botClient.SendTextMessageAsync(
            chatId: "前置作業給的頻道ID",
            text: "Trying *all the parameters* of `sendMessage` method");
      //回傳取得的機器人基本資訊
      return $"Hello, World! I am user {me.Id} and my name is {me.FirstName}.";
    }
```

![步驟5-2](https://user-images.githubusercontent.com/19286751/185796426-63bc64b0-b5bb-4d3e-b838-867457a3e420.png)

### 執行結果

F5執行後，依照下列步驟操作，並確認結果
![步驟6-1](https://user-images.githubusercontent.com/19286751/154981306-58a41739-acac-448d-851f-b7d3666999b1.png)

![步驟6-2](https://user-images.githubusercontent.com/19286751/154981450-28bd0211-3653-4b03-9ab3-877b060deb97.png)

![步驟6-3](https://user-images.githubusercontent.com/19286751/185796900-cc33c1bd-778f-46fb-9d23-d7f0bc91432d.png)

就可以看到telegram的機器人有發送一個訊息
![步驟6-4](https://user-images.githubusercontent.com/19286751/185796931-3b654dcf-6aa2-4a89-8a2c-332fb0d52761.png)

### 參考

[官方文件](https://telegrambots.github.io/book/1/quickstart.html) [holey’s Blog](https://blog.holey.cc/2017/08/30/csharp-send-messages-by-telegram-bot/)

### 範例檔[#](https://www.ci-yu.top/dotnet/鐵人賽-net6-telegram.bot範例/#範例檔)

[GitHub](https://github.com/CI-YU/2022-ITHelp/tree/main/TelegramBotExample)