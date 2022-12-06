在學習 C# 與資料庫的互動方式，有一個常見且實用的教學就是會員登入、註冊與修改會員資料等範例，學習過程中會用到資料庫新增、修改與查詢動作，是理解程式與資料庫互動的常見程式碼。
當學會了這個範例，將來為客戶開發系統的時候，馬上可以派上用場。

此篇文章是繼上一篇文章: [前台會員註冊範例 #CH1](https://blog.hungwin.com.tw/aspnet-mvc-member-register/) 接續教學。

範例內容以 ASP.NET MVC 為核心，前端使用 Vue.js 框架，而後端使用 SQL Server 當資料庫。

Vue.js 是前端3 大主流框架的其中之一，目標是透過簡單的 API 提供開發者實作資料綁定與操作網頁上的元件，Vue.js 的核心把焦點關注在狀態與畫面的同步層級上，適合與其他 JavsScript 函式庫整合，同時也適合當作 ASP.NET MVC 的前端框架。

SQL Server 是微軟推出的關聯式資料庫，使用 SQL 語言就可以輕鬆操作資料庫。

編寫此教學文章是為了幫助更多新加入的軟體工程師們，有更簡單實用的範例，可以快速學習程式語言。
這次我將會簡化這個基礎必學的前端會員範例，適合剛接觸 C# 與資料庫程式的新手學習。
文末有提供此操作範例的完整程式碼下載，有需要可以自行下載瀏覽。

##### 目錄 

[1 在 Controller 增加登入頁面 Action](#Step1)  
&emsp;&emsp;[1.1 增加登入頁面 View](#Step1)
[2 編寫登入 View 語法](#Step1)  
&emsp;&emsp;[2.1 加入 Vue.js 控制元件](#Step1)  
[3 編寫登入 Controller 語法](#Step1)  
&emsp;&emsp;[3.1 增加登入 Model](#Step1)  
[4 測試登入功能](#Step1)  
[5 重點整理](#Step1)  
&emsp;&emsp;[5.1 範例下載](#Step1)

## 在 Controller 增加登入頁面 Action

在上一篇已經完成了 MemberController.cs 的建立。
![img1](https://blog.hungwin.com.tw/wp-content/uploads/2021/09/aspnet-mvc-member-login-1.png)
這裡要新增一個登入的畫面，在 MemberController 類別內，增加 Login() 是登入畫面的 Action。
```c#
public ActionResult Login()
{
	return View();
}
```

### 增加登入頁面 View
在 Login() 語法上按右鍵選「新增檢視」。
![img2](https://blog.hungwin.com.tw/wp-content/uploads/2021/09/aspnet-mvc-member-login-2.png)
選擇「MVC 5 檢視」加入，確認名稱為 “Login”，有勾選「使用版面配置頁」。
![img3](https://blog.hungwin.com.tw/wp-content/uploads/2021/09/aspnet-mvc-member-login-3.png)
新增之後在 Views\Member\Login.cshtml 會新增 View 檢視頁面。
![img4](https://blog.hungwin.com.tw/wp-content/uploads/2021/09/aspnet-mvc-member-login-4.png)

## 編寫登入 View 語法

在 Bootstrap 3 的官方範例，有提供[表單的範例](https://getbootstrap.com/docs/3.3/css/#forms)、[面版的範例](https://getbootstrap.com/docs/3.3/components/#panels)及[按鈕的範例](https://getbootstrap.com/docs/3.3/css/#buttons)。
我從 Bootstrap 3 範例中語法組合變成我的登入畫面。

```html
<div class="panel panel-primary">
    <div class="panel-heading">登入頁面範例</div>
    <div class="panel-body">
        <div class="form-group">
            <label>帳號</label>
            <input type="text" class="form-control">
        </div>
        <div class="form-group">
            <label>密碼</label>
            <input type="password" class="form-control">
        </div>
    </div>
    <div class="panel-footer">
        <button type="button" class="btn btn-primary">登入</button>
    </div>
</div>
```
在 Login.cshtml 增加這些語法後，畫面就會出現登入表單。
![img5](https://blog.hungwin.com.tw/wp-content/uploads/2021/09/aspnet-mvc-member-login-5.png)
這只是一個沒有功能，純畫面的表單，目的在展示 Bootstrap 的語法。

### 加入 Vue.js 控制元件

我們在前面 _Layout.cshtml 已經加了 Vue.js 的底層元件，所以這登入頁面，就可以套用 Vue.js 的寫法。
我將剛剛的 HTML 修改一下，加入了 Vue.js 語法，並增加 `DoLogin()` 的方法，執行登入時傳送表單到 Controller 頁面。
我額外增加了 Bootstrap 的 modal 樣式，來顯示後端執行時的錯誤，這樣方便 Debug。
以下程式碼可以整個取代 Login.cshtml 內容。
```javascript
<div id="VuePage">
    <!--使用 Bootstrap 設計登入表單-->
    <div class="panel panel-primary">
        <div class="panel-heading">登入頁面範例</div>
        <div class="panel-body">
            <div class="form-group">
                <label>帳號</label>
                <input type="text" class="form-control" v-model="form.UserID">
            </div>
            <div class="form-group">
                <label>密碼</label>
                <input type="password" class="form-control" v-model="form.UserPwd">
            </div>
        </div>
        <div class="panel-footer">
            <button type="button" class="btn btn-primary" v-on:click="DoLogin()">登入</button>
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
                // 執行登入按鈕
                DoLogin: function () {
                    var self = this;

                    // 組合表單資料
                    var postData = {};
                    postData['UserID'] = self.form.UserID;
                    postData['UserPwd'] = self.form.UserPwd;

                    // 使用 jQuery Ajax 傳送至後端
                    $.ajax({
                        url:'@Url.Content("~/Member/DoLogin")',
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
`var postData` 主要在建立傳送表單，將 2 個欄位資料放進表單裡面，向後端傳送。

向後端傳送資料使用的是 [jQuery.ajax()](https://api.jquery.com/jquery.ajax/) 方法，方法內指定要傳送的網址 (url)、Http 協定(method)、資料型別 (dataType)、資料內容 (data)、成功回傳方法 (success)、失敗回傳方法 (error)。

關於 Vue.js 的教學語法，可以到[官網](https://cn.vuejs.org/v2/guide/)上面查詢，官網有完整的教學。

## 編寫登入 Controller 語法

剛剛在 View 會傳送一個動作呼叫 Member/DoLogin所以在 MemberController 需要建立回應的方法 `DoLogin()`。

```c#
/// <summary>
/// 執行登入
/// </summary>
/// <param name="inModel"></param>
/// <returns></returns>
public ActionResult DoLogin(DoLoginIn inModel)
{
	DoLoginOut outModel = new DoLoginOut();

	// 檢查輸入資料
	if (string.IsNullOrEmpty(inModel.UserID) || string.IsNullOrEmpty(inModel.UserPwd))
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

			// 將密碼轉為 SHA256 雜湊運算(不可逆)
			string salt = inModel.UserID.Substring(0, 1).ToLower(); //使用帳號前一碼當作密碼鹽
			SHA256 sha256 = SHA256.Create();
			byte[] bytes = Encoding.UTF8.GetBytes(salt + inModel.UserPwd); //將密碼鹽及原密碼組合
			byte[] hash = sha256.ComputeHash(bytes);
			StringBuilder result = new StringBuilder();
			for (int i = 0; i < hash.Length; i++)
			{
				result.Append(hash[i].ToString("X2"));
			}
			string CheckPwd = result.ToString(); // 雜湊運算後密碼

			// 檢查帳號、密碼是否正確
			string sql = "select * from Member where UserID = @UserID and UserPwd = @UserPwd";
			SqlCommand cmd = new SqlCommand();
			cmd.CommandText = sql;
			cmd.Connection = conn;

			// 使用參數化填值
			cmd.Parameters.AddWithValue("@UserID", inModel.UserID);
			cmd.Parameters.AddWithValue("@UserPwd", CheckPwd); // 雜湊運算後密碼

			// 執行資料庫查詢動作
			SqlDataAdapter adpt = new SqlDataAdapter();
			adpt.SelectCommand = cmd;
			DataSet ds = new DataSet();
			adpt.Fill(ds);

			if (ds.Tables[0].Rows.Count > 0)
			{
				// 有查詢到資料，表示帳號密碼正確

				// 將登入帳號記錄在 Session 內
				Session["UserID"] = inModel.UserID;

				outModel.ResultMsg = "登入成功";
			}
			else
			{
				// 查無資料，帳號或密碼錯誤
				outModel.ErrMsg = "帳號或密碼錯誤";
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

將傳入的參數來源宣告為 `DoLoginIn` 物件，將回傳的物件宣告為 `DoLoginOut`。
我習慣的命名方式為方法名稱的後面增加 In 及 Out 表示資料方向。
回傳的格式為 Json 格式，回傳前端呼叫 `Member/DoLogin()` 的登入結果。

當登入成功之後，我們將帳號寫入在 Session 裡面，之後在會員功能頁面檢查 Session 是否已完成登入。

在方法內主要是連線資料庫，在檢查密碼之前，先使用 SHA256 雜湊運算後，再檢查帳號密碼是否存在，存在時回傳”登入成功”，查無資料則回傳錯誤訊息。

### 增加登入 Model

因為在 Controller 增加了 2 個資料傳遞物件，
所以在 MemberModel.cs 類別內增加 `DoLoginIn` 及 `DoLoginOut` 兩個新類別。

```c#
/// <summary>
/// 登入參數
/// </summary>
public class DoLoginIn
{
	public string UserID { get; set; }
	public string UserPwd { get; set; }
}

/// <summary>
/// 登入回傳
/// </summary>
public class DoLoginOut
{
	public string ErrMsg { get; set; }
	public string ResultMsg { get; set; }
}
```
![img6](https://blog.hungwin.com.tw/wp-content/uploads/2021/09/aspnet-mvc-member-login-5-1.png)

`DoLoginIn` 定義由 View 傳入的欄位名稱，`DoLoginOut` 則定義 Controller 處理完之後，回傳給 View 的欄位名稱。
我對於 Model 的使用目的，只定義為 Controller 與 View 之間的資料傳遞物件。

## 測試登入功能
目前在資料庫內有一筆資料，帳號為 “admin”，密碼為 “123456”。
![img7](https://blog.hungwin.com.tw/wp-content/uploads/2021/09/aspnet-mvc-member-register-18-2.png)
在 VS 按「F5」執行專案，切換到「登入」頁面。
輸入正確的帳號密碼即會顯示 “登入成功” 的訊息，反之就會顯示 “帳號或密碼錯誤”。
![img8](https://blog.hungwin.com.tw/wp-content/uploads/2021/09/aspnet-mvc-member-login-7.png)

## 重點整理
1. MVC 為專案核心，Vue.js 處理前端控制，SQL Server 處理資料儲存
2. 在 Controller 增加 Login() 動作方法
3. 透過 Login() 動作方法新增 View 頁面
4. 使用 Bootstrap 樣式可快速製作美觀的表單
5. 使用 Vue.js 可取得網頁上的欄位資料，將資料利用 Ajax 傳送到後端
6. Controller 語法與資料庫連線，執行資料庫驗證帳號密碼
7. Model 定義 Controller 與 View 之間的資料傳遞物件


