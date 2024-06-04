# 開源程式碼檢測平台 SonarQube

SonarQube 是一個開源的程式檢測平台，旨在幫助軟體開發團隊提升代碼品質和可持續性。它通過靜態代碼分析，識別代碼中的技術債務、缺陷和安全漏洞，並提供即時反饋和詳細報告。

支援多種主流程式語言，如 Java、C#、JavaScript 等，該平台的核心功能包括代碼質量評估、缺陷檢測、安全漏洞掃描、測試覆蓋率分析等。

透過 SonarQube 團隊可以持續監控和改進代碼質量，降低技術債務，增加軟體的可維護性和穩定性，為開發團隊提供了優質代碼的保證，促進軟體項目的成功交付和持續發展。

# SonarQube 安裝

使用 Docker 來搭建 SonarQube 快速又方便

## Install Docker Desktop on Windows

### Get started with Docker for Windows. This guide covers system requirements, where to download, and instructions on how…

docs.docker.com

透過下列指令啟動 SonarQube

```
docker pull sonarqube
docker run --name sonarqube --restart always -p 9000:9000 -d sonarqube
```

開啟瀏覽器[ http://localhost:9000](http://localhost:9000/)，預設的帳號與密碼皆為 admin。

![img](https://miro.medium.com/v2/resize:fit:875/1*mCd8qZH_M6eZZ08fJeuvMw.png)

會要求變更密碼

![img](https://miro.medium.com/v2/resize:fit:875/1*O9SfAWeYkVR52tr9fbhA2g.png)

接下來選擇 Manually 建立專案

![img](https://miro.medium.com/v2/resize:fit:875/1*ODmiMJMsmNCZdDvGathJeQ.png)

輸入專案顯示名稱與專案 Key

- 專案顯示名稱：你開心就好，可以取重複。
- 專案 Key：專案的唯一碼，不得重複。

![img](https://miro.medium.com/v2/resize:fit:875/1*L0hZ-ZDvJW5IZhqxoN5SvQ.png)

定義代碼的哪一部分將被視為新代碼，選擇 Global Setting 即可。

以前的版本：自上一版本以來發生更改的任何代碼都被視為新代碼，推薦用於常規版本或發布之後的項目。

![img](https://miro.medium.com/v2/resize:fit:875/1*pURS6w6Qi0KpXTM-4T8Png.png)

選擇 Locally 分析專案

![img](https://miro.medium.com/v2/resize:fit:875/1*nwpxU3BvRw7BkGXAHaZ9XA.png)

需要產生一個 Token，稍後 Scanner 上傳分析結果使用。

![img](https://miro.medium.com/v2/resize:fit:875/1*1hDMOMGuqRt7oq2SQ0IvXg.png)

點選 Continue

![img](https://miro.medium.com/v2/resize:fit:875/1*PV1wJ2YjW2zF34TjLwLnPg.png)

選擇分析的語言與建置工具，我們用 .NET Core 作為演示範例。

![img](https://miro.medium.com/v2/resize:fit:875/1*Zej3uNqzpprW2GoSELaPXg.png)

# 前置作業

透過命令提示字元安裝 dotnet-sonarscanner。

![img](https://miro.medium.com/v2/resize:fit:875/1*Yy_QLg2W6nLQv1mhX36OGg.png)

```
dotnet tool install --global dotnet-sonarscanner
```

確認一下環境變數 Path 是否存在 dotnet tools 資料夾

![img](https://miro.medium.com/v2/resize:fit:773/1*rsTrkXmwZyMdgWWBWSZcLw.png)

使用 Visual Studio 2022 建立新的專案當作範例

![img](https://miro.medium.com/v2/resize:fit:875/1*cI2nSA1caXI6EdX0XSrysQ.png)

選擇 .NET 6.0

![img](https://miro.medium.com/v2/resize:fit:875/1*5zi_-mqvFaYb3uAtE2jFng.png)

使用命令提示字元切換到專案的根目錄

![img](https://miro.medium.com/v2/resize:fit:875/1*A3LJu6wz3SzA59g9p0Nrmw.png)

輸入以下指令，進行初始化。

```
dotnet sonarscanner begin /k:"WebApplication1" /d:sonar.host.url="http://localhost:9000"  /d:sonar.token="sqp_ac1c05ed18332b7fd3d1f47ae4e381298ff1e3bc"
```

![img](https://miro.medium.com/v2/resize:fit:875/1*VcySC50JlS1dDvR4n05Zeg.png)

會產生一個 .sonarqube 資料夾，用來存放分析的結果。

> 記得將 .sonarqube 加入 .gitignore

![img](https://miro.medium.com/v2/resize:fit:875/1*XRJ4yaM5ih5QIwcfyTFLJA.png)

接下來對專案進行建置

```
dotnet build
```

![img](https://miro.medium.com/v2/resize:fit:875/1*yDur5HCoF_2nxS5OcS7Jng.png)

開始進行分析，並將結果上傳回 SonarQube。

```
dotnet sonarscanner end /d:sonar.token="sqp_ac1c05ed18332b7fd3d1f47ae4e381298ff1e3bc"
```

![img](https://miro.medium.com/v2/resize:fit:875/1*t0LvTXFii039zu0B1kpHRA.png)

若指令出現以下錯誤，請記得安裝 JDK 11。

## Java Archive Downloads - Java SE 11 | Oracle 台灣

### Java Archive Downloads - Java SE 11

| Oracle 台灣 Java Archive Downloads - Java SE 11www.oracle.com

```
ERROR: JAVA_HOME not found in your environment, and no Java
       executable present in the PATH.
Please set the JAVA_HOME variable in your environment to match the
location of your Java installation, or add "java.exe" to the PATH

The SonarScanner did not complete successfully
ERROR: Error during SonarScanner execution
INFO: ------------------------------------------------------------------------
java.lang.UnsupportedClassVersionError: org/sonar/batch/bootstrapper/EnvironmentInformation has been compiled by a more recent version of the Java Runtime (class file version 55.0), this version of the Java Runtime only recognizes class file versions up to 52.0
        at java.lang.ClassLoader.defineClass1(Native Method)
        at java.lang.ClassLoader.defineClass(Unknown Source)
        at java.security.SecureClassLoader.defineClass(Unknown Source)
        at java.net.URLClassLoader.defineClass(Unknown Source)
        ...
ERROR:
The SonarScanner did not complete successfully
```

回到 Projects 就可看到分析後的結果

![img](https://miro.medium.com/v2/resize:fit:875/1*lZvBGcTjWLqj0hmMPFOe-g.png)

SonarQube 會將程式碼中可能潛藏的問題分為以下 3 種

- **Bug：**可能導致運行時錯誤或意外行為的編碼錯誤
- **Vulnerability：**代碼中容易受到攻擊的點
- **Code Smell：**可維護性問題，使您的代碼混亂且難以維護。

Security Hotspotsy 代表需要手動檢查以評估是否存在漏洞的安全敏感代碼。

![img](https://miro.medium.com/v2/resize:fit:875/1*EWX6mqHRTh-nV4hKBeJTyw.png)

# Overview

進入專案後可以看到 Measures 分為 2 種

- New Code：我們選擇 Global Setting，代表自上一版本以來發生更改的任何代碼都被視為新代碼。
- Overall Code：總體代碼的分析結果

基本上，我們只需要察看 Overall Code 的分析結果即可，除非想要知道新增的代碼的分析結果，才需要切到 New Code 查看。

![img](https://miro.medium.com/v2/resize:fit:875/1*cHj3rfC3yXltOv0xcchRnA.png)

New Code 的定義可在 Project Settings 的 New Code 進行修改，例如選擇 Number of Days 定義將多少天前的代碼視為 New Code。

# Issues

SonarQube 除了將被檢測出的問題分類為上述其中一種類型之外，也將問題依嚴重性分為 5 種程度。透過這些分類，使用者可迅速地查看程式碼哪個部分存在何種問題，並可根據嚴重性決定修復的優先順序，以提升維護程式碼品質的效率。

依嚴重性分為 5 種程度

1. **BLOCKER**：很可能影響生產中應用程式行為的錯誤。例如，記憶體洩漏或未關閉的 JDBC 連接都是必須立即修復的 BLOCKER 。
2. **CRITICAL**：影響生產中應用程式行為的可能性較低的錯誤或代表安全缺陷的問題。空的 Catch 區塊或 SQL 注入將是一個關鍵問題，必須立即審查程式碼。
3. **MAJOR**：可能嚴重影響開發人員生產力的質量缺陷。未覆蓋的程式碼、重複的區塊或未使用的參數都是主要問題的示例。
4. **MINOR**：可能會輕微影響開發人員生產力的質量缺陷。例如，行不應該太長，Switch 語句應該至少有 3 種情況，都被認為是次要問題。
5. **INFO**：既不是錯誤也不是質量缺陷，只是一個發現。

![img](https://miro.medium.com/v2/resize:fit:875/1*d8Ao8TIM7G-OqoMp4SGUow.png)

實際挑一個 Issue 來說明，SonarQube 偵測到有未使用的變數

Where is the issue？第 4 行清楚的告知作者是誰，以及第 9 行宣告的 _logger 未使用。

![img](https://miro.medium.com/v2/resize:fit:875/1*X8OMbL6rpWSSFwVBc4nyxA.png)

Why is this an issue？則會提供程式範例告訴你問題在哪以及如何修改。

![img](https://miro.medium.com/v2/resize:fit:875/1*OlKZEmUWWHJk6JIv768WtA.png)

More Info 則提供該 Issue 屬於哪種通用弱點列舉 CWE

![img](https://miro.medium.com/v2/resize:fit:875/1*Ag_fzfSQRq9-2O2UskeReQ.png)

專案若有加入 Git 版控，SonarQube 還會幫您統計每位作者的 Issue 數量，就可以知道團隊誰寫的程式品質不好。

![img](https://miro.medium.com/v2/resize:fit:875/1*WZakfzg4_iCz_mbi3mKl4A.png)

# Measures

將檢測到的問題依照分類透過圖表的方式呈現

![img](https://miro.medium.com/v2/resize:fit:875/1*7HH9GIPYCZ6FI10QV6oqWw.png)

# Code

將檢測到的問題依照專案結構使用表格呈現

![img](https://miro.medium.com/v2/resize:fit:875/1*3wR-AzXPXhTM4EHRSgXH-g.png)

# Activity

我們可以在 Activity 找到 SonarQube 每次分析的趨勢圖，例如第 2 次推送的結果 Code Smell 數量降低了。

![img](https://miro.medium.com/v2/resize:fit:875/1*7RMyaoc0nRTp61YX1CeZOg.png)

# Generate Tokens

還記得 Sonarscanner 需要 Token 才能將分析結果回傳至 SonarQube，如果我們忘記 Token 該怎麼辦？

點選右上方的 My Account 切換到 Security 頁籤，在這邊我們可以新建或者撤銷已經忘記的 Token。

![img](https://miro.medium.com/v2/resize:fit:875/1*PdJZb61R0v20-jmn23t2vg.png)

記得將 Token 給抄下來，只會出現一次喔。

![img](https://miro.medium.com/v2/resize:fit:875/1*SYrNgfGLmPMaMId0iKXkWg.png)

使用新的 Token 就可以繼續進行檢測

```
dotnet sonarscanner begin /k:"WebApplication1" /d:sonar.host.url="http://localhost:9000"  /d:sonar.token="sqp_ff2d695d1ef2bd42f97270f0b9fafaf3c2661698"
dotnet build
dotnet sonarscanner end /d:sonar.token="sqp_ff2d695d1ef2bd42f97270f0b9fafaf3c2661698"
```

# Rule

我們可以在 Rules 找到 SonarQube 每種程式語言的檢查規則，例如 C# 總共有 424 項。

![img](https://miro.medium.com/v2/resize:fit:875/1*qWZoEcm30XCPoNPvsFFtJA.png)

# Quality Profiles

每次 SonarQube 掃描到底要檢測多少規則，實際是透過 Quality Profiles 進行控制的，而預設的設定檔是無法修改的。

![img](https://miro.medium.com/v2/resize:fit:875/1*s7gCoAK6Kqn3WNdO-OIrtQ.png)

從上面的 Rules 我們知道 C# 總共有 424 項規則，預設的設定檔 Sonar Way 只啟用了 283 項規則，是沒有辦法將其中任何一條規則禁用的。

![img](https://miro.medium.com/v2/resize:fit:875/1*pLGCLt3SJQBxFqbX3ck1dA.png)

我們可以點選 Extend 或者 Copy 來進行調整

- Extend：繼承 Sonar Way 設定檔，已經啟用的規則無法修改，只能將原本禁用的規則進行啟用。
- Copy：複製 Sonar Way 設定檔，可以進行任何異動。

一般實務上，不太會直接使用預設的 Sonar Way 設定檔，因為它啟用的規則太多了。

透過右上角的 Create，建立屬於我們自己的設定檔。

![img](https://miro.medium.com/v2/resize:fit:875/1*DXpzz5oLADOBNFcyLWpPvQ.png)

再來挑選我們想要啟用的規則

![img](https://miro.medium.com/v2/resize:fit:875/1*L-ZuC-IVtnesQdJqsa_AqA.png)

回到 Project Settings 的 Quality Profiles 調整為自定義的 Profiles

![img](https://miro.medium.com/v2/resize:fit:875/1*_sSWr6-KTWfhuujULQx6Lg.png)

會在再下一次分析才生效

![img](https://miro.medium.com/v2/resize:fit:875/1*kqOF64xNRyn5NQNhNujSUA.png)

# Quality Gates

專案的分析結果是否通過，我們可以在 Quality Gates 查看與調整檢測的評分標準。

![img](https://miro.medium.com/v2/resize:fit:875/1*fvFfsuZh1ZUE1fPiN249SA.png)

今天的分享就到這邊，感謝收看。