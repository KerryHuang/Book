---
kind: original
---

# Azure DevOps 持續整合(CI) + Artifacts

## 在.Net  專案中建立 NuGet 套件

建立一個 .Net 類別庫專案
點選專案名稱 按右鍵 選擇屬性
1. 建置 -> 輸出 -> 勾選「產生包含 API 文件的檔案」
2. 套件 -> 一般 -> 勾選「在建置時產生 NuGet 套件」

## CI Pipeline Build

點選 Azure DevOps 左方主選單的 Pipelines -> New Pipeline

Connect：點選 Azure Repos Git
Select：選擇 Git 專案
Configure：ASP.NET Core (.NET Framework)

```yml
trigger:
- master

pool:
  vmImage: 'windows-latest'

variables:
  project: 'Presco.PAYUNI.SDK\Presco.PAYUNI.SDK.csproj'
  buildConfiguration: 'Release'

steps:
- task: DotNetCoreCLI@2
  inputs:
    command: 'build'
    arguments: '-c $(buildConfiguration) -o $(Build.ArtifactStagingDirectory) $(Build.SourcesDirectory)\$(project) /maxcpucount:1'

- task: PublishBuildArtifacts@1
  inputs:
    PathtoPublish: '$(Build.ArtifactStagingDirectory)'
    ArtifactName: 'artifacts'
    publishLocation: 'Container'
```

* 調整 project : 改由發行套件的 .csproj 專案路徑

## 建 Artifacts Feed

點選 Azure DevOps 左方主選單的 Artifacts -> Create Feed

```text
Name：自行定義
```

## 調整 Build Service 權限

點選 Azure DevOps 左方主選單的 Artifacts -> 鋸齒圖案 (Feed Settings)
```text
Feed Settings
點選第二個頁籤(Permissions) -> Add users/groups

User/Group* : [Project name] Build Service 或 Pipeline User name
Role : Contributor
```

## 在 Pipeline Build 中發佈 Artifacts

點選 Azure DevOps 左方主選單的 Pipelines -> Releases -> New -> New Release Pipeline
點選 Select a template 下方的 「Empty job」

1. Artifacts 區塊中點選 Add
```text
Add an artifact
Source type : Build
Project* : 你的專案 (會自動預設在目前專案)
Source (build pipeline)* : 選擇剛建立好的 Build Pipeline
Default version* : Latest (會自動預設在Latest)
Source alias* : (會自動產生)
```
2. Artifacts 區塊中新增 Trigger
```text
Continuous deployment trigger
啟用(Enabled)
Creates a release every time a new build is available.
```

3. Stages 區塊中點選 Add
* 在 Agent job 區塊中右邊點選「+」Add a task to Agent job
* Add tasks 選擇「.Net Core」 
```text
.Net Core 
Display name* : dotnet push (會自動預設 Command 類型)
Command* : 點選「nuget push」
Path to NuGet package(s) to publish* : 選擇 build 完後路徑下的 nupkg 檔案
	例如：(_Presco.PAYUNi/artifacts/Presco.PAYUNI.SDK.1.0.1.nupkg)
	再將 xxxxxxx.nupkg 改為 *.nupkg
	例如：(_Presco.PAYUNi/artifacts/*.nupkg)
Target feed* : 選擇在 Artifacts 建的 Feed
```

---

## Azure DevOps Pipelines 從建置一路到發行Artifacts

```yml
trigger:
- master  # 定義觸發建置的分支

pool:
  vmImage: 'windows-latest'  # 選擇建置代理機器的映像

variables:
  solution: 'Presco.Utility'  # 解決方案名稱
  project: 'Presco.Utility' # 專案名稱
  buildPlatform: 'Any CPU'
  buildConfiguration: 'Release'

steps:
- task: DotNetCoreCLI@2  # 使用DotNetCoreCLI建置解決方案中的所有專案
  displayName: 'dotnet build'
  inputs:
    command: 'build'
    arguments: '-c $(buildConfiguration) -o $(Build.ArtifactStagingDirectory) $(Build.SourcesDirectory)\$(solution)\$(project).csproj /maxcpucount:1'

- task: PublishBuildArtifacts@1  # 上傳Artifacts至Azure Pipelines
  displayName: 'publish build artifacts'
  inputs:
    PathtoPublish: '$(Build.ArtifactStagingDirectory)'
    ArtifactName: 'artifacts'
    publishLocation: 'Container'

- task: NuGetCommand@2  # 使用NuGet命令推送NuGet套件到Azure DevOps Artifacts
  displayName: 'nuget push'
  inputs:
    command: 'push'
    packagesToPush: '$(Build.ArtifactStagingDirectory)/*.nupkg;!$(Build.ArtifactStagingDirectory)/*.symbols.nupkg'  # 指定要推送的NuGet套件檔案的路徑
    nuGetFeedType: 'internal'  # 如果是Azure DevOps Artifacts，請設定為 'internal'
    publishVstsFeed: '641c97c7-78f8-4314-8e9b-3d272cc8325f/533f8755-94c3-4345-b70c-6e6174db92bf'  # 如果是Azure DevOps Artifacts，請提供你的Feed ID
    allowPackageConflicts: false # 當這個參數為false時，當套件版本已經存在於存儲庫中時不再進行處理    
```

## 建置所有專案

```yml
trigger:
- master  # 定義觸發建置的分支

pool:
  vmImage: 'windows-latest'  # 選擇建置代理機器的映像

variables:
  solution: '**/*.sln'  # 解決方案名稱
  project: 'Presco.Utility.Barcode' # 專案名稱
  buildPlatform: 'Any CPU'
  buildConfiguration: 'Release'

steps:
- task: DotNetCoreCLI@2  # 使用DotNetCoreCLI建置解決方案中的所有專案
  displayName: 'dotnet build'
  inputs:
    command: 'build'
    projects: '$(solution)'
    arguments: '-c $(buildConfiguration) -o $(Build.ArtifactStagingDirectory)'

- task: NuGetCommand@2  # 使用NuGet命令推送NuGet套件到Azure DevOps Artifacts
  displayName: 'nuget push'
  inputs:
    command: 'push'
    packagesToPush: '$(Build.ArtifactStagingDirectory)/*.nupkg;!$(Build.ArtifactStagingDirectory)/*.symbols.nupkg'  # 指定要推送的NuGet套件檔案的路徑
    nuGetFeedType: 'internal'  # 如果是Azure DevOps Artifacts，請設定為 'internal'
    publishVstsFeed: '641c97c7-78f8-4314-8e9b-3d272cc8325f/533f8755-94c3-4345-b70c-6e6174db92bf'  # 如果是Azure DevOps Artifacts，請提供你的Feed ID
    allowPackageConflicts: false # 當這個參數為false時，當套件版本已經存在於存儲庫中時不再進行處理   
```