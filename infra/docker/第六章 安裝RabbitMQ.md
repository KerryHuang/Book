---
kind: reprint
source: site:morosedog.gitlab.io
author: morosedog
---

# Docker - 第六章 | 安裝RabbitMQ

---

後面會使用到RabbitMQ，讓我們直接開始使用Docker啟動一個RabbitMQ環境吧。 在 docker hub 上 rabbitmq 的 tag 很多，但是我們使用 management ，因為可以看到監控頁面。

[官方教學](https://hub.docker.com/_/rabbitmq)

## 搜尋 Image
---
```
docker search rabbitmq:management
```

[![img](https://morosedog.gitlab.io/images/docker/chapter6/01.png)](https://morosedog.gitlab.io/images/docker/chapter6/01.png)

## 拉取 Image
---
```
docker pull rabbitmq:management
```

[![img](https://morosedog.gitlab.io/images/docker/chapter6/02.png)](https://morosedog.gitlab.io/images/docker/chapter6/02.png)

## 查看 Image
---
```
docker images
```

[![img](https://morosedog.gitlab.io/images/docker/chapter6/03.png)](https://morosedog.gitlab.io/images/docker/chapter6/03.png)

## 執行 Image
---
以下提供兩種執行指令，主要差異是在是否指定用戶和密碼。

```
docker run --name myrabbitmq -p 15672:15672 -p 5672:5672 -d rabbitmq:management
```

* --name myrabbitmq ：將 Container 取名為 myrabbitmq 
* -p 15672:15672 ：將 Container 的 15672 Port 映射到主機的 15672 Port (前面代表主機，後面代表容器) 
* -p 5672:5672 ：將 Container 的 5672 Port 映射到主機的 5672 Port (前面代表主機，後面代表容器) -d :後台執行 Container ，並返回ID 
* rabbitmq:management ：指定安裝的鏡像rabbitmq:management

[![img](https://morosedog.gitlab.io/images/docker/chapter6/04.png)](https://morosedog.gitlab.io/images/docker/chapter6/04.png)

## 登入管理介面
---
```
http://localhost:15672/ 預設用戶/密碼：guest/guest
```

[![img](https://morosedog.gitlab.io/images/docker/chapter6/06.png)](https://morosedog.gitlab.io/images/docker/chapter6/06.png)

```
docker run --name myrabbitmq -p 15672:15672 -p 5672:5672 -e RABBITMQ_DEFAULT_USER=user -e RABBITMQ_DEFAULT_PASS=123 -d rabbitmq:management
```

* --name myrabbitmq ：將 Container 取名為 myrabbitmq 
* -p 15672:15672 ：將 Container 的 15672 Port 映射到主機的 15672 Port (前面代表主機，後面代表容器) 
* -p 5672:5672 ：將 Container 的 5672 Port 映射到主機的 5672 Port (前面代表主機，後面代表容器) 
* -e RABBITMQ_DEFAULT_USER=user ：設定登入用戶user 
* -e RABBITMQ_DEFAULT_PASS=123 ：設定登入密碼123 
* -d :後台執行 Container ，並返回ID 
* rabbitmq:management ：指定安裝的鏡像rabbitmq:management

[![img](https://morosedog.gitlab.io/images/docker/chapter6/05.png)](https://morosedog.gitlab.io/images/docker/chapter6/05.png)

## 登入管理介面
---
```
http://localhost:15672/ 用戶/密碼：user/123
```

- 原預先用戶/密碼，已經無法登入
![img](https://morosedog.gitlab.io/images/docker/chapter6/07.png)](https://morosedog.gitlab.io/images/docker/chapter6/07.png)

- 使用user/123登入
[![img](https://morosedog.gitlab.io/images/docker/chapter6/08.png)](https://morosedog.gitlab.io/images/docker/chapter6/08.png)

