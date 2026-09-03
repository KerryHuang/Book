---
kind: reprint
source: site:blog.hungwin.com.tw
author: hungwin
---

}o`@إ\ObxsW@ơAMbexܸơAiγ̷s\AоǱN|ЧApإ߫xi@ɭAæbexܸơC

оǽdҷ|إ ASP.NET Core MVC sMסAsW@ӫxi޲zAzLdܸƮwiơC

dߥƧe{O²檺ʧ@Aӧڷ|[Wd߬۹Oʧ@Aڷ|ܽd@ӧڱ`ΪkUѦҡC

dҨϥ ASP.NET Core MVC O .NET6Aeݨϥ Vue3 ج[AݸƮwϥ SQL Server 2019Aϥ Dapper MsuA好dҥiHUC

##### ؿ
[1 إ߱M](#step1)  
[2 ]pd߭](#step2)  
[3 Ʈwyk](#step3)  
[4 Mװ¦]w](#step4)  
&emsp;&emsp;[4.1 [J Vue3 M](#step5)  
&emsp;&emsp;[4.2 [J jQuery BlockUI Plugin M](#step6)  
&emsp;&emsp;[4.3  Json ^ǹw]pg]w](#step7)  
[5 dߤi](#step8)  
&emsp;&emsp;[5.1 View [ Vue3 yk](#step9)  
&emsp;&emsp;[5.2 Controller yk](#step10)  
&emsp;&emsp;[5.3 Ū appsettings.json](#step11)  
&emsp;&emsp;[5.4 w Dapper](#step12)  
&emsp;&emsp;[5.5 إ ViewModel](#step13)  
[6 W[dߥ\](#step14)  
&emsp;&emsp;[6.1 sW VuePagination.js ](#step15)  
&emsp;&emsp;[6.2 ޥ VuePagination.js ](#step16)  
&emsp;&emsp;[6.3 U VuePagination.js ](#step17)  
&emsp;&emsp;[6.4 ϥΤ](#step18)  
&emsp;&emsp;[6.5 View dߥ\վ](#step19)  
&emsp;&emsp;[6.6 grid W[ݩ](#step20)  
&emsp;&emsp;[6.7 Controller dߥ\վ](#step21)  
&emsp;&emsp;[6.8 ViewModel վ](#step22)  
&emsp;&emsp;[6.9 dҤU](#step23)  

## إ߱M

} Visual Studio 2022Aإ߷sM׬uASP.NET Core Web ε{ (Model-View-Controller)vC

![img1](https://blog.hungwin.com.tw/wp-content/uploads/2022/02/aspnet-mvc-anno-backstage-query-1.png)

JMצW١B|C

![img2](https://blog.hungwin.com.tw/wp-content/uploads/2022/02/aspnet-mvc-anno-backstage-query-2.png)

[cܡu.NET 6.0vAUuإߡvN|إߦMסC

![img3](https://blog.hungwin.com.tw/wp-content/uploads/2022/02/aspnet-mvc-anno-backstage-query-3.png)

## ]pd߭

o̧ڭ̷sW@ Controller MBzxi@C
b Controllers ksW@ӡuvC

![img4](https://blog.hungwin.com.tw/wp-content/uploads/2022/02/aspnet-mvc-anno-backstage-query-4.png)

ܡuMVC  V ťաv, WuAdmAnnoControllervC

b \Controllers\AdmAnnoController.cs ɮת Index() kusW˵vAiHsW View C

![img5](https://blog.hungwin.com.tw/wp-content/uploads/2022/02/aspnet-mvc-anno-backstage-query-5.png)

ܡuRazor ˵vAWٺw]uIndexvAĿuϥΪtmvAusWvC

![img5-1](https://blog.hungwin.com.tw/wp-content/uploads/2022/02/aspnet-mvc-anno-backstage-query-5-1.png)

e]pڭ̴Nq [Bootstrap](https://getbootstrap.com/docs/5.0/getting-started/introduction/) ƻs@ǾAXdܪdҨ View ̭C
ڥΨ쪺˦ [Card](https://getbootstrap.com/docs/5.0/components/card/), [Form](https://getbootstrap.com/docs/5.0/forms/overview/), [Table](https://getbootstrap.com/docs/5.0/content/tables/), [Button](https://getbootstrap.com/docs/5.0/components/buttons/)

ڳ]pFdߵeAϥΥHUykN \Views\AdmAnno\Index.cshtml 즳ykC

```XHTML
<div id="QueryPanel" class="card">
    <div class="card-header">
        i@
    </div>
    <div class="card-body">
        <div class="row">
            <div class="col-auto">
                <label for="AnnoSubject" class="col-form-label">iDD</label>
            </div>
            <div class="col-auto">
                <input type="text" id="AnnoSubject" class="form-control">
            </div>
            <div class="col-auto">
                <label for="AnnoStatus" class="col-form-label">iA</label>
            </div>
            <div class="col-auto">
                <select class="form-select" id="AnnoStatus">
                    <option value="1"></option>
                    <option value="0"></option>
                </select>
            </div>
        </div>
    </div>
    <div class="card-header">
        <button type="button" class="btn btn-primary">d</button>
    </div>
	<div class="card-body">
		<table class="table">
			<thead>
				<tr>
					<th>i</th>
					<th>iDD</th>
					<th>ie</th>
					<th>iA</th>
				</tr>
			</thead>
			<tbody>
			</tbody>
		</table>
	</div>
</div>
```

NProgram.csɮ׭˼ƲĤG檺`pattern: "{controller=Home}/{action=Index}/{id?}");`אּ`pattern: "{controller=AdmAnno}/{action=Index}/{id?}");`C

 F5 N|ݨHUeC

![img6](https://blog.hungwin.com.tw/wp-content/uploads/2022/02/aspnet-mvc-anno-backstage-query-6.png)

o̥DnO]pڭ̪eAUӴNn]pƮwM}lg{XFC

## Ʈwyk

ڭ̷|ϥ SQL Server ӷ@ƨӷAڤwgsWn Teach ƮwFAۥHUyksWi TableC

```Transact-SQL
CREATE TABLE [dbo].[Announcement] (
[Pkey] int IDENTITY(1, 1) NOT NULL,
[AnnoDate] date NOT NULL,
[AnnoSubject] nvarchar(50) NOT NULL,
[AnnoContent] nvarchar(1000) NOT NULL,
[AnnoStatus] smallint NOT NULL,
PRIMARY KEY CLUSTERED ([Pkey] ASC)
 ON [PRIMARY]
)
```

F Table Ao̧ڴNsW 16 ոơA]ڭ̲Ĥ@ӥ\OdߡAFƤ~ݥXGC

```Transact-SQL
insert into [dbo].[Announcement]([AnnoDate],[AnnoSubject],[AnnoContent],[AnnoStatus]) values ('2022-02-01 00:00:00',N'Subject1',N'Content1',1)
insert into [dbo].[Announcement]([AnnoDate],[AnnoSubject],[AnnoContent],[AnnoStatus]) values ('2022-02-02 00:00:00',N'Subject2',N'Content2',1)
insert into [dbo].[Announcement]([AnnoDate],[AnnoSubject],[AnnoContent],[AnnoStatus]) values ('2022-02-03 00:00:00',N'Subject3',N'Content3',1)
insert into [dbo].[Announcement]([AnnoDate],[AnnoSubject],[AnnoContent],[AnnoStatus]) values ('2022-02-04 00:00:00',N'Subject4',N'Content4',1)
insert into [dbo].[Announcement]([AnnoDate],[AnnoSubject],[AnnoContent],[AnnoStatus]) values ('2022-02-05 00:00:00',N'Subject5',N'Content5',1)
insert into [dbo].[Announcement]([AnnoDate],[AnnoSubject],[AnnoContent],[AnnoStatus]) values ('2022-02-06 00:00:00',N'Subject6',N'Content6',1)
insert into [dbo].[Announcement]([AnnoDate],[AnnoSubject],[AnnoContent],[AnnoStatus]) values ('2022-02-07 00:00:00',N'Subject7',N'Content7',1)
insert into [dbo].[Announcement]([AnnoDate],[AnnoSubject],[AnnoContent],[AnnoStatus]) values ('2022-02-08 00:00:00',N'Subject8',N'Content8',1)
insert into [dbo].[Announcement]([AnnoDate],[AnnoSubject],[AnnoContent],[AnnoStatus]) values ('2022-02-09 00:00:00',N'Subject9',N'Content9',1)
insert into [dbo].[Announcement]([AnnoDate],[AnnoSubject],[AnnoContent],[AnnoStatus]) values ('2022-02-10 00:00:00',N'Subject10',N'Content10',1)
insert into [dbo].[Announcement]([AnnoDate],[AnnoSubject],[AnnoContent],[AnnoStatus]) values ('2022-02-11 00:00:00',N'Subject11',N'Content11',1)
insert into [dbo].[Announcement]([AnnoDate],[AnnoSubject],[AnnoContent],[AnnoStatus]) values ('2022-02-12 00:00:00',N'Subject12',N'Content12',1)
insert into [dbo].[Announcement]([AnnoDate],[AnnoSubject],[AnnoContent],[AnnoStatus]) values ('2022-02-13 00:00:00',N'Subject13',N'Content13',1)
insert into [dbo].[Announcement]([AnnoDate],[AnnoSubject],[AnnoContent],[AnnoStatus]) values ('2022-02-14 00:00:00',N'Subject14',N'Content14',1)
insert into [dbo].[Announcement]([AnnoDate],[AnnoSubject],[AnnoContent],[AnnoStatus]) values ('2022-02-15 00:00:00',N'Subject15',N'Content15',1)
insert into [dbo].[Announcement]([AnnoDate],[AnnoSubject],[AnnoContent],[AnnoStatus]) values ('2022-02-16 00:00:00',N'Subject16',N'Content16',1)
```

## Mװ¦]w

o̷|w ASP.NET Core MVC M׼W[@ǰ¦]wAHK}oC

### [J Vue3 M

Vue3 Oeݱ쪺ج[OwA} \Views\Shared\_Layout.cshtml ɮסAbU JavaScript ޥμW[ Vue3 OwykAǪnDnb jQuery ~C

`<script src="https://unpkg.com/vue@3"></script>`

![img7](https://blog.hungwin.com.tw/wp-content/uploads/2022/02/aspnet-mvc-anno-backstage-query-7.png)

b Layout [W Vue3 ޥΫAڭ̴NiHbҦϥ Vue3 ykFAޥλykӷiѦҩxC

### [J jQuery BlockUI Plugin M

[jQuery BlockUI](https://jquery.malsup.com/block/) OeݦVݩIsɡAȮweݵeAHGIDC
b[J Vue3 M󪺤UA[JޥλykC

`<script src="https://malsup.github.io/jquery.blockUI.js"></script>`

###  Json ^ǹw]pg]w

b .NET Framework ϥ Json ^ǮɡAeݦ쪺 Json jpg]wP ViewModel ۦPAӦb .NET Core ɫhw]}Ypg (mpRW)Ao̧ڳ|վ㦨P ViewModel ۦPC

b Program.cs [JHUykG

```C#
//  Json ^ǤjpgP ViewModel ۦP
builder.Services.AddControllers().AddJsonOptions(options =>
    {
        options.JsonSerializerOptions.PropertyNamingPolicy = null;
    });
```

![img7-1](https://blog.hungwin.com.tw/wp-content/uploads/2022/02/aspnet-mvc-anno-backstage-query-7-1.png)

## dߤi

o̷|}lg{XAb]peW 2 ӬdA1 Ӭd߫sAUd߶sAaJd߱AqƮwŪƧe{C

### View [ Vue3 yk

ڭ̦b Index.cshtml ϥ Bootstrap ]pnFeAۭn[W Vue3 d߰ʰ_ӡC
NHUykл\ \Views\AdmAnno\Index.cshtml ̭C

```JavaScript
<div id="app">
    <div id="QueryPanel" class="card">
        <div class="card-header">
            i@
        </div>
        <div class="card-body">
            <div class="row">
                <div class="col-auto">
                    <label for="queryFormAnnoSubject" class="col-form-label">iDD</label>
                </div>
                <div class="col-auto">
                    <input type="text" id="queryFormAnnoSubject" class="form-control" v-model="queryForm.AnnoSubject">
                </div>
                <div class="col-auto">
                    <label for="queryFormAnnoStatus" class="col-form-label">iA</label>
                </div>
                <div class="col-auto">
                    <select class="form-select" id="queryFormAnnoStatus" v-model="queryForm.AnnoStatus">
                        <option value="1"></option>
                        <option value="0"></option>
                    </select>
                </div>
            </div>
        </div>
        <div class="card-header">
            <button type="button" class="btn btn-primary" v-on:click="Query()">d</button>
        </div>
		<div class="card-body">
			<table class="table">
				<thead>
					<tr>
						<th>i</th>
						<th>iDD</th>
						<th>ie</th>
						<th>iA</th>
					</tr>
				</thead>
				<tbody>
					<tr v-for="(item, index) in grid.datas">
						<td>{{item.AnnoDate}}</td>
						<td>{{item.AnnoSubject}}</td>
						<td>{{item.AnnoContent}}</td>
						<td>{{item.AnnoStatusName}}</td>
					</tr>
				</tbody>
			</table>
		</div>
    </div>
</div>
@section scripts {
<script>
    const app = Vue.createApp({
    data() {
        return {
            queryForm:{
                AnnoSubject: ''
                , AnnoStatus: '1'
            }
            , grid:{
                datas:[]
            }
        }
    }
    , methods: {
        Query() {
            var self = this;
 
            // զX
            var postData = {};
            postData['AnnoSubject'] = self.queryForm.AnnoSubject;
            postData['AnnoStatus'] = self.queryForm.AnnoStatus;
			
            $.blockUI();
            // ϥ jQuery Ajax ǰeܫ
            $.ajax({
                url:'@Url.Content("~/AdmAnno/Query")',
                method:'POST',
                dataType:'json',
                data: { inModel: postData },
                success: function (datas) {
					$.unblockUI();
                    if (datas.ErrMsg) {
                        alert(datas.ErrMsg);
                        return;
                    }
                    // jwC
                    self.grid.datas = datas.Grid;
                },
                error: function (err) {
                    $.unblockUI();
                    alert(err.status + " " + err.statusText + '\n' + err.responseText);
                }
            });
 
        }
      }
    });
	const vm = app.mount('#app');
</script>
}
```

### Controller yk

b View d߫|Is ~/AdmAnno/QueryAb \Controllers\AdmAnnoController.cs [JHU ActionC

```C#
/// <summary>
/// dߤi
/// </summary>
/// <param name="inModel"></param>
/// <returns></returns>
public IActionResult Query(QueryIn inModel)
{
	QueryOut outModel = new QueryOut();
	outModel.Grid = new List<AnnoModel>();
 
	// Ʈwsur
	string connStr = _configuration.GetConnectionString("SqlServer");
	using (var cn = new SqlConnection(connStr))
	{
		// Dnd SQL
		string sql = @"SELECT Pkey, CONVERT(varchar(12) , AnnoDate, 111 ) as AnnoDate, AnnoSubject, AnnoContent, AnnoStatus, Case AnnoStatus when '1' then '' when '0' then '' end As AnnoStatusName
						FROM Announcement 
						WHERE 1=1 ";
 
		if (!string.IsNullOrEmpty(inModel.AnnoSubject))
		{
			sql += " AND AnnoSubject LIKE @AnnoSubject ";
		}
		if (!string.IsNullOrEmpty(inModel.AnnoStatus))
		{
			sql += " AND AnnoStatus = @AnnoStatus ";
		}
		sql += " ORDER BY AnnoDate desc, AnnoStatus ";
		
		object param = new
		{
			AnnoSubject = "%" + inModel.AnnoSubject + "%",
			AnnoStatus = inModel.AnnoStatus
		};
		
		// ϥ Dapper d
		var list = cn.Query<AnnoModel>(sql, param);
		
		// X
		foreach (var item in list)
		{
			outModel.Grid.Add(item);
		}
	}
	return Json(outModel);
}
```

### Ū appsettings.json

ڱNƮwsub appsettings.json ̭A} appsettings.json A[JHUsurC

```Jason
"ConnectionStrings": {
	"SqlServer": "Data Source=127.0.0.1;Initial Catalog=Teach;Persist Security Info=false;User ID=test;Password=test;"
}
```

![img8](https://blog.hungwin.com.tw/wp-content/uploads/2022/02/aspnet-mvc-anno-backstage-query-8.png)

b .NET 6 no appsettings.json ]wӷAnb Controller W[غclŪ ConfigurationC

```C#
private readonly IConfiguration _configuration;
 
public AdmAnnoController(IConfiguration configuration)
{
	_configuration = configuration;
}
```

### w Dapper

ڸƮwʪϥηL ORM M DapperAݭnw Dapper ~ϥΡC
}ҡuM > ޲z NuGet MvC

![img9](https://blog.hungwin.com.tw/wp-content/uploads/2022/02/aspnet-mvc-anno-backstage-query-9.png)

jMuDappervAw˦MC

![img10](https://blog.hungwin.com.tw/wp-content/uploads/2022/02/aspnet-mvc-anno-backstage-query-10.png)

### إ ViewModel

ViewModel OΨөwq Controller P View wqAڭ̭إߤFs ControllerAҥHoӫإߥ ViewModelC
buModel k > [J > OvC

![img11](https://blog.hungwin.com.tw/wp-content/uploads/2022/02/aspnet-mvc-anno-backstage-query-11.png)

MRW AdmAnnoViewModelC

![img12](https://blog.hungwin.com.tw/wp-content/uploads/2022/02/aspnet-mvc-anno-backstage-query-12.png)

Mb AdmAnnoViewModel O̭A[Jb Controller Ψ쪺 ViewModelC

```C#
public class QueryIn
{
	public string AnnoSubject { get; set; }
	public string AnnoStatus { get; set; }
}
 
public class QueryOut
{
	public List<AnnoModel> Grid { get; set; }
}
 
public class AnnoModel
{
	public string Pkey { get; set; }
	public string AnnoDate { get; set; }
	public string AnnoSubject { get; set; }
	public string AnnoContent { get; set; }
	public string AnnoStatus { get; set; }
	public string AnnoStatusName { get; set; }
}
```

![img12-1](https://blog.hungwin.com.tw/wp-content/uploads/2022/02/aspnet-mvc-anno-backstage-query-12-1.png)

o̤Aڭ̴NiH²檺dߥ\FAU F5 AudߡvsANiHܥXƮwƤFC

![img13](https://blog.hungwin.com.tw/wp-content/uploads/2022/02/aspnet-mvc-anno-backstage-query-13.png)

iOoɭԧڭٯʤ@Ӥ\AUӧڭ̴N~򧹦оǡC

## W[dߥ\

W˦ܦhءAӧڴѧڳ̱`Ϊ Vue3 󵹦UѦҡAڭ̫eݬOإߦb Vue3 WAҥHڷ|b Vue3 sW@ӤC

oqоǷ|@IAڬOvBykоǡApGLkzѪܡAiUݤ@U㪺dҨӤ|e@IC

### sW VuePagination.js 

O@Ӧhƭ|Ψ쪺\AĳiHsW@ɮסAN޿gb̭AMb Vue3 NޤJC

b /js ؿsW@ɮסAɮשRW VuePagination.jsC

![img14](https://blog.hungwin.com.tw/wp-content/uploads/2022/02/aspnet-mvc-anno-backstage-query-14.png)

MbVuePagination.js KWHUykC

```JavaScript
const VuePagination = {
    data() {
        return {
            PerPage:'C'
            , PageTiems:''
            , Page:''
            , Times:''
            , Total:'@'
            , TotalPage:''
        }
    }
    , props: ['pagination']
    , template: `
        <div style="text-align:right">
            <span v-for="pageNo in pagination.pages">
                <a v-if="pagination.pageNo != pageNo" v-on:click="gotoPage(pageNo)" style="cursor:pointer">
                    {{ pageNo }}
                </a>
                <label v-else>
                    {{ "[" + pageNo + "]" }}
                </label>&nbsp;
            </span>
            <span class="pager-nav">
                i{{PerPage}}&nbsp;<input type="text" maxlength="3" style="width:35px;text-align:center;font-size:12px;" name="pageSize" :value="pagination.pageSize" v-on:change="onchange"/>
                &nbsp;{{PageTiems}}A
                {{Total}} {{pagination.totalPage}} {{TotalPage}} {{pagination.totalCount}} {{PageTiems}}j
                <button type="button" class="btn btn-secondary btn-sm pager-btn" style="margin-bottom: 5px;margin-right:5px;" v-on:click="gotoPage()">Q</button>
            </span>
        </div>`
    , methods: {
        gotoPage(pageNo) {
            var self = this;
            console.log(pageNo);
            // O_ǤJw
            if (pageNo !== undefined) {
                if (pageNo === '<') {
                    self.pagination.pageNo = parseInt(self.pagination.pageNo) - 1;
                } else if (pageNo === '>') {
                    self.pagination.pageNo = parseInt(self.pagination.pageNo) + 1;
                } else if (pageNo === '<<') {
                    self.pagination.pageNo = (Math.floor((parseInt(self.pagination.pageNo) - 10) / 10) * 10 + 1);
                } else if (pageNo === '>>') {
                    self.pagination.pageNo = (Math.floor((parseInt(self.pagination.pageNo) + 10) / 10) * 10 + 1);
                } else {
                    self.pagination.pageNo = parseInt(pageNo);
                }
            } else {
                self.pagination.pageNo = 1;
            }
            // wƬ0A۰ܧ1
            if (parseInt(self.pagination.pageNo) === 0 || self.IsNumeric(self.pagination.pageNo) === false) {
                self.pagination.pageNo = 1;
            }
            // wƤj`ơA۰ܧ`
            self.pagination.pageNo =
                parseInt(self.pagination.pageNo) > parseInt(self.pagination.totalPage)
                    ? self.pagination.totalPage : self.pagination.pageNo;
            // wƬ0A۰ܧ10
            if (parseInt(self.pagination.pageSize) === 0 || self.IsNumeric(self.pagination.pageSize) === false) {
                self.pagination.pageSize = 10;
            }
            // call on even
            this.$emit('requery', { pagination: self.pagination });
        }
        , onchange(e) {
            var self = this;
            var re = /[^0-9]/;
            if (re.test(e.target.value) === false) {
                self.pagination[e.target.name] = parseInt(e.target.value);
            }
        }
        , IsNumeric(n) {
            return (n - 0) === n && n.toString().length > 0;
        }
    }
};
```

### ޥ VuePagination.js 

b \Views\Shared\_Layout.cshtml  JavaScript W[ޥ VuePagination.js ɮסC

`<script src="~/js/VuePagination.js"></script>`

![img15](https://blog.hungwin.com.tw/wp-content/uploads/2022/02/aspnet-mvc-anno-backstage-query-15.png)

### U VuePagination.js 

Vue3 ݭnUb\Views\AdmAnno\Index.cshtmlɮת Vue.createApp({}); ~A Vue UAW٬ vue-paginationC

`app.component('vue-pagination', VuePagination);`

![img16](https://blog.hungwin.com.tw/wp-content/uploads/2022/02/aspnet-mvc-anno-backstage-query-16.png)

### ϥΤ

UnANiHbeWmAWC

`<vue-pagination v-bind:pagination="grid.pagination" v-on:requery="reQuery"></vue-pagination>`

![img20](https://blog.hungwin.com.tw/wp-content/uploads/2022/02/aspnet-mvc-anno-backstage-query-20.png)

]|sdߡAҥHo|Isd߭ reQuery() \A歫sdߡC

### View dߥ\վ

ڭ̭wggnF򥻪d Query()Ao̦]\Aվ@UAüW[@ reQuery() ɥiHsIsC
վ᪺kOG

```C#
Query(reQuery) {
	var self = this;
 
	if (reQuery !== 'reQuery') {
		self.grid.pagination.pageNo = 1;
	}
 
	// զX
	var postData = {};
	postData['AnnoSubject'] = self.queryForm.AnnoSubject;
	postData['AnnoStatus'] = self.queryForm.AnnoStatus;
 
	// [
	postData['pagination'] =  JSON.parse(JSON.stringify(self.grid.pagination));
 
	$.blockUI();
	// ϥ jQuery Ajax ǰeܫ
	$.ajax({
		url:'@Url.Content("~/AdmAnno/Query")',
		method:'POST',
		dataType:'json',
		data: { inModel: postData },
		success: function (datas) {
			$.unblockUI();
			if (datas.ErrMsg) {
				alert(datas.ErrMsg);
				return;
			}
			// jwC
			self.grid.datas = datas.Grid;
			self.grid.pagination = datas.pagination;
		},
		error: function (err) {
			$.unblockUI();
			alert(err.status + " " + err.statusText + '\n' + err.responseText);
		}
	});
 
}
// 歫d
, reQuery(emitData) {
	var self = this;
	if (emitData !== undefined) {
		self.grid.pagination = emitData.pagination;
	}
	self.Query('reQuery');
}
```

### grid W[ݩ

b Vue3 즳ŧi data ݩ grid nW[@ӤݩʡG

```JavaScript
, pagination: {
	pages: [], pageNo: '1', pageSize: '10', totalCount: ''
}
```

![img20-1](https://blog.hungwin.com.tw/wp-content/uploads/2022/02/aspnet-mvc-anno-backstage-query-20-1.png)

### Controller dߥ\վ

b Controller 쥻]gnF򥻬dߥ\Ao̦]W[d߫A]nվ@UykAiΥHUykN쥻ykG

```C#
/// <summary>
/// dߤi
/// </summary>
/// <param name="inModel"></param>
/// <returns></returns>
public IActionResult Query(QueryIn inModel)
{
	QueryOut outModel = new QueryOut();
	outModel.Grid = new List<AnnoModel>();
 
	// Ʈwsur
	string connStr = _configuration.GetConnectionString("SqlServer");
	using (var cn = new SqlConnection(connStr))
	{
		// Dnd SQL
		string sql = @"SELECT Pkey, CONVERT(varchar(12) , AnnoDate, 111 ) as AnnoDate, AnnoSubject, AnnoContent, AnnoStatus, Case AnnoStatus when '1' then '' when '0' then '' end As AnnoStatusName
						FROM Announcement 
						WHERE 1=1 ";
 
		if (!string.IsNullOrEmpty(inModel.AnnoSubject))
		{
			sql += " AND AnnoSubject LIKE @AnnoSubject ";
		}
		if (!string.IsNullOrEmpty(inModel.AnnoStatus))
		{
			sql += " AND AnnoStatus = @AnnoStatus ";
		}
		sql += " ORDER BY AnnoDate desc, AnnoStatus ";
 
		object param = new
		{
			AnnoSubject = "%" + inModel.AnnoSubject + "%",
			AnnoStatus = inModel.AnnoStatus
		};
 
		// Bz
		int totalRowCount = 0;
		if (inModel.pagination.pageNo > 0)
		{
			string orderBy = "";
			// o`
			string totalRowSql = sql;
			if (totalRowSql.ToUpper().IndexOf("ORDER BY") > -1)
			{
				orderBy = totalRowSql.Substring(sql.ToUpper().LastIndexOf("ORDER BY"));
				totalRowSql = totalRowSql.Replace(orderBy, "");
			}
			totalRowSql = "SELECT COUNT(*) AS CNT FROM (" + totalRowSql + ") CNT_TABLE";
			var rowCnt = cn.Query(totalRowSql, param);
			foreach (var item in rowCnt)
			{
				totalRowCount = item.CNT;
			}
 
			// o SQL
			int startRow = ((inModel.pagination.pageNo - 1) * inModel.pagination.pageSize) + 1;
			int endRow = (startRow + inModel.pagination.pageSize) - 1;
			orderBy = sql.Substring(sql.ToString().ToUpper().LastIndexOf("ORDER BY"));
			sql = sql.Replace(orderBy, "");
			// h Order by OW
			orderBy = orderBy.ToUpper().Replace("ORDER BY", "");
			StringBuilder newOrderBy = new StringBuilder();
			int index = 0;
			string[] orderBys = orderBy.Split(',');
			for (int i = 0; i < orderBys.Length; i++)
			{
				if (newOrderBy.Length > 0) { newOrderBy.Append(","); }
				string ob = orderBys[i];
				index = ob.IndexOf('.');
				if (index > -1)
				{
					newOrderBy.Append(ob.Substring(index + 1));
				}
				else
				{
					newOrderBy.Append(ob);
				}
			}
			newOrderBy.Insert(0, "ORDER BY ");
 
			sql = string.Concat(
				new object[] {
					"SELECT * FROM (SELECT *, ROW_NUMBER() OVER (", newOrderBy.ToString(), ") AS RCOUNT FROM (", sql, ") PAGE_SQL ) PAGE_SQL2 WHERE PAGE_SQL2.RCOUNT BETWEEN "
					, startRow, " AND ", endRow, " ", newOrderBy.ToString() });
		}
 
		// ϥ Dapper d
		var list = cn.Query<AnnoModel>(sql, param);
 
		// X
		foreach (var item in list)
		{
			outModel.Grid.Add(item);
		}
 
		// p
		outModel.pagination = this.PreparePage(inModel.pagination, totalRowCount);
	}
	return Json(outModel);
}
 
/// <summary>
/// p
/// </summary>
/// <param name="model"></param>
/// <param name="TotalRowCount"></param>
/// <returns></returns>
public PaginationModel PreparePage(PaginationModel model, int TotalRowCount)
{
	List<string> pages = new List<string>();
	int pageStart = ((model.pageNo - 1) / 10) * 10;
	model.totalCount = TotalRowCount;
	model.totalPage =
			Convert.ToInt16(Math.Ceiling(
			 double.Parse(model.totalCount.ToString()) / double.Parse(model.pageSize.ToString())
			));
 
	if (model.pageNo > 10)
		pages.Add("<<");
	if (model.pageNo > 1)
		pages.Add("<");
	for (int i = 1; i <= 10; ++i)
	{
		if (pageStart + i > model.totalPage)
			break;
		pages.Add((pageStart + i).ToString());
	}
	if (model.pageNo < model.totalPage)
		pages.Add(">");
	if ((pageStart + 10) < model.totalPage)
		pages.Add(">>");
	model.pages = pages;
	return model;
}
```

b SQL Server AڬOק SQL ykAd`ơAAd߻ݭndơACɡA|spAud߻ݭnƽdC

### ViewModel վ

ViewModel NOW[Ao̧ڴNKWykAiHNe ModelC

```C#
public class QueryIn
{
	public string AnnoSubject { get; set; }
	public string AnnoStatus { get; set; }
 
	public PaginationModel pagination { get; set; }
}
 
public class QueryOut
{
	public List<AnnoModel> Grid { get; set; }
	public PaginationModel pagination { get; set; }
}
 
public class AnnoModel
{
	public string Pkey { get; set; }
	public string AnnoDate { get; set; }
	public string AnnoSubject { get; set; }
	public string AnnoContent { get; set; }
	public string AnnoStatus { get; set; }
	public string AnnoStatusName { get; set; }
}
 
/// <summary>
//  Model
/// </summary>
public class PaginationModel
{
	public List<string> pages { get; set; }
	public int pageNo { get; set; }
	public int pageSize { get; set; }
	public int totalPage { get; set; }
	public int totalCount { get; set; }
}
```

o̫ANiHդ\FA F5 MסAd߸ƫN|ܤGC

![img17](https://blog.hungwin.com.tw/wp-content/uploads/2022/02/aspnet-mvc-anno-backstage-query-17.png)

 2 C

![img18](https://blog.hungwin.com.tw/wp-content/uploads/2022/02/aspnet-mvc-anno-backstage-query-18.png)

oOګܱ`ΪeݤAɵAC