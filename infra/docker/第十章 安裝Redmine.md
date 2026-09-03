---
kind: reprint
source: site:ithelp.ithome.com.tw
---

# Docker - 第十章 | 安裝 Redmine

Redmine 是一個開源(Open Source)的項目管理系統，相信很多人早已對它不陌生。它的優點非常多，無論是免費、多國語系、角色管理、權限管理、問題追蹤、甘特圖以及日曆功能等等；但說到它的缺點，相信很多人的共識就是它在安裝和管理上並不容易，不過近年已有一鍵安裝(Bitnami Redmine Stack)、虛擬機器(Virtual Machine)或是容器(Docker)的安裝方式，也算是越來越便利了。

以下就用 Docker 的方式來建置 Redmine 的應用服務。

Install Redmine

鏡像內置SQLite3

```
docker run -d --name redmine -p 3000:3000 redmine:latest
```

創建 MySQL 的容器，在這裡指定的是 5.6 版本

```
docker run --name mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=root -d mysql:5.6
```
建立新資料庫，並直接指定UTF8字符集
```sql
CREATE DATABASE redmine CHARACTER SET utf8 COLLATE utf8_unicode_ci;

CREATE DATABASE redmine CHARACTER SET utf8;
RAILS_ENV=production REDMINE_LANG=zh-TW bundle exec rake redmine:load_default_data
```

創建 Redmine 的容器，並將資料庫指向(link)建立好的 MySQL 5.6 容器
```
docker run -d --name myredmine -p 8080:3000 -v /opt/redmine/data:/usr/src/redmine/files --link mysql:mysql redmine
```
或 Windows 
```
docker run -d --name myredmine -p 8080:3000 -v d:/docker/redmine:/usr/src/redmine/files --link mysql:mysql redmine
```

接著在瀏覽器上就可以看到建置好的 Redmine 頁面
![img](https://ithelp.ithome.com.tw/upload/images/20190308/20111830cjUgP8gIsv.png)

點選「登入」後，進入登入頁面，預設的帳號為 admin，密碼為 admin
![img](https://ithelp.ithome.com.tw/upload/images/20190308/20111830sOmqgHkV7m.png)

第一次登入成功後，系統會要求變更密碼
![img](https://ithelp.ithome.com.tw/upload/images/20190308/201118309O54YtjQ8W.png)

修改密碼完成後，就可以開始使用、管理 Redmine 了
![img](https://ithelp.ithome.com.tw/upload/images/20190308/201118307Zs9AXzWvV.png)