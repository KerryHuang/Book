## [使用 Visual Studio 2022 可透過 .editorconfig 鎖定文字檔案的儲存編碼格式](https://blog.miniasp.com/post/2024/06/07/Visual-Studio-2022-EditorConfig-UTF-8)分享

我們長久以來一直有一個蠻困擾的事情，就是 Visual Studio 2022 在存檔的時候，他不一定會將程式碼自動儲存成 UTF-8 編碼，若以 `Big5` 編碼來儲存文字檔案時，在其他程式讀取時就有可能出現異常。例如我們的程式碼都會需要 git push 到 Azure DevOps 的 Repos 中，若程式檔的編碼為 `Big5` 的時候，這些中文字在 Azure DevOps 上面都無法正常顯示，也就是我在 Code Review 時看到的都會是亂碼，真的是不勝其擾。這篇文章我就來告訴你怎樣解決！

![An abstract and conceptual wide banner image representing the idea of setting file encoding in Visual Studio 2022 using  editorconfig](https://blog.miniasp.com/image.axd?picture=/GitHub/d6377e13-a222-4ad7-9245-044fc4c179f9.webp)

因為我的 Windows 地區設定以 `Chinese (Traditional, Taiwan)` 為主，所以整個作業系統預設會以 `Big5` 編碼來讀寫文字檔案，讀取檔案時，如果沒有辦法自動判斷編碼，也會預設以 `Big5` 編碼開啟檔案。這算是歷史包袱了，因為在過去的 Windows 作業系統中，`Big5` 編碼是最常用的中文編碼，所以預設就是這樣設定的。解決方案也並不是沒有，所有檔案都改用 `UTF-8` 或 `UTF-8 with BOM` 來儲存即可，但事情往往沒有這麼簡單！


雖然我們可以直接從控制台的地區設定勾選 `Use Unicode UTF-8 for worldwide language support` 選項，將整台電腦預設全部都改用 `UTF-8` 編碼，但是相信我，你勾選下去後，一定會遇到更多問題的，因為真的太多檔案還是以 `Big5` 儲存了，你根本不太可能根除 `Big5` 的遺毒！

![SNAG-0361](https://github.com/doggy8088/i/assets/88981/7471bc8c-5cee-4f35-8814-2f15e1e3718d)

其實你只要在**專案**或**方案目錄**加入一個 `.editorconfig` 定義檔，明確的告訴他以下定義即可：

```ini
[*.{cs,csx,vb,vbx,txt,html,htm,css,js,json,yml,yaml,xml,config,ini,sh,ps1,psm1,psd1,ps1xml,psrc1xml,csproj,sln,gitignore,gitattributes,editorconfig,md,markdown,txt,asciidoc,adoc,asc,asciidoc,txt,ipynb,py}]
charset = utf-8-bom
```

這裡的 `charset = utf-8-bom` 設定是關鍵，設定好之後 Visual Studio 2022 也不用重開，只要存檔，所有 `*.cs`, `*.md`, `*.txt`, ... 以及我列出的所有**文字格式**的檔案，就會自動儲存成 `UTF-8 with BOM` 編碼，這樣日後就不會再有編碼問題了！🎉

這樣設定有以下注意事項：

1. 不要勾選控制台的地區設定的 `Use Unicode UTF-8 for worldwide language support` 選項。
2. 撰寫 `*.bat` 與 `*.cmd` 的時候，建議不要另存成 UTF-8 編碼，因為執行時可能會出現編碼錯誤。
3. 有想要的文字檔案類型時，請自行調整 `.editorconfig` 的設定，自己加入副檔名即可。
4. 用 Visual Studio 2022 開發 .NET 可以參考 Roslyn 專案的 [.editorconfig](https://github.com/dotnet/roslyn/blob/main/.editorconfig?raw=true) 檔案！👍
5. 這個方法可能也適用於「程式碼產生器」產生的檔案，我剛測試過 [EF Core Power Tools](https://github.com/ErikEJ/EFCorePowerTools) 在產生 *.cs 的時候，他會如實的遵照 `.editorconfig` 的設定來寫入檔案。至於其他的產生器會不會相同的設定，那就不一定了！

### 相關連結

- [EditorConfig 與分析器 - Visual Studio (Windows) | Microsoft Learn](https://learn.microsoft.com/zh-tw/visualstudio/code-quality/analyzers-faq?view=vs-2022&WT.mc_id=DT-MVP-4015686)