---
kind: reprint
source: https://sdwh.dev/posts/2020/06/VisualStudio-Git/
author: sdwh.dev
---

# Visual Studio 使用 Git 版本控制

------

1. 看圖說故事
   1. [View](https://sdwh.dev/posts/2020/06/VisualStudio-Git/#View)
   2. [Reset](https://sdwh.dev/posts/2020/06/VisualStudio-Git/#Reset)
   3. [Commit](https://sdwh.dev/posts/2020/06/VisualStudio-Git/#Commit)
   4. [Revert](https://sdwh.dev/posts/2020/06/VisualStudio-Git/#Revert)
   5. [Branch](https://sdwh.dev/posts/2020/06/VisualStudio-Git/#Branch)
   6. [Rebase](https://sdwh.dev/posts/2020/06/VisualStudio-Git/#Rebase)
   7. [Stash](https://sdwh.dev/posts/2020/06/VisualStudio-Git/#Stash)

------

在個人的實務開發情境中，一半是用 Visual Studio Code，另外一半則是用 Visual Studio，而 Visual Studio 已提供 GUI 介面來進行 git 的版本控制，為了讓專案的開發更流暢，熟悉 Visual Studio 的 Git GUI 有其必要。

[![logo](https://sdwh.dev/assets/DotNetIcon.png)](https://sdwh.dev/posts/2020/06/VisualStudio-Git/)

## 看圖說故事

### View

![檢視紀錄中可以對 Commit 操作的選單](https://sdwh.dev/assets/vs-git-menu.png)**檢視紀錄中可以對 Commit 操作的選單**

### Reset

![重設即為 Git Reset](https://sdwh.dev/assets/vs-git-before-reset.png)**重設即為 Git Reset**
![Reset 後原本的 Commit 在紀錄中會看不見](https://sdwh.dev/assets/vs-git-after-reset.png)**Reset 後原本的 Commit 在紀錄中會看不見**

### Commit

![暫存區的操作可以開啟命令提示字元](https://sdwh.dev/assets/vs-git-add.png)**暫存區的操作可以開啟命令提示字元**
![加入暫存區同時遞送](https://sdwh.dev/assets/vs-git-add-2.png)**加入暫存區同時遞送**

- 全部認可
- 全部認可並推送
- 全部認可並同步

![修改 Commit ，有助於 Commit不要過於混亂](https://sdwh.dev/assets/vs-git-ammend.png)**修改 Commit ，有助於 Commit不要過於混亂**

### Revert

![還原即為 Git Revert](https://sdwh.dev/assets/vs-git-revert.png)**還原即為 Git Revert**

### Branch

![新增分支的方式](https://sdwh.dev/assets/vs-git-new-branch.png)**新增分支的方式**
![右下角選單可以切換分支](https://sdwh.dev/assets/vs-git-branch-checkout.png)**右下角選單可以切換分支**

### Rebase

![檢視分支選單中可以做 Git Rebase](https://sdwh.dev/assets/vs-git-rebase.png)**檢視分支選單中可以做 Git Rebase**

### Stash

![隱藏即為 Git Stash](https://sdwh.dev/assets/vs-git-stash.png)**隱藏即為 Git Stash**
![Stash Pop 的數種方式](https://sdwh.dev/assets/vs-git-stashpop.png)**Stash Pop 的數種方式**

- 套用與快顯的差異