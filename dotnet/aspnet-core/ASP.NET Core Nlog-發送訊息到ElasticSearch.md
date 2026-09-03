---
kind: reprint
source: https://www.dotblogs.com.tw/Null/2020/08/10/112748
author: Null
---

# ASP.NET Core Nlog-發送訊息到ElasticSearch

### [ASP.NET Core] 透過 NLog 發送訊息到 ElasticSearch

在內部架了一套ELK，透過NLog把訊息一併發送給ElasticSearch，筆記一下過程

## 環境

- [ASP.NET](http://asp.net/) Core 3.1
- NLog.Web.AspNetCore 4.9.3
- ElasticSearch 7.8

## Nuget

安裝Nuget套件

```
dotnet add package NLog.Web.AspNetCore
dotnet add package NLog.Targets.ElasticSearch
```

## NLog.config

加上 ElasticSearch 的 target，相關參數說明可參考 [NLog.Targets.ElasticSearch 的 GitHub Wiki](https://github.com/markmcdowell/NLog.Targets.ElasticSearch/wiki)

```
<target name="ElasticSearch"
        xsi:type="ElasticSearch"
        index="nlog-elk-${date:format=yyyy.MM.dd}"
        documentType="logevent"
        includeAllProperties="true"
        layout="[${date:format=yyyy-MM-dd HH\:mm\:ss}][${level}] ${logger} ${message} ${exception:format=toString}">
    <field name="MachineName" layout="${machinename}" />
    <field name="ClientIp" layout="${aspnet-request-ip}" />
    <field name="TraceId" layout="${aspnet-TraceIdentifier}" />
    <field name="Time" layout="${longdate}" />
    <field name="level" layout="${level:uppercase=true}" />
    <field name="logger" layout=" ${logger}" />
    <field name="message" layout=" ${message}" />
    <field name="exception" layout=" ${exception:format=toString}" />
    <field name="processid" layout=" ${processid}" />
    <field name="threadname" layout=" ${threadname}" />
    <field name="stacktrace" layout=" ${stacktrace}" />
    <field name="Properties"
           layout="${machinename} ${longdate} ${level:uppercase=true} ${logger} ${message} ${exception}|${processid}|${stacktrace}|${threadname}" />
</target>
```

記得加上 roles

```
<rules>
    <logger name="*" minlevel="Info" writeTo="ElasticSearch" />
</rules>
```

## ElasticSearch Url

查閱到 ElasticSearch 的 Url 設定，目前有看到有幾種方式

1. 在 target 指定 ConnectionStringName，並且在 appsetting.json 指定對應的連線位置![img](https://i.imgur.com/uRC9ceD.png)
2. 在 target 指定 url，值則是透過 Layout Renderer 取得，需要安裝 nuget package

```
NLog.Extensions.Logging
<target name="ElasticSearch"
        xsi:type="ElasticSearch"
        url="${configsetting:item=ConnectionStrings.ElasticUrl}"
>
...
</target>
```

1. 直接在Nlog.config指定實際位址

```
<target name="ElasticSearch"
        xsi:type="ElasticSearch"
        url="http://127.0.0.1:9200/"
>
...
</target>
```

1. 從 Startup 直接指定 url 的值

```
public void Configure(IApplicationBuilder app, ILogger<Startup> logger)
{
    var logFactory = LogManager.LoadConfiguration("NLog.config");
    var target = (ElasticSearchTarget)logFactory.Configuration.FindTargetByName("ElasticSearch");
    target.Uri = Configuration["Elastic:Url"];
}
// appsetting.json
"Elastic": {
    "Url":"http://127.0.0.1:9200/"
}
```

個人測試只有3跟3可以正常運作，考慮不同環境會有需要不同的ElasticSearch Url，故最後採用第4種做法

## 參考

[[ASP.NET Core] 透過 NLog 發送訊息到 ElasticSearch](https://www.dotblogs.com.tw/Null/2020/08/10/112748)