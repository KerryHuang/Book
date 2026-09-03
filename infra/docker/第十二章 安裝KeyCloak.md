---
kind: original
---

# 第十二章 安裝KeyCloak

Keycloak 是一個開源身份和訪問管理 (Identity and Access Management, IAM) 解決方案，提供了集中式的用戶管理、單點登錄 (Single Sign-On, SSO)、以及多種協議支持（如 OpenID Connect、OAuth 2.0 和 SAML 2.0）等功能。它主要用於簡化應用程式的身份驗證和授權流程，特別適合整合到多應用系統中。以下是 Keycloak 的一些主要功能：

1. **單點登錄 (SSO)**：允許用戶在登錄一次後，可以在多個應用程式之間無縫切換，而不需要重複登錄。
2. **多協議支持**：支持 OpenID Connect、OAuth 2.0、SAML 等標準協議，方便與不同類型的應用集成。
3. **用戶自助註冊和管理**：提供用戶自助註冊、密碼找回和帳戶管理功能，用戶可以自行管理自己的帳戶。
4. **身份聯合 (Identity Federation)**：支持與其他身份提供者（如 LDAP、Active Directory）集成，實現多源身份聯合。
5. **角色與群組管理**：可以根據業務需求分配角色和群組，對用戶進行分層管理，並進行權限控制。
6. **多因素驗證 (MFA)**：支持多因素驗證（如 SMS 驗證、Google Authenticator 等），增強帳戶安全性。
7. **自定義化**：Keycloak 提供豐富的自定義選項，允許自定義登錄頁面、註冊頁面和登出流程等。

### 使用場景

Keycloak 通常被用於需要集中管理用戶身份的應用環境，特別適合分佈式系統和微服務架構。典型場景包括：

- 大型企業內部系統的用戶統一管理
- 微服務架構中的集中式身份驗證
- 需要多應用單點登錄的系統
- 整合多種身份源（如 AD、LDAP、社交登入）的應用

Keycloak 讓開發者能夠專注於業務邏輯，而不需要花費大量精力在身份驗證和用戶管理上，提供了高效、安全的解決方案。

在 Docker 上安裝 Keycloak 是一個簡單的過程，可以利用官方的 Keycloak Docker 映像來快速啟動。以下是 Keycloak 在 Docker 上的安裝步驟：

### 1. 使用 Docker 指令安裝 Keycloak

首先，確認你已經安裝好 Docker。如果沒有，請先安裝 Docker。

使用以下指令來拉取並啟動 Keycloak 容器：

```bash
docker run -d \
  --name keycloak \
  -p 8080:8080 \
  -e KEYCLOAK_ADMIN=admin \
  -e KEYCLOAK_ADMIN_PASSWORD=admin_password \
  quay.io/keycloak/keycloak:latest \
  start-dev
```

- `--name keycloak`：設置容器名稱為 `keycloak`。
- `-p 8080:8080`：將本地端口 `8080` 映射到容器中的端口 `8080`。
- `-e KEYCLOAK_ADMIN=admin`：設置 Keycloak 的預設管理員用戶名。
- `-e KEYCLOAK_ADMIN_PASSWORD=admin_password`：設置管理員密碼。
- `quay.io/keycloak/keycloak:latest`：指定使用 Keycloak 的最新版本映像。
- `start-dev`：以開發模式啟動 Keycloak。

### 2. 檢查 Keycloak 是否啟動成功

可以使用以下指令來確認容器是否正在執行：

```bash
docker ps
```

如果容器正在運行，您應該會看到 `keycloak` 容器的相關信息。

### 3. 訪問 Keycloak 管理界面

Keycloak 啟動後，可以透過瀏覽器訪問管理介面。打開瀏覽器並輸入：

```arduino
http://localhost:8080
```

您會看到 Keycloak 的登錄頁面，使用您在啟動容器時設置的管理員用戶名和密碼（例如：`admin` 和 `admin_password`）來登錄。

### 4. 使用 Docker Compose（可選）

如果需要更多的配置，或者想讓 Keycloak 和其他服務一同啟動，可以使用 Docker Compose 來定義容器。以下是使用 Docker Compose 啟動 Keycloak 的範例：

```yaml
version: '3'
services:
  keycloak:
    image: quay.io/keycloak/keycloak:latest
    container_name: keycloak
    ports:
      - "8080:8080"
    environment:
      - KEYCLOAK_ADMIN=admin
      - KEYCLOAK_ADMIN_PASSWORD=admin_password
    command: start-dev
```

保存此文件為 `docker-compose.yml`，然後在該文件所在目錄中執行：

```bash
docker-compose up -d
```

這樣，Keycloak 會在 Docker 中以容器的形式啟動並運行，您可以隨時使用 Docker Compose 管理它。

### 5. 後續配置

在進入 Keycloak 管理介面後，您可以創建領域 (Realm)、用戶、角色和客戶端 (Client)，並配置單點登錄和其他身份驗證設定。

這樣就完成了 Keycloak 在 Docker 上的安裝。