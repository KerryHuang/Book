---
kind: reprint
source: site:blog.hungwin.com.tw
author: hungwin
---

在學習 C# 與資料庫的互動方式，有一個常見且實用的教學就是會員登入、註冊與修改會員資料等範例，學習過程中會用到資料庫新增、修改與查詢動作，是理解程式與資料庫互動的常見程式碼。
當學會了這個範例，將來為客戶開發系統的時候，就可以派上用場。

此篇文章主要以 ASP.NET MVC 為核心，前端使用[ Vue.js](https://cn.vuejs.org/index.html) 框架，而後端使用 [SQL Server](https://www.microsoft.com/zh-tw/sql-server/sql-server-downloads) 當資料庫。

[Vue.js](https://cn.vuejs.org/index.html) 是前端 3 大主流框架的其中之一，目標是透過簡單的 API 提供開發者實作資料綁定與操作網頁上的元件，Vue.js 的核心把焦點關注在狀態與畫面的同步層級上，適合與其他 Javascript 函式庫整合，同時也適合當作 ASP.NET MVC 的前端框架。

[SQL Server](https://www.microsoft.com/zh-tw/sql-server/sql-server-downloads) 是微軟推出的關聯式資料庫，使用 SQL 語言就可以輕鬆操作資料庫。

編寫此教學文章是為了幫助更多新加入的軟體工程師們，有更簡單實用的範例，可以快速學習程式語言。
這次我將會簡化這個基礎必學的前端會員範例，適合剛接觸 C# 與資料庫程式的新手學習。
文末有提供此操作範例的完整程式碼下載，有需要可以自行下載瀏覽。

##### 目錄  

[1 建立新 MVC 專案](#Step1)  
[2 調整 MVC 範本 – 佈局頁](#Step1)  
&emsp;&emsp;[2.1 引用 Vue.js 底層元件](#Step1)  
&emsp;&emsp;[2.2 增加註冊及登入選單](#Step1)  
[3 增加新 Controller – Member](#Step1)  
&emsp;&emsp;[3.1 增加註冊頁面 Action](#Step1)  
&emsp;&emsp;[3.2 增加註冊頁面 View](#Step1)  
[4 編寫註冊 View 語法](#Step1)  
&emsp;&emsp;[4.1 加入 Vue.js 控制元件](#Step1)  
[5 編寫註冊 Controller 語法](#Step1)  
&emsp;&emsp;[5.1 密碼儲存觀念](#Step1)  
&emsp;&emsp;[5.2 設定資料庫連線字串](#Step1)  
&emsp;&emsp;[5.3 增加註冊 Model](#Step1)  
[6 新增資料庫與資料表](#Step1)  
[7 測試範例](#Step1)  
[8 重點整理](#Step1)  
&emsp;&emsp;[8.1 範例下載](#Step1)

## 建立新 MVC 專案

尚未安裝 Visual Studio 2022 的話，請先參考此文章安裝：[微軟整合開發工具 Visual Studio 2022 安裝教學](https://blog.hungwin.com.tw/vs2022install/)。

開啟 Visual Studio 2022 選擇「建立新專案」，專案類型為「ASP.NET Web 應用程式(.NET Framework)」。
![img1](https://blog.hungwin.com.tw/wp-content/uploads/2021/09/aspnet-mvc-member-register-1.png)
輸入專案名稱及儲存位置。
![img2](https://blog.hungwin.com.tw/wp-content/uploads/2021/09/aspnet-mvc-member-register-2.png)
選擇「MVC」類型。
![img3](https://blog.hungwin.com.tw/wp-content/uploads/2021/09/aspnet-mvc-member-register-3.png)
完成後即會開啟 MVC 的範本專案，執行「F5」，可以瀏覽範本初始畫面。

## 調整 MVC 範本 – 佈局頁
打開 \Views\Shared\_Layout.cshtml 頁面。
![img4](https://blog.hungwin.com.tw/wp-content/uploads/2021/09/aspnet-mvc-member-register-3-1.png)

### 引用 Vue.js 底層元件
在 [Vue.js 官方教學](https://cn.vuejs.org/v2/guide/)找到 CDN 網址。
<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
在 `@Scripts.Render("~/bundles/bootstrap")` 語法下面，加入 Vue.js 底層元件。
![img5](https://blog.hungwin.com.tw/wp-content/uploads/2021/11/csharp-qr-code-gen-8-1.png)

### 增加註冊及登入選單
打開佈局頁 Views\Shared\_Layout.cshtml，在原有的選單後面增加 2 個新連結。
```html
<li>@Html.ActionLink("註冊", "Register", "Member")</li>
<li>@Html.ActionLink("登入", "Login", "Member")</li>
```
![img6](https://blog.hungwin.com.tw/wp-content/uploads/2021/09/aspnet-mvc-member-register-6.png)

## 增加新 Controller – Member
我們將所有處理會員的頁面及邏輯都放在 MemberController 裡面。
在「Controllers」按右鍵，新增一個「控制器」。
![img7](https://blog.hungwin.com.tw/wp-content/uploads/2021/09/aspnet-mvc-member-register-7.png)
加入「MVC 5 控制器-空白」，取名為「MemberController」。

### 增加註冊頁面 Action
在MemberController 頁面增加一個回傳 Register 的 View 頁面。
![img8](https://blog.hungwin.com.tw/wp-content/uploads/2021/09/aspnet-mvc-member-register-8.png)

### 增加註冊頁面 View
在 Register() 語法上按右鍵選「新增檢視」。
![img9](https://blog.hungwin.com.tw/wp-content/uploads/2021/09/aspnet-mvc-member-register-9.png)
選擇「MVC 5 檢視」加入，確認名稱為 “Register”，有勾選「使用版面配置頁」。
![img10](https://blog.hungwin.com.tw/wp-content/uploads/2021/09/aspnet-mvc-member-register-10.png)
新增之後在 Views\Member\Register.cshtml 會新增 View 檢視頁面。
![img11](https://blog.hungwin.com.tw/wp-content/uploads/2021/09/aspnet-mvc-member-register-11.png)

## 編寫註冊 View 語法
因為 VS 在MVC 的專案，預設加入了 jQuery 及 Bootstrap 的元件，所以我們可以直接使用 Bootstrap 語法來設計畫面。
![img12](https://blog.hungwin.com.tw/wp-content/uploads/2021/09/aspnet-mvc-member-register-12.png)

我直接在 [Bootstrap 3 的官方說明文件](https://getbootstrap.com/docs/3.3/css/#forms)，取一些表單語法來用。

```html
<div class="panel panel-primary">
    <div class="panel-heading">註冊頁面範例</div>
    <div class="panel-body">
        <div class="form-group">
            <label>帳號</label>
            <input type="text" class="form-control">
        </div>
        <div class="form-group">
            <label>密碼</label>
            <input type="password" class="form-control">
        </div>
        <div class="form-group">
            <label>姓名</label>
            <input type="text" class="form-control">
        </div>
        <div class="form-group">
            <label>EMail</label>
            <input type="text" class="form-control">
        </div>
    </div>
    <div class="panel-footer">
        <button type="button" class="btn btn-primary">註冊</button>
    </div>
</div>
```
在 Register.cshtml 增加這些語法後，畫面就會出現輸入表單。
![img13](https://blog.hungwin.com.tw/wp-content/uploads/2021/09/aspnet-mvc-member-register-13.png)

### 加入 Vue.js 控制元件
我們在前面 _Layout.cshtml 已經加了 Vue.js 的底層元件，所以這註冊頁面，就可以套用 Vue.js 的寫法。

我將剛剛的 HTML 修改一下，加入了 Vue.js 語法，並增加 DoRegister() 的方法，執行註冊時傳送表單到 Controller 頁面。

以下程式碼可以整個取代 Register.cshtml 內容。
```html
<div id="VuePage">
    <!--使用 Bootstrap 設計註冊表單-->
    <div class="panel panel-primary">
        <div class="panel-heading">註冊頁面範例</div>
        <div class="panel-body">
            <div class="form-group">
                <label>帳號</label>
                <input type="text" class="form-control" v-model="form.UserID">
            </div>
            <div class="form-group">
                <label>密碼</label>
                <input type="password" class="form-control" v-model="form.UserPwd">
            </div>
            <div class="form-group">
                <label>姓名</label>
                <input type="text" class="form-control" v-model="form.UserName">
            </div>
            <div class="form-group">
                <label>EMail</label>
                <input type="text" class="form-control" v-model="form.UserEmail">
            </div>
        </div>
        <div class="panel-footer">
            <button type="button" class="btn btn-primary" v-on:click="DoRegister()">註冊</button>
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
                return data;
            }
            , methods: {
                // 執行註冊按鈕
                DoRegister: function () {
                    var self = this;

                    // 組合表單資料
                    var postData = {};
                    postData['UserID'] = self.form.UserID;
                    postData['UserPwd'] = self.form.UserPwd;
                    postData['UserName'] = self.form.UserName;
                    postData['UserEmail'] = self.form.UserEmail;

                    // 使用 jQuery Ajax 傳送至後端
                    $.ajax({
                        url:'@Url.Content("~/Member/DoRegister")',
                        method:'POST',
                        dataType:'json',
                        data: { inModel: postData },
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

Vue.js 可取得網頁上的欄位資料，將資料利用 Ajax 傳送到後端。

`var postData` 主要在建立傳送表單，將 4 個欄位資料放進表單裡面，向後端傳送。

向後端傳送資料使用的是 [jQuery.ajax()](https://api.jquery.com/jquery.ajax/) 方法，方法內指定要傳送的網址 (url)、Http 協定(method)、資料型別 (dataType)、資料內容 (data)、成功回傳方法 (success)、失敗回傳方法 (error)。

關於 Vue.js 的教學語法，可以到[官網](https://cn.vuejs.org/v2/guide/)上面查詢，官網有完整的教學。

## 編寫註冊 Controller 語法

剛剛在 View 會傳送一個動作呼叫 Member/DoRegister 所以在 Controller 需要建立回應的方法。

```c#
/// <summary>
/// 執行註冊
/// </summary>
/// <param name="inModel"></param>
/// <returns></returns>
public ActionResult DoRegister(DoRegisterIn inModel)
{
	DoRegisterOut outModel = new DoRegisterOut();

	if (string.IsNullOrEmpty(inModel.UserID) || string.IsNullOrEmpty(inModel.UserPwd) || string.IsNullOrEmpty(inModel.UserName) || string.IsNullOrEmpty(inModel.UserEmail))
	{
		outModel.ErrMsg = "請輸入資料";
	}
	else
	{
		SqlConnection conn = null;
		try
		{
			// 資料庫連線
			string connStr = System.Web.Configuration.WebConfigurationManager.ConnectionStrings["ConnDB"].ConnectionString;
			conn = new SqlConnection();
			conn.ConnectionString = connStr;
			conn.Open();

			// 檢查帳號是否存在
			string sql = "select * from Member where UserID = @UserID";
			SqlCommand cmd = new SqlCommand();
			cmd.CommandText = sql;
			cmd.Connection = conn;

			// 使用參數化填值
			cmd.Parameters.AddWithValue("@UserID", inModel.UserID);

			// 執行資料庫查詢動作
			DbDataAdapter adpt = new SqlDataAdapter();
			adpt.SelectCommand = cmd;
			DataSet ds = new DataSet();
			adpt.Fill(ds);

			if (ds.Tables[0].Rows.Count > 0)
			{
				outModel.ErrMsg = "此登入帳號已存在";
			}
			else
			{
				// 將密碼使用 SHA256 雜湊運算(不可逆)
				string salt = inModel.UserID.Substring(0, 1).ToLower(); //使用帳號前一碼當作密碼鹽
				SHA256 sha256 = SHA256.Create();
				byte[] bytes = Encoding.UTF8.GetBytes(salt + inModel.UserPwd); //將密碼鹽及原密碼組合
				byte[] hash = sha256.ComputeHash(bytes);
				StringBuilder result = new StringBuilder();
				for (int i = 0; i < hash.Length; i++)
				{
					result.Append(hash[i].ToString("X2"));
				}
				string NewPwd = result.ToString(); // 雜湊運算後密碼

				// 註冊資料新增至資料庫
				sql = @"INSERT INTO Member (UserID,UserPwd,UserName,UserEmail) VALUES (@UserID, @UserPwd, @UserName, @UserEmail)";
				cmd = new SqlCommand();
				cmd.Connection = conn;
				cmd.CommandText = sql;

				// 使用參數化填值
				cmd.Parameters.AddWithValue("@UserID", inModel.UserID);
				cmd.Parameters.AddWithValue("@UserPwd", NewPwd); // 雜湊運算後密碼
				cmd.Parameters.AddWithValue("@UserName", inModel.UserName);
				cmd.Parameters.AddWithValue("@UserEmail", inModel.UserEmail);

				// 執行資料庫更新動作
				cmd.ExecuteNonQuery();

				outModel.ResultMsg = "註冊完成";
			}
		}
		catch (Exception ex)
		{
			throw ex;
		}
		finally
		{
			if (conn != null)
			{
				//關閉資料庫連線
				conn.Close();
				conn.Dispose();
			}
		}
	}

	// 輸出json
	return Json(outModel);
}
```

這是我習慣的回應寫法，將傳入的來源宣告為 `DoRegisterIn` 物件，將要回傳的物件宣告為`DoRegisterOut`。
命名方式為方法名稱的後面增加 In 及 Out 表示資料方向。
回傳的格式一律為 Json 格式。

在方法內主要是連線資料庫，檢查帳號是否存在，當不存在時，才會寫入一筆資料進資料庫。

在產生儲存密碼時，我使用了 SHA256 雜湊運算 + 密碼鹽的處理，提高了密碼保存的安全性，
有關密碼鹽的知識，可以參考[維基百科說明](https://zh.wikipedia.org/wiki/盐_(密码学))。

### 密碼儲存觀念

有關使用者重要的密碼儲存在資料庫的時候，建議使用不可逆的雜湊運算，例如 [SHA256](https://zh.wikipedia.org/wiki/SHA-2)，在產生儲存密碼時，建議加入[密碼鹽](https://zh.wikipedia.org/wiki/盐_(密码学))來混淆原密碼泄漏風險。

若使用者忘記密碼時，可以採用身份驗證後，直接更換使用者密碼。

### 設定資料庫連線字串
剛剛在連線資料庫的語法中使用到
```c#
System.Web.Configuration.WebConfigurationManager.ConnectionStrings["ConnDB"].ConnectionString;
```
這指的是連線字串由 Web.config 中取出 connectionStrings 名稱為 “ConnDB” 的連線字串，
接下來就開啟專案根目錄下的「Web.config」，設定資料庫連線字串。

在 <configuration></configuration> 範圍內加入語法：

```xml
<connectionStrings>
    <add name="ConnDB" connectionString="Data Source=127.0.0.1;Initial Catalog=Teach;Persist Security Info=false;User ID=test;Password=test;" providerName="System.Data.SqlClient"/>
</connectionStrings>
```
![img14](https://blog.hungwin.com.tw/wp-content/uploads/2021/09/aspnet-mvc-member-register-13-1.png)
連線字串的參數需改成你們的環境，參數為:
Data Source=資料庫主機名稱或位址
Initial Catalog=資料庫名稱
User ID=帳號
Password=密碼

### 增加註冊 Model
剛剛在 Controller 宣告的 DoRegisterIn 及 DoRegisterOut 都是新物件名稱，所以還需要在 Model 建立類別。

要加入一個新 Model 的方法是在「Models」按右鍵選「加入 > 類別」。
![img15](https://blog.hungwin.com.tw/wp-content/uploads/2021/09/aspnet-mvc-member-register-14.png)
選擇「類別」，輸入與 Controller 同名的 “MemberModel”，執行「新增」加入類別。
![img16](https://blog.hungwin.com.tw/wp-content/uploads/2021/09/aspnet-mvc-member-register-15.png)
在 MemberModel 的類別內加入 DoRegisterIn 及 DoRegisterOut 兩個新類別。

```c#
/// <summary>
/// 註冊參數
/// </summary>
public class DoRegisterIn
{
	public string UserID { get; set; }
	public string UserPwd { get; set; }
	public string UserName { get; set; }
	public string UserEmail { get; set; }
}

/// <summary>
/// 註冊回傳
/// </summary>
public class DoRegisterOut
{
	public string ErrMsg { get; set; }
	public string ResultMsg { get; set; }
}
```

![img17](https://blog.hungwin.com.tw/wp-content/uploads/2021/09/aspnet-mvc-member-register-15-1-1.png)

DoRegisterIn 定義由 View 會傳入的欄位名稱，DoRegisterOut 則定義 Controller 處理完之後，會回傳給 View 的欄位名稱。

我對於 Model 的使用目的，均為定義 Controller 與 View 之間的傳遞欄位型別。

## 新增資料庫與資料表

我使用的資料庫是 SQL Server 2019，尚未安裝的朋友可以參考這篇文章先安裝：[如何安裝 SQL Server 2019 免費開發版](https://blog.hungwin.com.tw/windows-server-sql-server-2019-install/)。

安裝之後，使用 [SSMS](https://zh.wikipedia.org/wiki/SQL_Server_Management_Studio) 登入，在檔案總管的「資料庫」按右鍵可以新增一個資料庫。

![img18](https://blog.hungwin.com.tw/wp-content/uploads/2021/09/aspnet-mvc-member-register-16.png)

我在本機新建一個 “Teach” 的資料庫，然後使用語法新增一個 “Member” 的資料表。

```sql
CREATE TABLE [dbo].[Member](
	[UserID] [varchar](10) NOT NULL,
	[UserPwd] [varchar](64) NOT NULL,
	[UserName] [nvarchar](20) NOT NULL,
	[UserEmail] [varchar](50) NOT NULL,
 CONSTRAINT [PK_Member] PRIMARY KEY CLUSTERED 
(
	[UserID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
```
這是要儲存網頁的註冊資料。

## 測試範例
完成程式碼及資料庫後，就可以執行「F5」運行專案。
切換至「註冊」範例，輸入資料後，執行「註冊」功能。
![img19](https://blog.hungwin.com.tw/wp-content/uploads/2021/09/aspnet-mvc-member-register-17-1.png)
確認畫面出現「註冊完成」後，就可以檢查資料庫。
使用 SSMS 登入資料庫，檢查 Member 的資料，
就可以看到剛剛在畫面上新增的資料了。
![img20](https://blog.hungwin.com.tw/wp-content/uploads/2021/09/aspnet-mvc-member-register-18-2.png)

## 重點整理
1. MVC 為專案核心，Vue.js 處理前端控制，SQL Server 處理資料儲存
2. 調整佈局頁 Javascript 位置、加入 Vue.js 底層
3. 使用 Bootstrap 樣式可快速製作美觀的表單
4. 使用 Vue.js 可取得網頁上的欄位資料，將資料利用 Ajax 傳送到後端
5. Controller 語法與資料庫連線，執行查詢與新增動作
6. Model 定義 Controller 與 View 之間的傳遞欄位型別
7. 建立資料庫，執行範例
