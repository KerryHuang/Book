---
kind: reprint
source: https://www.cnblogs.com/liang24/p/13910368.html
author: liang24 (91suke)
---

# ASP.NET Core Authentication系列（一）理解Claim, ClaimsIdentity, ClaimsPrincipal

# 前言

首先我們來看一下在ASP.NET時代，Authentication是如何使用的。下面介紹的是`System.Web.Security.FormsAuthentication`：

```scss
// 登录
System.Web.Security.FormsAuthentication.SetAuthCookie("userName", false);

if(User.Identity.IsAuthenticated) {  // 已认证
    
}

// 退出登录
System.Web.Security.FormsAuthentication.SignOut();
```

這是一個最簡單的認證用法：

1. 用戶填寫賬號密碼並提交登錄；
2. 服務器應用通過`System.Web.Security.FormsAuthentication.SetAuthCookie(string userName, bool createPersistentCookie)`來生成Auth Cookie，並返回到browser；
3. 用戶進行下一個操作時，會帶上Auth Cookie發到服務器應用；
4. 服務器應用解析並綁定到`Controller.User`屬性上，通過`User.Identity.IsAuthenticated`判斷用戶是否已認證；
5. 最後通過`System.Web.Security.FormsAuthentication.SignOut()`來刪除Auth Cookie；

想要設置生成的Auth Cookie屬性，可以通過修改`web.cofig`的`<authentication>`配置項：

```xml
<configuration>
  ...
  
  <system.web>
    <authentication mode="Forms" >
      <forms cookieless="UseCookies" domain="" path="" name="" timeout="" loginUrl=""></forms>
    </authentication>
    
  </system.web> 
  
  ....
</configuration>
```

更多配置項可查看[FormsAuthenticationConfiguration](https://docs.microsoft.com/zh-cn/dotnet/api/system.web.configuration.formsauthenticationconfiguration?view=netframework-4.8)。

# Authentication in ASP.NET Core

雖然ASP.NET與ASP.NET Core的底層設計很不一樣，但Authentication的基本用法並沒有太大的改變，同樣通過`HttpContext.User`來判斷認證。

ASP.NET的Authorisation是role-based的，而ASP.NET Core的是基於claims-based的（雖然ASP.NET Core同樣支持role-based，但這更多是為了向後兼容，推薦使用claims-based）。

# Claims-based authentication

要理解Claims-based authentication，就必須理解Claim, ClaimsIdentity, ClaimsPrincipal這三者的關係。

**Claim**是對被認證主體特徵的一種表述，比如：登錄用戶名是...，email是...，用戶Id是...，其中的“登錄用戶名”，“email”，“用戶Id”就是ClaimType。

對應現實中的事物，比如駕照，駕照中的“身份證號碼：xxx”是一個claim，“姓名：xxx”是另一個claim。

一組claims構成了一個identity，具有這些claims的identity就是**ClaimsIdentity**，駕照就是一種ClaimsIdentity，可以把ClaimsIdentity理解為“證件”，駕照是一種證件，護照也是一種證件。

ClaimsIdentity的持有者就是**ClaimsPrincipal**，一個ClaimsPrincipal可以持有多個ClaimsIdentity，就比如一個人既持有駕照，又持有護照。

# 舉例說明

上面對Claim, ClaimsIdentity, ClaimsPrincipal三者的描述可能還有些不太好理解，下面會舉例說明這三者的關係：

以登機為例，在登機前需要完成以下步驟：

1. 取登機牌
2. 過安檢
3. VIP區候機（假設你是VIP）

### 1. 取登機牌

你到了機場，要向客服打印登機牌（雖然現在已經是通過機操打印的了），客服問你叫什麼名字，並要求出示能證明你名字的相關證書，例如Passport，其中名字就是一個`Claim`，Passport就是一個`ClaimsIdentity`。

### 2. 過安檢

當你拿到了登機牌（BoardingPass）並準備過安檢，此時安檢人員要求你出示航班號，此時你拿出登機牌給安檢人員查看航班號，其中航班號就是一個`Claim`，BoardingPass就是一個`ClaimsIdentity`。

### 3. VIP區候機

當你通過安檢進入了候機區，你是機場的VIP，就打算到VIP區休息一下，此時工作人員要求你出示VIP號，你拿出VIP片給工作人員查看，其中VIP號就是一個`Claim`，VIP片就是一個`ClaimsIdentity`。

上面的每個步驟如果都不能出示相應的`ClaimsIdentity`就會被拒絕執行指示，下面的圖展示了這個過程：

![image](https://andrewlock.net/content/images/2016/08/Untitled.png)

最後全部的`ClaimsIdentity`代表了你本人，而你就是`ClaimsPrincipal`。

# 參考資料

- [Introduction to Authentication with ASP.NET Core](https://andrewlock.net/introduction-to-authentication-with-asp-net-core/)
- [理解ASP.NET Core驗證模型(Claim, ClaimsIdentity, ClaimsPrincipal)不得不讀的英文博文](https://www.cnblogs.com/dudu/p/6367303.html)
