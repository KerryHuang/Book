---
kind: original
---

# ECFIT

## API 範例

# Order

# Order - 取得訂單內容

利用提供的 訂單號碼 :order 取得訂單資訊，包含開立時的商品資料與折讓紀錄，此功能有存取頻率限制 ( 每分鐘 30 次 )，若超過將會回傳 429: Too Many Attempts.，除 Response 外，API 在標頭也會回傳 X-RateLimit-Limit、X-RateLimit-Remaining、Retry-After ( 如果到達限制次數就只能得到 Retry-After )

### GET
```html
https://{company}.ecfit.cc/api/order/:order
```

## Header
| Field                 | Type    | Description                |
| :-------------------- | :------ | :------------------------- |
| X-RateLimit-Limit     | Integer | 指定時間內最大允許存取次數 |
| X-RateLimit-Remaining | Integer | 指定時間內剩餘存取次數     |
| Retry-After           | Integer | 距離下次重新請求的等待時間 |

## Parameter
| Field | Type   | Description                                   |
| :---- | :----- | :-------------------------------------------- |
| order | String | 訂單號碼，ex : EC201601010001Size range: `16` |

## Success 200
| Field             | Type     | Description                                                  |
| :---------------- | :------- | :----------------------------------------------------------- |
| status            | String   | 開立結果 success : 成功，fail : 失敗                         |
| code              | String   | 結果代號                                                     |
| 00                | String   | 查詢成功                                                     |
| 01                | String   | 訂單編號為空                                                 |
| 11                | String   | 訂單不存在                                                   |
| msg               | String   | 回傳處理結果                                                 |
| content           | Array[]  | 內容陣列                                                     |
| orderNo           | String   | 原始訂單編號                                                 |
| ecfitNo           | String   | ECFIT訂單流水號                                              |
| amount            | Integer  | 訂單金額                                                     |
| invoiced          | Integer  | 是否開立發票                                                 |
| ban               | String   | 買家統編                                                     |
| AllPayLogisticsID | String   | 綠界物流交易編號                                             |
| paidDate          | Date     | 付款日期                                                     |
| NPO               | String   | 捐贈碼                                                       |
| demand            | String   | 是否有索取紙本發票                                           |
| collection        | Integer  | 代收金額                                                     |
| logisticsId       | String   | 貨運公司                                                     |
| production        | Array[]  | 購買商品陣列                                                 |
| pid               | String   | 商品品號                                                     |
| barcode           | String   | 商品條碼                                                     |
| name              | String   | 名稱                                                         |
| quantity          | Integer  | 數量                                                         |
| price             | Integer  | 單價                                                         |
| deliveryRecord    | Object[] | 物流紀錄                                                     |
| key               | String   | 物流 ID                                                      |
| value             | Array[]  | 物流過程                                                     |
| customer          | Object   | 消費者資料                                                   |
| name              | String   | 名字                                                         |
| address           | String   | 地址                                                         |
| phone             | String   | 電話                                                         |
| buyer             | Object   | 購買人資料                                                   |
| name              | String   | 名字                                                         |
| address           | String   | 地址                                                         |
| email             | String   | 信箱                                                         |
| phone             | String   | 電話                                                         |
| status            | String   | 0 : 尚未檢查1 : 上傳完成2 : 等待開立發票 (只有有配合開立發票的訂單才會有此狀態)3 : 發票開立完成 (只有有配合開立發票的訂單才會有此狀態)5 : 發票開立完成等待撿貨( 無發票的訂單是 1 的時候就是上傳成功準備出貨，需要開立發票的訂單需要到5 才是可以出貨。以上狀態都可以按訂單結案。 )4 : 撿貨中( 代表此訂單正在理貨批次處理中，但是不代表此訂單今天可以出貨，有可能因為缺貨所以無法包貨成功。撿貨中不可以結案只能取消。 )--以下狀態代表此訂單生命週期結束--6 : 完成( 代表此訂單已經包貨完畢，會看得到物流編號。但是不一定代表已經被物流公司收走，因為物流公司收貨時間是固定。 )8 : 結案( 結案代表為您已經人工將此訂單點選為結案，此訂單已經不會再被處理 )10 : 取消( 代表此訂單您已經人工點選取消，此訂單已經不會再被處理 )99 : 訂單錯誤( 代表此訂單建立失敗，可於修正並刪除錯誤紀錄後重新建立 ) |

- [成功回傳:](https://guide.ecfit.cc/apiDoc/#success-examples-Order-Get_Order-0_0_0-0)
```json
HTTP/1.1 200 OK
{
    "status"        : "success",
    "code"          : "00",
    "msg"           : "查詢成功",
    "content"       : [{
    "orderNo"       : "EC20160101001",
    "ecfitNo"       : "00000013332",
    "amount"        : 5040,
    "remain"        : 3360,
    "invoice"       : "AB00000001",
    "ban"           : "",
    "AllPayLogisticsID" : "2583129",
    "paidDate"      : "2016-01-01",
    "invoicingDate" : "2016-01-01 01:01:01",
    "NPO"           : "",
    "demand"        : "N",
    "collection"    : 0,
    "logisticsId"   : "黑貓宅急便",
    "production"    : [{
        "id"        : "0104030143",
        "name"      : "【Fitty】運動壓力褲／壓縮褲（女款・七分全黑）【M】",
        "quantity"  : 1,
        "price"     : 1680
    },
    {
        "id"        : "0204030255",
        "name"      : "【Fitty】運動壓力褲／壓縮褲（邊彩七分款）﹣舞蝶粉【舞蝶粉 M】",
        "quantity"  : 1,
        "price"     : 1680
    }],
    "deliveryRecord" : {
        "4718037235420" : [{
            "CheckID"               : "4718037235420",
            "Name"                  : "宜蘭營業本所",
            "Date"                  : "20161003163751",
            "RtnCode"               : "300",
            "AllPayLogisticsID"     : "2583129",
            "Description"           : "轉運中",
            "ClientID"              : "",
            "Transport"             : "黑貓",
            "Status"                : 1
        }, {
            "CheckID"               : "4718037235420",
            "Name"                  : "三重一營業本所",
            "Date"                  : "20161004072045",
            "RtnCode"               : "300",
            "AllPayLogisticsID"     : "2583129",
            "Description"           : "配送中",
            "ClientID"              : "",
            "Transport"             : "黑貓",
            "Status"                : 1
        }, {
            "CheckID"               : "4718037235420",
            "Name"                  : "三重一營業本所",
            "Date"                  : "20161004080753",
            "RtnCode"               : "300",
            "AllPayLogisticsID"     : "2583129",
            "Description"           : "轉交配送中",
            "ClientID"              : "",
            "Transport"             : "黑貓",
            "Status"                : 1
        }, {
            "CheckID"               : "4718037235420",
            "Name"                  : "三重一營業本所",
            "Date"                  : "20161004081513",
            "RtnCode"               : "310",
            "AllPayLogisticsID"     : "2583129",
            "Description"           : "配完",
            "ClientID"              : "",
            "Transport"             : "黑貓",
            "Status"                : 1
        }],
        "4718037236366" : [{
            "CheckID"               : "4718037236366",
            "Name"                  : "宜蘭營業本所",
            "Date"                  : "20161003163751",
            "RtnCode"               : "300",
            "AllPayLogisticsID"     : "2583129",
            "Description"           : "轉運中",
            "ClientID"              : "",
            "Transport"             : "黑貓",
            "Status"                : 1
        }, {
            "CheckID"               : "4718037236366",
            "Name"                  : "三重一營業本所",
            "Date"                  : "20161004072045",
            "RtnCode"               : "300",
            "AllPayLogisticsID"     : "2583129",
            "Description"           : "配送中",
            "ClientID"              : "",
            "Transport"             : "黑貓",
            "Status"                : 1
        }, {
            "CheckID"               : "4718037236366",
            "Name"                  : "三重一營業本所",
            "Date"                  : "20161004080753",
            "RtnCode"               : "300",
            "AllPayLogisticsID"     : "2583129",
            "Description"           : "轉交配送中",
            "ClientID"              : "",
            "Transport"             : "黑貓",
            "Status"                : 1
        }, {
            "CheckID"               : "4718037236366",
            "Name"                  : "三重一營業本所",
            "Date"                  : "20161004081513",
            "RtnCode"               : "310",
            "AllPayLogisticsID"     : "2583129",
            "Description"           : "配完",
            "ClientID"              : "",
            "Transport"             : "黑貓",
            "Status"                : 1
        }]
    },
    "customer"      : {
        "name"      : "林先生",
        "address"   : "台北市松山區",
        "phone"     : "0937000000"
    },
    "buyer"      : {
        "name"      : "陳小姐",
        "address"   : "台北市士林區",
        "email"     : "fgh@mail.com",
        "phone"     : "0912345678"
    },
    "status"       : "6"
    }]
 }
```
- [失敗回傳:](https://guide.ecfit.cc/apiDoc/#success-examples-Order-Get_Order-0_0_0-1)
```
HTTP/1.1 200 OK
{
    "status" : "fail",
    "code"   : "01",
    "msg"    : "訂單編號為空"
}
```


# Order - 取得訂單內容(post方法)

利用提供的 訂單號碼 取得訂單資訊，包含開立時的商品資料與折讓紀錄，此功能有存取頻率限制 ( 每分鐘 30 次 )，若超過將會回傳 429: Too Many Attempts.，除 Response 外，API 在標頭也會回傳 X-RateLimit-Limit、X-RateLimit-Remaining、Retry-After ( 如果到達限制次數就只能得到 Retry-After )

### POST
```html
https://{company}.ecfit.cc/api/orderContent
```

## Header
| Field                 | Type    | Description                |
| :-------------------- | :------ | :------------------------- |
| X-RateLimit-Limit     | Integer | 指定時間內最大允許存取次數 |
| X-RateLimit-Remaining | Integer | 指定時間內剩餘存取次數     |
| Retry-After           | Integer | 距離下次重新請求的等待時間 |

## Parameter
| Field   | Type   | Description                                   |
| :------ | :----- | :-------------------------------------------- |
| orderNo | String | 訂單號碼，ex : EC201601010001Size range: `16` |

## Success 200
| Field             | Type     | Description                                                  |
| :---------------- | :------- | :----------------------------------------------------------- |
| status            | String   | 開立結果 success : 成功，fail : 失敗                         |
| code              | String   | 結果代號                                                     |
| 00                | String   | 查詢成功                                                     |
| 01                | String   | 訂單編號為空                                                 |
| 11                | String   | 訂單不存在                                                   |
| msg               | String   | 回傳處理結果                                                 |
| content           | Array[]  | 內容陣列                                                     |
| orderNo           | String   | 原始訂單編號                                                 |
| ecfitNo           | String   | ECFIT訂單流水號                                              |
| amount            | Integer  | 訂單金額                                                     |
| invoiced          | Integer  | 是否開立發票                                                 |
| invoiceNo         | Integer  | 發票號碼                                                     |
| collection        | Integer  | 代收金額                                                     |
| logisticsId       | String   | 貨運公司                                                     |
| ban               | String   | 買家統編                                                     |
| paidDate          | Date     | 付款日期                                                     |
| NPO               | String   | 捐贈碼                                                       |
| demand            | String   | 是否有索取紙本發票                                           |
| creditNo          | String   | 信用卡後4碼                                                  |
| carrierType       | String   | 載具類型                                                     |
| carrierId         | String   | 載具號碼                                                     |
| AllPayLogisticsID | String   | 綠界物流交易編號                                             |
| status            | String   | 0 : 尚未檢查1 : 上傳完成2 : 等待開立發票 (只有有配合開立發票的訂單才會有此狀態)3 : 發票開立完成 (只有有配合開立發票的訂單才會有此狀態)5 : 發票開立完成等待撿貨( 無發票的訂單是 1 的時候就是上傳成功準備出貨，需要開立發票的訂單需要到5 才是可以出貨。以上狀態都可以按訂單結案。 )4 : 撿貨中( 代表此訂單正在理貨批次處理中，但是不代表此訂單今天可以出貨，有可能因為缺貨所以無法包貨成功。撿貨中不可以結案只能取消。 )--以下狀態代表此訂單生命週期結束--6 : 完成( 代表此訂單已經包貨完畢，會看得到物流編號。但是不一定代表已經被物流公司收走，因為物流公司收貨時間是固定。 )8 : 結案( 結案代表為您已經人工將此訂單點選為結案，此訂單已經不會再被處理 )10 : 取消( 代表此訂單您已經人工點選取消，此訂單已經不會再被處理 )99 : 訂單錯誤( 代表此訂單建立失敗，可於修正並刪除錯誤紀錄後重新建立 ) |
| production        | Array[]  | 購買商品陣列                                                 |
| pid               | String   | 商品品號                                                     |
| barcode           | String   | 商品條碼                                                     |
| name              | String   | 名稱                                                         |
| quantity          | Integer  | 數量                                                         |
| price             | Integer  | 單價                                                         |
| serial            | Integer  | 流水編號                                                     |
| deliveryRecord    | Object[] | 物流紀錄                                                     |
| key               | String   | 物流 ID                                                      |
| value             | Array[]  | 物流過程                                                     |
| customer          | Object   | 消費者資料                                                   |
| name              | String   | 名字                                                         |
| address           | String   | 地址                                                         |
| phone             | String   | 電話                                                         |
| buyer             | Object   | 購買人資料                                                   |
| name              | String   | 名字                                                         |
| address           | String   | 地址                                                         |
| email             | String   | 信箱                                                         |
| phone             | String   | 電話                                                         |

- [成功回傳:](https://guide.ecfit.cc/apiDoc/#success-examples-Order-Post_OrderContent-0_0_0-0)
```json
HTTP/1.1 200 OK
{
	"status"        : "success",
	"code"          : "00",
	"msg"           : "查詢成功",
	"content"       : [{
		"orderNo"       : "EC20160101001",
		"ecfitNo"       : "00000013332",
		"amount"        : 5040,
		"remain"        : 3360,
		"invoiced"      : "Y",
		"invoiceNo"     : "AB00000001",
		"collection"    : 0,
		"logisticsId"   : "黑貓宅急便",
		"ban"           : "",
		"paidDate"      : "2016-01-01",
		"NPO"           : "",
		"demand"        : "N",
		"creditNo"      : "1234",
		"carrierType"   : "",
		"carrierId"     : "",
            "AllPayLogisticsID" : "2583129",
		"status"        : "8",
		"production"    : [{
			"id"        : "0104030143",
			"name"      : "【Fitty】運動壓力褲／壓縮褲（女款・七分全黑）【M】",
			"quantity"  : 1,
			"price"     : 1680
		},
		{
			"id"        : "0204030255",
			"name"      : "【Fitty】運動壓力褲／壓縮褲（邊彩七分款）﹣舞蝶粉【舞蝶粉 M】",
			"quantity"  : 1,
			"price"     : 1680
		}],
		"deliveryRecord" : {
			"4718037235420" : [{
				"CheckID"     : "4718037235420",
				"Name"        : "宜蘭營業本所",
				"Date"        : "20161003163751",
				"Description" : "轉運中",
				"ClientID"    : "",
				"Transport"   : "黑貓",
				"Status"      : 1
			}, {
				"CheckID"     : "4718037235420",
				"Name"        : "三重一營業本所",
				"Date"        : "20161004072045",
				"Description" : "配送中",
				"ClientID"    : "",
				"Transport"   : "黑貓",
				"Status"      : 1
			}, {
				"CheckID"     : "4718037235420",
				"Name"        : "三重一營業本所",
				"Date"        : "20161004080753",
				"Description" : "轉交配送中",
				"ClientID"    : "",
				"Transport"   : "黑貓",
				"Status"      : 1
			}, {
				"CheckID"     : "4718037235420",
				"Name"        : "三重一營業本所",
				"Date"        : "20161004081513",
				"Description" : "配完",
				"ClientID"    : "",
				"Transport"   : "黑貓",
				"Status"      : 1
			}],
			"4718037236366" : [{
				"CheckID"     : "4718037236366",
				"Name"        : "宜蘭營業本所",
				"Date"        : "20161003163751",
				"Description" : "轉運中",
				"ClientID"    : "",
				"Transport"   : "黑貓",
				"Status"      : 1
			}, {
				"CheckID"     : "4718037236366",
				"Name"        : "三重一營業本所",
				"Date"        : "20161004072045",
				"Description" : "配送中",
				"ClientID"    : "",
				"Transport"   : "黑貓",
				"Status"      : 1
			}, {
				"CheckID"     : "4718037236366",
				"Name"        : "三重一營業本所",
				"Date"        : "20161004080753",
				"Description" : "轉交配送中",
				"ClientID"    : "",
				"Transport"   : "黑貓",
				"Status"      : 1
			}, {
				"CheckID"     : "4718037236366",
				"Name"        : "三重一營業本所",
				"Date"        : "20161004081513",
				"Description" : "配完",
				"ClientID"    : "",
				"Transport"   : "黑貓",
				"Status"      : 1
			}]
		},
		"customer"      : {
			"name"      : "林先生",
			"address"   : "台北市松山區",
			"phone"     : "0937000000"
		},
		"buyer"      : {
			"name"      : "陳小姐",
			"address"   : "台北市士林區",
			"email"     : "fgh@mail.com",
			"phone"     : "0912345678"
		}
	}]
}
```
- [失敗回傳:](https://guide.ecfit.cc/apiDoc/#success-examples-Order-Post_OrderContent-0_0_0-1)
```
HTTP/1.1 200 OK
{
    "status" : "fail",
    "code"   : "01",
    "msg"    : "訂單編號為空"
}
```


# Order - 取消訂單

### POST
```html
https://{company}.ecfit.cc/api/orderCancel/:orderNo
```

## Parameter
| Field   | Type   | Description                                   |
| :------ | :----- | :-------------------------------------------- |
| orderNo | String | 訂單編號，ex : EC201601010001Size range: `16` |

## Success 200
| Field        | Type   | Description                          |
| :----------- | :----- | :----------------------------------- |
| status       | String | 開立結果 success : 成功，fail : 失敗 |
| code         | String | 結果代號                             |
| 00           | String | 成功                                 |
| 01           | String | 訂單不存在                           |
| 02           | String | 訂單已為 取消 或 結案                |
| 03           | String | 訂單狀態為 錯誤 不可執行取消         |
| msg          | String | 回傳處理結果                         |
| orderNo      | String | 訂單編號                             |
| orderstatusS | String | 訂單處理前狀態                       |
| orderstatusE | String | 訂單處理後狀態                       |

- [成功回傳:](https://guide.ecfit.cc/apiDoc/#success-examples-Order-Cancel_Order-0_0_0-0)
- [失敗回傳:](https://guide.ecfit.cc/apiDoc/#success-examples-Order-Cancel_Order-0_0_0-1)

```json
HTTP/1.1 200 OK
{
    "status"         : "success",
    "code"           : "00",
    "msg"            : "訂單已取消出貨",
    "orderNo"        : "EC201601010001",
    "orderstatusS"   : "撿貨中",
    "orderstatusE"   : "訂單取消"
}
```


# Order - 開立訂單

### POST
```html
https://{company}.ecfit.cc/api/order
```

## Parameter
| Field         | Type    | Description                                                  |
| :------------ | :------ | :----------------------------------------------------------- |
| orderNo       | String  | 訂單編號Size range: `16`                                     |
| amount        | Integer | 訂單金額                                                     |
| paidDate      | String  | 付款日期 ex: 2016-01-01Size range: `10`                      |
| creditNo      | Integer | 信用卡末 4 碼（使用非信用卡消費時可以留空）Size range: `4`   |
| NPO           | String  | 捐贈給社福單位的愛心碼 (不捐贈可以留空)                      |
| ban           | String  | 買方統編 (沒有時可以留空)Size range: `8`                     |
| taxType       | String  | 課稅類別 1 : 應稅, 2 : 零稅率, 3 : 免稅, 9 : 混稅(限收銀機發票無法分辨時使用) 預設為 1 : 應稅Allowed values: `1`, `2`, `3`, `9` |
| clearanceMark | String  | 通關方式 1 : 非經海關出口, 2 : 經海關出口 (若課稅類別不為零稅率者，此欄無須填寫)Allowed values: `1`, `2` |
| invoiced      | String  | 是否開立發票Size range: `1`Allowed values: `N`, `Y`          |
| demand        | String  | 是否索取發票Size range: `1`Allowed values: `N`, `Y`          |
| carrierType   | String  | 使用載具 cellphone : 手機載具, citizen : 自然人憑證 (若不使用載具此欄可以不填)Allowed values: `cellphone`, `citizen` |
| carrierId     | String  | 載具號碼                                                     |
| collection    | Integer | 代收款項                                                     |
| arrive        | String  | 預計出貨日 ex: 2016-01-01Size range: `10`                    |
| arriveType    | String  | 配送時段代號，預設為 4(不指定) [09:00~12:00 上午到貨為1/12:00~17:00 下午到貨為2/不指定為4] |
| logisticsId   | String  | 貨運公司[黑貓宅急便/通盈/全家/綠界/海外/自訂1]               |
| code          | String  | 商店代碼(貨運為全家/綠界時必填，非全家/綠界可以不傳或是傳空值) |
| note          | Text    | 備註                                                         |
| production    | Array[] | 購買商品陣列                                                 |
| barcode       | String  | 商品條碼                                                     |
| name          | String  | 名稱                                                         |
| quantity      | Integer | 數量                                                         |
| price         | Integer | 單價                                                         |
| taxType       | Integer | 商品課稅類別， 1 : 應稅, 2 : 零稅率, 3 : 免稅，預設為 1 : 應稅API 開立發票以「taxType」為開立依據；若課稅類別為「混稅」之發票，須另外填寫個別商品之稅率及稅別，預設為 應稅Allowed values: `1`, `2`, `3` |
| taxRate       | Integer | 商品稅率，填寫正整數，預設為 5(%)API 開立發票以「taxType」為開立依據；若課稅類別為「混稅」之發票，須另外填寫商品之個別稅率及稅別，預設為 應稅 |
| customer      | Object  | 消費者資料 (姓名、地址、郵遞區號、電話 為必填)               |
| name          | String  | 姓名                                                         |
| address       | String  | 地址                                                         |
| postal        | String  | 郵遞區號                                                     |
| phone         | String  | 電話                                                         |
| buyer         | Object  | 購買人資料 (欲開立發票者須填寫 姓名、地址、郵遞區號、信箱、電話，用以發票與折讓單的開立及寄送，其餘狀況則不須填寫) |
| name          | String  | 姓名                                                         |
| address       | String  | 地址                                                         |
| postal        | String  | 郵遞區號                                                     |
| email         | String  | 信箱                                                         |
| phone         | String  | 電話                                                         |

- [Request-Example:](https://guide.ecfit.cc/apiDoc/#parameter-examples-Order-ordering-0_0_0-0)

```json
{
    "orderNo": "EC2016010100001",
    "amount": "1680",
    "paidDate": "2016-09-01",
    "creditNo": "1234",
    "invoiced": "Y",
    "ban": "",
    "taxType": "1",
    "clearanceMark": "1",
    "NPO": "919",
    "demand": "N",
    "collection": 0,
    "arrive": "2016-11-4",
    "arriveType": "4",
    "note": "Test",
    "logisticsId": "黑貓宅急便",
    "production": [
        {
            "barcode": "0206030028",
            "name": "【Fitty】運動壓力褲（秋冬九分・女款﹣經典全黑）2015 版 ",
            "quantity": "1",
            "price": "1480",
            "taxType": "1",
            "taxRate": "5"
        },
        {
            "barcode": "shipment",
            "name": "運費",
            "quantity": "1",
            "price": "200"
        }
    ],
    "customer": {
        "name": "林先生",
        "address": "台北市松山區",
        "postal": "204",
        "phone": "0937000000"
    },
    "buyer": {
        "name": "陳小姐",
        "address": "台北市中山區",
        "email": "fghe@mail.com",
        "postal": "104",
        "phone": "0912345678"
    }
}
```

## Success 200
| Field   | Type   | Description                          |
| :------ | :----- | :----------------------------------- |
| status  | String | 開立結果 success : 成功，fail : 失敗 |
| code    | String | 結果代號                             |
| 00      | String | 成功                                 |
| 01      | String | 訂單編號為空                         |
| 02      | String | 是否開立發票欄位為空值               |
| 03      | String | 買方統一編號錯誤                     |
| 04      | String | 捐贈碼錯誤                           |
| 05      | String | 捐贈發票不得開立買方統一編號         |
| 06      | String | 捐贈發票不得索取                     |
| 07      | String | 消費者資訊有缺                       |
| 08      | String | 品項空白 或 產品數量為 0             |
| 09      | String | 金額錯誤 (與產品價格對不起來)        |
| 10      | String | 不明原因問題                         |
| msg     | String | 回傳處理結果                         |
| orderNo | String | 訂單編號                             |

- [成功回傳:](https://guide.ecfit.cc/apiDoc/#success-examples-Order-ordering-0_0_0-0)
```json
HTTP/1.1 200 OK
{
    "status"         : "success",
    "code"           : "00",
    "msg"            : "成功",
    "orderNo"        : "EC20160101001"
}
```
- [失敗回傳:](https://guide.ecfit.cc/apiDoc/#success-examples-Order-ordering-0_0_0-1)
```
HTTP/1.1 200 OK
{
    "status"         : "fail",
    "code"           : "01",
    "msg"            : "訂單編號為空"
}
```


# Invoice

# Invoice - 開立發票

### POST
```html
https://{company}.ecfit.cc/api/invoice
```

## Parameter
| Field         | Type    | Description                                                  |
| :------------ | :------ | :----------------------------------------------------------- |
| orderNo       | String  | 訂單編號Size range: `16`                                     |
| amount        | Integer | 訂單金額                                                     |
| paidDate      | String  | 付款日期 ex: 2016-01-01Size range: `10`                      |
| creditNo      | Integer | 信用卡末 4 碼（使用非信用卡消費時可以留空）Size range: `4`   |
| note          | String  | 備註Size range: `200`                                        |
| NPO           | String  | 捐贈給社福單位的愛心碼 (不捐贈可以留空)                      |
| buyerBan      | String  | 買方統編 (沒有時可以留空)Size range: `8`                     |
| demand        | Number  | 是否索取發票Allowed values: `0`, `1`                         |
| carrierType   | String  | 使用載具 cellphone : 手機載具, citizen : 自然人憑證 (若不使用載具此欄可以不填)Allowed values: `cellphone`, `citizen` |
| carrierId     | String  | 載具號碼                                                     |
| files         | string  | 是否夾帶檔案，0：否、1：是Allowed values: `0`, `1`           |
| taxType       | String  | 課稅類別 1 : 應稅, 2 : 零稅率, 3 : 免稅, 9 : 混稅(限收銀機發票無法分辨時使用) 預設為 1 : 應稅Allowed values: `1`, `2`, `3`, `9` |
| clearanceMark | String  | 通關方式 1 : 非經海關出口, 2 : 經海關出口 (若課稅類別不為零稅率者，此欄無須填寫)Allowed values: `1`, `2` |
| production    | Array[] | 購買商品陣列                                                 |
| barcode       | String  | 商品條碼                                                     |
| name          | String  | 名稱                                                         |
| quantity      | Integer | 數量                                                         |
| price         | Integer | 單價                                                         |
| taxType       | Integer | 商品課稅類別， 1 : 應稅, 2 : 零稅率, 3 : 免稅，預設為 1 : 應稅API 開立發票以「taxType」為開立依據；若課稅類別為「混稅」之發票，須另外填寫個別商品之稅率及稅別，預設為 應稅Allowed values: `1`, `2`, `3` |
| taxRate       | Integer | 商品稅率，填寫正整數，預設為 5(%)API 開立發票以「taxType」為開立依據；若課稅類別為「混稅」之發票，須另外填寫商品之個別稅率及稅別，預設為 應稅 |
| customer      | Object  | 消費者資料 (姓名、地址、信箱為必填，用以發票與折讓單的寄送及開立) |
| name          | String  | 名字                                                         |
| postal        | String  | 郵遞區號                                                     |
| address       | String  | 地址                                                         |
| email         | String  | 信箱                                                         |
| phone         | String  | 電話                                                         |

- [Request-Example:](https://guide.ecfit.cc/apiDoc/#parameter-examples-Invoice-Invoicing-0_0_0-0)

```json
{
    "orderNo": "EC20160101001",
    "amount": 5040,
    "paidDate": "2016-01-01",
    "creditNo": "1234",
    "note": "TEST",
    "buyerBan": "12345678",
    "NPO": 876,
    "demand": 1,
    "carrierType": "cellphone",
    "carrierId": "/425WP5Q",
    "taxType": "1",
    "clearanceMark": "1",
    "production": [
        {
            "barcode": "0104030143",
            "name": "【Fitty】運動壓力褲／壓縮褲（女款・七分全黑）【M】",
            "quantity": 1,
            "price": 1680,
            "taxType": "1",
            "taxRate": "5"
        },
        {
            "barcode": "0204030255",
            "name": "【Fitty】運動壓力褲／壓縮褲（邊彩七分款）﹣舞蝶粉【舞蝶粉 M】",
            "quantity": 2,
            "price": 1680,
            "taxType": "1",
            "taxRate": "5"
        }
    ],
    "customer": {
        "name": "林先生",
        "postal": "105",
        "address": "台北市松山區",
        "email": "abcde@mail.com",
        "phone": "0937000000"
    }
}
```

## Success 200
| Field         | Type     | Description                          |
| :------------ | :------- | :----------------------------------- |
| status        | String   | 開立結果 success : 成功，fail : 失敗 |
| code          | String   | 結果代號                             |
| 00            | String   | 開立成功                             |
| 01            | String   | 訂單編號為空                         |
| 02            | String   | 無法產生開立時間                     |
| 03            | String   | 買方統一編號錯誤                     |
| 04            | String   | 捐贈碼錯誤                           |
| 05            | String   | 捐贈發票不得開立買方統一編號         |
| 06            | String   | 捐贈發票不得索取                     |
| 07            | String   | 金額錯誤 (與產品價格對不起來)        |
| 08            | String   | 消費者資訊有缺                       |
| 09            | String   | 品項空白 或 產品數量為 0             |
| 10            | String   | 不明原因問題                         |
| msg           | String   | 回傳處理結果                         |
| orderNo       | String   | 訂單編號                             |
| invoice       | String   | 發票號碼                             |
| invoicingDate | DateTime | 開立時間                             |

- [成功回傳:](https://guide.ecfit.cc/apiDoc/#success-examples-Invoice-Invoicing-0_0_0-0)
```json
HTTP/1.1 200 OK
{
    "status"         : "success",
    "code"           : "00",
    "msg"            : "開立成功",
    "orderNo"        : "EC20160101001",
    "invoice"        : "AB00000001",
    "invoicingDate"  : "2016-01-01 01:01:01"
}
```
- [失敗回傳:](https://guide.ecfit.cc/apiDoc/#success-examples-Invoice-Invoicing-0_0_0-1)
```
HTTP/1.1 200 OK
{
    "status"         : "fail",
    "code"           : "01",
    "msg"            : "訂單金額有誤"
}
```

# Invoice - 作廢發票

### POST
```html
https://{company}.ecfit.cc/api/invoiceCancel/:invoice
```

## Parameter
| Field   | Type   | Description                               |
| :------ | :----- | :---------------------------------------- |
| invoice | String | 發票號碼，ex : AB00000001Size range: `10` |

## Success 200
| Field      | Type     | Description                          |
| :--------- | :------- | :----------------------------------- |
| status     | String   | 開立結果 success : 成功，fail : 失敗 |
| code       | String   | 結果代號                             |
| 00         | String   | 作廢成功                             |
| 01         | String   | 發票不存在                           |
| 02         | String   | 發票尚未開立完成                     |
| 03         | String   | 此發票已被作廢                       |
| 04         | String   | 已過允許作廢期間                     |
| msg        | String   | 回傳處理結果                         |
| invoice    | String   | 發票號碼                             |
| cancelDate | DateTime | 作廢時間                             |

- [成功回傳:](https://guide.ecfit.cc/apiDoc/#success-examples-Invoice-Invoice_Cancel-0_0_0-0)
```json
HTTP/1.1 200 OK
{
    "status"         : "success",
    "code"           : "00",
    "msg"            : "作廢成功",
    "invoice"        : "AB00000001",
    "cancelDate"     : "2016-01-01 01:01:01"
}
```
- [失敗回傳:](https://guide.ecfit.cc/apiDoc/#success-examples-Invoice-Invoice_Cancel-0_0_0-1)
```
HTTP/1.1 200 OK
{
    "status"         : "fail",
    "code"           : "01",
    "msg"            : "發票不存在"
}
```


# Invoice - 取得發票內容

利用提供的 發票號碼 :invoice 取得發票資訊，包含開立時的商品資料與折讓紀錄

### GET
```html
https://{company}.ecfit.cc/api/invoice/:invoice
```

## Parameter
| Field   | Type   | Description                               |
| :------ | :----- | :---------------------------------------- |
| invoice | String | 發票號碼，ex : AB00000001Size range: `10` |

## Success 200
| Field         | Type     | Description                                                  |
| :------------ | :------- | :----------------------------------------------------------- |
| status        | String   | 發票開立結果：0. 檢查發票內容中1. 等待確認上傳中2. 加值中心正上傳至財政部3. 等待財政部回應開立資訊4. 發票開立成功5. 開立錯誤7. 發票已註銷8. 發票已作廢9. 加值中心處理中 |
| code          | String   | 結果代號                                                     |
| 00            | String   | 查詢成功                                                     |
| 01            | String   | 發票號碼為空                                                 |
| 02            | String   | 發票不存在                                                   |
| msg           | String   | 回傳處理結果                                                 |
| orderNo       | String   | 訂單編號                                                     |
| amount        | String   | 訂單金額                                                     |
| remain        | String   | 有效金額                                                     |
| invoice       | String   | 發票號碼                                                     |
| randomNum     | String   | 隨機碼                                                       |
| buyerBan      | String   | 買家統編                                                     |
| paidDate      | Date     | 付款日期                                                     |
| creditNo      | Integer  | 信用卡末 4 碼（使用非信用卡消費時可以留空）                  |
| invoicingDate | DateTime | 開立時間                                                     |
| cancel        | String   | 是否作廢? (1 : 已作廢)                                       |
| cancelDate    | DateTime | 作廢日期 (若無作廢沒有值)                                    |
| NPO           | String   | 捐贈碼                                                       |
| demand        | Integer  | 是否有索取紙本發票                                           |
| carrierType   | String   | 使用載具 cellphone : 手機載具, citizen : 自然人憑證 (若不使用載具此欄為空)Allowed values: `cellphone`, `citizen` |
| carrierId     | String   | 載具號碼                                                     |
| url           | String   | 發票明細連結                                                 |
| production    | Array[]  | 購買商品陣列                                                 |
| pid           | String   | 商品品號                                                     |
| barcode       | String   | 商品條碼                                                     |
| name          | String   | 名稱                                                         |
| quantity      | Integer  | 數量                                                         |
| price         | Integer  | 單價                                                         |
| customer      | Object   | 消費者資料                                                   |
| name          | String   | 名字                                                         |
| postal        | String   | 郵遞區號                                                     |
| address       | String   | 地址                                                         |
| email         | String   | 信箱                                                         |
| phone         | String   | 電話                                                         |
| allowacne     | Array[]  | 折讓紀錄 (若沒有折讓則為空)                                  |
| allowacneNo   | String   | 折讓單號                                                     |
| allowanceDate | DateTime | 折讓日期                                                     |
| cancel        | String   | 是否作廢? (1 : 已作廢)                                       |
| cancelDate    | DateTime | 折讓作廢日期 (若無作廢沒有值)                                |
| reason        | String   | 折讓作廢原因 (若無作廢沒有值)                                |
| amount        | String   | 折讓金額                                                     |
| production    | Array[]  | 折讓商品陣列                                                 |
| id            | String   | 商品 ID                                                      |
| name          | String   | 名稱                                                         |
| quantity      | Integer  | 數量                                                         |
| price         | Integer  | 單價                                                         |

- [成功回傳:](https://guide.ecfit.cc/apiDoc/#success-examples-Invoice-Get_Invoice-0_0_0-0)
```json
HTTP/1.1 200 OK
{
    "status"        : "發票開立成功",
    "code"          : "00",
    "msg"           : "查詢成功",
    "orderNo"       : "EC20160101001",
    "amount"        : 5040,
    "remain"        : 3360,
    "invoice"       : "AB00000001",
    "randomNum"     : "0000",
    "buyerBan"      : "",
    "paidDate"      : "2016-01-01",
    "creditNo"      : "1234",
    "invoicingDate" : "2016-01-01 01:01:01",
    "NPO"           : "",
    "demand"        : 0,
    "carrierType"   : "cellphone",
    "carrierId"     : "/425WP5Q",
    "production"    : [{
        "pid"       : "0104030143",
        "barcode"   : "0104030143",
        "name"      : "【Fitty】運動壓力褲／壓縮褲（女款・七分全黑）【M】",
        "quantity"  : 1,
        "price"     : 1680
    },
    {
        "pid"       : "0204030255",
        "barcode"   : "0204030255",
        "name"      : "【Fitty】運動壓力褲／壓縮褲（邊彩七分款）﹣舞蝶粉【舞蝶粉 M】",
        "quantity"  : 1,
        "price"     : 1680
    }],
    "customer"      : {
        "name"      : "林先生",
        "postal"    : "105",
        "address"   : "台北市松山區",
        "email"     : "abcde@mail.com",
        "phone"     : "0937000000"
    },
    "allowacne"        : [{
        "allowacneNo"  : "AW0000000000001",
        "allowanceDate": "2016-01-02 01:01:01",
        "cancel"       : 0,
        "cancelDate"   : "0000-00-00 00:00:00",
        "reason"       : "",
        "amount"       : 1680,
        "production"   : [{
            "id"       : "0104030143",
            "name"     : "【Fitty】運動壓力褲／壓縮褲（女款・七分全黑）【M】",
            "quantity" : 1,
            "price"    : 1680
        }]
    }]
}
```
- [失敗回傳:](https://guide.ecfit.cc/apiDoc/#success-examples-Invoice-Get_Invoice-0_0_0-1)
```
HTTP/1.1 200 OK
{
    "status" : "fail",
    "code"   : "01",
    "msg"    : "發票號碼為空"
}
```


# Invoice - 取得發票內容(依訂單編號)

利用提供的 訂單編號 :order 取得所有發票資訊，包含開立時的商品資料與折讓紀錄

### GET
```html
https://{company}.ecfit.cc/api/invoiceByOrder/:order
```

## Parameter
| Field | Type   | Description                               |
| :---- | :----- | :---------------------------------------- |
| order | String | 訂單編號，ex : AB00000001Size range: `10` |

## Success 200
| Field         | Type     | Description                                                  |
| :------------ | :------- | :----------------------------------------------------------- |
| status        | String   | 開立結果 success : 成功，fail : 失敗                         |
| code          | String   | 結果代號                                                     |
| 00            | String   | 查詢成功                                                     |
| 02            | String   | 發票不存在                                                   |
| 03            | String   | 訂單編號為空                                                 |
| msg           | String   | 回傳處理結果                                                 |
| invoiceArr    | Array[]  | 所有發票資料                                                 |
| orderNo       | String   | 訂單編號                                                     |
| status        | String   | 開立結果：0. 檢查發票內容中1. 等待確認上傳中2. 加值中心正上傳至財政部3. 等待財政部回應開立資訊4. 發票開立成功5. 開立錯誤7. 發票已註銷8. 發票已作廢9. 加值中心處理中 |
| amount        | String   | 訂單金額                                                     |
| remain        | String   | 有效金額                                                     |
| invoice       | String   | 發票號碼                                                     |
| randomNum     | String   | 隨機碼                                                       |
| buyerBan      | String   | 買家統編                                                     |
| paidDate      | Date     | 付款日期                                                     |
| creditNo      | Integer  | 信用卡末 4 碼（使用非信用卡消費時可以留空）                  |
| invoicingDate | DateTime | 開立時間                                                     |
| cancel        | String   | 是否作廢? (1 : 已作廢)                                       |
| cancelDate    | DateTime | 作廢日期 (若無作廢沒有值)                                    |
| NPO           | String   | 捐贈碼                                                       |
| demand        | Integer  | 是否有索取紙本發票                                           |
| carrierType   | String   | 使用載具 cellphone : 手機載具, citizen : 自然人憑證 (若不使用載具此欄為空)Allowed values: `cellphone`, `citizen` |
| carrierId     | String   | 載具號碼                                                     |
| url           | String   | 發票明細連結                                                 |
| production    | Array[]  | 購買商品陣列                                                 |
| pid           | String   | 商品品號                                                     |
| barcode       | String   | 商品條碼                                                     |
| name          | String   | 名稱                                                         |
| quantity      | Integer  | 數量                                                         |
| price         | Integer  | 單價                                                         |
| customer      | Object   | 消費者資料                                                   |
| name          | String   | 名字                                                         |
| postal        | String   | 郵遞區號                                                     |
| address       | String   | 地址                                                         |
| email         | String   | 信箱                                                         |
| phone         | String   | 電話                                                         |
| allowacne     | Array[]  | 折讓紀錄 (若沒有折讓則為空)                                  |
| allowacneNo   | String   | 折讓單號                                                     |
| allowanceDate | DateTime | 折讓日期                                                     |
| cancel        | String   | 是否作廢? (1 : 已作廢)                                       |
| cancelDate    | DateTime | 折讓作廢日期 (若無作廢沒有值)                                |
| reason        | String   | 折讓作廢原因 (若無作廢沒有值)                                |
| amount        | String   | 折讓金額                                                     |
| production    | Array[]  | 折讓商品陣列                                                 |
| id            | String   | 商品 ID                                                      |
| name          | String   | 名稱                                                         |
| quantity      | Integer  | 數量                                                         |
| price         | Integer  | 單價                                                         |

- [成功回傳:](https://guide.ecfit.cc/apiDoc/#success-examples-Invoice-Get_InvoiceByorderNo-0_0_0-0)
```json
HTTP/1.1 200 OK
{
    "status"            : "success",
    "code"              : "00",
    "msg"               : "查詢成功",
    "invoiceArr"        : [{
        "orderNo"       : "EC20160101001",
        "status"        : "發票開立成功",
        "amount"        : 5040,
        "remain"        : 3360,
        "invoice"       : "AB00000001",
        "randomNum"     : "0000",
        "buyerBan"      : "",
        "paidDate"      : "2016-01-01",
        "invoicingDate" : "2016-01-01 01:01:01",
        "NPO"           : "",
        "demand"        : "0",
        "creditNo"      : "",
        "carrierType"   : "cellphone",
        "carrierId"     : "/425WP5Q",
        "production"    : [{
            "pid"       : "0104030143",
            "barcode"   : "0104030143",
            "name"      : "【Fitty】運動壓力褲／壓縮褲（女款・七分全黑）【M】",
            "quantity"  : 1,
            "price"     : 1680
        }],
        "customer"      : {
            "name"      : "林先生",
            "postal"    : "105",
            "address"   : "台北市松山區",
            "email"     : "abcde@mail.com",
            "phone"     : "0937000000"
        },
        "allowacne"        : [{
            "allowacneNo"  : "AW0000000000001",
            "allowanceDate": "2016-01-02 01:01:01",
            "cancel"       : 0,
            "cancelDate"   : "0000-00-00 00:00:00",
            "reason"       : "",
            "amount"       : 1680,
            "production"   : [{
                "id"       : "0104030143",
                "name"     : "【Fitty】運動壓力褲／壓縮褲（女款・七分全黑）【M】",
                "quantity" : 1,
                "price"    : 1680
            }]
        }]
    }]
}
```
- [失敗回傳:](https://guide.ecfit.cc/apiDoc/#success-examples-Invoice-Get_InvoiceByorderNo-0_0_0-1)
```
HTTP/1.1 200 OK
{
    "status" : "fail",
    "code"   : "03",
    "msg"    : "訂單編號為空"
}
```


# Invoice - 取得發票內容(多筆)

提供 多筆訂單編號 或 多筆發票號碼 查詢發票資訊

### POST
```html
https://{company}.ecfit.cc/api/postInvoice
```

## Parameter

| Field       | Type  | Description |
| :---------- | :---- | :---------- |
| orderNo[]   | Array | 訂單編號    |
| invoiceNo[] | Array | 發票號碼    |

- [Request-Example:](https://guide.ecfit.cc/apiDoc/#parameter-examples-Invoice-Invoice__multi_-0_0_0-0)

```array
{
    "orderNo":[
    "EC2008010100001",
    "EC2009010100001",
    "EC2010010100001"
 ],
    "invoiceNo":[
   "AB00000002",
   "AB00000003",
   "AB00000005"
  ]
}
```

## Success 200

| Field         | Type    | Description                                                  |
| :------------ | :------ | :----------------------------------------------------------- |
| status        | String  | 開立結果 success : 成功，fail : 失敗                         |
| code          | String  | 結果代號                                                     |
| 00            | String  | 查詢成功                                                     |
| 01            | String  | 發票不存在                                                   |
| msg           | String  | 回傳處理結果                                                 |
| orderNo       | Array[] | 依訂單編號查詢結果                                           |
| orderNo       | String  | 訂單編號                                                     |
| invoice       | String  | 發票號碼                                                     |
| invoicingDate | Date    | 發票開立日期                                                 |
| status        | String  | 發票開立結果：0. 檢查發票內容中1. 等待確認上傳中2. 加值中心正上傳至財政部3. 等待財政部回應開立資訊4. 發票開立成功5. 開立錯誤7. 發票已註銷8. 發票已作廢9. 加值中心處理中 |
| amount        | Integer | 發票開立金額                                                 |
| remain        | Integer | 發票有效金額                                                 |
| invoiceNo     | Array[] | 依發票號碼查詢結果                                           |
| orderNo       | String  | 訂單編號                                                     |
| invoice       | String  | 發票號碼                                                     |
| invoicingDate | Date    | 發票開立日期                                                 |
| status        | String  | 發票開立結果                                                 |
| amount        | Integer | 發票開立金額                                                 |
| remain        | Integer | 發票有效金額                                                 |

- [成功回傳:](https://guide.ecfit.cc/apiDoc/#success-examples-Invoice-Invoice__multi_-0_0_0-0)
```json
HTTP/1.1 200 OK
{
    "orderNo": {
        "EC20080101001": [
            {
                "orderNo": "EC20080101001",
                "invoice": "",
                "invoicingDate": null,
                "status": "開立錯誤",
                "amount": "1680",
                "remain": "1680"
            }
        ],
        "EC20090101001": [
            {
                "orderNo": "EC20090101001",
                "invoice": "AB00000001",
                "invoicingDate": "2016-01-01 01:01:01",
                "status": "發票開立成功",
                "amount": "1680",
                "remain": "1680"
            }
        ],
        "EC20100101001": [
            {
                "orderNo": "EC20100101001",
                "invoice": "BC00000002",
                "invoicingDate": "2016-01-01 01:01:01",
                "status": "發票開立成功",
                "amount": "1680",
                "remain": "1680"
            }
        ]
    },
    "invoiceNo": {
       "AB00000002": [
            {
                "orderNo": "EC20100101002",
                "invoice": "AB00000002",
                "invoicingDate": "2017-06-20 15:26:55",
                "status": "發票開立成功",
                "amount": "1026",
                "remain": "1026"
            }
        ],
        "AB00000003": [
            {
                "orderNo": "EC20100101003",
                "invoice": "AB00000003",
                "invoicingDate": "2017-06-16 11:21:24",
                "status": "發票開立成功",
                "amount": "1026",
                "remain": "1026"
            }
        ],
        "AB00000005": [
            {
                "orderNo": "EC20100101006",
                "invoice": "AB00000005",
                "invoicingDate": "2017-06-16 11:21:22",
                "status": "發票開立成功",
                "amount": "1680",
                "remain": "1680"
            }
        ]
    },
    "status": "success",
    "code": "00",
    "msg": "查詢成功"
}
```
- [失敗回傳:](https://guide.ecfit.cc/apiDoc/#success-examples-Invoice-Invoice__multi_-0_0_0-1)
```
HTTP/1.1 200 OK
{
    "status": "fail",
    "code": "01",
    "msg": "發票號碼為空"
}
```


# Invoice - 開立發票 - 測試用

與開立發票傳遞的參數完全相同，但並不會真正開立發票，只有做傳遞參數的格式以及內容檢查，並固定回傳假的發票號嗎 (TE00000000)

### POST
```html
https://{company}.ecfit.cc/api/invoice/test
```

## Parameter

| Field       | Type    | Description                                                  |
| :---------- | :------ | :----------------------------------------------------------- |
| orderNo     | String  | 訂單編號Size range: `16`                                     |
| amount      | Integer | 訂單金額                                                     |
| paidDate    | String  | 付款日期 ex: 2016-01-01Size range: `10`                      |
| NPO         | String  | 捐贈給社福單位的愛心碼 (不捐贈可以留空)                      |
| buyerBan    | String  | 買方統編 (沒有時可以留空)Size range: `8`                     |
| demand      | Number  | 是否索取發票Allowed values: `0`, `1`                         |
| carrierType | String  | 使用載具 cellphone : 手機載具, citizen : 自然人憑證 (若不使用載具此欄可以不填)Allowed values: `cellphone`, `citizen` |
| carrierId   | String  | 載具號碼                                                     |
| files       | string  | 是否夾帶檔案，0：否、1：是Allowed values: `0`, `1`           |
| production  | Array[] | 購買商品陣列                                                 |
| barcode     | String  | 商品條碼                                                     |
| name        | String  | 名稱                                                         |
| quantity    | Integer | 數量                                                         |
| price       | Integer | 單價                                                         |
| customer    | Object  | 消費者資料 (姓名、地址、信箱為必填，用以發票與折讓單的寄送及開立) |
| name        | String  | 名字                                                         |
| address     | String  | 地址                                                         |
| email       | String  | 信箱                                                         |
| phone       | String  | 電話                                                         |

- [Request-Example:](https://guide.ecfit.cc/apiDoc/#parameter-examples-Invoice-Invoicing_Test-0_0_0-0)

```json
{
    "orderNo": "EC20160101001",
    "amount": 5040,
    "paidDate": "2016-01-01",
    "buyerBan": "12345678",
    "NPO": 876,
    "demand": 1,
    "carrierType": "cellphone",
    "carrierId": "/425WP5Q",
    "production": [
        {
            "barcode": "0104030143",
            "name": "【Fitty】運動壓力褲／壓縮褲（女款・七分全黑）【M】",
            "quantity": 1,
            "price": 1680
        },
        {
            "barcode": "0204030255",
            "name": "【Fitty】運動壓力褲／壓縮褲（邊彩七分款）﹣舞蝶粉【舞蝶粉 M】",
            "quantity": 2,
            "price": 1680
        }
    ],
    "customer": {
        "name": "林先生",
        "address": "台北市松山區",
        "email": "abcde@mail.com",
        "phone": "0937000000"
    }
}
```

## Success 200
| Field         | Type     | Description                          |
| :------------ | :------- | :----------------------------------- |
| status        | String   | 開立結果 success : 成功，fail : 失敗 |
| code          | String   | 結果代號                             |
| 00            | String   | 開立成功                             |
| 01            | String   | 訂單編號為空                         |
| 02            | String   | 無法產生開立時間                     |
| 03            | String   | 買方統一編號錯誤                     |
| 04            | String   | 捐贈碼錯誤                           |
| 05            | String   | 捐贈發票不得開立買方統一編號         |
| 06            | String   | 捐贈發票不得索取                     |
| 07            | String   | 金額錯誤 (與產品價格對不起來)        |
| 08            | String   | 消費者資訊有缺                       |
| 09            | String   | 品項空白 或 產品數量為 0             |
| 10            | String   | 不明原因問題                         |
| msg           | String   | 回傳處理結果                         |
| orderNo       | String   | 訂單編號                             |
| invoice       | String   | 發票號碼                             |
| invoicingDate | DateTime | 開立時間                             |

- [成功回傳:](https://guide.ecfit.cc/apiDoc/#success-examples-Invoice-Invoicing_Test-0_0_0-0)
```json
HTTP/1.1 200 OK
{
    "status"         : "success",
    "code"           : "00",
    "msg"            : "開立成功",
    "orderNo"        : "EC20160101001",
    "invoice"        : "TE00000000",
    "invoicingDate"  : "2016-01-01 01:01:01"
}
```
- [失敗回傳:](https://guide.ecfit.cc/apiDoc/#success-examples-Invoice-Invoicing_Test-0_0_0-1)
```
HTTP/1.1 200 OK
{
    "status"         : "fail",
    "code"           : "01",
    "msg"            : "訂單金額有誤"
}
```


# Allowance

# Allowance - 折讓發票

### POST
```html
https://{company}.ecfit.cc/api/allowance
```

## Parameter
| Field      | Type    | Description                               |
| :--------- | :------ | :---------------------------------------- |
| invoice    | String  | 發票號碼，ex : AB00000001Size range: `10` |
| production | Array[] | 退貨項目                                  |
| name       | String  | 開立的商品名稱                            |
| quantity   | Integer | 數量 (需小於等於剩餘數量)                 |
| price      | Integer | 單價 (不一定要跟原本相同)                 |

- [Request-Example:](https://guide.ecfit.cc/apiDoc/#parameter-examples-Allowance-Allowance-0_0_0-0)

```json
{
    "invoice": "AB00000001",
    "production": [
        {
            "name": "【Fitty】運動壓力褲／壓縮褲（女款・七分全黑）【M】",
            "quantity": 1,
            "price": 1680
        }
    ]
}
```

## Success 200
| Field        | Type       | Description                          |
| :----------- | :--------- | :----------------------------------- |
| status       | String     | 開立結果 success : 成功，fail : 失敗 |
| code         | String     | 結果代號                             |
| 00           | String     | 等待折讓單確認                       |
| 01           | String     | 發票號碼為空                         |
| 02           | String     | 發票不存在                           |
| 03           | String     | 沒有退貨商品                         |
| 04           | String     | 退貨超過購買數量                     |
| 05           | String     | 退貨商品中包含無購買的商品           |
| 06           | String     | 退貨金額超過發票剩餘金額             |
| 07           | String     | 不明原因問題                         |
| msg          | String     | 回傳處理結果                         |
| allowanceSeq | String(16) | 折讓序號                             |

- [成功回傳:](https://guide.ecfit.cc/apiDoc/#success-examples-Allowance-Allowance-0_0_0-0)
```json
HTTP/1.1 200 OK
{
    "status"         : "success",
    "code"           : "00",
    "msg"            : "開立折讓成功",
    "allowanceSeq"   : "AB0000000100001001"
}
```
- [失敗回傳:](https://guide.ecfit.cc/apiDoc/#success-examples-Allowance-Allowance-0_0_0-1)
```
HTTP/1.1 200 OK
{
    "status" : "fail",
    "code"   : "01",
    "msg"    : "沒有發票號碼"
}
```


# Allowance - 折讓確認

### POST
```html
https://{company}.ecfit.cc/api/allowanceConfirm
```

## Parameter
| Field        | Type   | Description              |
| :----------- | :----- | :----------------------- |
| allowanceSeq | String | 折讓序號Size range: `18` |

- [Request-Example:](https://guide.ecfit.cc/apiDoc/#parameter-examples-Allowance-AllowanceConfirm-0_0_0-0)

```json
{
    "allowanceSeq": "AB0000000100001001"
}
```

## Success 200
| Field         | Type     | Description                          |
| :------------ | :------- | :----------------------------------- |
| status        | String   | 開立結果 success : 成功，fail : 失敗 |
| code          | String   | 結果代號                             |
| 00            | String   | 折讓單已確認                         |
| 01            | String   | 折讓序號為空                         |
| 02            | String   | 折讓序號不存在                       |
| 03            | String   | 該折讓序號未在等待確認的狀態         |
| 04            | String   | 不明原因問題                         |
| msg           | String   | 回傳處理結果                         |
| allowance     | String   | 折讓單號                             |
| allowanceDate | DateTime | 折讓確認時間                         |

- [成功回傳:](https://guide.ecfit.cc/apiDoc/#success-examples-Allowance-AllowanceConfirm-0_0_0-0)
```json
HTTP/1.1 200 OK
{
    "status"     : "success",
    "code"       : "00",
    "msg"        : "折讓單已確認",
    "allowance"  : "AW0000000000001",
    "allowanceDate" : "2016-01-01 01:01:01"
}
```
- [失敗回傳:](https://guide.ecfit.cc/apiDoc/#success-examples-Allowance-AllowanceConfirm-0_0_0-1)
```
HTTP/1.1 200 OK
{
    "status" : "fail",
    "code"   : "01",
    "msg"    : "折讓序號為空"
}
```


# Allowance - 折讓作廢

### POST
```html
https://{company}.ecfit.cc/api/allowanceCancel
```

## Parameter
| Field     | Type   | Description              |
| :-------- | :----- | :----------------------- |
| allowance | String | 折讓單號Size range: `16` |
| reason    | Text   | 取消原因                 |

- [Request-Example:](https://guide.ecfit.cc/apiDoc/#parameter-examples-Allowance-AllowanceCancel-0_0_0-0)

```json
{
    "allowance": "AW0000000000001",
    "reason": "消費者取消折讓"
}
```

## Success 200
| Field      | Type     | Description                          |
| :--------- | :------- | :----------------------------------- |
| status     | String   | 開立結果 success : 成功，fail : 失敗 |
| code       | String   | 結果代號                             |
| 00         | String   | 折讓作廢成功                         |
| 01         | String   | 折讓單號為空                         |
| 02         | String   | 折讓單號不存在                       |
| 03         | String   | 取消原因為空                         |
| 04         | String   | 該折讓單已作廢                       |
| 05         | String   | 不明原因問題                         |
| msg        | String   | 回傳處理結果                         |
| allowance  | String   | 折讓單號                             |
| cancelDate | DateTime | 折讓作廢時間                         |

- [成功回傳:](https://guide.ecfit.cc/apiDoc/#success-examples-Allowance-AllowanceCancel-0_0_0-0)
```json
HTTP/1.1 200 OK
{
    "status"     : "success",
    "code"       : "00",
    "msg"        : "作廢成功",
    "allowance"  : "AW0000000000001",
    "cancelDate" : "2016-01-01 01:01:01"
}
```
- [失敗回傳:](https://guide.ecfit.cc/apiDoc/#success-examples-Allowance-AllowanceCancel-0_0_0-1)
```
HTTP/1.1 200 OK
{
    "status" : "fail",
    "code"   : "01",
    "msg"    : "折讓單號為空或不存在"
}
```


# Stock

# Stock - 庫存查詢

此功能有存取頻率限制 ( 每分鐘 5 次 )，若超過將會回傳 429: Too Many Attempts.，除 Response 外，API 在標頭也會回傳 X-RateLimit-Limit、X-RateLimit-Remaining、Retry-After ( 如果到達限制次數就只能得到 Retry-After )

### GET
```html
https://{company}.ecfit.cc/api/stock/:barcode
```

## Header
| Field                 | Type    | Description                |
| :-------------------- | :------ | :------------------------- |
| X-RateLimit-Limit     | Integer | 指定時間內最大允許存取次數 |
| X-RateLimit-Remaining | Integer | 指定時間內剩餘存取次數     |
| Retry-After           | Integer | 距離下次重新請求的等待時間 |

## Parameter
| Field   | Type   | Description |
| :------ | :----- | :---------- |
| barcode | String | 產品條碼    |

## Success 200
| Field         | Type    | Description                          |
| :------------ | :------ | :----------------------------------- |
| status        | String  | 開立結果 success : 成功，fail : 失敗 |
| code          | String  | 結果代號                             |
| 00            | String  | 查詢成功                             |
| 01            | String  | 該條碼不存在                         |
| msg           | String  | 回傳處理結果                         |
| barcode       | String  | 條碼                                 |
| name          | String  | 名稱                                 |
| spec          | String  | 規格                                 |
| quantity      | Integer | 系統庫存                             |
| availQuantity | Integer | 可用庫存                             |

- [成功回傳:](https://guide.ecfit.cc/apiDoc/#success-examples-Stock-Stock-0_0_0-0)
```json
HTTP/1.1 200 OK
{
    "status"          : "success",
    "code"            : "00",
    "msg"             : "查詢成功",
    "barcode" 	      : "0206030028",
    "name"            : "【Fitty】運動壓力褲（秋冬九分・女款﹣經典全黑）2015 版",
    "spec"            : "M",
    "quantity"        : 500
    "availQuantity"   : 400
}
```
- [失敗回傳:](https://guide.ecfit.cc/apiDoc/#success-examples-Stock-Stock-0_0_0-1)
```
HTTP/1.1 200 OK
{
    "status" : "fail",
    "code"   : "01",
    "msg"    : "該條碼不存在"
}
```


# Stock - 庫存查詢 (多筆)

此功能有存取頻率限制 ( 每分鐘 5 次 )，若超過將會回傳 429: Too Many Attempts.，除 Response 外，API 在標頭也會回傳 X-RateLimit-Limit、X-RateLimit-Remaining、Retry-After ( 如果到達限制次數就只能得到 Retry-After )

### POST
```html
https://{company}.ecfit.cc/api/stock
```

## Header
| Field                 | Type    | Description                |
| :-------------------- | :------ | :------------------------- |
| X-RateLimit-Limit     | Integer | 指定時間內最大允許存取次數 |
| X-RateLimit-Remaining | Integer | 指定時間內剩餘存取次數     |
| Retry-After           | Integer | 距離下次重新請求的等待時間 |

## Parameter
| Field     | Type  | Description |
| :-------- | :---- | :---------- |
| barcode[] | Array | 產品條碼    |

- [Request-Example:](https://guide.ecfit.cc/apiDoc/#parameter-examples-Stock-Stock__multi_-0_0_0-0)

```array
["barcodeNotExist", "4718037231164", "4718037231163", ...]
```

## Success 200
| Field         | Type    | Description                          |
| :------------ | :------ | :----------------------------------- |
| status        | String  | 開立結果 success : 成功，fail : 失敗 |
| code          | String  | 結果代號                             |
| 00            | String  | 查詢成功                             |
| 02            | String  | 超過單次能查詢的數量上限 (100 筆)    |
| msg           | String  | 回傳處理結果                         |
| stock         | Object  | 庫存物件                             |
| barcode       | String  | 條碼                                 |
| name          | String  | 名稱                                 |
| spec          | String  | 規格                                 |
| quantity      | Integer | 系統庫存                             |
| availQuantity | Integer | 可用庫存                             |

- [成功回傳:](https://guide.ecfit.cc/apiDoc/#success-examples-Stock-Stock__multi_-0_0_0-0)
```json
HTTP/1.1 200 OK
{
    "status"     : "success",
    "code"       : "00",
    "msg"        : "查詢成功",
    "stock"      : {
        "barcodeNotExist" : {
            "status"    : false,
            "msg"       : "該條碼不存在",
            "barcode"   : "barcodeNotExist"
        },
        "4718037231164" : {
            "status"         : true,
            "barcode"        : "4718037231164",
            "name"           : "【Fitty】超顯瘦 PS 機能運動褲",
            "spec"           : "XL",
            "quantity"       : 100
            "availQuantity"  : 50
        },
        "4718037231163" : {
            "status"         : true,
            "barcode"        : "4718037231163",
            "name"           : "【Fitty】飄花微透感修身短袖運動上衣（輕柔粉）",
            "spec"           : "S",
            "quantity"       : 100
            "availQuantity"  : 100
        }
    }
}
```
- [失敗回傳:](https://guide.ecfit.cc/apiDoc/#success-examples-Stock-Stock__multi_-0_0_0-1)
```
HTTP/1.1 200 OK
{
    "status" : "fail",
    "code"   : "02",
    "msg"    : 超過單次能查詢的數量上限 (100 筆)
}
```