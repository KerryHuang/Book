---
kind: original
---

# Spectre.Console

在 .NET 中，**Spectre.Console** 是一個用來建構豐富命令列應用程式的套件。這個套件提供了許多工具和功能，可以幫助開發者在命令列中呈現更具吸引力的視覺效果，例如表格、進度條、圖表、樹狀結構和文字樣式等。這對於需要在命令列介面上提供更佳使用者體驗的應用程式非常有用。

### 主要功能

Spectre.Console 提供的功能包括：

1. **文字樣式**：讓你可以使用不同顏色、字體樣式（如粗體、斜體、底線）來格式化文字。
2. **表格**：快速建立和格式化表格，使資料展示更具條理性。
3. **進度條**：適合用來展示長時間執行操作的進度，例如下載檔案或執行批次處理。
4. **樹狀結構**：用來顯示層次結構，特別適合用於展示目錄或分層的資料結構。
5. **提示和訊息框**：支援提示框、警告框、錯誤框等，便於在命令列中提供更友善的使用者回饋。
6. **選單**：建立互動式選單，讓使用者在命令列中進行選擇。
7. **圖表**：支援簡單的長條圖，用來展示資料。

### 安裝方式

可以通過 NuGet 安裝 Spectre.Console 套件：

```shell
dotnet add package Spectre.Console
```

### 使用範例

#### 1. 格式化文字

```csharp
using Spectre.Console;

AnsiConsole.Markup("[bold red]Hello, World![/]");
```

#### 2. 建立表格

```csharp
var table = new Table();
table.AddColumn("Name");
table.AddColumn("Age");

table.AddRow("Alice", "30");
table.AddRow("Bob", "25");

AnsiConsole.Write(table);
```

#### 3. 顯示進度條

```csharp
AnsiConsole.Progress()
    .Start(ctx => {
        var task = ctx.AddTask("[green]Processing...[/]");
        while (!task.IsFinished)
        {
            task.Increment(10);
            Thread.Sleep(500);
        }
    });
```

Spectre.Console 讓命令列應用程式更具互動性和視覺效果，特別適合開發 CLI 工具、系統管理指令碼、或任何需要在命令列中與使用者互動的應用程式。