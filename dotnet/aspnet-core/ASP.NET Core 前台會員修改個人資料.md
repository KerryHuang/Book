---
kind: reprint
source: site:blog.hungwin.com.tw
author: hungwin
---

在學習 C# 與資料庫的互動方式，有一個常見且實用的教學就是會員登入、註冊與修改會員資料等範例，學習過程中會用到資料庫新增、修改與查詢動作，是理解程式與資料庫互動的常見程式碼。
當學會了這個範例，將來為客戶開發系統的時候，馬上可以派上用場。

此篇文章是繼上一篇文章: [前台會員登入範例 #CH2](https://blog.hungwin.com.tw/aspnet-mvc-member-login/) 接續教學。

範例內容主要以 ASP.NET MVC 為核心，前端使用 Vue.js 框架，而後端使用 SQL Server 當資料庫。

[Vue.js](https://cn.vuejs.org/index.html) 是前端3 大主流框架的其中之一，目標是透過簡單的 API 提供開發者實作資料綁定與操作網頁上的元件，Vue.js 的核心把焦點關注在狀態與畫面的同步層級上，適合與其他 JavsScript 函式庫整合，同時也適合當作 ASP.NET MVC 的前端框架。

[SQL Server](https://www.microsoft.com/zh-tw/sql-server) 是微軟推出的關聯式資料庫，使用 SQL 語言就可以輕鬆操作資料庫。

編寫此教學文章是為了幫助更多新加入的軟體工程師們，有更簡單實用的範例，可以快速學習程式語言。
這次我將會簡化這個基礎必學的前端會員範例，適合剛接觸 C# 與資料庫程式的新手學習。
文末有提供此操作範例的完整程式碼下載，有需要可以自行下載瀏覽。

#### 目錄

[1 在 MemberController 增加修改個人資料頁面](#Step1)  
&emsp;&emsp;[1.1 增加修改個人資料頁面 View](#Step1)  
[2 編寫修改個人資料 View 語法](#Step1)  
&emsp;&emsp;[2.1 加入 Vue.js 控制元件](#Step1)  
[3 編寫Controller 語法](#Step1)  
&emsp;&emsp;[3.1 取得個人資料 Controller 語法](#Step1)  
&emsp;&emsp;[3.2 修改個人資料 Controller 語法](#Step1)  
&emsp;&emsp;[3.3 修改密碼 Controller 語法](#Step1)  
&emsp;&emsp;[3.4 增加修改個人資料 Model](#Step1)  
[4 測試修改個人資料功能](#Step1)  
[5 重點整理](#Step1)

## 在 MemberController 增加修改個人資料頁面

在上一篇已經完成了 MemberController.cs 的建立。
![img1](https://blog.hungwin.com.tw/wp-content/uploads/2021/10/aspnet-mvc-member-edit-profile-1.png)
這裡要新增一個修改個人資料的畫面，在 MemberController 類別內，增加 EditProfile() 是呈現畫面的 Action。
```c#
// GET: 修改個人資料頁面
public ActionResult EditProfile()
{
	return View();
}
```
![img2](https://blog.hungwin.com.tw/wp-content/uploads/2021/10/aspnet-mvc-member-edit-profile-2.png)

### 增加修改個人資料頁面 View
在 `EditProfile()` 語法上按右鍵選「新增檢視」。
![img3](https://blog.hungwin.com.tw/wp-content/uploads/2021/10/aspnet-mvc-member-edit-profile-3.png)
選擇「MVC 5 檢視」加入。
![img4](https://blog.hungwin.com.tw/wp-content/uploads/2021/10/aspnet-mvc-member-edit-profile-4.png)
確認名稱為 “EditProfile”，有勾選「使用版面配置頁」。
![img5](https://blog.hungwin.com.tw/wp-content/uploads/2021/10/aspnet-mvc-member-edit-profile-5.png)
新增之後在 Views\Member\EditProfile.cshtml 會新增 View 檢視頁面。
![img6](https://blog.hungwin.com.tw/wp-content/uploads/2021/10/aspnet-mvc-member-edit-profile-6.png)

## 編寫修改個人資料 View 語法

在 Bootstrap 3 的官方範例，有提供[表單的範例](https://getbootstrap.com/docs/3.3/css/#forms)、[面版的範例](https://getbootstrap.com/docs/3.3/components/#panels)及[按鈕的範例](https://getbootstrap.com/docs/3.3/css/#buttons)。
我從 Bootstrap 3 範例中語法組合變成我的修改個人資料畫面。

```html
<!--使用 Bootstrap 設計登入表單-->
<div class="panel panel-primary">
    <div class="panel-heading">修改個人資料範例</div>
    <div class="panel-body">
        <div class="form-group">
            <label>帳號</label>
            <p class="form-control-static"></p>
        </div>
        <div class="form-group">
            <label>姓名</label>
            <input type="text" class="form-control">
        </div>
        <div class="form-group">
            <label>Email</label>
            <input type="text" class="form-control">
        </div>
    </div>
    <div class="panel-footer">
        <button type="button" class="btn btn-primary">修改個人資料</button>
    </div>
</div>

<!--使用 Bootstrap 設計登入表單-->
<div class="panel panel-primary">
    <div class="panel-heading">修改密碼範例</div>
    <div class="panel-body">
        <div class="row">
            <div class="col-md-6">
                <div class="form-group">
                    <label>修改密碼</label>
                    <input type="password" class="form-control">
                </div>
            </div>
            <div class="col-md-6">
                <div class="form-group">
                    <label>確認新密碼</label>
                    <input type="password" class="form-control">
                </div>
            </div>
        </div>
    </div>
    <div class="panel-footer">
        <button type="button" class="btn btn-primary">修改密碼</button>
    </div>
</div>
```
在 EditProfile.cshtml 增加這些語法後，畫面就會出現修改個人資料及修改密碼表單。
![img7](https://blog.hungwin.com.tw/wp-content/uploads/2021/10/aspnet-mvc-member-edit-profile-7.png)
這只是一個沒有功能，純畫面的表單，目的在展示 Bootstrap 的語法。

### 加入 Vue.js 控制元件
我們在前面 _Layout.cshtml 已經加了 Vue.js 的底層元件，所以這頁面，就可以套用 Vue.js 的寫法。
我將剛剛的 HTML 修改一下，加入了 Vue.js 語法，並增加 `GetUserProfile()`,`DoEditProfile()`,`DoEditPwd()` 3 個方法，可傳送表單到 Controller 頁面。
我額外增加了 Bootstrap 的 modal 樣式，來顯示後端執行時的錯誤，這樣方便 Debug。
以下程式碼可以整個取代 EditProfile.cshtml 內容。
```javascript
<div id="VuePage">
    <!--使用 Bootstrap 設計登入表單-->
    <div class="panel panel-primary">
        <div class="panel-heading">修改個人資料範例</div>
        <div class="panel-body">
            <div class="form-group">
                <label>帳號</label>
                <p class="form-control-static">{{form.UserID}}</p>
            </div>
            <div class="form-group">
                <label>姓名</label>
                <input type="text" class="form-control" v-model="form.UserName">
            </div>
            <div class="form-group">
                <label>Email</label>
                <input type="text" class="form-control" v-model="form.UserEmail">
            </div>
        </div>
        <div class="panel-footer">
            <button type="button" class="btn btn-primary" v-on:click="DoEditProfile()">修改個人資料</button>
        </div>
    </div>

    <!--使用 Bootstrap 設計登入表單-->
    <div class="panel panel-primary">
        <div class="panel-heading">修改密碼範例</div>
        <div class="panel-body">
            <div class="row">
                <div class="col-md-6">
                    <div class="form-group">
                        <label>修改密碼</label>
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
            <button type="button" class="btn btn-primary" v-on:click="DoEditPwd()">修改密碼</button>
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
            </div><!-- /.modal-content -->
        </div><!-- /.modal-dialog -->
    </div><!-- /.modal -->
</div>
@section scripts {
    <script>
        var VuePage = new Vue({
            el: '#VuePage'
            , data: function () {
                var data = {
                    form: {}
                };

                // 設定表單初始值
                data.form = {
                    UserID: ""
                    , UserName: ""
                    , UserEmail:""
                }
                return data;
            }
            // Vue 實體與掛載完成
            , mounted: function () {
                var self = this;

                // 當 Vue 掛載完成，取得個人資料
                self.GetUserProfile();
            }
            , methods: {
                // 前端驗證權杖
                GetToken: function () {
                    var token = '@Html.AntiForgeryToken()';
                    token = $(token).val();
                    return token;
                }
                // 取得個人資料
                , GetUserProfile: function () {
                    var self = this;
                    var postData = {};

                    // 使用 jQuery Ajax 傳送至後端
                    $.ajax({
                        url:'@Url.Content("~/Member/GetUserProfile")',
                        method:'POST',
                        dataType:'json',
                        data: { inModel: postData },
                        success: function (datas) {
                            if (datas.ErrMsg) {
                                alert(datas.ErrMsg);
                                return;
                            }
                            self.form.UserID = datas.UserID;
                            self.form.UserName = datas.UserName;
                            self.form.UserEmail = datas.UserEmail;
                        },
                        error: function (err) {
                            $('#ErrorMsg').html(err.responseText);
                            $('#ErrorAlert').modal('toggle');
                        },
                    });
                }
                // 修改個人資料
                , DoEditProfile: function () {
                    var self = this;

                    // 組合表單資料
                    var postData = {};
                    postData['UserName'] = self.form.UserName;
                    postData['UserEmail'] = self.form.UserEmail;

                    // 使用 jQuery Ajax 傳送至後端
                    $.ajax({
                        url:'@Url.Content("~/Member/DoEditProfile")',
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
                 // 修改密碼
                , DoEditPwd: function () {
                    var self = this;

                    // 組合表單資料
                    var postData = {};
                    postData['NewUserPwd'] = self.form.NewUserPwd;
                    postData['CheckUserPwd'] = self.form.CheckUserPwd;

                    // 使用 jQuery Ajax 傳送至後端
                    $.ajax({
                        url:'@Url.Content("~/Member/DoEditPwd")',
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

我使用 Vue.js [生命週期中的 mounted 事件](https://v3.cn.vuejs.org/api/options-lifecycle-hooks.html#mounted)，當 Vue 掛載完成，就呼叫 `GetUserProfile()` 方法取得個人資料，取得後端會員資料後，再放到前端畫面上。
當使用者修改資料時，就呼叫 `DoEditProfile()` 或 `DoEditPwd()` 方法，將前端資料往後端送。
關於 Vue.js 的教學語法，可以到[官網](https://cn.vuejs.org/v2/guide/)上面查詢，官網有完整的教學。

## 編寫Controller 語法

### 取得個人資料 Controller 語法

剛剛 View 在頁面載入完成時會呼叫 `~/Member/GetUserProfile` 方法，以下是 `GetUserProfile()` 的 Controller 寫法。
```c#
/// <summary>
/// 取得個人資料
/// </summary>
/// <returns></returns>
public ActionResult GetUserProfile()
{
	GetUserProfileOut outModel = new GetUserProfileOut();

	// 檢查會員 Session 是否存在
	if (Session["UserID"] == null || Session["UserID"].ToString() == "")
	{
		outModel.ErrMsg = "無會員登入記錄";
		return Json(outModel);
	}

	// 取得連線字串
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
		cmd.Parameters.AddWithValue("@UserID", Session["UserID"]);

		// 執行資料庫查詢動作
		SqlDataAdapter adpt = new SqlDataAdapter();
		adpt.SelectCommand = cmd;
		DataSet ds = new DataSet();
		adpt.Fill(ds);
		DataTable dt = ds.Tables[0];

		if (dt.Rows.Count > 0)
		{
			// 將資料回傳給前端
			outModel.UserID = dt.Rows[0]["UserID"].ToString();
			outModel.UserName = dt.Rows[0]["UserName"].ToString();
			outModel.UserEmail = dt.Rows[0]["UserEmail"].ToString();
		}
		else
		{
			outModel.ErrMsg = "查無會員資料";
		}
	}

	// 回傳 Json 給前端
	return Json(outModel);
}
```
這方法主要是取得 Session 中的 UserID，將 UserID 查詢資料庫 Member 表中的 UserID 欄位，將資料表中的資料，回傳到前端去。

### 修改個人資料 Controller 語法
當在畫面上執行「修改個人資料」按鈕，View 會呼叫 `~/Member/DoEditProfile`，以下是 `DoEditProfile()` 的 Controller 寫法。
```c#
/// <summary>
/// 修改個人資料
/// </summary>
/// <param name="inModel"></param>
/// <returns></returns>
[ValidateAntiForgeryToken]
public ActionResult DoEditProfile(DoEditProfileIn inModel)
{
	DoEditProfileOut outModel = new DoEditProfileOut();

	// 檢查個人資料是否有輸入
	if (string.IsNullOrEmpty(inModel.UserName) || string.IsNullOrEmpty(inModel.UserEmail))
	{
		outModel.ErrMsg = "請輸入資料";
		return Json(outModel);
	}

	// 檢查會員 Session 是否存在
	if (Session["UserID"] == null || Session["UserID"].ToString() == "")
	{
		outModel.ErrMsg = "無會員登入記錄";
		return Json(outModel);
	}

	// 取得連線字串
	string connStr = System.Web.Configuration.WebConfigurationManager.ConnectionStrings["ConnDB"].ConnectionString;

	// 當程式碼離開 using 區塊時，會自動關閉連接
	using (SqlConnection conn = new SqlConnection(connStr))
	{
		// 資料庫連線
		conn.Open();

		// 修改個人資料至資料庫
		string sql = @"UPDATE Member SET UserName = @UserName, UserEmail = @UserEmail WHERE UserID = @UserID";
		SqlCommand cmd = new SqlCommand();
		cmd.Connection = conn;
		cmd.CommandText = sql;

		// 使用參數化填值
		cmd.Parameters.AddWithValue("@UserID", Session["UserID"]);
		cmd.Parameters.AddWithValue("@UserName", inModel.UserName);
		cmd.Parameters.AddWithValue("@UserEmail", inModel.UserEmail);

		// 執行資料庫更新動作
		int Ret = cmd.ExecuteNonQuery();

		if (Ret > 0)
		{
			outModel.ResultMsg = "修改個人資料完成";
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

這次方法特別在開頭加一個 [[ValidateAntiForgeryToken\] 驗證](https://docs.microsoft.com/zh-tw/aspnet/core/security/anti-request-forgery?view=aspnetcore-5.0)，這是防止跨網站偽造要求的攻擊，也稱為 CSRF (Cross-Site Request Forgery) 攻擊，這是對 MVC 網頁提升安全性的做法。

在前端的 `DoEditProfile()` 方法內在 Ajax 傳送資料時，需要加一段 `__RequestVerificationToken: self.GetToken()` 參數，將前端驗證碼往後端傳送，後端才能驗證來源是合法來源。

修改資料時的 SQL 都是使用[參數化填值](https://zh.wikipedia.org/wiki/參數化查詢)方式，這是為了防止 SQL 注入攻擊。

此功能是先經過登入才能呈現的畫面，在登入成功時，已經帳號存入 Session 內，在此頁面帳號由 Session 來取得，就不需要由前端傳送了。

### 修改密碼 Controller 語法
當在畫面上執行「修改密碼」按鈕，View 會呼叫 `~/Member/DoEditPwd`，以下是 `DoEditPwd()` 的 Controller 寫法。
```c#
/// <summary>
/// 修改密碼
/// </summary>
/// <param name="inModel"></param>
/// <returns></returns>
[ValidateAntiForgeryToken]
public ActionResult DoEditPwd(DoEditPwdIn inModel)
{
	DoEditPwdOut outModel = new DoEditPwdOut();

	// 檢查是否有輸入密碼
	if (string.IsNullOrEmpty(inModel.NewUserPwd))
	{
		outModel.ErrMsg = "請輸入修改密碼";
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

	// 檢查會員 Session 是否存在
	if (Session["UserID"] == null || Session["UserID"].ToString() == "")
	{
		outModel.ErrMsg = "無會員登入記錄";
		return Json(outModel);
	}

	// 將新密碼使用 SHA256 雜湊運算(不可逆)
	string salt = Session["UserID"].ToString().Substring(0, 1).ToLower(); //使用帳號前一碼當作密碼鹽
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
		cmd.Parameters.AddWithValue("@UserID", Session["UserID"]);
		cmd.Parameters.AddWithValue("@UserPwd", NewPwd);

		// 執行資料庫更新動作
		int Ret = cmd.ExecuteNonQuery();

		if (Ret > 0)
		{
			outModel.ResultMsg = "修改密碼完成";
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
修改密碼建議使用者輸入 2 次，以確保沒有手誤，同時在後端驗證 2 次密碼是否相同。
資料庫內的密碼建議經過雜湊運算後再儲存，以防止被盜取密碼時，使用者重要密碼外洩。
此功能是先經過登入才能呈現的畫面，登入帳號由 Session 來取得，就不需要由前端傳送了，修改資料時的會員帳號也是由 Session 內的值提供。

### 增加修改個人資料 Model
剛剛在 Controller 建立時，新增了一些新參數類別及新回傳類別，打開 MemberModel.cs 檔案，在裡面增加新增的類別。
```c#
/// <summary>
/// 取得個人資料回傳
/// </summary>
public class GetUserProfileOut
{
	public string ErrMsg { get; set; }
	public string UserID { get; set; }
	public string UserName { get; set; }
	public string UserEmail { get; set; }
}

/// <summary>
/// 修改個人資料參數
/// </summary>
public class DoEditProfileIn
{
	public string UserName { get; set; }
	public string UserEmail { get; set; }
}

/// <summary>
/// 修改個人資料回傳
/// </summary>
public class DoEditProfileOut
{
	public string ErrMsg { get; set; }
	public string ResultMsg { get; set; }
}

/// <summary>
/// 修改密碼參數
/// </summary>
public class DoEditPwdIn
{
	public string NewUserPwd { get; set; }
	public string CheckUserPwd { get; set; }
}

/// <summary>
/// 修改密碼回傳
/// </summary>
public class DoEditPwdOut
{
	public string ErrMsg { get; set; }
	public string ResultMsg { get; set; }
}
```
關於 Controller 與 View 之間的資料傳遞物件都定義在 Model 裡面

## 測試修改個人資料功能

之前做登入的時候，登入成功只是 alert 訊息而已，這次在 alert 之後，增加導向到「修改個人資料」頁面。

打開 \Views\Member\Login.cshtml 頁面，在 DoLogin() 方法內增加以下語法。

```
window.location = '@Url.Content("~/Member/EditProfile")';
```
![img8](https://blog.hungwin.com.tw/wp-content/uploads/2021/10/aspnet-mvc-member-edit-profile-8.png)
在 VS 按 <F5> 執行專案，先在「登入」畫面，輸入正確的帳號密碼，就會跳到「修改個人資料畫面」。
在顯示「修改個人資料」頁面會先顯示會員資料。
![img9](https://blog.hungwin.com.tw/wp-content/uploads/2021/10/aspnet-mvc-member-edit-profile-9.png)
接著可以分別測試「修改個人資料」與「修改密碼」兩個功能。

## 重點整理
1. 在 Controller 增加 EditProfile() 顯示修改個人資料畫面
2. 使用 Bootstrap 樣式可快速製作美觀的表單
3. 在 View 增加取得個人資料、修改個人資料及修改密碼的方法
4. 在 Controller 後端增加對應的 3 個方法
5. Model 定義 Controller 與 View 之間的資料傳遞物件