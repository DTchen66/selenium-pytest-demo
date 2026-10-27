# 第一次git push记录（2026-10-28）

## 用例
(pytest-env) PS D:\pytest> git remote add origin https://github.com/DTchen66/selenium-pytest-demo.git
(pytest-env) PS D:\pytest> git branch -M main
(pytest-env) PS D:\pytest> git push -u origin main

## 现象
已配置本机与GitHub账户的SSH链接，发现在push时依旧无法跳过登录

## 报错
弹出弹窗提示账户登录，取消后显示
fatal: User canceled device code authentication
error: cannot spawn d:\Users\Alan\AppData\Local\Programs\Microsoft VS Code\resources\app\extensions\git\dist\askpass.sh: No such file or directory
Username for 'https://github.com': 

## 初步判断
fatal: User canceled device code authentication	
Git Credential Manager（GCM）弹了 GitHub 设备码登录框，你没完成（关掉了/超时了），所以 OAuth 流程被取消。
SSH 是通的，但现在 remote 还是 HTTPS，HTTPS 这条链路上三个环节全崩了。

error: cannot spawn ...askpass.sh: No such file or directory
VS Code 自带了一个 askpass.sh 脚本用来弹窗填账号密码，但 Windows 下 Git 找不到它（路径是给 Linux/mac 用的 shell 脚本，PowerShell 里 spawn 不了）。这是 VS Code + Windows 的经典坑。

Username for 'https://github.com':
上面两个认证助手都失败了，Git 退回到“在终端里手动问你要用户名”。如果你直接在终端回车或者没输，就一直卡着。

## 主观原因
想使用SSH协议来提交远程仓库以避免后续提交时重复登陆，但在设置远程仓库时使用了HTTPS协议。

## 补充
git remote 命令用于用于管理 Git 仓库中的远程仓库。
git remote add <remote_name> <remote_url>：添加一个新的远程仓库。指定一个远程仓库的名称和 URL，将其添加到当前仓库中。
git remote rename <old_name> <new_name>：将已配置的远程仓库重命名
git remote remove <remote_name>：从当前仓库中删除指定的远程仓库。
git remote set-url <remote_name> <new_url>：修改指定远程仓库的 URL。
git remote：列出当前仓库中已配置的远程仓库。
git remote -v：列出当前仓库中已配置的远程仓库，并显示它们的 URL。

## 下一步
把git远程地址改成 SSH,重新提交。