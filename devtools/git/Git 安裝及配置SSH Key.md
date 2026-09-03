---
kind: original
---

# Git 安裝及配置SSH Key

# 檢查SSH keys

到使用者資料夾`C:\Users\<user>\`中看是否有`.ssh`資料夾（`<user>`為你的Windows用戶名稱，本範例為`john`），如果有的話點進去看是否有下表中任一SSH keys檔案。下表的第一欄為加密方式，第二欄為公鑰檔名，第三欄為私鑰檔名。若SSH keys已存在則跳過「產生SSH keys」的步驟。

| 加密算法                         | Public key       | Private key  |
| :------------------------------- | :--------------- | :----------- |
| ED25519 (preferred)              | `id_ed25519.pub` | `id_ed25519` |
| RSA (at least 2048-bit key size) | `id_rsa.pub`     | `id_rsa`     |
| DSA (deprecated)                 | `id_dsa.pub`     | `id_dsa`     |
| ECDSA                            | `id_ecdsa.pub`   | `id_ecdsa`   |

# 產生SSH keys

在Windows 10可使用[Git Bash](https://gitforwindows.org/)命令列產生SSH keys，預設會把產生的SSH keys存在`C:\Users\<user>\.ssh`目錄。下面示範產生RSA 2048位元的SSH keys的方式。

開啟Git Bash，輸入`ssh-keygen -t rsa -b 2048 -C <email>`，`<email>`輸入你的信箱。

```
$ ssh-keygen -t rsa -b 2048 -C john@abc.com
Generating public/private rsa key pair.
```

然後出現要把產生的SSH keys檔要存在哪裡的提問，直接按Enter鍵使用預設位置`/c/Users/<user>/.ssh/id_rsa`。

```
Enter file in which to save the key (/c/Users/john/.ssh/id_rsa):
```

然後會出現提示要輸入passphrase的訊息按Enter鍵跳過。

```
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
```

最後會提示把產生的SSH keys放到指定的位置。

```
Your identification has been saved in /c/Users/john/.ssh/id_rsa.
Your public key has been saved in /c/Users/john/.ssh/id_rsa.pub.
The key fingerprint is:
SHA256:7jyDUHfNi/kNFLRXutR/.... john@abc.com
The key's randomart image is:
+---[RSA 2048]---+
|           ..   |
|          ..  + |
|         o..+ . |
|   .. . . +o o .|
|   .o.S. + .o o |
|  .o .  o.o. . .|
|.  oo.+ ..0=    |
| +.  +=+=o  ++. |
|E. . oB*.oo.oo..|
+----[SHA256]----+
```

在C:\Users\用戶名\.ssh\資料夾中新建一個名稱為config的檔案，用記事本開啟
將下面內容複製貼上並保存, 最後一行記得換成你的id_rsa路徑

```
# Gitlab
Host gitlab.com
HostName gitlab.com
PreferredAuthentications publickey
AddKeysToAgent yes
IdentityFile C:\Users\用戶名\.ssh\id_rsa

# 設定檔參數
# Host : Host可以看作是一個你要識別的模式，對識別的模式，進行配置對應的主機名稱和ssh文件
# HostName : 要登入主機的主機名
# User : 登入名
# IdentityFile : 指明上面User對應的identityFile路徑
```

## **本地設定多個SSH Key**

建立 GitLab 的 SSH Key
```
ssh-keygen -t rsa -C 'yourEmail@xx.com' -f ~/.ssh/gitlab-rsa
```

建立 Github 的 SSH Key

```
ssh-keygen -t rsa -C 'yourEmail@xx.com' -f ~/.ssh/github-rsa
```

```
# Gitlab
Host gitlab.com
HostName gitlab.com
PreferredAuthentications publickey
IdentityFile ~/.ssh/gitlab-rsa

# Github
Host github.com
HostName github.com
PreferredAuthentications publickey
IdentityFile ~/.ssh/github-rsa

# 設定檔參數
# Host : Host可以看作是一個你要識別的模式，對識別的模式，進行配置對應的主機名稱和ssh文件
# HostName : 要登入主機的主機名
# User : 登入名
# IdentityFile : 指明上面User對應的identityFile路徑
```

# 複製public key到GitLab

到SSH keys預設的存放位置`C:\Users\<user>\.ssh`找到產生的SSH keys。用記事本或Notepad++開啟public key檔`id_rsa.pub`，內容為ssh-rsa後接一長串亂碼如下，按Ctrl + A複製全部內容。

```
ssh-rsa
AAAAAB3NzaC1yc....................................................................
..................................................................................
......................................................................7QEO9eOoMtPd
john@abc.com
```

登入GitLab網頁，點選右上方的使用者頭像，點選[Preferences]，在左側選單找到[SSH Keys]。在[Key]欄位貼上剛剛從`id_rsa.pub`中複製的內容，然後點Add key

# 使用SSH Clone專案

在GitLab專案的Clone按鈕複製[Clone with SSH]欄位的內容例如`git@gitlab.abc.com:demos/demo.git`，然後在Git Bash輸入
`git clone git@gitlab.abc.com:demos/demo.git`
即可把專案clone到命令執行的所在目錄。

```
$ git clone git@gitlab.abc.com:demos/demo.git
Cloning into 'demo'...
remote: Enumerating objects: ..., done.
...
Resolving deltas: 100% (...), done.
```

---

在 Mac 上使用可以按照以下步驟操作：

### **1. 生成 SSH Key**

如果你尚未生成 SSH Key，請按以下步驟操作：

#### **步驟**

1. **打開終端機**，執行以下命令生成新的 SSH Key：

   ```bash
   ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
   ```

   - `-t rsa`: 使用 RSA 演算法。
   - `-b 4096`: 生成 4096 位元的密鑰。
   - `-C "your_email@example.com"`: 填入你在 GitLab 使用的 Email。

2. **儲存路徑**：

   - 系統會提示你輸入儲存路徑，預設是 `~/.ssh/id_rsa`，直接按 Enter 即可。

3. **設定密碼短語（可選）**：

   - 如果不需要設定密碼短語，直接按 Enter 跳過。

4. **確認生成成功**：

   - 在終端機執行以下命令，確認密鑰已生成：

     ```bash
     ls ~/.ssh
     ```

     確認是否有`id_rsa`和`id_rsa.pub`這兩個檔案。
