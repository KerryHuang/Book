# Docker Desktop (含更改 Docker Image 路徑)


在 Windows 10 要能充分整合 Docker 應用與開發，安裝 [Docker Desktop](https://www.docker.com/products/docker-desktop) 是最理想的。

關於 Docker Desktop 可以參考[官方文件的介紹](https://docs.docker.com/desktop/)。

> Docker Desktop is an easy-to-install application for your Mac or Windows environment that enables you to build and share containerized applications and microservices.
> Docker Desktop includes Docker Engine, Docker CLI client, Docker Compose, Docker Content Trust, Kubernetes, and Credential Helper.

安裝 Docker Desktop 之前，要先確認在 Windows 10 系統上已安裝建置好 WSL 2 的 Linux 子系統，可以參考前寫的：[[安裝筆記\] Windows 10 安裝 Linux 子系統 (WSL2)。](http://www.kenming.idv.tw/note_window10_install_wsl2/)

安裝 Docker Desktop 只要[下載官方的安裝檔](https://desktop.docker.com/win/main/amd64/Docker Desktop Installer.exe?utm_source=docker&utm_medium=webreferral&utm_campaign=dd-smartbutton&utm_location=header)並執行安裝即可。這裡有篇很詳細的安裝文件，可以參考：[How to Set Up Docker in WSL [Step-by-Step\]](https://andrewlock.net/installing-docker-desktop-for-windows/)。

安裝完 Docker Desktop，系統會提示登出 (logout) 再重新登入，如此 Docker 已常駐於系統 (可觀察工作列的通知區有否鯨魚圖示)，點擊該圖示即可出現 Docker Desktop 操作介面。
[![[安裝筆記\] Windows 10 WSL 2 安裝 Docker Desktop (含更改 Docker Image 路徑)](http://images.kenming.idv.tw/2021/07-12/docker-01.png)](http://images.kenming.idv.tw/2021/07-12/docker-01.png)



#### 更改 Docker Image 路徑

預設 Docker Image (WSL 2 docker-desktop-data vm disk image) 是儲放於：

```
%USERPROFILE%\AppData\Local\Docker\wsl\data\ext4.vhdx
```

這個儲放路徑是可以更改的，以免佔用到系統主磁碟空間 (Disk C)。

參考這篇教學文：[HowTo: Change Docker containers storage location with WSL2 on Windows 10](https://blog.codetitans.pl/post/howto-docker-over-wsl2-location/)，打開「PowerShell」，執行以下操作命令。

1. 檢視 WSL 狀態：

   ```
   wsl -l -v
   ```

   [![Docker Desktop UI](http://images.kenming.idv.tw/2021/07-12/docker-02.png)](http://images.kenming.idv.tw/2021/07-12/docker-02.png)

2. 關閉 WSL：

   ```
   wsl --shutdown
   ```

   ```
     NAME                   STATE           VERSION
   * docker-desktop         Stopped         2
     docker-desktop-data    Stopped         2
   ```

3. 匯出 (export) docker-desktop-data：

   ```
   wsl --export docker-desktop-data "D:\Docker\wsl\data\docker-desktop-data.tar"
   ```

4. 註銷 (unregister) docker-desktop-data，會自動移除原路徑上的 ext4.vhdx 檔案。

   ```
   wsl --unregister docker-desktop-data
   ```

5. 匯入 docker-desktop-data 回 WSL 並指定所匯入的路徑 (預先已創建路徑)：

   ```
   wsl --import docker-desktop-data "D:\Docker\wsl\data" "D:\Docker\wsl\data\docker-desktop-data.tar" --version 2
   ```

重新啟動 Docker Desktop，當啟動正常，可以刪除原匯出的檔案：*D:\Docker\wsl\data\docker-desktop-data.tar*。