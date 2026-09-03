---
kind: reprint
source: site:blog.hungwin.com.tw
author: hungwin
---

在學習 C# 與資料庫的互動方式，有一個常見且實用的教學就是會員登入、註冊與修改會員資料等範例，學習過程中會用到資料庫新增、修改與查詢動作，是理解程式與資料庫互動的常見程式碼。
當學會了這個範例，將來為客戶開發系統的時候，馬上可以派上用場。

此篇文章是繼上一篇文章: [前台會員修改個人資料範例 #CH3](https://blog.hungwin.com.tw/aspnet-mvc-member-edit-profile/) 接續教學。
此範例展示會員忘記密碼時，輸入帳號至後端查詢信箱後，寄送驗證碼至會員信箱，在信件中有連結回網站重設密碼。

範例內容主要以 ASP.NET MVC 為核心，前端使用 Vue.js 框架，而後端使用 SQL Server 當資料庫。

編寫此教學文章是為了幫助更多新加入的軟體工程師們，有更簡單實用的範例，可以快速學習
C# 與資料庫程式語言。
文末有提供此操作範例的完整程式碼下載，有需要可以自行下載瀏覽。

##### 目錄
[1 在 MemberController 增加忘記密碼頁面](#step1)  
&emsp;&emsp;[1.1 增加忘記密碼連結](#step2)  
&emsp;&emsp;[1.2 增加忘記密碼頁面](#step3)  
&emsp;&emsp;[1.3 增加忘記密碼頁面 View](#step4)  
[2 編寫「忘記密碼」 View 語法](#step5)  
[3 編寫「寄送驗證碼」Controller 語法](#step6)  
&emsp;&emsp;[3.1 調整 Web.config](#step7)  
&emsp;&emsp;[3.2 調整 Google 發信設定](#step8)  
&emsp;&emsp;[3.3 增加忘記密碼 Model](#step9)  
[4 測試忘記密碼](#step10)  
[5 在 MemberController 增加重設密碼頁面](#step11)  
&emsp;&emsp;[5.1 增加重設密碼頁面 View](#step12)  
[6 編寫「重設密碼」 View 語法](#step13)  
[7 編寫「重設密碼」Controller 語法](#step14)  
&emsp;&emsp;[7.1 增加重設密碼 Model](#step15)  
[8 測試忘記密碼與重設密碼功能](#step16)  
[9 重點整理](#step17)  
&emsp;&emsp;[9.1 範例下載](#step18)

## 在 MemberController 增加忘記密碼頁面

### 增加忘記密碼連結

這次會新增一個頁面，所以在「登入」的頁面，增加一個連結，導向「忘記密碼」畫面。
打開 \Views\Member\Login.cshtml 在「登入」按鈕下面增加一個「忘記密碼」連結。

`@Html.ActionLink("忘記密碼", "ForgetPwd", "Member")`

![img1](https://blog.hungwin.com.tw/wp-content/uploads/2021/10/aspnet-mvc-member-forget-reset-pwd-1.png)

修改後畫面

![img2](https://blog.hungwin.com.tw/wp-content/uploads/2021/10/aspnet-mvc-member-forget-reset-pwd-2.png)

### 增加忘記密碼頁面

這裡要新增一個忘記密碼的畫面，在 \Controllers\MemberController.cs 類別內，增加 ForgetPwd() 方法然後 Return View()。
```C#
// GET: 忘記密碼頁面
public ActionResult ForgetPwd()
{
	return View();
}
```

![img3](https://blog.hungwin.com.tw/wp-content/uploads/2021/10/aspnet-mvc-member-forget-reset-pwd-3.png)

### 增加忘記密碼頁面 View

在 ForgetPwd() 語法上按右鍵選「新增檢視」。

![img4](https://blog.hungwin.com.tw/wp-content/uploads/2021/10/aspnet-mvc-member-forget-reset-pwd-4.png)

選擇「MVC 5 檢視」加入。

![img5](https://blog.hungwin.com.tw/wp-content/uploads/2021/10/aspnet-mvc-member-forget-reset-pwd-5.png)

確認名稱為 “ForgetPwd”，有勾選「使用版面配置頁」。

![img6](https://blog.hungwin.com.tw/wp-content/uploads/2021/10/aspnet-mvc-member-forget-reset-pwd-6.png)

新增之後在 Views\Member\ForgetPwd.cshtml 會新增 View 檢視頁面。

![img7](https://blog.hungwin.com.tw/wp-content/uploads/2021/10/aspnet-mvc-member-forget-reset-pwd-7.png)

## 編寫「忘記密碼」 View 語法

這個頁面我設計只需要輸入帳號，再點擊「寄送驗證碼」。

在 Bootstrap 3 的官方範例，有提供[表單的範例](https://getbootstrap.com/docs/3.3/css/#forms)、[面版的範例](https://getbootstrap.com/docs/3.3/components/#panels)及[按鈕的範例](https://getbootstrap.com/docs/3.3/css/#buttons)。

我從 Bootstrap 3 範例中組合表單 HTML 及套用 Vue.js 語法變成以下的 ForgetPwd.cshtml 程式碼。
```C#
<div id="VuePage">
    <!--使用 Bootstrap 設計表單-->
    <div class="panel panel-primary">
        <div class="panel-heading">忘記密碼範例</div>
        <div class="panel-body">
            <div class="form-group">
                <label>帳號</label>
                <input type="text" class="form-control" v-model="form.UserID">
            </div>
        </div>
        <div class="panel-footer">
            <button type="button" class="btn btn-primary" v-on:click="SendMailToken()">寄送驗證碼</button>
        </div>
    </div>
 
    <!--使用 Bootstrap Modal 樣式，當執行有錯誤時，顯示錯誤訊息-->
    <div class="modal fade" id="ErrorAlert" tabindex="-1" role="dialog">
        <div class="modal-dialog modal-lg" role="document">
            <div class="modal-content">
                <div class="modal-header">
                    <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                    <h4 class="modal-title">錯誤訊息</h4>
                </div>
                <div class="modal-body" id="ErrorMsg" style="overflow-x:auto;width:100%;">
 
                </div>
            </div>
        </div>
    </div><!-- /.modal -->
</div>
@section scripts{
    <script>
        var VuePage = new Vue({
            el: '#VuePage'
            , data: function () {
                var data = {
                    form: {}
                };
                return data;
            }
            , methods: {
                // 前端驗證權杖
                GetToken: function () {
                    var token = '@Html.AntiForgeryToken()';
                    token = $(token).val();
                    return token;
                }
                // 寄送驗證碼
                , SendMailToken: function () {
                    var self = this;
 
                    // 組合表單資料
                    var postData = {};
                    postData['UserID'] = self.form.UserID;
 
                    // 使用 jQuery Ajax 傳送至後端
                    $.ajax({
                        url:'@Url.Action("SendMailToken", "Member")',
                        method:'POST',
                        dataType:'json',
                        data: { inModel: postData, __RequestVerificationToken: self.GetToken() },
                        success: function (datas) {
                            if (datas.ErrMsg) {
                                alert(datas.ErrMsg);
                                return;
                            }
                            alert(datas.ResultMsg);
                        },
                        error: function (err) {
                            $('#ErrorMsg').html(err.responseText);
                            $('#ErrorAlert').modal('toggle');
                        }
                    });
                }
            }
        })
    </script>
}
```

修改後畫面

![img8](https://blog.hungwin.com.tw/wp-content/uploads/2021/10/aspnet-mvc-member-forget-reset-pwd-8.png)

此頁面重點在按下「寄送驗證碼」後，將前台資料傳送到後端的 ~/Member/SendMailToken 方法，並取得後端的訊息。

我額外增加了 Bootstrap 的 modal 樣式，來顯示後端執行時的錯誤，這樣方便 Debug。

關於 Vue.js 的教學語法，可以到[官網](https://cn.vuejs.org/v2/guide/)上面查詢，官網有完整的教學。

## 編寫「寄送驗證碼」Controller 語法

當畫面上執行「寄送驗證碼」按鈕，View 會呼叫 MemberController 裡面的SendMailToken() 方法。
以下是 SendMailToken() 寫法。

```C#
/// <summary>
/// 寄送驗證碼
/// </summary>
/// <returns></returns>
[ValidateAntiForgeryToken]
public ActionResult SendMailToken(SendMailTokenIn inModel)
{
	SendMailTokenOut outModel = new SendMailTokenOut();
 
	// 檢查輸入來源
	if (string.IsNullOrEmpty(inModel.UserID))
	{
		outModel.ErrMsg = "請輸入帳號";
		return Json(outModel);
	}
 
	// 檢查資料庫是否有這個帳號
 
	// 取得資料庫連線字串
	string connStr = System.Web.Configuration.WebConfigurationManager.ConnectionStrings["ConnDB"].ConnectionString;
 
	// 當程式碼離開 using 區塊時，會自動關閉連接
	using (SqlConnection conn = new SqlConnection(connStr))
	{
		// 資料庫連線
		conn.Open();
 
		// 取得會員資料
		string sql = "select * from Member where UserID = @UserID";
		SqlCommand cmd = new SqlCommand();
		cmd.CommandText = sql;
		cmd.Connection = conn;
 
		// 使用參數化填值
		cmd.Parameters.AddWithValue("@UserID", inModel.UserID);
 
		// 執行資料庫查詢動作
		SqlDataAdapter adpt = new SqlDataAdapter();
		adpt.SelectCommand = cmd;
		DataSet ds = new DataSet();
		adpt.Fill(ds);
		DataTable dt = ds.Tables[0];
 
		if (dt.Rows.Count > 0)
		{
			// 取出會員信箱
			string UserEmail = dt.Rows[0]["UserEmail"].ToString();
 
			// 取得系統自定密鑰，在 Web.config 設定
			string SecretKey = ConfigurationManager.AppSettings["SecretKey"];
 
			// 產生帳號+時間驗證碼
			string sVerify = inModel.UserID + "|" + DateTime.Now.ToString("yyyy/MM/dd HH:mm:ss");
 
			// 將驗證碼使用 3DES 加密
			TripleDESCryptoServiceProvider DES = new TripleDESCryptoServiceProvider();
			MD5 md5 = new MD5CryptoServiceProvider();
			byte[] buf = Encoding.UTF8.GetBytes(SecretKey);
			byte[] result = md5.ComputeHash(buf);
			string md5Key = BitConverter.ToString(result).Replace("-", "").ToLower().Substring(0, 24);
			DES.Key = UTF8Encoding.UTF8.GetBytes(md5Key);
			DES.Mode = CipherMode.ECB;
			ICryptoTransform DESEncrypt = DES.CreateEncryptor();
			byte[] Buffer = UTF8Encoding.UTF8.GetBytes(sVerify);
			sVerify = Convert.ToBase64String(DESEncrypt.TransformFinalBlock(Buffer, 0, Buffer.Length)); // 3DES 加密後驗證碼
 
			// 將加密後密碼使用網址編碼處理
			sVerify = HttpUtility.UrlEncode(sVerify);
 
			// 網站網址
			string webPath = Request.Url.Scheme + "://" + Request.Url.Authority + Url.Content("~/");
 
			// 從信件連結回到重設密碼頁面
			string receivePage = "Member/ResetPwd";
 
			// 信件內容範本
			string mailContent = "請點擊以下連結，返回網站重新設定密碼，逾期 30 分鐘後，此連結將會失效。<br><br>";
			mailContent = mailContent + "<a href='" + webPath + receivePage + "?verify=" + sVerify + "'  target='_blank'>點此連結</a>";
 
			// 信件主題
			string mailSubject = "[測試] 重設密碼申請信";
 
			// Google 發信帳號密碼
			string GoogleMailUserID = ConfigurationManager.AppSettings["GoogleMailUserID"];
			string GoogleMailUserPwd = ConfigurationManager.AppSettings["GoogleMailUserPwd"];
 
			// 使用 Google Mail Server 發信
			string SmtpServer = "smtp.gmail.com";
			int SmtpPort = 587;
			MailMessage mms = new MailMessage();
			mms.From = new MailAddress(GoogleMailUserID);
			mms.Subject = mailSubject;
			mms.Body = mailContent;
			mms.IsBodyHtml = true;
			mms.SubjectEncoding = Encoding.UTF8;
			mms.To.Add(new MailAddress(UserEmail));
			using (SmtpClient client = new SmtpClient(SmtpServer, SmtpPort))
			{
				client.EnableSsl = true;
				client.Credentials = new NetworkCredential(GoogleMailUserID, GoogleMailUserPwd);//寄信帳密 
				client.Send(mms); //寄出信件
			}
			outModel.ResultMsg = "請於 30 分鐘內至你的信箱點擊連結重新設定密碼，逾期將無效";
		}
		else
		{
			outModel.ErrMsg = "查無此帳號";
		}
	}
 
	// 回傳 Json 給前端
	return Json(outModel);
}
```

輸入帳號後，會從資料庫內取得會員的信箱，程式碼會信件到會員信箱。
在信件的連結會導回網站，並夾帶帳號與時間資訊，我將帳號與時間加密後放在驗證碼裡面。
等導回網站時，再解密取出帳號與時間。

在註冊的時候，我並沒有驗證使用者信箱，是因為先講解寫入資料庫就好，驗證信箱的範例，就留到這裡再教學，一次學一點新的東西。
通常在註冊的時候，就會一起驗證信箱是否正常使用，在這裡學到的發信方法，就可以自行應用到註冊那邊去了喔。

### 調整 Web.config

這次方法使用到了 3DES 加密功能，所以需要設定加密金鑰，我將加密金鑰放在 Web.config 內。
還有 Google 發信的帳號密碼，我也放在 Web.config 內。

在 Web.config 的 <appSettings> 範圍內，新增以下 Key/Value。

```C#
<!-- 3DES 密鑰範例-->
<add key="SecretKey" value="MyKey"/>
<!-- Google 發信帳號-->
<add key="GoogleMailUserID" value="xxx@gmail.com"/>
<!-- Google 發信密碼-->
<add key="GoogleMailUserPwd" value="xxxxxx"/>
```

![img9](https://blog.hungwin.com.tw/wp-content/uploads/2021/10/aspnet-mvc-member-forget-reset-pwd-9.png)

密鑰為加密使用的鑰匙，相同的資料用不同的鑰匙，就會加密出不同的結果，所以密鑰很重要，需要好好保存。

### 調整 Google 發信設定

Google 帳號可以借用 Gmail SMTP 發件，可是需要開通一些權限。

開啟此網頁<https://myaccount.google.com/u/1/security>，登入身份後，將「允許低安全性應用程式」設為「啟用」。

![img10](https://blog.hungwin.com.tw/wp-content/uploads/2021/10/aspnet-mvc-member-forget-reset-pwd-10.png)

如果 Google 帳號登入有設定二階段驗證，也需要停用二階段驗證，才可以正常發信。

我這裡為了示範，所以選擇了 Gmail SMTP 來做發信伺服器，開啟「允許低安全性應用程式」會降低帳號的安全性，請確認好會承受的風險再執行。

若為正式發信伺服器，可使用[ Google Workspace ](https://workspace.google.com/intl/zh-TW/)(舊稱G Suite)，或使用企業 SMTP 來發信較適合。

### 增加忘記密碼 Model

這裡要增加在 Controller 新增的 SendMailTokenIn, SendMailTokenOut 類別。
打開 \Models\MemberModel.cs 檔案，在 MemberModel 裡面增加新的類別。

```C#
/// <summary>
/// [寄送驗證碼]參數
/// </summary>
public class SendMailTokenIn
{
	public string UserID { get; set; }
}
 
/// <summary>
/// [寄送驗證碼]回傳
/// </summary>
public class SendMailTokenOut
{
	public string ErrMsg { get; set; }
	public string ResultMsg { get; set; }
}
```

## 測試忘記密碼

在 VS 按 <F5> 執行專案，先在「登入」畫面，點「忘記密碼」換頁，輸入帳號後，執行「寄送驗證碼」。
在 Controller 取得帳號後，會查詢資料庫的 Email，然後對 Email 寄出信件。

![img11](https://blog.hungwin.com.tw/wp-content/uploads/2021/10/aspnet-mvc-member-forget-reset-pwd-11.png)

這是收到信件的畫面，點擊「點此連結」後，就會再導回網站。

![img12](https://blog.hungwin.com.tw/wp-content/uploads/2021/10/aspnet-mvc-member-forget-reset-pwd-12.png)

回網站後會開啟 /Member/ResetPwd 頁面，這一頁還沒製作，接下來我們就繼續完成這一頁面。

## 在 MemberController 增加重設密碼頁面

這裡要新增一個重設密碼的畫面，在 \Controllers\MemberController.cs 類別內，增加 ResetPwd() 方法然後 Return View()。

從信件連結回到網頁時，就要先檢查驗證碼是否正確，從驗證碼裡面取得帳號，以及寄件時間，再檢查寄件時間跟現在時間是否超過時效。

檢查成功，將帳號記在 Session 裡面，以方便重設密碼時使用。

```C#
// GET: 重設密碼頁面
public ActionResult ResetPwd(string verify)
{
	// 由信件連結回來會帶參數 verify
 
	if (verify == "")
	{
		ViewData["ErrorMsg"] = "缺少驗證碼";
		return View();
	}
 
	// 取得系統自定密鑰，在 Web.config 設定
	string SecretKey = ConfigurationManager.AppSettings["SecretKey"];
 
	try
	{
		// 使用 3DES 解密驗證碼
		TripleDESCryptoServiceProvider DES = new TripleDESCryptoServiceProvider();
		MD5 md5 = new MD5CryptoServiceProvider();
		byte[] buf = Encoding.UTF8.GetBytes(SecretKey);
		byte[] md5result = md5.ComputeHash(buf);
		string md5Key = BitConverter.ToString(md5result).Replace("-", "").ToLower().Substring(0, 24);
		DES.Key = UTF8Encoding.UTF8.GetBytes(md5Key);
		DES.Mode = CipherMode.ECB;
		DES.Padding = System.Security.Cryptography.PaddingMode.PKCS7;
		ICryptoTransform DESDecrypt = DES.CreateDecryptor();
		byte[] Buffer = Convert.FromBase64String(verify);
		string deCode = UTF8Encoding.UTF8.GetString(DESDecrypt.TransformFinalBlock(Buffer, 0, Buffer.Length));
 
		verify = deCode; //解密後還原資料
	}
	catch (Exception ex)
	{
		ViewData["ErrorMsg"] = "驗證碼錯誤";
		return View();
	}
 
	// 取出帳號
	string UserID = verify.Split('|')[0];
 
	// 取得重設時間
	string ResetTime = verify.Split('|')[1];
 
	// 檢查時間是否超過 30 分鐘
	DateTime dResetTime = Convert.ToDateTime(ResetTime);
	TimeSpan TS = new System.TimeSpan(DateTime.Now.Ticks - dResetTime.Ticks);
	double diff = Convert.ToDouble(TS.TotalMinutes);
	if (diff > 30)
	{
		ViewData["ErrorMsg"] = "超過驗證碼有效時間，請重寄驗證碼";
		return View();
	}
 
	// 驗證碼檢查成功，加入 Session
	Session["ResetPwdUserId"] = UserID;
 
	return View();
}
```

### 增加重設密碼頁面 View

在 ResetPwd() 語法上按右鍵選「新增檢視」。

![img13](https://blog.hungwin.com.tw/wp-content/uploads/2021/10/aspnet-mvc-member-forget-reset-pwd-13.png)

選擇「MVC 5 檢視」加入。

![img14](https://blog.hungwin.com.tw/wp-content/uploads/2021/10/aspnet-mvc-member-forget-reset-pwd-14.png)

確認名稱為 “ResetPwd”，有勾選「使用版面配置頁」。

![img15](https://blog.hungwin.com.tw/wp-content/uploads/2021/10/aspnet-mvc-member-forget-reset-pwd-15.png)

新增之後在 Views\Member\ResetPwd.cshtml 會新增 View 檢視頁面。

![img16](https://blog.hungwin.com.tw/wp-content/uploads/2021/10/aspnet-mvc-member-forget-reset-pwd-16.png)

## 編寫「重設密碼」 View 語法

這個頁面設計重點跟修改個人資料的「修改密碼」是類似的。
我從修改個人資料的「修改密碼」複製一些 View 程式碼來使用，並加上 Vue.js 的語法。

```C#
<div id="VuePage">
    <!--使用 Bootstrap 設計重設密碼表單-->
    <div class="panel panel-primary">
        <div class="panel-heading">重新密碼範例</div>
        <div class="panel-body">
            <div class="row">
                <div class="col-md-6">
                    <div class="form-group">
                        <label>新密碼</label>
                        <input type="password" class="form-control" v-model="form.NewUserPwd">
                    </div>
                </div>
                <div class="col-md-6">
                    <div class="form-group">
                        <label>確認新密碼</label>
                        <input type="password" class="form-control" v-model="form.CheckUserPwd">
                    </div>
                </div>
            </div>
        </div>
        <div class="panel-footer">
            <button type="button" class="btn btn-primary" v-on:click="DoResetPwd()">重設密碼</button>
        </div>
    </div>
 
    <!--使用 Bootstrap Modal 樣式，當執行有錯誤時，顯示錯誤訊息-->
    <div class="modal fade" id="ErrorAlert" tabindex="-1" role="dialog">
        <div class="modal-dialog modal-lg" role="document">
            <div class="modal-content">
                <div class="modal-header">
                    <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                    <h4 class="modal-title">錯誤訊息</h4>
                </div>
                <div class="modal-body" id="ErrorMsg" style="overflow-x:auto;width:100%;">
                </div>
            </div>
        </div>
    </div><!-- /.modal -->
</div>
@section scripts{
    <script>
        var VuePage = new Vue({
            el: '#VuePage'
            , data: function () {
                var data = {
                    form: {}
                };
                return data;
            }
            , created: function () {
                var ErrorMsg = '@ViewData["ErrorMsg"]';
                if (ErrorMsg != '') {
                    alert(ErrorMsg);
                    // 解析驗證碼失敗，導回登入頁面
                    window.location = '@Url.Action("Login", "Member")';
                }
            }
            , methods: {
                // 前端驗證權杖
                GetToken: function () {
                    var token = '@Html.AntiForgeryToken()';
                    token = $(token).val();
                    return token;
                }
                 // 重設密碼
                , DoResetPwd: function () {
                    var self = this;
 
                    // 組合表單資料
                    var postData = {};
                    postData['NewUserPwd'] = self.form.NewUserPwd;
                    postData['CheckUserPwd'] = self.form.CheckUserPwd;
 
                    // 使用 jQuery Ajax 傳送至後端
                    $.ajax({
                        url:'@Url.Action("DoResetPwd", "Member")',
                        method:'POST',
                        dataType:'json',
                        data: { inModel: postData, __RequestVerificationToken: self.GetToken() },
                        success: function (datas) {
                            if (datas.ErrMsg) {
                                alert(datas.ErrMsg);
                                return;
                            }
                            alert(datas.ResultMsg);
                        },
                        error: function (err) {
                            $('#ErrorMsg').html(err.responseText);
                            $('#ErrorAlert').modal('toggle');
                        },
                    });
                }
            }
        })
    </script>
}
```

修改後畫面

![img17](https://blog.hungwin.com.tw/wp-content/uploads/2021/10/aspnet-mvc-member-forget-reset-pwd-17.png)

此頁面重點在按下「重設密碼」後，將前台資料傳送到後端的 ~/Member/DoResetPwd 方法，並取得後端的訊息。

我額外增加了 Bootstrap 的 modal 樣式，來顯示後端執行時的錯誤，這樣方便 Debug。

關於 Vue.js 的教學語法，可以到官網上面查詢，官網有完整的教學。

## 編寫「重設密碼」Controller 語法

以下是 \Controllers\MemberController.cs 的 DoResetPwd() 寫法。

```C#
/// <summary>
/// 重設密碼
/// </summary>
/// <param name="inModel"></param>
/// <returns></returns>
[ValidateAntiForgeryToken]
public ActionResult DoResetPwd(DoResetPwdIn inModel)
{
	DoResetPwdOut outModel = new DoResetPwdOut();
 
	// 檢查是否有輸入密碼
	if (string.IsNullOrEmpty(inModel.NewUserPwd))
	{
		outModel.ErrMsg = "請輸入新密碼";
		return Json(outModel);
	}
	if (string.IsNullOrEmpty(inModel.CheckUserPwd))
	{
		outModel.ErrMsg = "請輸入確認新密碼";
		return Json(outModel);
	}
	if (inModel.NewUserPwd != inModel.CheckUserPwd)
	{
		outModel.ErrMsg = "新密碼與確認新密碼不相同";
		return Json(outModel);
	}
 
	// 檢查帳號 Session 是否存在
	if (Session["ResetPwdUserId"] == null || Session["ResetPwdUserId"].ToString() == "")
	{
		outModel.ErrMsg = "無修改帳號";
		return Json(outModel);
	}
 
	// 將新密碼使用 SHA256 雜湊運算(不可逆)
	string salt = Session["ResetPwdUserId"].ToString().Substring(0, 1).ToLower(); //使用帳號前一碼當作密碼鹽
	SHA256 sha256 = SHA256.Create();
	byte[] bytes = Encoding.UTF8.GetBytes(salt + inModel.NewUserPwd); //將密碼鹽及新密碼組合
	byte[] hash = sha256.ComputeHash(bytes);
	StringBuilder result = new StringBuilder();
	for (int i = 0; i < hash.Length; i++)
	{
		result.Append(hash[i].ToString("X2"));
	}
	string NewPwd = result.ToString(); // 雜湊運算後密碼
 
	// 取得連線字串
	string connStr = System.Web.Configuration.WebConfigurationManager.ConnectionStrings["ConnDB"].ConnectionString;
 
	// 當程式碼離開 using 區塊時，會自動關閉連接
	using (SqlConnection conn = new SqlConnection(connStr))
	{
		// 資料庫連線
		conn.Open();
 
		// 修改個人資料至資料庫
		string sql = @"UPDATE Member SET UserPwd = @UserPwd WHERE UserID = @UserID";
		SqlCommand cmd = new SqlCommand();
		cmd.Connection = conn;
		cmd.CommandText = sql;
 
		// 使用參數化填值
		cmd.Parameters.AddWithValue("@UserID", Session["ResetPwdUserId"]);
		cmd.Parameters.AddWithValue("@UserPwd", NewPwd);
 
		// 執行資料庫更新動作
		int Ret = cmd.ExecuteNonQuery();
 
		if (Ret > 0)
		{
			outModel.ResultMsg = "重設密碼完成";
		}
		else
		{
			outModel.ErrMsg = "無異動資料";
		}
	}
 
	// 回傳 Json 給前端
	return Json(outModel);
}
```

在傳入的參數中沒有包含帳號，而是從 Session[“ResetPwdUserId”] 取出帳號，是比較安全的做法，把重要的資訊存在 Session 中取用，可以避免前端由駭客傳入假資料，導致修改到別人的密碼。

### 增加重設密碼 Model

打開 \Models\MemberModel.cs 檔案，在 MemberModel 裡面增加新的類別。

```C#
/// <summary>
/// [重設密碼]參數
/// </summary>
public class DoResetPwdIn
{
	public string NewUserPwd { get; set; }
	public string CheckUserPwd { get; set; }
}
 
/// <summary>
/// [重設密碼]回傳
/// </summary>
public class DoResetPwdOut
{
	public string ErrMsg { get; set; }
	public string ResultMsg { get; set; }
}
```

## 測試忘記密碼與重設密碼功能

在 VS 按 <F5> 執行專案，先在「登入」畫面，點連結到「忘記密碼」畫面。
輸入帳號，按「寄送驗證碼」。

![img18](https://blog.hungwin.com.tw/wp-content/uploads/2021/10/aspnet-mvc-member-forget-reset-pwd-18.png)

帳號驗證且寄信成功，就會出現訊息。

![img19](https://blog.hungwin.com.tw/wp-content/uploads/2021/10/aspnet-mvc-member-forget-reset-pwd-19.png)

在會員的信箱會收到以下的信件。

![img20](https://blog.hungwin.com.tw/wp-content/uploads/2021/10/aspnet-mvc-member-forget-reset-pwd-20.png)

在 `ResetPwd(string verify)` 的方法內會解密驗證碼，就會取得原始資料。

![img21](https://blog.hungwin.com.tw/wp-content/uploads/2021/10/aspnet-mvc-member-forget-reset-pwd-21.png)

解密出帳號及時間，檢查寄件時間跟現在時間是否超過 30 分鐘以上，
如果檢查成功，就將帳號存入 Session 以利重設密碼時使用。

![img22](https://blog.hungwin.com.tw/wp-content/uploads/2021/10/aspnet-mvc-member-forget-reset-pwd-22.png)

接著在畫面上輸入新密碼及確認新密碼，按下「重設密碼」。

![img23](https://blog.hungwin.com.tw/wp-content/uploads/2021/10/aspnet-mvc-member-forget-reset-pwd-23.png)

畫面出現「重設密碼完成」，就是修改成功了。

## 重點整理

1. 增加「忘記密碼」和「重設密碼」兩個頁面。
2. 忘記密碼會發件至會員信箱，再由信箱導連結回網站改密碼。
3. 信件內的連結會帶有帳號及時間資訊，建議轉成加密文字，讓使用者無法修改內容。
4. 從信件連結回網頁需要檢查驗證碼。
5. 重設密碼與之前修改密碼的方法是一樣的。