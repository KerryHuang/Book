# Docker 中部署 .NET 8 Web App 並支援 HTTPS

本文件詳細說明如何在 **Docker** 中部署 **.NET 8 Web App**，並讓其支援 **HTTPS**，同時使用 `docker-compose` 進行管理。

------

## **📌 目錄**

1. [建立 .NET 8 Web App](#建立-net-8-web-app)
2. [建立 Dockerfile](#建立-dockerfile)
3. [建立 HTTPS 憑證](#建立-https-憑證)
4. [建立 docker-compose.yml](#建立-docker-composeyml)
5. [執行與測試](#執行與測試)
6. [常見錯誤與解決方案](#常見錯誤與解決方案)

------

## **1️⃣ 建立 .NET 8 Web App**

如果尚未建立 .NET 8 Web 應用程式，請執行以下指令：

```sh
dotnet new web -n MyWebApp
cd MyWebApp
```

------

## **2️⃣ 建立 `Dockerfile`**

在專案根目錄建立 `Dockerfile`，並填入以下內容：

```dockerfile
# 使用官方 .NET 8 運行時
FROM mcr.microsoft.com/dotnet/aspnet:8.0 AS base
WORKDIR /app
EXPOSE 80
EXPOSE 443

# 設定 ASP.NET Core 環境變數（HTTPS）
ENV ASPNETCORE_URLS="https://+:443;http://+:80"
ENV ASPNETCORE_HTTPS_PORT=443
ENV ASPNETCORE_Kestrel__Certificates__Default__Path=/https/aspnetapp.pfx

# 複製 HTTPS 憑證
COPY aspnetapp.pfx /https/aspnetapp.pfx

# 建置應用程式
FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build
ARG BUILD_CONFIGURATION=Release
WORKDIR /src

# 複製專案檔案
COPY ["03.Presentation/WayDoSoft.MoldPlan.TableSpecWeb/WayDoSoft.MoldPlan.TableSpecWeb.csproj", "03.Presentation/WayDoSoft.MoldPlan.TableSpecWeb/"]
COPY . .
WORKDIR "/src/03.Presentation/WayDoSoft.MoldPlan.TableSpecWeb"

# 還原相依性
RUN dotnet restore "./WayDoSoft.MoldPlan.TableSpecWeb.csproj"

# 建置應用程式
RUN dotnet build "./WayDoSoft.MoldPlan.TableSpecWeb.csproj" -c "${BUILD_CONFIGURATION}" -o /app/build

# 發佈應用程式
FROM build AS publish
ARG BUILD_CONFIGURATION=Release
RUN dotnet publish "./WayDoSoft.MoldPlan.TableSpecWeb.csproj" -c "${BUILD_CONFIGURATION}" -o /app/publish /p:UseAppHost=false

# 部署階段
FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "WayDoSoft.MoldPlan.TableSpecWeb.dll"]
```

------

## **3️⃣ 建立 HTTPS 憑證**

ASP.NET Core 需要 **`.pfx`** 憑證來啟用 HTTPS，請執行：

```sh
dotnet dev-certs https -ep aspnetapp.pfx -p YourPfxPassword
```

這將建立 `aspnetapp.pfx`，並將其放入專案目錄。

------

## **4️⃣ 建立 `docker-compose.yml`**

在專案目錄內建立 **`docker-compose.yml`** 檔案。

### **🔹 適用於標準 80/443 端口**

```yaml
version: "3.8"

services:
  tablespecweb:
    image: waydosoft.moldplan.tablespecweb-image
    container_name: waydosoft.moldplan.tablespecweb-container
    restart: always
    ports:
      - "5000:80"
      - "5001:443"
    environment:
      ASPNETCORE_URLS: "https://+:443;http://+:80"
      ASPNETCORE_HTTPS_PORT: 443
      ASPNETCORE_Kestrel__Certificates__Default__Path: "/https/aspnetapp.pfx"
      ASPNETCORE_Kestrel__Certificates__Default__Password: "YourPfxPassword"
    volumes:
      - "./aspnetapp.pfx:/https/aspnetapp.pfx"
```

### **🔹 若要使用 `8080/8081` 端口**

```yaml
version: "3.8"

services:
  tablespecweb:
    image: waydosoft.moldplan.tablespecweb-image
    container_name: waydosoft.moldplan.tablespecweb-container
    restart: always
    ports:
      - "5000:8080"
      - "5001:8081"
    environment:
      ASPNETCORE_URLS: "https://+:8081;http://+:8080"
      ASPNETCORE_HTTPS_PORT: 8081
      ASPNETCORE_Kestrel__Certificates__Default__Path: "/https/aspnetapp.pfx"
      ASPNETCORE_Kestrel__Certificates__Default__Password: "YourPfxPassword"
    volumes:
      - "./aspnetapp.pfx:/https/aspnetapp.pfx"
```

------

## **5️⃣ 執行與測試**

### **🔹 啟動容器**

執行以下指令來建置並啟動容器：

```sh
docker-compose up --build -d
```

### **🔹 檢查運行狀態**

```sh
docker-compose ps
```

### **🔹 檢查容器日誌**

```sh
docker-compose logs -f
```

### **🔹 測試應用程式**

- **HTTP**: `http://localhost:5000`
- **HTTPS**: `https://localhost:5001`

### **🔹 停止並移除容器**

```sh
docker-compose down
```

------

## **6️⃣ 常見錯誤與解決方案**

### **❌ 錯誤 1：`The system cannot find the path specified.`**

**原因**：指定的 `docker-compose.yml` 路徑錯誤。
**解決方案**：

```sh
cd C:\Users\zihao\source\repos\waydosoft.moldplan.backend\03.Presentation\WayDoSoft.MoldPlan.TableSpecWeb
docker-compose up --build -d
```

------

### **❌ 錯誤 2：`Error mounting aspnetapp.pfx: not a directory`**

**原因**：

- `aspnetapp.pfx` 不存在或未正確掛載。

**解決方案**：

- 檢查檔案是否存在

  ```sh
  ls -l "C:\Users\zihao\source\repos\waydosoft.moldplan.backend\03.Presentation\WayDoSoft.MoldPlan.TableSpecWeb\aspnetapp.pfx"
  ```

- 確保 `volumes` 使用完整路徑

  ```yaml
  volumes:
    - "C:/Users/zihao/source/repos/waydosoft.moldplan.backend/03.Presentation/WayDoSoft.MoldPlan.TableSpecWeb/aspnetapp.pfx:/https/aspnetapp.pfx"
  ```

------

### **❌ 錯誤 3：環境變數內含敏感資訊**

**解決方案**： 在 `docker run` 時傳入：

```sh
docker run -d -p 5000:80 -p 5001:443 \
  --env ASPNETCORE_Kestrel__Certificates__Default__Password=YourPfxPassword \
  -v $(pwd)/aspnetapp.pfx:/https/aspnetapp.pfx \
  waydosoft.moldplan.tablespecweb-image
```

------

## **🎯 總結**

- 建立 `.NET 8 Web App` 並撰寫 `Dockerfile`。
- 建立 `aspnetapp.pfx` 來啟用 HTTPS。
- 使用 `docker-compose.yml` 進行管理。
- 使用 `docker-compose up --build -d` 啟動應用程式。
- 修正常見錯誤，確保應用程式順利運行。

這樣，你的 `.NET 8 Web App` 就可以 **成功運行於 Docker 並支援 HTTPS！**