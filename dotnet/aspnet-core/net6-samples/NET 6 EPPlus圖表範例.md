---
kind: reprint
source: https://github.com/CI-YU/2022-ITHelp/tree/main/EPPlusExample_Advanced
author: CI-YU
---

# .NET 6 EPPlus圖表範例

### 目的

使用epplus製作長條圖

### 建立新專案

選擇ASP.NET Core Web API專案範本，並執行下一步
![步驟1](https://user-images.githubusercontent.com/19286751/143255617-9964a993-becd-414b-aba2-632e99dd985d.png)

### 設定新的專案

命名你的專案名稱，並選擇專案要存放的位置。
![步驟2](https://user-images.githubusercontent.com/19286751/191029365-2d7a7c68-4b42-48dd-aa1f-b293738f857f.png)

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
![步驟6-1](https://user-images.githubusercontent.com/19286751/154978191-e218edc4-5df3-49ad-9b7b-c4ddfa9fcdb1.png)寫新的對外API

```C#
    [HttpGet(Name = "Import")]
    public ActionResult ImportExcel() {
      //建立excel所有操作的實例
      using ExcelPackage excelPackage = new();
      var ws = excelPackage.Workbook.Worksheets.Add("第一頁");
      Random Random = new Random();
      //ws.Cells[上下(row),左右(col)]
      ws.Cells[1, 2].Value = "第一季";
      ws.Cells[1, 3].Value = "第二季";
      ws.Cells[1, 4].Value = "第三季";
      ws.Cells[1, 5].Value = "第四季";
      ws.Cells[2, 1].Value = "A組";
      ws.Cells[3, 1].Value = "B組";
      ws.Cells[4, 1].Value = "C組";
      ws.Cells[5, 1].Value = "D組";
      for (int i = 2; i <= 5; i++) {
        for (int j = 2; j <= 5; j++) {
          ws.Cells[i, j].Value = Random.Next(70, 150);
        }
      }
      //建立長條圖
      var BarChart = ws.Drawings.AddBarChart("BarChart", eBarChartType.ColumnClustered);
      //長條圖名稱
      BarChart.Title.Text = "年度季報表";
      //長條圖的位置
      BarChart.SetPosition(6, 0, 6, 0);
      //長條圖大小
      BarChart.SetSize(400, 400);
      //第一個顏色長條圖BarChart.Series.Add(數據區間，x軸名稱區間)=>數據區間從(2,2)到(2,5)，X軸名稱(第一季、第二季、第三季、第四季)
      var Ateam = BarChart.Series.Add(ExcelCellBase.GetAddress(2, 2, 2, 5), ExcelCellBase.GetAddress(1, 2, 1, 5));
      //第一條顏色的名稱(A組)
      Ateam.Header = ws.Cells[2, 1].Text;
      var Bteam = BarChart.Series.Add(ExcelCellBase.GetAddress(3, 2, 3, 5), ExcelCellBase.GetAddress(1, 2, 1, 5));
      Bteam.Header = ws.Cells[3, 1].Text;
      var Cteam = BarChart.Series.Add(ExcelCellBase.GetAddress(4, 2, 4, 5), ExcelCellBase.GetAddress(1, 2, 1, 5));
      Cteam.Header = ws.Cells[4, 1].Text;
      var Dteam = BarChart.Series.Add(ExcelCellBase.GetAddress(5, 2, 5, 5), ExcelCellBase.GetAddress(1, 2, 1, 5));
      Dteam.Header = ws.Cells[5, 1].Text;
      //樣式使用1
      BarChart.StyleManager.SetChartStyle(ePresetChartStyle.HistogramChartStyle1);

      //將檔案匯出
      return File(excelPackage.GetAsByteArray(), "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", "製作長條圖");
    }
```

範例太長，只擷取部分
![範例6-1](https://user-images.githubusercontent.com/19286751/191067779-cb6f4853-54e5-4ab2-86bf-9a3d7f39a88a.png)

### 執行結果

![範例7-1](https://user-images.githubusercontent.com/19286751/191068075-b18f983a-c057-4a47-84f7-1ccffa0ff784.png)

### 範例檔

[GitHub](https://github.com/CI-YU/2022-ITHelp/tree/main/EPPlusExample_Advanced)