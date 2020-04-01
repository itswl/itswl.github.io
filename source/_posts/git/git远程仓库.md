---
title: (3) git远程仓库
date: 2018-11-07 00:03:32
tags:
categories: git
---

Git是分布式版本控制系统，同一个Git仓库，可以分布到不同的机器上。一般找一台电脑充当服务器的角色，每天24小时开机，其他每个人都从这个“服务器”仓库克隆一份到自己的电脑上，并且各自把各自的提交推送到服务器仓库里，也从服务器仓库中拉取别人的提交。**也可使用github远程仓库**
Git仓库和GitHub仓库之间的传输是通过SSH加密的，需要一点设置：

**第1步：创建SSH Key。在用户主目录下，看看有没有.ssh目录，如果有，再看看这个目录下有没有id_rsa和id_rsa.pub这两个文件，如果已经有了，可直接跳到下一步。如果没有，打开Shell（Windows下打开Git Bash），创建SSH Key：**

```
$ ssh-keygen -t rsa -C "imwl@live.com"
```
把邮件地址换成自己的邮件地址，然后一路回车，使用默认值即可。

如果一切顺利的话，可以在用户主目录里找到.ssh目录，里面有id_rsa和id_rsa.pub两个文件，这两个就是SSH Key的秘钥对，id_rsa是私钥，不能泄露出去，id_rsa.pub是公钥，可以放心地告诉任何人。

**第2步：登陆GitHub，打开“Account settings”，“SSH Keys”页面：**

然后，点“Add SSH Key”，填上任意Title，在Key文本框里粘贴id_rsa.pub文件的内容：
![github-addkey-1](http://upload-images.jianshu.io/upload_images/14597179-10901f2c6cdb2f6a?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

点“Add Key”，你就应该看到已经添加的Key：

![github-addkey-2](http://upload-images.jianshu.io/upload_images/14597179-63e04ca796774279?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
