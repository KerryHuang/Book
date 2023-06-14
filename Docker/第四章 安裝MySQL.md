# Docker - 第四章 | 安裝MySQL

---

前面主要是介紹了下 Dockerfile 的一些常用命令的說明。我們知道，利用 Dockerfile 可以建立一個新的Image，比如運行 Java 環境，就需要一個JDK環境的Image，但直接使用公共的Image時，一般上大小都比較大。所以本章節就主要結合 Dockerfile 文件，建立屬於自己的 Image ，同時對 Image 進行壓縮和優化，同時也是對 Dockerfile 知識的一個實踐。

[官方教學](https://hub.docker.com/_/mysql)

## 搜尋 Image

---

```
docker search mysql
```

[![img](https://morosedog.gitlab.io/images/docker/chapter4/01.png)](https://morosedog.gitlab.io/images/docker/chapter4/01.png)

## 拉取 Image

---

```
docker pull mysql:5.7
```

[![img](https://morosedog.gitlab.io/images/docker/chapter4/02.png)](https://morosedog.gitlab.io/images/docker/chapter4/02.png)

## 查看 Image

---

```
docker images
```

[![img](https://morosedog.gitlab.io/images/docker/chapter4/03.png)](https://morosedog.gitlab.io/images/docker/chapter4/03.png)

## 執行 Image

---

以下提供兩種執行指令，主要差異是在conf、logs、data掛載在預設的位置，或是將其指定到本機上。

```
docker run --name mymysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=root -d mysql:5.7 mysqld
```

- -p 3306:3306：將 Container 的 3306 Port 映射到主機的 3306 Port。 (前面代表主機，後面代表容器)

- -e MYSQL_ROOT_PASSWORD=root：初始化 root 用戶的密碼。

- -d :後台執行 Container ，並返回ID

[![img](https://morosedog.gitlab.io/images/docker/chapter4/04.png)](https://morosedog.gitlab.io/images/docker/chapter4/04.png)

```
cd /Users/morose/Documents/Temp/Docker/MySQL
docker run --name mymysql -p 3306:3306 -v $PWD/conf:/etc/mysql/conf.d -v $PWD/logs:/logs -v $PWD/data:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=root -d mysql:5.7 mysqld
```

- -p 3306:3306：將 Container 的 3306 Port 映射到主機的 3306 Port。 (前面代表主機，後面代表容器

- -v $PWD/conf:/etc/mysql/conf.d：將主機當前目錄下的 conf/my.cnf 掛載到 Container 的 /etc/mysql/my.cnf。

- -v $PWD/logs:/logs：將主機當前目錄下的 logs 目錄掛載到 Container 的 /logs。

- -v $PWD/data:/var/lib/mysql：將主機當前目錄下的data目錄掛載到 Container 的 /var/lib/mysql 。

- -e MYSQL_ROOT_PASSWORD=root：初始化 root 用戶的密碼。

- -d :後台執行 Container ，並返回ID

[![img](https://morosedog.gitlab.io/images/docker/chapter4/05.png)](https://morosedog.gitlab.io/images/docker/chapter4/05.png)

主機當前目錄下的data目錄掛載到 Container 的 /var/lib/mysql

[![img](https://morosedog.gitlab.io/images/docker/chapter4/06.png)](https://morosedog.gitlab.io/images/docker/chapter4/06.png)

## 進入 Container

---

```
docker exec -it mymysql bash
```

- -i ：即使沒有附加也保持STDIN 打開

- -t ：分配一個偽終端

[![img](https://morosedog.gitlab.io/images/docker/chapter4/07.png)](https://morosedog.gitlab.io/images/docker/chapter4/07.png)

## 資料庫測試

---

```
mysql -hlocalhost -p3306 -uroot -proot
```

[![img](https://morosedog.gitlab.io/images/docker/chapter4/08.png)](https://morosedog.gitlab.io/images/docker/chapter4/08.png)

## Database Client 測試

---

這邊使用了 [Navicat Premium] 工具來做連線測試，網路上還有很多 [Database Client] 工具，每個工具都有其特色，建議找個自己用的習慣的工具來做使用，必會事半功倍。

[![img](https://morosedog.gitlab.io/images/docker/chapter4/09.png)](https://morosedog.gitlab.io/images/docker/chapter4/09.png)

[![img](https://morosedog.gitlab.io/images/docker/chapter4/10.png)](https://morosedog.gitlab.io/images/docker/chapter4/10.png)

**恭喜！這邊已經建立一個MySQL資料庫可以做使用了。**

## 使用 Dockerfile 建立

---

首先，建立目錄 mysql 用於存放後面的相關東西。

```
$ mkdir -p ~/mysql/data ~/mysql/logs ~/mysql/conf
```

- data：容器配置的資料文件存放路徑

- logs：目錄將映射為mysql容器的日誌目錄

- conf：目錄裡的配置文件將映射為mysql容器的配置文件

進入建立的 mysql 目錄，建立Dockerfile：

```
FROM debian:jessie

# add our user and group first to make sure their IDs get assigned consistently, regardless of whatever dependencies get added
RUN groupadd -r mysql && useradd -r -g mysql mysql

# add gosu for easy step-down from root
ENV GOSU_VERSION 1.7
RUN set -x \
    && apt-get update && apt-get install -y --no-install-recommends ca-certificates wget && rm -rf /var/lib/apt/lists/* \
    && wget -O /usr/local/bin/gosu "https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg --print-architecture)" \
    && wget -O /usr/local/bin/gosu.asc "https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg --print-architecture).asc" \
    && export GNUPGHOME="$(mktemp -d)" \
    && gpg --keyserver ha.pool.sks-keyservers.net --recv-keys B42F6819007F00F88E364FD4036A9C25BF357DD4 \
    && gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \
    && rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc \
    && chmod +x /usr/local/bin/gosu \
    && gosu nobody true \
    && apt-get purge -y --auto-remove ca-certificates wget

RUN mkdir /docker-entrypoint-initdb.d

# FATAL ERROR: please install the following Perl modules before executing /usr/local/mysql/scripts/mysql_install_db:
# File::Basename
# File::Copy
# Sys::Hostname
# Data::Dumper
RUN apt-get update && apt-get install -y perl pwgen --no-install-recommends && rm -rf /var/lib/apt/lists/*

# gpg: key 5072E1F5: public key "MySQL Release Engineering <mysql-build@oss.oracle.com>" imported
RUN apt-key adv --keyserver ha.pool.sks-keyservers.net --recv-keys A4A9406876FCBD3C456770C88C718D3B5072E1F5

ENV MYSQL_MAJOR 5.6
ENV MYSQL_VERSION 5.6.31-1debian8

RUN echo "deb http://repo.mysql.com/apt/debian/ jessie mysql-${MYSQL_MAJOR}" > /etc/apt/sources.list.d/mysql.list

# the "/var/lib/mysql" stuff here is because the mysql-server postinst doesn't have an explicit way to disable the mysql_install_db codepath besides having a database already "configured" (ie, stuff in /var/lib/mysql/mysql)
# also, we set debconf keys to make APT a little quieter
RUN { \
        echo mysql-community-server mysql-community-server/data-dir select ''; \
        echo mysql-community-server mysql-community-server/root-pass password ''; \
        echo mysql-community-server mysql-community-server/re-root-pass password ''; \
        echo mysql-community-server mysql-community-server/remove-test-db select false; \
    } | debconf-set-selections \
    && apt-get update && apt-get install -y mysql-server="${MYSQL_VERSION}" && rm -rf /var/lib/apt/lists/* \
    && rm -rf /var/lib/mysql && mkdir -p /var/lib/mysql /var/run/mysqld \
    && chown -R mysql:mysql /var/lib/mysql /var/run/mysqld \
# ensure that /var/run/mysqld (used for socket and lock files) is writable regardless of the UID our mysqld instance ends up having at runtime
    && chmod 777 /var/run/mysqld

# comment out a few problematic configuration values
# don't reverse lookup hostnames, they are usually another container
RUN sed -Ei 's/^(bind-address|log)/#&/' /etc/mysql/my.cnf \
    && echo 'skip-host-cache\nskip-name-resolve' | awk '{ print } $1 == "[mysqld]" && c == 0 { c = 1; system("cat") }' /etc/mysql/my.cnf > /tmp/my.cnf \
    && mv /tmp/my.cnf /etc/mysql/my.cnf

VOLUME /var/lib/mysql

COPY docker-entrypoint.sh /usr/local/bin/
RUN ln -s usr/local/bin/docker-entrypoint.sh /entrypoint.sh # backwards compat
ENTRYPOINT ["docker-entrypoint.sh"]

EXPOSE 3306
CMD ["mysqld"]
```

通過Dockerfile建立一個鏡像，替換成你自己的名字。

```
$ docker build -t mysql .
```

建立完成後，我們可以在本地的鏡像列表裡查找到剛剛建立的鏡像。

## 執行.sql檔

---

這邊額外做個筆記，當MySQL Docker建立起來後，我們會需要執行.sql檔來做還原。

- 進入 Container
- 進入 mysql 命令窗
- 執行指令

```
use dbname; //指定要運行的資料庫
source /etc/data/test.sql //執行目錄下的test.sql
```

---

# 【Docker 攻略】MySQL 安裝篇

說明
以下為「 Docker 安裝 MySQL 」影片中，使用到的文件內容。

除了安裝步驟還會介紹 Docker 是什麼 ? 以及為什麼要使用 Docker !

學會後，以後資料庫的安裝，都可以向 Python 的 pip 一樣，一行指令，動作直接完成 !

Docker 官網
https://www.docker.com/

Docker Hub
https://hub.docker.com/_/mysql

Docker 映像
拉取 mysql 映像
```
docker pull mysql:8
```
檢查映像
```
docker images
```

檢查 mysql 映像
```
docker images | grep mysql
```

Output:
```
REPOSITORY   TAG       IMAGE ID       CREATED       SIZE
mysql        8         0716d6ebcc1a   10 days ago   514MB
```

刪除映像
```
docker rmi ${IMAGE ID}
docker rmi 0716d6ebcc1a
```

Docker 容器
運行 mysql 容器
```
docker run --name sql2 -p 3306:3306 -e MYSQL_ROOT_PASSWORD=Dev127336 -d mysql:8
```

參數功能：

run : docker 建立 container 並且執行的指令
--name : 指定容器為 sql2
-p 3306:3306 : 將容器的 3306 端口映射到主機的 3306 端口。
-e MYSQL_ROOT_PASSWORD=Dev127336 : 初始化 root 用戶的密碼為 Dev127336。
-d mysql:8 : 背景執行 MySQL 映像
檢查容器 (運行中)
```
docker ps
```

Output:

```
CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS         PORTS                                                  NAMES
925859fd62b1   mysql:8   "docker-entrypoint.s…"   5 seconds ago   Up 4 seconds   0.0.0.0:3306->3306/tcp, :::3306->3306/tcp, 33060/tcp   sql2
```

停止容器
```
docker stop sql2
```

檢查容器 (全部)
```
docker ps -a
```

Output:
```
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS                       PORTS     NAMES
115863d85607   mysql:8   "docker-entrypoint.s…"   24 seconds ago   Exited (137) 2 seconds ago             sql2
```

啟動容器
```
docker start sql2
```

進入容器
```
docker exec -it sql2 bash
```

退出容器
```
exit
```

刪除容器
```
docker rm sql2
```

進入容器
進入到 Linux 的操作環境
```
docker exec -it sql2 bash
```

登錄 mysql
```
mysql -u root -p
```

修改 Root 密碼
```
ALTER USER 'root'@'localhost' IDENTIFIED BY 'Dev127336';
```

之前如果未設定正確，可以再用 SQL 修改。
添加遠程登錄用戶
```
CREATE USER 'DevAuth'@'%' IDENTIFIED WITH mysql_native_password BY 'Dev127336';
GRANT ALL PRIVILEGES ON *.* TO 'DevAuth'@'%';
CREATE USER : 創建使用者
GRANT : 權限設定
```
SQL 測試
資料庫
```
create database DevDb; -- 創建資料庫
show databases; -- 顯示資料庫
use DevDb; -- 使用資料庫
```
資料表

創建:
```
drop table if exists app_info;
create table app_info (
    id int auto_increment primary key ,
    name nvarchar(50),
    version nvarchar(30),
    author nvarchar(50),
    remark nvarchar(100)
);
```

資料:
```
insert into app_info(name,version,author,remark) values
('JavaProjSE-v1.0.3','1.0.3','Enoxs','Java Project Simple Example - Version 1.0.3'),
('JUnitSE','1.0.2','Enoxs', 'Java Unit Test Simple Example'),
('SpringMVC-SE','1.0.2','Enoxs','Java Web Application Spring MVC - Simple Example （MyBatis）');
```

查詢:
```
select * from app_info;
```

離開 mysql
```
quit
```

退出容器
```
exit
```

Dbeaver
Host : localhost
Port : 3306
Database : DevDb
Username : DevAuth
Password : Dev127336
MySQL Driver
https://www.mysql.com/products/connector/