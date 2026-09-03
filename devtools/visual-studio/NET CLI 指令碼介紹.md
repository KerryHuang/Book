---
kind: original
---

# .NET CLI 指令碼介紹

`.NET CLI` 是一組用於開發、建置、執行、發布 .NET 應用程式的命令列工具。以下是完整的介紹，包括常用指令及其使用方式。

------

## **1. 安裝與檢查版本**

### **安裝 .NET SDK**

前往 [.NET 官方網站](https://dotnet.microsoft.com/download) 下載並安裝適合您系統的 SDK。

### **檢查版本**

```bash
dotnet --version
```

顯示已安裝的 .NET SDK 版本。

### **檢查所有已安裝的 SDK 和 Runtimes**

```bash
dotnet --list-sdks
dotnet --list-runtimes
```

------

## **2. 專案相關指令**

### **2.1 建立專案**

使用 `dotnet new` 指令建立新專案。

#### **範例：建立不同類型的專案**

```bash
# 建立控制台應用程式
dotnet new console -o MyConsoleApp

# 建立 ASP.NET Core Web 應用程式
dotnet new webapp -o MyWebApp

# 建立 ASP.NET Core Web API
dotnet new webapi -o MyWebAPI

# 建立類別庫
dotnet new classlib -o MyLibrary

# 建立單元測試專案
dotnet new xunit -o MyTests

# 查看所有範本
dotnet new --list
```

### **2.2 還原依賴項**

從 `csproj` 或 `sln` 檔案中下載和安裝依賴項：

```bash
dotnet restore
```

### **2.3 編譯專案**

建置專案並生成輸出：

```bash
dotnet build
```

- 新增 

  ```
  --configuration
  ```

  （或 `-c`）指定建置設定：

  ```bash
  dotnet build -c Release
  ```

### **2.4 執行專案**

執行專案中的主程式（`Program.cs`）：

```bash
dotnet run
```

------

## **3. 包管理**

### **3.1 新增 NuGet 套件**

向專案中新增 NuGet 套件：

```bash
dotnet add package <PackageName> --version <Version>
```

範例：

```bash
dotnet add package Newtonsoft.Json --version 13.0.1
```

### **3.2 查看已安裝的包**

```bash
dotnet list package
```

### **3.3 升級 NuGet 套件**

```bash
dotnet add package <PackageName> --version <NewVersion>
```

------

## **4. 測試與偵錯**

### **4.1 執行測試**

執行單元測試專案：

```bash
dotnet test
```

### **4.2 查看測試結果格式**

生成詳細的測試結果：

```bash
dotnet test --logger "trx;LogFileName=TestResults.trx"
```

------

## **5. 發布與部署**

### **5.1 發布專案**

生成可發布的檔案：

```bash
dotnet publish -c Release -o ./publish
```

- 發布自包含應用程式（不依賴 .NET Runtime）：

  ```bash
  dotnet publish -r <RID> --self-contained true
  ```

  範例：

  ```bash
  dotnet publish -r win-x64 --self-contained true
  ```

------

## **6. 解決方案與多專案管理**

### **6.1 建立解決方案**

```bash
dotnet new sln -n MySolution
```

### **6.2 新增專案到解決方案**

```bash
dotnet sln add <ProjectPath>
```

### **6.3 刪除專案**

```bash
dotnet sln remove <ProjectPath>
```

------

## **7. 查看與診斷**

### **7.1 查看已安裝範本**

```bash
dotnet new --list
```

### **7.2 查看專案依賴項樹**

```bash
dotnet list package --include-transitive
```

### **7.3 查看可用指令**

```bash
dotnet --help
```

------

## **8. 版本管理**

### **8.1 全域工具安裝**

安裝 .NET CLI 工具：

```bash
dotnet tool install -g <ToolName>
```

範例：

```bash
dotnet tool install -g dotnet-ef
```

### **8.2 更新工具**

```bash
dotnet tool update -g <ToolName>
```

### **8.3 解除安裝工具**

```bash
dotnet tool uninstall -g <ToolName>
```

------

## **9. 常見的進階操作**

### **9.1 執行指令碼或 DLL**

直接執行已編譯的 DLL 檔案：

```bash
dotnet <PathToDll>
```

### **9.2 本地生成 Docker 映像檔**

如果專案包含 Docker 支援，可以使用：

```bash
dotnet publish -c Release -o out
docker build -t myapp:latest .
```

------

### **參考資源**

- 官方文件：[.NET CLI Documentation](https://learn.microsoft.com/en-us/dotnet/core/tools/)
- 提示：在每個指令後新增 `--help` 可以查看該指令的所有可用參數。