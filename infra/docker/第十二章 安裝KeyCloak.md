---
kind: original
---

# 第十二章 安裝KeyCloak

Keycloak 是一個開源身分和存取管理 (Identity and Access Management, IAM) 解決方案，提供了集中式的使用者管理、單點登入 (Single Sign-On, SSO)、以及多種協定支援（如 OpenID Connect、OAuth 2.0 和 SAML 2.0）等功能。它主要用於簡化應用程式的身分驗證和授權流程，特別適合整合到多應用系統中。以下是 Keycloak 的一些主要功能：

1. **單點登入 (SSO)**：允許使用者在登入一次後，可以在多個應用程式之間無縫切換，而不需要重複登入。
2. **多協定支援**：支援 OpenID Connect、OAuth 2.0、SAML 等標準協定，方便與不同類型的應用整合。
3. **使用者自助註冊和管理**：提供使用者自助註冊、密碼找回和帳戶管理功能，使用者可以自行管理自己的帳戶。
4. **身分聯合 (Identity Federation)**：支援與其他身分提供者（如 LDAP、Active Directory）整合，實現多源身分聯合。
5. **角色與群組管理**：可以根據業務需求分配角色和群組，對使用者進行分層管理，並進行權限控制。
6. **多因素驗證 (MFA)**：支援多因素驗證（如 SMS 驗證、Google Authenticator 等），增強帳戶安全性。
7. **自訂化**：Keycloak 提供豐富的自訂選項，允許自訂登入頁面、註冊頁面和登出流程等。

### 使用場景

Keycloak 通常被用於需要集中管理使用者身分的應用環境，特別適合分散式系統和微服務架構。典型場景包括：

- 大型企業內部系統的使用者統一管理
- 微服務架構中的集中式身分驗證
- 需要多應用單點登入的系統
- 整合多種身分源（如 AD、LDAP、社交登入）的應用

Keycloak 讓開發者能夠專注於業務邏輯，而不需要花費大量精力在身分驗證和使用者管理上，提供了高效、安全的解決方案。

在 Docker 上安裝 Keycloak 是一個簡單的過程，可以利用官方的 Keycloak Docker 映像檔來快速啟動。以下是 Keycloak 在 Docker 上的安裝步驟：

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

- `--name keycloak`：設定容器名稱為 `keycloak`。
- `-p 8080:8080`：將本地連接埠 `8080` 映射到容器中的連接埠 `8080`。
- `-e KEYCLOAK_ADMIN=admin`：設定 Keycloak 的預設管理員使用者名稱。
- `-e KEYCLOAK_ADMIN_PASSWORD=admin_password`：設定管理員密碼。
- `quay.io/keycloak/keycloak:latest`：指定使用 Keycloak 的最新版本映像檔。
- `start-dev`：以開發模式啟動 Keycloak。

### 2. 檢查 Keycloak 是否啟動成功

可以使用以下指令來確認容器是否正在執行：

```bash
docker ps
```

如果容器正在執行，您應該會看到 `keycloak` 容器的相關資訊。

### 3. 存取 Keycloak 管理介面

Keycloak 啟動後，可以透過瀏覽器存取管理介面。打開瀏覽器並輸入：

```arduino
http://localhost:8080
```

您會看到 Keycloak 的登入頁面，使用您在啟動容器時設定的管理員使用者名稱和密碼（例如：`admin` 和 `admin_password`）來登入。

### 4. 使用 Docker Compose（可選）

如果需要更多的設定，或者想讓 Keycloak 和其他服務一同啟動，可以使用 Docker Compose 來定義容器。以下是使用 Docker Compose 啟動 Keycloak 的範例：

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

保存此檔案為 `docker-compose.yml`，然後在該檔案所在目錄中執行：

```bash
docker-compose up -d
```

這樣，Keycloak 會在 Docker 中以容器的形式啟動並執行，您可以隨時使用 Docker Compose 管理它。

### 5. 後續設定

在進入 Keycloak 管理介面後，您可以建立領域 (Realm)、使用者、角色和客戶端 (Client)，並設定單點登入和其他身分驗證設定。

這樣就完成了 Keycloak 在 Docker 上的安裝。