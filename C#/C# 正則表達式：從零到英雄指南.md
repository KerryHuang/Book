# C# 正則表達式：從零到英雄指南

## 讀完本文你就會明白“^(?=.*[az])(?=.*[AZ])(?=.*).*”是什麼意思😎👍

![img](https://miro.medium.com/v2/resize:fit:875/1*MIdw9bQ9DZTK6t03bVWRFw.png)

# C# 正則表達式簡介：為什麼它是文本操作的強大工具

在深入了解正則表達式的神奇世界之前，我們先了解一下為什麼使用 C# Regex 很重要，以及它如何提高開發人員的工作效率。

在本節中，我們將介紹正則表達式的基礎知識、語法和關鍵元素，以幫助您入門。

## 什麼是 C# 正則表達式以及為什麼應該學習它

C# Regex（或 C# 中的正則表達式）是一個功能強大的工具，允許您通過搜索、匹配和替換文本中的模式來操作文本數據。

它有助於解決大量與文本相關的任務，例如表單驗證、數據提取和文本轉換。

掌握 C# 正則表達式將使您成為更高效的開發人員，並讓您能夠輕鬆處理複雜的文本操作任務。

## C# 中的正則表達式：簡要概述

正則表達式是一種用於指定文本數據模式的語言。它就像您熟悉的通配符功能的超級版本，但更強大、更靈活。

在 C# 中，您無需擔心包含任何特殊庫，因為 Regex 是原生支持的。命名`System.Text.RegularExpressions`空間包含`Regex`類，該類提供在 C# 中使用正則表達式所需的所有工具。

# .NET Regex 的強大功能：終極字符串搜索模式工具

.NET Regex 引擎不僅高效且廣泛使用，而且還支持廣泛的功能集。告別冗長、容易出錯的字符串操作代碼。

掌握 C# Regex 的強大功能將幫助您創建更準確、簡潔且高效的字符串搜索模式，從而使您的應用程序更加可靠和健壯。

## C# 中的正則表達式入門：基本構建塊

要在 C# 中有效使用正則表達式，必須了解語法和構建塊。

在本節中，我們將介紹 C# 正則表達式語法的基礎知識、匹配、捕獲和替換文本的關鍵元素，並為您提供一個開始使用匹配模式的示例。

## 了解 C# 正則表達式語法

正則表達式有自己的語法，一開始可能會令人生畏。但不要害怕！通過練習和一點耐心，您將開始看到這種簡潔而富有表現力的語言的美感。以下是您需要了解的一些語法元素的快速概述：

- `^`: 表示一行的開始。
- `$`: 表示一行的結束。
- `.`：匹配除換行符之外的任何字符。
- `*`：匹配前面的元素0次或多次。
- `+`：匹配前面的元素1次或多次。
- `{n}`：精確匹配前一個元素出現的 n 次。
- `[abc]`：匹配字符a、b或c中的任意一個。
- `(abc)`：將括號內的表達式分組並將它們視為單個元素。

這只是冰山一角！隨著您在正則表達式之旅中取得進展，您將發現更多高級元素來創建更強大的搜索模式。

## 關鍵正則表達式 C# 元素：匹配、捕獲和替換

在 C# 中使用正則表達式從三個基本技術開始：匹配、捕獲和替換。匹配涉及查找輸入文本中是否存在模式，而捕獲則超越匹配範圍並提取匹配的文本以進行進一步處理。顧名思義，替換涉及更改匹配的文本並用新內容替換它。

例如，假設您有一個電子郵件地址[列表](https://www.bytehide.com/blog/list-csharp/)，並且想要從中提取用戶名（@ 符號之前的部分）。下面是一個簡單的 C# 正則表達式示例，演示了三種技術的實際應用：

```c#
using System;
using System.Text.RegularExpressions;

class MainClass
{
    public static void Main(string[] args)
    {
        string input = "alice@example.com, bob@example.com, carol@example.com";
        string pattern = @"([\w]+)@";
        // Matching and Capturing
        MatchCollection matches = Regex.Matches(input, pattern);
        foreach (Match match in matches)
        {
            Console.WriteLine(match.Groups[1].Value); // Extract the captured group (username)
        }
        // Replacing
        string replaced = Regex.Replace(input, pattern, "$1 is at ");
        Console.WriteLine(replaced);
    }
}
```

此代碼片段演示瞭如何：

1. 使用正則表達式匹配並捕獲用戶名`([\\w]+)@`
2. 在循環中提取捕獲的組（用戶名）
3. 將電子郵件地址替換為修改後的版本，以便電子郵件地址顯示為“用戶名位於 example.com”

## 正則表達式 C# 匹配：C# 中準確匹配的重要性

準確匹配是 C# 中正則表達式使用的關鍵。不正確的模式可能會導致應用程序中出現錯誤和問題，因此深入掌握正則表達式模式至關重要。

正則表達式可能非常複雜，但通過練習，您將能夠創建精確、高效且易於理解的模式。花時間測試和完善您的正則表達式模式，因為從長遠來看，這將證明是無價的。

## 正則表達式匹配 C# 示例：開始匹配的基本代碼

為了讓您在掌握 C# 正則表達式中的匹配方面取得先機，這裡有一個基本示例，演示如何將正則表達式模式與輸入字符串進行匹配：

```c#
using System;
using System.Text.RegularExpressions;

class MainClass
{
    public static void Main(string[] args)
    {
        string input = "Hooray for Regex! It's a match made in code heaven!";
        string pattern = @"\bmatch\b";
        // Check if the word "match" is in the input string
        bool isMatch = Regex.IsMatch(input, pattern);
        Console.WriteLine(isMatch); // Output: True
    }
}
```

在此示例中，我們使用該`Regex.IsMatch`方法檢查輸入字符串中是否存在單詞“match”，然後輸出相應的結果（True/False）。

## C# 正則表達式模式：構建複雜且高效的模式

隨著您獲得 C# 正則表達式的經驗，您將熟悉正則表達式模式的無限潛力。

創建複雜而高效的模式需要理解新的語法元素，以及有效嵌套和組合它們的能力。

繼續練習和探索正則表達式資源，以幫助您構建日益複雜和強大的模式。

# 通過簡單的正則表達式示例掌握 C# 中的正則表達式 C#

為了幫助您在正則表達式之旅中快速取得進展，我們將探討三個示例 - 基礎、中級和高級 - 演示在現實情況下使用 C# 正則表達式。

每個示例都將展示不同的正則表達式概念和技術，幫助您成為真正的正則表達式愛好者。

## 基本 C# 正則表達式示例：用於電子郵件驗證的簡單正則表達式

電子郵件驗證是開發人員遇到的常見任務。以下示例演示了一個基本的正則表達式模式，用於檢查輸入字符串是否是有效的電子郵件地址：

```c#
using System;
using System.Text.RegularExpressions;

class MainClass
{
    public static void Main(string[] args)
    {
        string input = "john.doe@example.com";
        string pattern = @"^\S+@\S+\.\S+$";
        // Check if the input is a valid email address
        bool isValidEmail = Regex.IsMatch(input, pattern);
        Console.WriteLine(isValidEmail); // Output: True
    }
}
```

在此示例中，我們再次使用該`Regex.IsMatch`方法，但使用更複雜的模式來檢查有效的電子郵件格式。

## 中級 C# 正則表達式示例：使用正則表達式進行網頁抓取

此中間示例演示如何使用正則表達式從 HTML 文本塊中提取特定信息。考慮以下示例，該示例從 HTML 頁面中的鏈接列表中提取所有 URL：

```c#
using System;
using System.Text.RegularExpressions;

class MainClass
{
    public static void Main(string[] args)
    {
        string input = @"<a href=""https://www.example.com"">Example 1</a>
                         <a href=""https://www.example2.com"">Example 2</a>
                         <a href=""https://www.example3.com"">Example 3</a>";
        string pattern = @"href=""(https?://\S+?)""";
        // Find and output each URL in the input string
        MatchCollection matches = Regex.Matches(input, pattern);
        foreach (Match match in matches)
        {
            Console.WriteLine(match.Groups[1].Value); // Output: Extracted URL
        }
    }
}
```

在這裡，我們使用該`Regex.Matches`方法查找並捕獲`<a>`輸入字符串中標籤內的所有 URL。然後，提取的 URL 將打印到控制台。

## 高級 C# 正則表達式示例：從非結構化文本中提取結構化數據的案例研究

在這個高級示例中，我們將從非結構化文本塊中提取結構化數據：比方說，從類似簡歷的文本中獲取姓名、位置和電子郵件。

```c#
using System;
using System.Text.RegularExpressions;

class MainClass
{
    public static void Main(string[] args)
    {
        string input = @"Name: Jane Smith
                         Location: New York, NY
                         Email: jane.smith@email.com";
        string pattern = @"Name:\s+(?<name>.+)
                           Location:\s+(?<location>.+)
                           Email:\s+(?<email>\S+@\S+\.\S+)";
        RegexOptions options = RegexOptions.Multiline | RegexOptions.IgnorePatternWhitespace;
        Match match = Regex.Match(input, pattern, options);
        if (match.Success)
        {
            Console.WriteLine($"Name: {match.Groups["name"].Value}");
            Console.WriteLine($"Location: {match.Groups["location"].Value}");
            Console.WriteLine($"Email: {match.Groups["email"].Value}");
        }
    }
}
```

`(?<name>...)`在此示例中，採用命名捕獲組（使用）來更輕鬆地提取所需信息。

此外，`RegexOptions.Multiline`和`RegexOptions.IgnorePatternWhitespace`選項分別用於允許多行匹配並忽略模式中的空格。

# C# 正則表達式替換：精確高效地更新文本

高效的文本操作不僅僅涉及查找和捕獲文本。了解如何精確使用 C# 正則表達式替換技術將顯著提高您的文本處理技能。

在本節中，我們將探索 C# 中的正則表達式替換藝術，並深入研究獲得最佳結果的提示和技巧。

## C# 正則表達式替換的藝術：如何像專業人士一樣替換文本

正則表達式替換允許我們根據正則表達式模式修改輸入文本，用新內容替換匹配的文本。這在清理或轉換數據時特別有用。

正則表達式替換提供的強大功能和靈活性將使您立即成為文本操作大師！

## 在 C# 中使用正則表達式替換文本：獲得最佳結果的提示和技巧

以下是在 C# 中使用正則表達式替換來實現最佳結果的一些提示和技巧：

1. `(?:...)`當不需要捕獲匹配的文本時，使用非捕獲組。它使正則表達式模式更加高效和可讀。
2. 使用 regex 替換 lambda 表達式來進行更複雜的替換。
3. 保持正則表達式模式簡潔易讀，以便於維護。

## Regex.Replace C# 示例：實現高級替換規則

假設您有一個包含格式為“yyyy-MM-dd”的日期的字符串，並且需要將它們替換為格式“dd-MM-yyyy”：

```c#
using System;
using System.Text.RegularExpressions;

class MainClass
{
    public static void Main(string[] args)
    {
        string input = "I was born on 2001-05-15 and started my job on 2020-01-01.";
        string pattern = @"(\d{4})-(\d{2})-(\d{2})";
        string replacement = "$3-$2-$1";
        // Replace dates with the new format
        string output = Regex.Replace(input, pattern, replacement);
        Console.WriteLine(output); // Output: I was born on 15-05-2001 and started my job on 01-01-2020.
    }
}
```

在此示例中，我們使用捕獲組創建替換模板，該模板使用所需的模式重新格式化日期字符串。

# .NET 正則表達式基本功能：讓您的 C# 正則表達式更強大

要真正利用 C# 中正則表達式的強大功能，必須掌握內置的 .NET Regex 函數。`Regex.IsMatch`在本節中，我們將介紹、`Regex.Matches`、`Regex.Replace`等關鍵功能，為您提供輕鬆處理最複雜的文本操作任務所需的技能。

## C# Regex IsMatch：快速檢查字符串是否與模式匹配

該`Regex.IsMatch`方法允許您快速檢查輸入字符串是否與正則表達式模式匹配，並返回`bool`表示結果的值。

此函數對於簡單的驗證和模式檢查特別有用。下面的示例確保密碼至少包含一個大寫字母、一個小寫字母、一個數字，並且長度在 8 到 14 個字符之間：

```c#
using System;
using System.Text.RegularExpressions;

class MainClass
{
    public static void Main(string[] args)
    {
        string input = "Abc12345";
        string pattern = @"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,14}$";
        // Check if the input is a valid password
        bool isValidPassword = Regex.IsMatch(input, pattern);
        Console.WriteLine(isValidPassword); // Output: True
    }
}
```

在此示例中，該`Regex.IsMatch`方法檢查輸入字符串是否與模式中指定的密碼要求匹配。

## 使用 C# Regex.Matches：從單個調用中提取多個匹配項

該`Regex.Matches`方法使您能夠從單個輸入字符串中提取多個匹配項，並返回`MatchCollection`包含找到的所有匹配項的對象。

這種方法對於從大型非結構化文本中提取數據非常有用。下面的示例查找字符串中包含 4 個或更多字符的所有單詞：

```c#
using System;
using System.Text.RegularExpressions;

class MainClass
{
    public static void Main(string[] args)
    {
        string input = "Regex can do wonders for your text manipulation skills!";
        string pattern = @"\b\w{4,}\b";
        // Find and output all words containing 4 or more characters
        MatchCollection matches = Regex.Matches(input, pattern);
        foreach (Match match in matches)
        {
            Console.WriteLine(match.Value);
        }
    }
}
```

在此示例中，該`Regex.Matches`方法查找並提取輸入字符串中與指定模式匹配的所有單詞。

## 掌握 C# Regex.Replace：提昇文本操作能力

正如我們在前面的示例中所看到的，該`Regex.Replace`方法通過用新內容替換輸入字符串的匹配部分，提供了一種操作文本的強大方法。

要真正掌握 C# 中的文本操作，您需要深入了解`Regex.Replace`，包括如何將其與捕獲組、反向引用和 Lambda 表達式結合使用，以增強功能和靈活性。

## 探索其他正則表達式 C# 方法：C# 替換正則表達式、檢查正則表達式等

除了我們討論過的核心 C# Regex 方法之外，請務必探索類中可用的其他有用方法`Regex`，例如`Regex.Split`、`Regex.Escape`和`Regex.Unescape`。

這些方法中的每一種都提供了附加功能，可以幫助您簡化文本處理任務並創建更高級、更高效的應用程序。

# C# 正則表達式備忘單：常見正則表達式任務的便捷參考指南

為了幫助您鞏固對 C# 中正則表達式的理解，這裡有一個備忘單，其中包含每個 C# 開發人員都應該了解的大量基本正則表達式語法元素、函數和模式。

## C# 字符串模式要點：每個開發人員都應該了解的構建塊

- `^`: 一行的開頭
- `$`: 一行結束
- `.`: 除換行符外的任何字符
- `*`: 0 個或多個前面的字符
- `{n,m}`：至少n個，最多m個前一個字符
- `(abc)`：捕獲組
- `[abc]`：字符集（匹配a、b或c）
- `[^abc]`：否定字符集（匹配不在a、b或c中的字符）
- `|`: 交替（匹配 兩側的表達式之一`|`）

這些只是您將遇到的正則表達式語法元素的幾個示例。正則表達式語法元素的完整列表可以在官方 .NET 文檔中找到。

## System.Text.RegularExpressions.Regex.IsMatch：快速匹配的首選函數

如前所述，該`Regex.IsMatch`方法是檢查輸入字符串是否與正則表達式模式匹配的快速且簡單的方法。將此方法添加到您的工具箱中，可以輕鬆處理簡單的模式檢查和驗證。

## 正則表達式 C# 匹配字符和快捷方式的綜合列表：從簡單到高級

- `\d`: 一個數字
- `\D`: 非數字字符
- `\w`：單詞字符（字母、數字或下劃線）
- `\W`: 非單詞字符
- `\s`：空白字符（空格、製表符、換行符等）
- `\S`: 非空白字符
- `(?=...)`：正向前瞻
- `(?!...)`：負前瞻
- `(?<=...)`：積極的向後看
- `(?<!...)`: 負向後看
- `(?:...)`：非捕獲組
- `\1`、`\2`等：向後引用先前捕獲的組

此擴展列表提供了對可用的各種正則表達式元素的更全面的了解。通過探索正則表達式教程、指南和文檔不斷擴展您的知識，以更好地理解和在項目中利用 C# 正則表達式模式。

# 高級 C# 正則表達式：提高效率和性能的技術

隨著您越來越熟練地使用 C# 正則表達式，您將希望探索可以提高效率和性能的高級技術。

在本節中，我們將討論如何優化正則表達式模式以獲得更快的結果、實現複雜的正則表達式要求以及採用 C# 最佳實踐來獲得乾淨有效的代碼。

## 優化您的正則表達式 C# 匹配搜索以獲得更快的結果

高效的正則表達式模式可以產生更好的性能。以下是一些通過實際示例優化正則表達式搜索的技巧：

1. 盡可能使用非捕獲組。
   不要使用`(expression)`which 捕獲表達式，而是使用`(?:expression)`which 匹配但不會捕獲表達式。

```c#
//Capturing group example
string input = "The color is red.";
Match match = Regex.Match(input, "The color is (red|blue)");
Console.WriteLine(match.Groups[1].Value); // Output: red

//Non-capturing group example
input = "The color is red.";
match = Regex.Match(input, "The color is (?:red|blue)");
Console.WriteLine(match.Groups[0].Value); // Output: The color is red.
```

1. 避免過於復雜或嵌套的模式。
   簡化您的正則表達式模式，並根據需要將其分成更小的模式。重構代碼以使用多個簡單模式而不是單個複雜模式。
2. 利用錨點（`^`和`$`）來限制搜索範圍。
   錨點可以幫助加快正則表達式匹配速度，因為它們限制了搜索範圍，從而減少了處理時間。

```c#
string input = "apple\nbanana\ngrape\norange";
string pattern = "^grape$";
Match match = Regex.Match(input, pattern, RegexOptions.Multiline);
Console.WriteLine(match.Value); // Output: grape
```

## 實現 C# 字符串搜索模式以滿足複雜的正則表達式要求

實現複雜的正則表達式要求通常涉及使用高級正則表達式功能，例如前向斷言和後向斷言。這些允許您創建考慮周圍上下文的模式，而無需實際捕獲文本。

了解和利用這些高級功能將使您能夠創建更強大、更精確的搜索模式。

## 展望

正向先行`(?=...)`可確保先行內的模式出現在字符串中，但不會消耗字符串中的字符。

```c#
string input = "I want to buy a car and a bike";
string pattern = @"\ba(?:\w+)(?= a\b)";
MatchCollection matches = Regex.Matches(input, pattern);
foreach (Match match in matches)
{
    Console.WriteLine(match.Value);
}
// Output:
// car
```

負先行`(?!...)`確保先行內的模式**不**存在於字符串中，但不會消耗字符串中的字符。

```c#
input = "I want to buy a car and a bike";
pattern = @"\ba(\w+)(?! a\b)";
matches = Regex.Matches(input, pattern);
foreach (Match match in matches)
{
    Console.WriteLine(match.Value);
}
// Output:
// bike
```

## 向後看

正向lookbehind`(?<=...)`可確保lookbehind 內的模式出現在字符串中，但不會消耗字符串中的字符。

```c#
input = "100 kg of apples and 200 kg of oranges";
pattern = @"(?<=\d{3}\s)kg";
matches = Regex.Matches(input, pattern);
foreach (Match match in matches)
{
    Console.WriteLine(match.Value);
}
// Output:
// kg
```

負lookbehind`(?<!...)`可確保lookbehind 內的模式**不**存在於字符串中，但不會消耗字符串中的字符。

```c#
string input = "123/apple 456/orange";
string pattern = @"(?<!123/)apple";
Match match = Regex.Match(input, pattern);
Console.WriteLine(match.Value);
// Output: (no match found)
```

## .NET 中的正則表達式：C# 項目中無縫互操作性的技巧

C# 中的正則表達式是 .NET 庫的一部分，這意味著它們可以輕鬆地與其他 .NET 語言和工具進行互操作。

確保您熟悉 .NET 正則表達式語法，並在多語言環境中工作時遵循既定的最佳實踐。這將幫助您保持一致的代碼，減少潛在的錯誤，並確保整個項目的無縫正則表達式體驗。

例如，與 VB.NET 或 F# 開發人員合作時，共享您的正則表達式模式並確保每個人都了解項目中使用的模式的語法和結構。

使用正則表達式模式的既定命名約定，並在所有語言中保持模式相似，以便來自不同語言背景的開發人員更容易閱讀和理解它們。

## 正則表達式 C# 最佳實踐：開髮乾淨、高效且可讀的代碼

花時間開髮乾淨、高效且可讀的正則表達式代碼。保持您的模式簡潔且可維護，以確保長期穩定性和效率。

包括複雜正則表達式的註釋和解釋，以指導其他開發人員，使他們更容易理解和維護代碼。

與所有編程場景一樣，遵循最佳實踐是使用 C# 正則表達式實現獲得最佳結果的關鍵。

例如：

```c#
string pattern =
    @"^                    # Start of the line
    (?<header>[\w\s]+)    # Header (word and whitespace characters)
    :                     # Literal colon separator
    (?<content>.+?)       # Content (any non-newline chars)
    $                     # End of the line";
```

此模式演示瞭如何使用註釋來解釋正則表達式模式的每個部分，使其他人（以及未來的您）更容易理解正則表達式模式的目的和行為。

# 綜合起來：用於實際應用程序的 C# 正則表達式

正如您在本指南中所看到的，C# 正則表達式是一種多功能且強大的工具，用於在各種實際應用程序中進行文本操作。讓我們通過示例回顧一下 C# 中正則表達式的一些實際用例，以提供進一步的見解。

## C Sharp 中正則表達式的實際用例

以下是一些可以從 C# 中正則表達式的強大功能中受益的示例應用程序：

- Web 應用程序的表單驗證和輸入清理：

正則表達式可用於驗證 Web 應用程序中的表單字段，例如檢查電子郵件地址是否遵循正確的格式。

```c#
string emailPattern = @"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b";
bool isValidEmail = Regex.IsMatch("john.doe@example.com", emailPattern, RegexOptions.IgnoreCase);
Console.WriteLine(isValidEmail); // Output: True
```

- 提取和轉換數據以進行數據分析或報告：

例如，正則表達式可用於解析日誌文件，並提取有用的信息，如錯誤消息、時間戳和用戶數據。

```c#
string logText = "2021-08-01 12:00:00 - ERROR - Could not connect to database.";
string regexPattern = @"\bERROR\b\s-\s(.+)";
Match match = Regex.Match(logText, regexPattern);
Console.WriteLine(match.Groups[1].Value); // Output: Could not connect to database.
```

- 網頁抓取和數據挖掘：

正則表達式可用於從網頁中提取內容，例如獲取網頁上的所有鏈接。

```c#
string htmlText = "<a href=\"https://example1.com\">Example 1</a> <a href=\"https://example2.com\">Example 2</a>";
string linkPattern = @"<a\s+href=""([^""]+)""[^>]*>";
MatchCollection matches = Regex.Matches(htmlText, linkPattern);
foreach (Match match in matches)
{
    Console.WriteLine(match.Groups[1].Value);
}
```

- 文本編輯器或 IDE 中的搜索功能：

正則表達式可用於在大型代碼文件或文本文檔中查找特定模式或字符串，幫助您快速找到所需的信息。

```c#
string code = "using System;\nnamespace HelloWorld{class Program{static void Main(string[] args){Console.WriteLine(\"Hello, World!\");}}}";

// Regex pattern to find "Console.WriteLine" method and find all matches
MatchCollection matches = Regex.Matches(code, @"Console\.WriteLine\(");

// Print the number of matches found
Console.WriteLine($"Found {matches.Count} matches.");
```

- 日誌文件分析與調試：

通過使用正則表達式模式，您可以解析日誌文件以查找特定的錯誤消息或發生的情況，從而幫助調試過程。

```
string logContents = "2012-07-12 INFO Success\n2012-07-15 ERROR Failure";
string errorPattern = "^.*ERROR.*$";
MatchCollection errorMatches = Regex.Matches(logContents, errorPattern, RegexOptions.Multiline);
foreach (Match match in errorMatches)
{
    Console.WriteLine(match.Value);
}
```

## 在 ASP.NET 中使用 Regex C# 進行表單驗證和輸入清理

正則表達式在 Web 應用程序中的表單驗證和輸入清理中發揮著至關重要的作用。掌握 C# 中的正則表達式可讓您創建強大且安全的 ASP.NET 應用程序，從而有效驗證用戶輸入、確保數據完整性並防止潛在的安全問題。例如，您可以將正則表達式與驗證器控件（例如 ）結合使用`RegularExpressionValidator`，以匹配用戶提交的輸入中的特定模式。

```html
<asp:TextBox ID="emailTextBox" runat="server" />
<asp:RegularExpressionValidator ID="emailValidator" runat="server" 
    ControlToValidate="emailTextBox"
    ErrorMessage="Invalid email format."
    ValidationExpression="\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b">
</asp:RegularExpressionValidator>
```

## 數據處理中的 C# 正則表達式：實時提取和轉換文本

在數據處理方面，正則表達式是一個遊戲規則改變者。它使您能夠輕鬆地實時提取和轉換文本數據，簡化複雜的數據處理任務並提高應用程序的整體效率。

例如，您可能需要解析數千行文本文件並提取特定信息，例如文本中的所有電子郵件地址：

```c#
string input = "Contact Alice at alice@example.com and Bob at bob@example.org";
string emailPattern = @"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b";
MatchCollection emailMatches = Regex.Matches(input, emailPattern, RegexOptions.IgnoreCase);

foreach (Match match in emailMatches)
{
    Console.WriteLine(match.Value);
}
// Output:
// alice@example.com
// bob@example.org
```

另一個例子是轉換格式化文本，例如從給定文本中刪除所有 HTML 標籤，同時保留內容：

```c#
string htmlText = "<h1>Hello, world!</h1><p>This is <strong>bold</strong> text.</p>";
string htmlTagPattern = @"</?[^>]+>";
string plainText = Regex.Replace(htmlText, htmlTagPattern, string.Empty);

Console.WriteLine(plainText);
// Output:
// Hello, world!This is bold text.
```

當您深入研究 C# 正則表達式的世界時，您會發現無數的應用程序領域可以受益於正則表達式提供的強大功能和靈活性。

通過掌握正則表達式，您可以直接處理複雜的文本操作任務，增強應用程序的性能和功能，並最終成為更高效、更熟練的 C# 開發人員。

# 結論：成為 C# 正則表達式大師

在本指南中，您已經探索了 C# 正則表達式的世界，從基本語法元素到高級技術。一旦您掌握了 C# 中的正則表達式，可能性幾乎是無限的。

繼續磨練您的正則表達式技能並將其應用到實際應用程序中，以充分利用 C# 正則表達式提供的強大功能和靈活性。

快樂的調整！