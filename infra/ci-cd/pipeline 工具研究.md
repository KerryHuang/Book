---
kind: original
---

# pipeline工具研究

## SonarQube

#### 版本比較

* SonarCloud只針對開發人員報告，跟sonarqube Community一樣(企業版有更多分析的報表)
* SonarCloud跟雲端集成，不需要管理版本，SonarQube需要自己管理版本
* SonarCloud要收費，SonarQube Community免費
* SonarQube Community : Azure pipelines will work on master branch only
* SonarQube Developer : Azure pipelines will work on master branches, other branches and for PR decoration
* SonarCloud : Work like the SQ Developer edition.

***

#### 安裝流程

總覽: [SonarQube跟Azure DevOps整合](https://docs.sonarqube.org/9.6/devops-platform-integration/azure-devops-integration/#analyzing-projects-with-azure-pipelines)

1. 自建SonarQube Server [各種安裝方式指示](https://docs.sonarqube.org/9.8/setup-and-upgrade/install-the-server/#installing-sonarqube-from-the-docker-image)
   1.  [下載](https://www.sonarsource.com/products/sonarqube/downloads/)

       * 如果用docker建環境的話，因為SonarQube有使用到ElasticSearch，要先將資源設定成符合ElasticSearch啟用的最低需求 [參考](https://www.elastic.co/guide/en/elasticsearch/reference/current/docker.html#\_windows\_with\_docker\_desktop\_wsl\_2\_backend)

       ```powershell
       wsl -d docker-desktop
       sysctl -w vm.max_map_count=262144
       ```
   2. 安裝完成後預設部署在 http://localhost:9000，預設系統管理員帳密: admin/admin
2. 整合SonarQube Server可連結到Azure DevOps
   1. 在Azure DevOps的 UserSetting -> Personal Access Tokens 建立一個 Code > Read & Write 的權杖
   2. 在SonarQube Server的 Administration -> DevOps Platform Integrations -> Azure DevOps-> Create a configuration 輸入相關資料跟權杖
3. 在SonarQube Server建立Project
   1. Project -> create project -> From Azure DevOps 選專案
   2. 透過Azure Pipelines進行分析
   3. 複製第三步的 Project Key，之後Pipeline要用
4. 在SonarQube Server建立Token
   * MyAccount -> Security -> Generate Tokens
     * Token Name，之後Service Connection要用
     * Type: Global/Project Analysis Token
5. 建立 http://localhost:9000 的外網連結
6. 安裝Azure DevOps套件 [SonarQube](https://marketplace.visualstudio.com/items)
7. 在Azure DevOps建立Service Connection
   * Project -> Project Setting -> Service connections 選擇SonarQube
     * Server Url = http://localhost:9000 的外網連結
     * Token = 第4點的Token
     * Service connection name，之後Pipeline要用
8. 建立Pipeline

```yaml
trigger:
- master # or the name of your main branch

steps:
# Prepare Analysis Configuration task
- task: SonarQubePrepare@5
  inputs:
    SonarQube: '{Service connection name}'
    scannerMode: 'MSBuild'
    projectKey: '{Project Key}'

# Dotnet build task
- task: DotNetCoreCLI@2
  displayName: 'dotnet build'
  inputs:
    command: 'build'

# Run Code Analysis task
- task: SonarQubeAnalyze@5

# Publish Quality Gate Result task
- task: SonarQubePublish@5
  inputs:
    pollingTimeoutSec: '300'
```

9. 以上部署完成。執行完分析後，報告會在SonarQube Server頁面上出現

## Mend Bolt

* https://docs.mend.io/bundle/community\_tools/page/mend\_bolt\_for\_azure\_pipelines.html
* https://learn.microsoft.com/en-us/azure/devops/organizations/accounts/connect-organization-to-azure-ad?view=azure-devops
* https://portal.azure.com/
