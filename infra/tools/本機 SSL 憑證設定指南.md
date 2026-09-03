---
kind: original
---

# 本機 SSL 憑證設定指南

本專案使用 HTTPS 進行本機開發，需要設定本機信任的 SSL 憑證。

## 前置需求

- Windows 作業系統
- Chocolatey 套件管理器

## 安裝步驟

### 1. 安裝 mkcert

```powershell
choco install mkcert -y
```

### 2. 安裝本機 CA 憑證

```powershell
mkcert -install
```

此步驟會在系統中安裝一個本機信任的 CA（Certificate Authority），讓後續產生的憑證被瀏覽器信任。

### 3. 確認 CA 路徑

```powershell
mkcert -CAROOT
```

輸出範例：
```
C:\Users\<username>\AppData\Local\mkcert
```

### 4. 產生 localhost 憑證

切換到 mkcert 目錄並產生憑證：

```powershell
cd "C:\Users\<username>\AppData\Local\mkcert"
mkcert localhost 127.0.0.1 ::1
```

輸出範例：
```
Created a new certificate valid for the following names:
 - "localhost"
 - "127.0.0.1"
 - "::1"

The certificate is at "./localhost+2.pem" and the key at "./localhost+2-key.pem"
```

### 5. 設定環境變數

編輯專案根目錄的 `.env` 檔案，更新 SSL 路徑：

```env
# SSL (update paths as needed)
SSL_KEY_PATH=C:\Users\<username>\AppData\Local\mkcert\localhost+2-key.pem
SSL_CERT_PATH=C:\Users\<username>\AppData\Local\mkcert\localhost+2.pem
SSL_CA_PATH=C:\Users\<username>\AppData\Local\mkcert\rootCA.pem
```

將 `<username>` 替換為你的 Windows 使用者名稱。

## 驗證

設定完成後，執行 `bun dev` 啟動開發伺服器，瀏覽器應該會顯示安全的 HTTPS 連線（綠色鎖頭）。

## 常見問題

### 瀏覽器顯示憑證不受信任

重新執行 `mkcert -install`，然後重啟瀏覽器。

### 找不到憑證檔案

確認 `.env` 中的路徑與 `mkcert -CAROOT` 輸出的路徑一致。

### 憑證過期

mkcert 產生的憑證有效期為 27 個月。過期後重新執行步驟 4 產生新憑證。