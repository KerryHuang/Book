# 第八章 安裝SonarQube

SonarQube 是一套 `程式碼品質檢查工具`，可以幫我們檢查 code 的 bugs、 vulenrability、code smell 與 duplication，也屬於 `持續整合` 重要的一環，亦可使用 Docker 安裝，將來管理會更加容易。



## Version

------

macOS High Sierra 10.13.3
Docker for Mac 18.03.0-ce-mac59 (23608)
SonarQube 6.7.2 (build 37468)

## 下載 Docker Image

------

```
$ docker run -d --name sonarqube -p 9000:9000 -p 9092:9092 sonarqube:lts
```

使用 `docker run` 下載 image 並建立 container 並執行之。

- **-d**：`d` etach，建立 container 後，就脫離目前 process

- **–name**：替 container 取一個人能夠識別的名字

- **-p**：Docker 外部與 SonarQube內部所對應的 port，其中左邊為外部 Docker 的 port，右邊為 SonarQube 內部的 port

- **sonarqube:lts**：SonarQube 的 LTS 版本，目前為 `6.7.2`

  若要下載最新版 SonarQube，可使用以下指令：

```
docker run -d --name sonarqube -p 9000:9000 -p 9092:9092 sonarqube
```

不指定為 LTS 版，則下載最新版 SonarQube。

[![ocker00](https://old-oomusou.goodjack.tw/images/sonarqube/docker/docker000.png)](https://old-oomusou.goodjack.tw/images/sonarqube/docker/docker000.png)

1. 輸入 `docker run …` 下載 SonarQube 的 docker image，並建立 container 執行之

[![ocker00](https://old-oomusou.goodjack.tw/images/sonarqube/docker/docker001.png)](https://old-oomusou.goodjack.tw/images/sonarqube/docker/docker001.png)

輸入 `localhost:9000`，若看到 SonarQube 首頁，則表示安裝成功。

## 啟動 SonarQube

------

```
$ docker start sonarqube
```

使用 `docker start` 啟動 SonarQube container。

[![ocker00](https://old-oomusou.goodjack.tw/images/sonarqube/docker/docker003.png)](https://old-oomusou.goodjack.tw/images/sonarqube/docker/docker003.png)

1. 輸入 `docker start sonarqube` 啟動 SonarQube container

## 停止 SonarQube

------

```
$ docker stop sonarqube
```

使用 `docker stop` 停止 SonarQube container。

[![ocker00](https://old-oomusou.goodjack.tw/images/sonarqube/docker/docker002.png)](https://old-oomusou.goodjack.tw/images/sonarqube/docker/docker002.png)

1. 輸入 `docker stop sonarqube` 停止 sonarqube container



#### 安裝 SonarQube 中文化套件 (Traditional Chinese Language Pack)

工具列上找到 Administration (配置) 點選後，在點選 Marketplace (應用市場)，輸入 Traditional Chinese Language Pack，按下安裝。



#### 安裝 SonarQube 報表套件 (SonarQube CNES Report)

工具列上找到 Administration (配置) 點選後，在點選 Marketplace (應用市場)，輸入 SonarQube CNES Report，按下安裝。