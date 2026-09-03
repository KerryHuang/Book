---
kind: original
---

# Azure Blob Storage

將應用程式部署在雲端平台上，除非是自己開虛擬機器，不然要儲存檔案的話，應該都是要再另外使用雲端的檔案儲存服務，[Azure Blob Storage](https://azure.microsoft.com/zh-tw/services/storage/blobs/) 即是其中一個由微軟推出的雲端檔案儲存解決方案，這篇文章我就來簡單介紹一下如何用 C# 在 Azure Blob Storage 上對一個檔案做 CRUD。

**目錄**

\[Blob 檔案架構]\(#Blob 檔案架構) [建立儲存體帳戶](<Azure Blob Storage.md#建立儲存體帳戶>) [建立容器](<Azure Blob Storage.md#建立容器>) \[新增 Blob]\(#新增 Blob) \[讀取 Blob]\(#讀取 Blob) \[更新 Blob]\(#更新 Blob) \[刪除 Blob]\(#刪除 Blob)

Blob 檔案架構要使用 Azure Blob Storage 來儲存檔案，我們需要先了解「儲存體帳戶（Account）」、「容器（Container）」、「Blob」這三者的## 建立儲存體帳戶我們登入到 Azure 後台，點擊「所有服務」，搜尋「儲存體帳戶」就能找到。!\[1]\(/Users/kerry/Library/CloudStorage/OneDrive-個人/公司/Soetek/My Briefcase/My Books/Markdown Cheatsheet 中文版/Azure Blob Storage/1.png)

1. 訂用帳戶：用來付錢的帳戶資源群組：每一個我們建立的 Azure 服務都會隸屬一個資源群組，假設我們正在開發一個專案，我們就可以用專案名稱來為資源群組命名，方便我們來管理專案所使用到的 Azure 服務。儲存體帳戶名稱區域：Azure 資料中心的位置效能：「標準」選項可以符合大多數的使用情境，如果想要獲得更高的存取效能，我們可以選用「進階」。
2. 備援：備份資料的方式，依據選擇的區域跟效能的不同，會有不同的選項，大致上分為「本地」跟「異地」兩種類型，有一些選項要額外付費，有一些不用，通常本地備援是不用另外收錢，我們可以參考官方文件 - [Azure 儲存體冗余](https://docs.microsoft.com/zh-tw/azure/storage/common/storage-redundancy)，裡面有更詳細的說明。

完成基本設定之後，其他設定頁面的選項，我們暫時保持預設值，接著我們就按下「`檢閱＋建立`」將儲存體帳戶建立起來。

!\[]\(/Users/kerry/Library/CloudStorage/OneDrive-個人/公司/Soetek/My Briefcase/My Books/Markdown Cheatsheet 中文版/Azure Blob Storage/2.png)

然後，我們到建立好的儲存體帳戶底下，找到「`存取金鑰`」，按下「`顯示金鑰`」，我們可以看到有 2 組金鑰，隨便挑一組，將其「`連線字串`」複製下來，待會兒寫程式會用到。

!\[]\(/Users/kerry/Library/CloudStorage/OneDrive-個人/公司/Soetek/My Briefcase/My Books/Markdown Cheatsheet 中文版/Azure Blob Storage/3.png)

建立容器再回到儲存體帳戶底下，找到「`容器`」，在容器頁籤底下點擊「`＋容器`」來建立容器，我們有 2 個選項要填。!\[]\(/Users/kerry/Library/CloudStorage/OneDrive-個人/公司/Soetek/My Briefcase/My Books/Markdown Cheatsheet 中文版/Azure Blob Storage/4.png)名稱公用存取層級：用來決定哪些資源可以「匿名讀取」，有`私人`、`Blob`、`容器` 3 個選項。私人：Blob 及容器不允許被匿名讀取Blob：只有 Blob 可以被匿名讀取容器：Blob 及容器都可以被匿名讀取選項填完之後，我們就點擊「`建立`」將容器建起來。新增 Blob

到這邊我們要開始寫程式了，我們建立一個 ASP.NET Core MVC 應用程式來處理檔案的 CRUD，首先我們需要安裝 [Azure.Storage.Blobs](https://www.nuget.org/packages/Azure.Storage.Blobs) 套件。

!\[]\(/Users/kerry/Library/CloudStorage/OneDrive-個人/公司/Soetek/My Briefcase/My Books/Markdown Cheatsheet 中文版/Azure Blob Storage/5.png)

當有檔案上傳上來的時候，我們就利用剛剛複製的連線字串建立 Blob 服務的客戶端，進行檔案的儲存，程式碼如下，說明寫在註解中，為了方便，請容許我將 CURD 寫在同一個 Action 裡面。

```c#
[HttpPost]
public async Task<IActionResult> Upload(string blobName)
{
    var myFile = this.Request.Form.Files["myFile"];

    // 建立 Blob 服務客戶端
    var blobServiceClient = new BlobServiceClient(_blobStorageConnectionString);

    // 建立容器客戶端
    var myFilesContainer = blobServiceClient.GetBlobContainerClient("myfiles");

    // 建立 Blob 客戶端
    var myFileBlob = myFilesContainer.GetBlobClient($"{DateTime.Today:yyyyMMdd}/{myFile.FileName}");

    // 利用檔案名稱取得 ContentType
    if (!new FileExtensionContentTypeProvider().TryGetContentType(myFile.FileName, out var contentType))
    {
        contentType = "application/octet-stream";
    }

    // 上傳檔案到 Blob
    await myFileBlob.UploadAsync(
        myFile.OpenReadStream(),
        new BlobUploadOptions
        {
            HttpHeaders =
            new BlobHttpHeaders
            {
                ContentType = contentType
            }
        });

    // ...
    return View();
}
```

其中在「建立 Blob 客戶端」的時候，我們還可以為 Blob 增加階層目錄，這些階層目錄是邏輯性的，屬於 Blob 名稱的一部分，所以完整的 Blob 名稱是包含階層目錄的。

上傳完成之後，如果當初在建立容器時，公用存取層級不是選私人的話，每個 Blob 都有專屬的網址，透過這個專屬網址就可以瀏覽檔案，專屬網址的格式為「`https://{儲存體帳戶名稱}.blob.core.windows.net/{容器名稱}/{Blob 名稱}`」，在 Azure 後台也可以找得到。

!\[]\(/Users/kerry/Library/CloudStorage/OneDrive-個人/公司/Soetek/My Briefcase/My Books/Markdown Cheatsheet 中文版/Azure Blob Storage/6.png)

讀取 Blob如果我們容器的公用存取層級選的是私人的話，要讀取 Blob 就得帶上授權，或者由應用程式透過 Azure.Storage.Blobs 套件讀取 Blob 之後再傳到客戶端，下面的程式碼呈現的是後者的作法，說明在註解中。public async Task\<IActionResult> GetImage(){    // 建立 Blob 服務客戶端    var blobServiceClient = new BlobServiceClient(\_blobStorageConnectionString);    // 建立容器客戶端    var myFilesContainer = blobServiceClient.GetBlobContainerClient("myfiles");    // 建立 Blob 客戶端    var myFileBlob = myFilesContainer.GetBlobClient(\_blobName);    // 讀取 Blob 屬性    var myFilePropertiesResult = await myFileBlob.GetPropertiesAsync();    // 讀取 Blob 內容    var downloadStreamingResult = await myFileBlob.DownloadStreamingAsync();    return File(downloadStreamingResult.Value.Content, myFilePropertiesResult.Value.ContentType);}更新 Blob「`更新 Blob`」跟「新增 Blob」是一樣的，UploadAsync() 方法會自動幫我們覆寫 Blob。刪除 Blob最後是「`刪除 Blob`」，我建議使用 `DeleteIfExistsAsync()` 方法，如果單純使用 `DeleteAsync()` 方法的話，檔案不存在時，會有例外錯誤。public async Task\<IActionResult> DeleteImage(){    // 建立 Blob 服務客戶端    var blobServiceClient = new BlobServiceClient(\_blobStorageConnectionString);    // 建立容器客戶端    var myFilesContainer = blobServiceClient.GetBlobContainerClient("myfiles");    // 建立 Blob 客戶端    var myFileBlob = myFilesContainer.GetBlobClient(\_blobName);    // 如果 Blob 存在就刪除    \_ = await myFileBlob.DeleteIfExistsAsync();    return this.StatusCode(200);}Azure Blob Storage 對於一些靜態檔案不多的網站來說，算是一個物美價廉的解決方案，標準經常性存取的儲存體，每月每 GB 空間的費用是 $0.024 鎂，折合台幣大約是 NT$0.664，一般的小型網站，靜態檔案要佔用到 1 GB 的空間其實很難
