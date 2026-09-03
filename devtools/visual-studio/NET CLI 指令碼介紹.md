---
kind: original
---

# .NET CLI 指令碼介紹

`.NET CLI` 是一組用於開發、構建、運行、發布 .NET 應用程序的命令行工具。以下是完整的介紹，包括常用命令及其使用方式。

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

## **2. 項目相關命令**

### **2.1 創建項目**

使用 `dotnet new` 命令創建新項目。

#### **範例：創建不同類型的項目**

```bash
# 創建控制台應用程序
dotnet new console -o MyConsoleApp

# 創建 ASP.NET Core Web 應用程序
dotnet new webapp -o MyWebApp

# 創建 ASP.NET Core Web API
dotnet new webapi -o MyWebAPI

# 創建類庫
dotnet new classlib -o MyLibrary

# 創建單元測試項目
dotnet new xunit -o MyTests

# 查看所有模板
dotnet new --list
```

### **2.2 還原依賴項**

從 `csproj` 或 `sln` 文件中下載和安裝依賴項：

```bash
dotnet restore
```

### **2.3 編譯項目**

構建項目並生成輸出：

```bash
dotnet build
```

- 添加 

  ```
  --configuration
  ```

  （或 `-c`）指定構建配置：

  ```bash
  dotnet build -c Release
  ```

### **2.4 運行項目**

運行項目中的主程序（`Program.cs`）：

```bash
dotnet run
```

------

## **3. 包管理**

### **3.1 添加 NuGet 包**

向項目中添加 NuGet 包：

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

### **3.3 升級 NuGet 包**

```bash
dotnet add package <PackageName> --version <NewVersion>
```

------

## **4. 測試與調試**

### **4.1 運行測試**

運行單元測試項目：

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

### **5.1 發布項目**

生成可發布的文件：

```bash
dotnet publish -c Release -o ./publish
```

- 發布自包含應用程序（不依賴 .NET Runtime）：

  ```bash
  dotnet publish -r <RID> --self-contained true
  ```

  範例：

  ```bash
  dotnet publish -r win-x64 --self-contained true
  ```

------

## **6. 解決方案與多項目管理**

### **6.1 創建解決方案**

```bash
dotnet new sln -n MySolution
```

### **6.2 添加項目到解決方案**

```bash
dotnet sln add <ProjectPath>
```

### **6.3 刪除項目**

```bash
dotnet sln remove <ProjectPath>
```

------

## **7. 查看與診斷**

### **7.1 查看已安裝模板**

```bash
dotnet new --list
```

### **7.2 查看項目依賴項樹**

```bash
dotnet list package --vulnerable
```

### **7.3 查看可用命令**

```bash
dotnet --help
```

------

## **8. 版本管理**

### **8.1 全局工具安裝**

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

### **8.3 卸載工具**

```bash
dotnet tool uninstall -g <ToolName>
```

------

## **9. 常見的進階操作**

### **9.1 執行腳本或 DLL**

直接運行已編譯的 DLL 文件：

```bash
dotnet <PathToDll>
```

### **9.2 本地生成 Docker 映像**

如果項目包含 Docker 支持，可以使用：

```bash
dotnet publish -c Release -o out
docker build -t myapp:latest .
```

------

### **參考資源**

- 官方文檔：[.NET CLI Documentation](https://learn.microsoft.com/en-us/dotnet/core/tools/)
- 提示：在每個命令後添加 `--help` 可以查看該命令的所有可用參數。