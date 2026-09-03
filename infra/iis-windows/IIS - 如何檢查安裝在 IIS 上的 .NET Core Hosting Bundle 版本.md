---
kind: unknown
---

# 如何檢查安裝在 IIS 上的 .NET Core Hosting Bundle 版本

透過 [.NET Core CLI](https://docs.microsoft.com/zh-tw/dotnet/core/tools/?tabs=netcore2x&WT.mc_id=DT-MVP-5003022) 的命令，我們可以透過 `dotnet --list-runtimes` 查詢本機有安裝的執行環境版本，如果你是使用 IIS 來架設 .NET Core 的站台，還需要安裝 .NET Core Hosting Bundle 才能正確執行，但如何檢查本機所安裝的 .NET Core Hosting Bundle 版本呢？這裡有個 Script 很好用。

要檢查 .NET Core Hosting Bundle 版本沒有工具或指令可以幫忙，最土法煉鋼的方式是透過 `regedit.exe` 檢查登錄檔內的 .NET Core Hosting Bundle 版本名稱，路徑為 `HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\Microsoft\Updates\.NET Core`，如下圖就安裝了 3 個 .NET Core Hosting Bundle 版本。

![在登錄檔中查詢 .NET Core Hosting Bundle 版本](https://i.imgur.com/drq0rpp.png)

但每次都要這樣找，其實滿累的，[這裡](https://gallery.technet.microsoft.com/How-to-determine-ASPNET-512379b5)有人寫了一個 PowerShell Script 來快速將登錄檔內 .NET Core Hosting Bundle 版本名稱列出來，指令碼如下：

.Net Core
```
$DotNETCoreUpdatesPath = "Registry::HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Updates\.NET Core"
$DotNetCoreItems = Get-Item -ErrorAction Stop -Path $DotNETCoreUpdatesPath
$NotInstalled = $True
$DotNetCoreItems.GetSubKeyNames() | Where { $_ -Match "Microsoft .NET Core.*Windows Server Hosting" } | ForEach-Object {
    $NotInstalled = $False
    Write-Host "The host has installed $_"
}
If ($NotInstalled) {
    Write-Host "Can not find ASP.NET Core installed on the host"
}
```

.NET
```
$DotNETCoreUpdatesPath = "Registry::HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Updates\.NET"
$DotNetCoreItems = Get-Item -ErrorAction Stop -Path $DotNETCoreUpdatesPath
$NotInstalled = $True
$DotNetCoreItems.GetSubKeyNames() | Where { $_ -Match "Microsoft .NET .*Windows Server Hosting" } | ForEach-Object {
    $NotInstalled = $False
    Write-Host "The host has installed $_"
}
If ($NotInstalled) {
    Write-Host "Can not find ASP.NET Core installed on the host"
}
```

使用上相當簡單，基本上只要貼上 PowerShell 上去執行就可以了，下圖的紅框就是執行的結果。

![透過 PowerShell 查詢  .NET Core Hosting Bundle 版本](https://i.imgur.com/urZpiM4.png)

如果你經常需要查詢的話，也可以將這個 PowerShell 指令碼存成檔案，隨時叫用執行（但應該不會需要天天查吧 XD），我個人是存到 [Gist](https://gist.github.com/poychang/239f6a11fd9e9d1606b499839d991b62) 方便我查找。