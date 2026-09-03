---
kind: reprint
source: https://blog.hungwin.com.tw/windows-server-iis-install/
author: Hungwin
---

# Windows Server 2019 如何安裝 IIS 運行 ASP.NET 專案

ASP.NET 是微軟推出的網頁語言，其主要由 C# 所開發，也有少數人使用 VB.Net 開發。
網頁運作需要網站伺服器，而 IIS 是 Windows 作業系統內建的網站伺服器，在伺服器及個人電腦上都可以安裝。

最近將一台主機重新安裝了 Windows Server 2019 要來跑 [ASP.NET](https://dotnet.microsoft.com/apps/aspnet) 的專案。我的專案是 C# .Net Framework 4.7 版本。
接下來要在 Windows Server 2019 上安裝 IIS For ASP.NET 版本。記錄一下。

目錄 [[hide](https://blog.hungwin.com.tw/windows-server-iis-install/#)]

- [1 影片教學](https://blog.hungwin.com.tw/windows-server-iis-install/#i)
- 2 安裝 IIS
  - [2.1 新增角色及功能](https://blog.hungwin.com.tw/windows-server-iis-install/#i-2)
  - [2.2 勾選網頁伺服器(IIS)](https://blog.hungwin.com.tw/windows-server-iis-install/#IIS)
  - [2.3 勾選應用程式開發-ASP.NET](https://blog.hungwin.com.tw/windows-server-iis-install/#-ASPNET)
- 3 啟動 IIS
  - [3.1 測試本機網頁](https://blog.hungwin.com.tw/windows-server-iis-install/#i-3)
- [4 重點整理](https://blog.hungwin.com.tw/windows-server-iis-install/#i-4)

## 影片教學



## 安裝 IIS

### 新增角色及功能

在「伺服器管理員」上執行「新增角色及功能」。

[![安裝 IIS](https://blog.hungwin.com.tw/wp-content/uploads/2021/07/windows-server-iis-install-1.png)](https://blog.hungwin.com.tw/wp-content/uploads/2021/07/windows-server-iis-install-1.png)

點擊「下一步」。

[![安裝 IIS](https://blog.hungwin.com.tw/wp-content/uploads/2021/07/windows-server-iis-install-2.png)](https://blog.hungwin.com.tw/wp-content/uploads/2021/07/windows-server-iis-install-2.png)

安裝類型選擇「角色型或功能型安裝」。

[![安裝 IIS](https://blog.hungwin.com.tw/wp-content/uploads/2021/07/windows-server-iis-install-3.png)](https://blog.hungwin.com.tw/wp-content/uploads/2021/07/windows-server-iis-install-3.png)

目的地伺服器選擇「從伺服器集區選取伺服器」。

[![安裝 IIS](https://blog.hungwin.com.tw/wp-content/uploads/2021/07/windows-server-iis-install-4.png)](https://blog.hungwin.com.tw/wp-content/uploads/2021/07/windows-server-iis-install-4.png)

### 勾選網頁伺服器(IIS)

伺服器角色勾選「網頁伺服器(IIS)」。

[![安裝 IIS](https://blog.hungwin.com.tw/wp-content/uploads/2021/07/windows-server-iis-install-5.png)](https://blog.hungwin.com.tw/wp-content/uploads/2021/07/windows-server-iis-install-5.png)

點「新增功能」。

[![安裝 IIS](https://blog.hungwin.com.tw/wp-content/uploads/2021/07/windows-server-iis-install-6.png)](https://blog.hungwin.com.tw/wp-content/uploads/2021/07/windows-server-iis-install-6.png)

確認「網頁伺服器(IIS)」有勾選就按「下一步」。

[![安裝 IIS](https://blog.hungwin.com.tw/wp-content/uploads/2021/07/windows-server-iis-install-7.png)](https://blog.hungwin.com.tw/wp-content/uploads/2021/07/windows-server-iis-install-7.png)

選取功能這邊檢查 .NET Framework 4.x 功能是否有打勾。
目前.Net Framework 版本主要分 2 種。
.Net 2.0 到 3.5 都可使用 .NET Framework 3.5 版本。
超過 4.0 以上的都選 4.x 版本。
畫面上看到的 4.7 版本有向下支援到 4.0 版本。

[![安裝 IIS](https://blog.hungwin.com.tw/wp-content/uploads/2021/07/windows-server-iis-install-8.png)](https://blog.hungwin.com.tw/wp-content/uploads/2021/07/windows-server-iis-install-8.png)

這邊直接點「下一步」。

[![img](https://blog.hungwin.com.tw/wp-content/uploads/2021/07/windows-server-iis-install-9.png)](https://blog.hungwin.com.tw/wp-content/uploads/2021/07/windows-server-iis-install-9.png)



### 勾選應用程式開發-ASP.NET

在角色服務這邊要勾選「應用程式開發 > ASP.NET 4.7」版本。
如果你們版本寫的是 4.X 都行。

[![安裝 IIS](https://blog.hungwin.com.tw/wp-content/uploads/2021/07/windows-server-iis-install-10.png)](https://blog.hungwin.com.tw/wp-content/uploads/2021/07/windows-server-iis-install-10.png)

勾選時按「新增功能」。

[![安裝 IIS](https://blog.hungwin.com.tw/wp-content/uploads/2021/07/windows-server-iis-install-11.png)](https://blog.hungwin.com.tw/wp-content/uploads/2021/07/windows-server-iis-install-11.png)

這邊是確認安裝功能，按「安裝」。

[![img](https://blog.hungwin.com.tw/wp-content/uploads/2021/07/windows-server-iis-install-12.png)](https://blog.hungwin.com.tw/wp-content/uploads/2021/07/windows-server-iis-install-12.png)

最後等待安裝完成就行了喔。

[![img](https://blog.hungwin.com.tw/wp-content/uploads/2021/07/windows-server-iis-install-13.png)](https://blog.hungwin.com.tw/wp-content/uploads/2021/07/windows-server-iis-install-13.png)

## 啟動 IIS

在開始輸入「IIS」就可以執行程式了。

[![IIS](https://blog.hungwin.com.tw/wp-content/uploads/2021/07/windows-server-iis-install-14.png)](https://blog.hungwin.com.tw/wp-content/uploads/2021/07/windows-server-iis-install-14.png)

這是 IIS 管理介面。

[![IIS](https://blog.hungwin.com.tw/wp-content/uploads/2021/07/windows-server-iis-install-15.png)](https://blog.hungwin.com.tw/wp-content/uploads/2021/07/windows-server-iis-install-15.png)

### 測試本機網頁

當 IIS 安裝完成之後，預設就會啟用本機的 localhost 網頁。
在網頁上輸入 localhost 檢查是否正常啟動。

[![IIS](https://blog.hungwin.com.tw/wp-content/uploads/2021/07/windows-server-iis-install-16.png)](https://blog.hungwin.com.tw/wp-content/uploads/2021/07/windows-server-iis-install-16.png)

看到這畫面就表示 IIS 裝好了。

## 重點整理

1. 開啟新增角色及功能
2. 勾選網頁伺服器(IIS)
3. 勾選應用程式開發-ASP.NET
4. 輸入「IIS」啟動管理程式
5. 預設網頁 http://localhost/