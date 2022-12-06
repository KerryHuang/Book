# 如何強制讓 DBeaver 在 Mac 上使用英文介面

## How to force DBeaver to use English as the interface language on macOS?

[開源](https://github.com/dbeaver/dbeaver)的 DB client — [DBeaver](https://dbeaver.io/) 在 Mac 上會直接使用系統語言設定來選擇介面語言，因此如果系統語言設定成繁體中文（台灣）的話，介面會變成 Chinese — 簡體中文 🤦 非常不直覺而且在 Settings 裡沒地方可以 override 掉這個設定。

![img](https://miro.medium.com/max/1400/1*YmUlRQwoLw4dwX-mx1uHTA.png)

誰知道某個英文術語會被翻譯成什麼平行宇宙的中文。

[唯一設定語言的方法，是用 command line 來啟動 DBeaver，並加上 ](https://github.com/dbeaver/dbeaver/issues/1423#issuecomment-285690209)`-nl en`[參數](https://github.com/dbeaver/dbeaver/issues/1423#issuecomment-285690209)：

```
/Applications/DBeaver.app/Contents/MacOS/dbeaver -nl en
```

但如果每次要用 DBeaver 都要從 command line 啟動很麻煩，如何才能從 GUI 啟動 DBeaver.app 都預設用英文呢？

後來找到的做法是去 patch `DBeaver.app`。

首先在 `DBeaver.app/Contents/MacOS` 底下新增一個叫 `dbeaver-en`(`DBeaver.app/Contents/MacOS/dbeaver-en`) 的檔案，加入以下內容：

新增檔案
```
touch dbeaver-en
```

```
#!/usr/bin/env bash"$(dirname "$0")/dbeaver" -nl en
```

然後執行 `chmod +x DBeaver.app/Contents/MacOS/dbeaver-en`。

再來，修改 `DBeaver.app/Contents/Info.plist`，把 `<key>CFBundleExecutable</key>` 底下的 `<string>dbeaver</string>` 改成 `<string>dbeaver-en</string>`。

最後，為了清掉系統對 `Info.plist` 的 cache，必須用 Finder 把 `DBeaver.app`從 `/Application` 搬到其他地方，再搬回來。

完成之後，從 Launcher 或其他地方打開 `DBeaver.app`，介面就會是英文的了。

![img](https://miro.medium.com/max/1400/1*VS9tNMA029k8mdiN5B_HmQ.png)

好！