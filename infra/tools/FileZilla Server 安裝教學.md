---
kind: reprint
source: https://blog.hungwin.com.tw/ftp-filezilla/
author: Hungwin
---

# 免費 FTP 伺服器 FileZilla Server 安裝教學 (新版設定)


FileZilla Server 是一款免費的 FTP (File Transfer Protocol) 檔案傳輸伺服器，可以提供外部電腦直接存取電腦內部檔案。

登入 FTP 後就像操作自己電腦上的資料夾一樣，可以新增、修改、刪除檔案及資料夾，當然 FTP 可以提供權限設定，可以限制登入者只能做某些功能。

安裝 FileZilla Server 需要為每一個登入者設定帳號密碼以及使用權限，在某些情況下也可以設定匿名使用者，不需帳號也可以登入，但是方便的情況下，安全性就比較低。

FileZilla 有分為 Server 及 Client 兩個版本，這篇文章主要分享 Server 安裝設定教學，最後面用 Client 簡單登入測試。

目錄 [[hide](https://blog.hungwin.com.tw/ftp-filezilla/#)]

- 1 FileZilla Server 檔案下載安裝
  - [1.1 安裝教學](https://blog.hungwin.com.tw/ftp-filezilla/#i)
  - [1.2 管理者登入](https://blog.hungwin.com.tw/ftp-filezilla/#i-2)
- 2 設定使用者帳號
  - [2.1 設定目錄權限](https://blog.hungwin.com.tw/ftp-filezilla/#i-4)
- 3 FileZilla 連接埠 Port 設定
  - [3.1 防火牆設定](https://blog.hungwin.com.tw/ftp-filezilla/#i-5)
- [4 FileZilla Client 客戶端測試](https://blog.hungwin.com.tw/ftp-filezilla/#FileZilla_Client)

## FileZilla Server 檔案下載安裝

- FileZilla 官方網站: https://filezilla-project.org/
- 軟體屬性: 免費開源、額外付費功能
- 語系: 英文，可中文化
- 系統平台: 支援 Windows (64bit, x86) , macOS, Linux

到官網點擊 Server 版本下載，不管 64 或 32 位元都下載相同檔案。

[![FileZilla Server 檔案下載](https://blog.hungwin.com.tw/wp-content/uploads/2022/10/ftp-filezilla-1.png)](https://blog.hungwin.com.tw/wp-content/uploads/2022/10/ftp-filezilla-1.png)

下載選擇免費版本下載。

[![FileZilla Server 檔案下載](https://blog.hungwin.com.tw/wp-content/uploads/2022/10/ftp-filezilla-2.png)](https://blog.hungwin.com.tw/wp-content/uploads/2022/10/ftp-filezilla-2.png)

### 安裝教學

執行安裝檔後，可以選擇安裝全部選項。

[![FileZilla Server 檔案下載安裝](https://blog.hungwin.com.tw/wp-content/uploads/2022/10/ftp-filezilla-3.png)](https://blog.hungwin.com.tw/wp-content/uploads/2022/10/ftp-filezilla-3.png)

接著安裝路徑可以預設就好。
在安裝選項這裡，可以預設是開機自動啟動，如果不要的話，可以選另一個。
中間的管理者 Port 可以預設就好，下面輸入管理者密碼。

[![FileZilla Server 檔案下載安裝](https://blog.hungwin.com.tw/wp-content/uploads/2022/10/ftp-filezilla-4.png)](https://blog.hungwin.com.tw/wp-content/uploads/2022/10/ftp-filezilla-4.png)

是否同意所有 Windows 用戶登入時都啟動此服務，因為我只有一位管理者使用者，所以我會使用預設。

[![是否同意所有 Windows 用戶登入時都啟動此服務](https://blog.hungwin.com.tw/wp-content/uploads/2022/10/ftp-filezilla-5.png)](https://blog.hungwin.com.tw/wp-content/uploads/2022/10/ftp-filezilla-5.png)

下一步就安裝完成了。

### 管理者登入

安裝後，首次登入可以輸入剛剛的管理者密碼，Port 的部份可以預設就好，除非剛剛有修改管理者 Port。
下面的勾選是儲存密碼，以及下次啟動時自動登入

[![管理者登入](https://blog.hungwin.com.tw/wp-content/uploads/2022/10/ftp-filezilla-6.png)](https://blog.hungwin.com.tw/wp-content/uploads/2022/10/ftp-filezilla-6.png)

是否信任此電腦可以執行「Yes」。

[![是否信任此電腦可以執行「Yes」](https://blog.hungwin.com.tw/wp-content/uploads/2022/10/ftp-filezilla-7.png)](https://blog.hungwin.com.tw/wp-content/uploads/2022/10/ftp-filezilla-7.png)

完成就會開啟主畫面了。

[![FileZilla Server](https://blog.hungwin.com.tw/wp-content/uploads/2022/10/ftp-filezilla-8.png)](https://blog.hungwin.com.tw/wp-content/uploads/2022/10/ftp-filezilla-8.png)

## 設定使用者帳號

在建立使用者帳號之前，可以選擇是否要建立群組，建立群組的目的是幫助分類，可以在群組內設定目錄存取權限，可以將使用者放在不同的群組。

開啟建立群組或使用者的操作在「Server > Configure」

[![設定使用者帳號](https://blog.hungwin.com.tw/wp-content/uploads/2022/10/ftp-filezilla-9.png)](https://blog.hungwin.com.tw/wp-content/uploads/2022/10/ftp-filezilla-9.png)

在 Rights management 底下有群組和使用者的選單。

[![設定使用者帳號](https://blog.hungwin.com.tw/wp-content/uploads/2022/10/ftp-filezilla-10.png)](https://blog.hungwin.com.tw/wp-content/uploads/2022/10/ftp-filezilla-10.png)

這裡我簡單用建立使用者做示範，在「Users」的選單，可以點「Add」加一位使用者。

[![設定使用者帳號](https://blog.hungwin.com.tw/wp-content/uploads/2022/10/ftp-filezilla-11.png)](https://blog.hungwin.com.tw/wp-content/uploads/2022/10/ftp-filezilla-11.png)

然後輸入使用者名稱、密碼，建議要求登入時輸入密碼。

[![設定使用者帳號](https://blog.hungwin.com.tw/wp-content/uploads/2022/10/ftp-filezilla-12.png)](https://blog.hungwin.com.tw/wp-content/uploads/2022/10/ftp-filezilla-12.png)

### 設定目錄權限

目錄的權限設定跟之前版本不太一樣，簡化了一些設定。
接著我增加一個登入主目錄，在「Mount points」執行「Add」，在「Virtual path」輸入「/」，在「Native path」輸入本機要顯示的目錄，我以「C:\Temp」示範。

[![設定目錄權限](https://blog.hungwin.com.tw/wp-content/uploads/2022/10/ftp-filezilla-13.png)](https://blog.hungwin.com.tw/wp-content/uploads/2022/10/ftp-filezilla-13.png)

右邊的部份就是對目錄的讀寫權限，下面第一個勾選是權限是否可應用於子目錄，第二個勾選是否可增加目錄的權限。

[![設定目錄權限](https://blog.hungwin.com.tw/wp-content/uploads/2022/10/ftp-filezilla-14.png)](https://blog.hungwin.com.tw/wp-content/uploads/2022/10/ftp-filezilla-14.png)

有了主目錄之後，可以再按「Add」增加其他的子目錄，「Virtual path」都用「/」 開頭指定虛擬路徑。
做到這裡第一個使用者就完成了，可以開始測試了。

## FileZilla 連接埠 Port 設定

如果要開放給外部電腦連線 FTP 的話，要記得開啟防火牆設定，FTP 要開啟的 Port 有 2 種。

第 1 種是登入的 Port 是 21。
第 2 種是資料傳輸 Port，這個不是固定 Port，而是設定一段區間範圍，讓 FTP 自行決定開啟範圍內其中一個 Port 讓使用者傳輸資料。

登入 Port 的查詢位置在「Server listeners」裡面，要修改的話，就可以將 21 改掉就行了。

[![FileZilla 連接埠 Port 設定](https://blog.hungwin.com.tw/wp-content/uploads/2022/10/ftp-filezilla-15.png)](https://blog.hungwin.com.tw/wp-content/uploads/2022/10/ftp-filezilla-15.png)

資料傳輸 Port 位置在「Protocols settings > FTP and FTP over TLS (FTPS) > Passive mode」裡面。
它預設使用範圍從 49152 到 65534，由使用者連線時隨機使用其中一個 Port。

[![FileZilla 連接埠 Port 設定](https://blog.hungwin.com.tw/wp-content/uploads/2022/10/ftp-filezilla-16.png)](https://blog.hungwin.com.tw/wp-content/uploads/2022/10/ftp-filezilla-16.png)

這個範圍很大，你可以依實際連線人數設定剛好的範圍就好，例如我的服務大概就 100 人使用，那我範圍就設 100 就可以了。
將「Use custom port range」勾選，輸入指定的範圍，

[![FileZilla 連接埠 Port 設定](https://blog.hungwin.com.tw/wp-content/uploads/2022/10/ftp-filezilla-17.png)](https://blog.hungwin.com.tw/wp-content/uploads/2022/10/ftp-filezilla-17.png)

當範圍縮小後，在防火牆就只要允許範圍內的 Port 連線就好。

### 防火牆設定

防火牆有兩種方式設定，直接允許 FileZilla Server 執行程式，或是在進階設定開放 21 Port 及資料傳輸範圍 Port 。

設定允許 FileZilla Server 執行程式會是比較簡單的方式。

[![防火牆設定](https://blog.hungwin.com.tw/wp-content/uploads/2022/10/ftp-filezilla-18.png)](https://blog.hungwin.com.tw/wp-content/uploads/2022/10/ftp-filezilla-18.png)

要允許程式的話，點擊「允許其他應用程式」，然後找到執行檔路徑。

[![允許其他應用程式](https://blog.hungwin.com.tw/wp-content/uploads/2022/10/ftp-filezilla-19.png)](https://blog.hungwin.com.tw/wp-content/uploads/2022/10/ftp-filezilla-19.png)

預設路徑在 C:\Program Files\FileZilla Server\filezilla-server.exe

[![C:\Program Files\FileZilla Server\filezilla-server.exe](https://blog.hungwin.com.tw/wp-content/uploads/2022/10/ftp-filezilla-20.png)](https://blog.hungwin.com.tw/wp-content/uploads/2022/10/ftp-filezilla-20.png)

允許這程式就可以了。

## FileZilla Client 客戶端測試

當 Server 端建立好之後，可以到 [FileZilla Client](https://filezilla-project.org/download.php?type=client) 下載客戶端程式，安裝過程很簡單，一直下一步就行了。

開啟後輸入主機 IP，我剛剛是本機測試，所以可以輸入「127.0.0.1」，然後輸入帳號及密碼，連接埠的話，如果 Server 沒有特別修改的話，預設是 21 Port，而這裡連接埠輸入空白也可以，它預設是 21 Port，然後按「快速連線」就會登入 FTP 了。

[![FileZilla Client 客戶端測試](https://blog.hungwin.com.tw/wp-content/uploads/2022/10/ftp-filezilla-21.png)](https://blog.hungwin.com.tw/wp-content/uploads/2022/10/ftp-filezilla-21.png)

登入後就可以看到剛剛設定的目錄 (在右邊)，可以在目錄裡新增、修改、刪除檔案，也可以增加目錄，權限就由建立使用者時決定。