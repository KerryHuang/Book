---
kind: reprint
source: https://github.com/CI-YU/2022-ITHelp/tree/main/EPPlusExample
author: CI-YU
---

# .NET 6 EPPlus範例

### 目的

將資料匯出成excel

### 建立新專案

選擇ASP.NET Core Web API專案範本，並執行下一步
![步驟1](https://user-images.githubusercontent.com/19286751/143255617-9964a993-becd-414b-aba2-632e99dd985d.png)

### 設定新的專案

命名你的專案名稱，並選擇專案要存放的位置。
![步驟2](https://user-images.githubusercontent.com/19286751/154066831-f2c7efaa-d848-442a-ae69-ba5c2b7bff85.png)

### 其他資訊

直接進行下一步
![步驟3](https://user-images.githubusercontent.com/19286751/148767425-ef0c8469-3d95-4f86-87ca-1c47c5cd0791.png)

### NuGet加入套件

- Epplus
![步驟4](https://user-images.githubusercontent.com/19286751/154067251-9336f13a-6830-48cb-a50f-8ba4bc999323.png)

### 設定appsetting檔案

為了避免LicenseException，故需要在appsetting加入下列文字

```json
  "EPPlus": {
    "ExcelPackage": {
      "LicenseContext": "Commercial" //The license context used
    }
  }
```

![步驟5](https://user-images.githubusercontent.com/19286751/154070744-45a5cdbf-ab5e-4eac-81d1-2bea8d6cf1b1.png)

### 編輯WeatherForecastController檔案

將預設的API註解
![步驟6-1](https://user-images.githubusercontent.com/19286751/154978191-e218edc4-5df3-49ad-9b7b-c4ddfa9fcdb1.png)

寫新的對外API

```c#
    [HttpGet(Name = "Import")]
    public ActionResult ImportExcel() {
      //建立excel所有操作的實例
      using ExcelPackage excelPackage = new();
      //properties為excel的屬性，開啟excel後要特別去查看屬性才能看到的資訊
      excelPackage.Workbook.Properties.Author = "Bill Huang";
      excelPackage.Workbook.Properties.Title = "範例檔案";
      excelPackage.Workbook.Properties.Created = DateTime.Now;
      //建立第一頁工作表(下方所顯示的頁簽)
      ExcelWorksheet worksheet = excelPackage.Workbook.Worksheets.Add("第一頁");
      int i = 1;
      foreach (var c in Summaries) {
        //選擇指定欄位將資料放入
        worksheet.Cells[i,1].Value = c;
        i++;
      }
      //將檔案匯出
      return File(excelPackage.GetAsByteArray(), "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", "excel檔案預設名稱");
    }
```

![步驟6-2](https://user-images.githubusercontent.com/19286751/154978457-dcd3365c-7e3a-4992-ac46-f1333a26349f.png)

### 執行結果

F5執行後，依照下列步驟操作，並將檔案下載下來
![步驟7-1](https://user-images.githubusercontent.com/19286751/154981306-58a41739-acac-448d-851f-b7d3666999b1.png)

![步驟7-2](https://user-images.githubusercontent.com/19286751/154981450-28bd0211-3653-4b03-9ab3-877b060deb97.png)

![步驟7-3](https://user-images.githubusercontent.com/19286751/154981703-4e5c3c92-12be-4c73-934a-dcfb22e6fed9.png)

### 參考

[伊果的沒人看筆記本](https://igouist.github.io/post/2020/04/epplus/)

### 範例檔

[GitHub](https://github.com/CI-YU/2022-ITHelp/tree/main/EPPlusExample)