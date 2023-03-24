# ASP.NET Core SFTP (使用第三方套建 [SSH.Net](http://ssh.net/)) - 類別庫為案例

## 在 Visual Studio 安裝 [SSH.Net](http://ssh.net/)

新增 SshDotNet 類別庫
![img](https://i.imgur.com/wZNS9Ii.png)

在專案點右鍵 > 選「管理 NuGet」
![img](https://i.imgur.com/KNLlioD.png)

搜尋「SSH」> 點 [SSH.NET](http://ssh.net/) > 安裝
![img](https://i.imgur.com/ACuWr0k.png)

把 `class1` 刪除；
新增一個 class 名為 SshSftp，實作 SFTP 功能：

```c#
using Renci.SshNet;
using Renci.SshNet.Sftp;
using System;
using System.Collections;
using System.Collections.Generic;
using System.IO;
using System.Text.RegularExpressions;

namespace SshDotNet
{
    public class SshSftp
    {
        private SftpClient sftp;
        /// <summary>
        /// SFTP 連接狀態
        /// </summary>
        public bool Connected { get { return sftp.IsConnected; } }

        /// <summary>
        /// 建構子
        /// </summary>
        /// <param name="ip">IP</param>
        /// <param name="port">端口</param>
        /// <param name="user">id</param>
        /// <param name="pwd">passwd</param>
        public SshSftp(string ip, string port, string user, string pwd)
        {
            sftp = new SftpClient(ip, Int32.Parse(port), user, pwd);
        }

        /// <summary>
        /// SFTP 連線
        /// </summary>
        /// <returns>true成功</returns>
        public bool Connect()
        {
            try
            {
                if (!Connected)
                {
                    sftp.Connect();
                }
                return true;
            }
            catch (Exception ex)
            {
                throw ex;
            }
        }

        /// <summary>
        /// SFTP 關閉
        /// </summary> 
        public void Disconnect()
        {
            try
            {
                if (sftp != null && Connected)
                {
                    sftp.Disconnect();
                }
            }
            catch (Exception ex)
            {
                throw ex;
            }
        }

        /// <summary>
        /// SFTP 上傳檔案
        /// </summary>
        /// <param name="localPath">本機檔案 (要上傳的檔案)</param>
        /// <param name="uploadPath">要上傳到 FTP 的路徑</param>
        /// <param name="uploadFileName">指定新檔名 (若無，預設為原本的檔名)</param>
        public void Upload(string localFile, string uploadPath, string uploadFileName = "")
        {
            try
            {
                uploadPath = setFullFileName(uploadPath, uploadFileName, localFile);
                using (var file = File.OpenRead(localFile))
                {
                    Connect();
                    sftp.UploadFile(file, uploadPath);
                    Disconnect();
                }
            }
            catch (Exception ex)
            {
                throw ex;
            }
        }

        /// <summary>
        /// SFTP 搬移檔案
        /// </summary>
        /// <param name="moveFile">要搬移的檔案</param>
        /// <param name="newPath">要搬移到的新路徑</param>
        /// <param name="newFileName">指定新檔名 (若無，預設為原本的檔名)</param>
        /// <param name="isPosix">若新路徑已有相同檔案是否要覆蓋</param>
        public void Move(string moveFile, string newPath, string newFileName = "", bool isPosix = false)
        {
            try
            {
                newPath = setFullFileName(newPath, newFileName, moveFile);
                Connect();
                sftp.RenameFile(moveFile, newPath, isPosix);
                Disconnect();
            }
            catch (Exception ex)
            {
                throw ex;
            }
        }

        /// <summary>
        /// SFTP 下載檔案
        /// </summary>
        /// <param name="localPath">本機端路徑 (要下載到本機的路徑)</param>
        /// <param name="downloadFile">遠端路徑</param>
        /// <param name="localFileName">指定新檔名 (若無，預設為原本的檔名)</param>
        public void Download(string localPath, string downloadFile, string localFileName)
        {
            try
            {
                localPath = setFullFileName(localPath, localFileName, downloadFile);
                Connect();
                var byt = sftp.ReadAllBytes(downloadFile);
                Disconnect();
                File.WriteAllBytes(localPath, byt);
            }
            catch (Exception ex)
            {
                throw ex;
            }

        }

        /// <summary>
        /// SFTP 刪除檔案
        /// </summary>
        /// <param name="deleteFile">要刪除的檔案</param>
        public void Delete(string deleteFile)
        {
            try
            {
                Connect();
                sftp.Delete(deleteFile);
                Disconnect();
            }
            catch (Exception ex)
            {
                throw ex;
            }
        }

        /// <summary>
        /// 取得 SFTP 路徑上的檔案與文件夾
        /// </summary>
        /// <param name="sftpPath">遠端路徑</param>
        /// <param name="filenameExtension">附檔名</param>
        /// <returns></returns>
        public List<string> GetFileList(string sftpPath, string filenameExtension = "")
        {
            try
            {
                Connect();
                IEnumerable<SftpFile> files = sftp.ListDirectory(sftpPath);
                Disconnect();

                if (string.IsNullOrEmpty(filenameExtension))
                {
                    List<string> fileList = new List<string>();
                    foreach (var file in files)
                    {
                        string fileName = Path.GetFileName(file.FullName);
                        if(fileName == "." || fileName == "..")
                        {
                            continue;
                        }
                        fileList.Add(fileName);
                    }

                    return fileList;
                }
                else
                {
                    return matchFileName(filenameExtension, files);
                }
            }
            catch (Exception ex)
            {
                throw ex;
            }
        }

        /// <summary>
        /// 設定路徑與檔名
        /// </summary>
        /// <param name="path">路徑</param>
        /// <param name="fileName">檔名</param>
        /// <param name="sourceFullFileName">來源路徑與檔名</param>
        private string setFullFileName(string path, string fileName, string sourceFullFileName)
        {
            fileName = string.IsNullOrEmpty(fileName) ? Path.GetFileName(sourceFullFileName) : fileName;
            path += fileName;
            return path;
        }

        /// <summary>
        /// 配對檔名條件 (e.g. file_*.cs*)
        /// </summary>
        /// <param name="filenameExtension"></param>
        /// <param name="files"></param>
        private List<string> matchFileName(string filenameExtension, IEnumerable<SftpFile> files)
        {
            string[] splitFileNameArry = filenameExtension.Split('.');
            string filterFileName = "";
            string filterExtension = splitFileNameArry[splitFileNameArry.Length - 1];
            for (int i = 0; i < splitFileNameArry.Length - 1; i++)
            {
                filterFileName += splitFileNameArry[i] + ((splitFileNameArry.Length - 2 == i) ? "" : @"\.");
            }

            string fileNamePattern = "^" + filterFileName.Replace("*", ".*") + @"$";
            string extensionPattern = @"\." + filterExtension.Replace("*", ".*") + @"$";

            List<string> fileList = new List<string>();
            foreach (var file in files)
            {
                string fileName = Path.GetFileNameWithoutExtension(file.FullName);
                string extension = Path.GetExtension(file.FullName);
                bool isMatchFileName = Regex.IsMatch(fileName, fileNamePattern);
                bool isMatchExtension = Regex.IsMatch(extension, extensionPattern);
                if (isMatchFileName && isMatchExtension)
                {
                    fileList.Add(fileName + extension);
                }
            }

            return fileList;
        }
    }
}
```

建置成功後，就可以把這個類別庫的專案資料夾放進你想使用的 SFTP 的專案來使用它

## 使用 SFTP

把 SshSftp 資料夾 複製到 要使用的專案裡
![img](https://i.imgur.com/wujwRA7.png)

在專案點右鍵 > 加入 > 現有專案
![img](https://i.imgur.com/BjOt6zx.png)

將剛剛製過來的 SshDotNet 資料夾裡的 SshDotNet.csproj 開啟
![img](https://i.imgur.com/2zjYA4q.png)

在你要使用的專案加入參考
![img](https://i.imgur.com/G4YAMY3.png)

專案 > 方案 > 將 SshSftp 勾起來 > 確定
![img](https://i.imgur.com/fLZZZkj.png)

就可以使用 SFTP 了

```c#
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using SshDotNet;

namespace ConsoleSshSftp
{
    class Program
    {
        static void Main(string[] args)
        {
            string sftpIp = "127.0.0.1";
            string sftpProt = "21";
            string sftpAccount = "account";
            string sftpPassword = "password";

            string localFile = @"D:\your file*.txt";
            string uploadSftpPath = "/SFTP/Folder/";
            string uploadSftpNewName = "upload.txt";

            string sftpMoveFile = "/SFTP/Folder/upload.txt";
            string sftpMoveNewPath = "/SFTP/Folder/New Folder/";
            string sftpMoveNewFileName = "move.txt";

            string localPath = @"D:\";
            string sftpDownloadFile = "/SFTP/Folder/New Folder/move.txt";
            string sftpDownloadNewFileNme = "download.txt";

            string deleteFile = "/SFTP/Folder/New Folder/move.txt";

            try
            {
                SshSftp sftp = new SshSftp(sftpIp, sftpProt, sftpAccount, sftpPassword);

                sftp.Upload(localFile, uploadSftpPath, uploadSftpNewName);
                var fileList = sftp.GetFileList(uploadSftpPath, "*a.*f*d.cs*");

                sftp.Move(sftpMoveFile, sftpMoveNewPath, sftpMoveNewFileName, true);
                fileList = sftp.GetFileList(sftpMoveNewPath);
                fileList = sftp.GetFileList(uploadSftpPath);

                sftp.Download(localPath, sftpDownloadFile, sftpDownloadNewFileNme);

                sftp.Delete(deleteFile);
                fileList = sftp.GetFileList(sftpMoveNewPath);
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);
                Console.ReadKey();
            }
        }
    }
}
```

