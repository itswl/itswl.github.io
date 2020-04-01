---
title: VPS搭建SSR过程
date: 2018-10-24 22:53:08
tags:
categories: VPS
---

首先我们得先有一个VPS。我用的vultr，已经用了快两年了吧，能用支付宝和微信支付，也挺便宜的，我选的3.5美元一月的。这是我的邀请地址https://www.vultr.com/?ref=7349334。点地址进去注册好像都有奖励啥!
的，不过从来没有人点我的邀请地址，我之前给别人介绍的时候也是直接让他们去官网上直接注册，感觉亏大了😄。

**这个billing是支付**
![可选支付宝和微信支付](https://upload-images.jianshu.io/upload_images/14597179-afcf9aeaf90f2eba.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
**首先可以先建一个VPS**

![VPS地址](https://upload-images.jianshu.io/upload_images/14597179-ee8c2c12ec38c41d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
先在网页中那个加**+**号，然后选择VPS所在地址，我自己选的Los,感觉应该日本新加坡的延迟会低一点吧0.0，但我现在用的挺好的，也没去换。就只是换了一个便宜的资费，以前并没有3.5刀一月的。

![价格与操作系统](https://upload-images.jianshu.io/upload_images/14597179-6144a6b944f010dc.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
我选的就是图中的，debian 9 然后3.5刀的，我需求较少，自用足够了了。

![左键可以复制IP地址和密码](https://upload-images.jianshu.io/upload_images/14597179-5b4710846183c3ce.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

然后通过SSH，登录到VPS上搭建ssr。我个人用的是**brook**,brook自带PAC模式，并且还很精准。
我ssh使用的是MobaXterm_Portable。下载地址https://mobaxterm.mobatek.net/download-home-edition.html。
以root的方式登录，然后输入密码，就会出现以下界面。
![root@vultr](https://upload-images.jianshu.io/upload_images/14597179-17039f753374123d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
**然后刷入SSR**
一键代码来自秋水逸冰的博客

把下面这三段代码分三次复制粘贴到putty或者终端并按回车运行：

第一段（此段较长，请全部复制粘贴到putty，然后按回车键运行，点击右键即可粘贴）

wget --no-check-certificate -O shadowsocks-all.sh https://raw.githubusercontent.com/teddysun/shadowsocks_install/master/shadowsocks-all.sh
\#从github上下载shadowsocks-all.sh
第二段**（同样复制粘贴然后运行）**

chmod +x shadowsocks-all.sh
\#给shadowsocks-all.sh 执行权限
第三段

./shadowsocks-all.sh 2>&1 | tee shadowsocks-all.log
\运行并记录

下面就是安装过程

![这有四个不同的版本](https://upload-images.jianshu.io/upload_images/14597179-b0df92b3ef5c8d6a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
我选的是2，shadowsocksR,后面的过程可以默认，一直点回车，也可以更改配置。最后安装成功后也会提示所安装的信息。也可以通过vi /etc/shadowsocks-r/config.json 修改配置
**提速**
现在自带bbr提速，所以不用更改。。
**一些常用相关命令**
修改SSR密码或者协议　vi /etc/shadowsocks-r/config.json（改了密码后需要重启SS）
SSR重启　/etc/init.d/shadowsocks-r restart
查看SSR状态   /etc/init.d/shadowsocks-r status
卸载SSR　./shadowsocks-all.sh uninstall

做到以上服务器端SSR就搭建完成了，然后就是配置客户端了。
**路由器**
有些路由器自带SSR，把配置信息填进去就可以用了。我用的裴讯K2P刷了一个openwrt固件，然后可用SSR。路由器好处是，手机电脑可以不用下载客户端，连上网就可以使用SSR带来的功能😊
![1.png](https://upload-images.jianshu.io/upload_images/14597179-a8921e33abe8bf03.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
**手机端**
ios可用shaodowrocket,potatso 2等，当然国区不行0.0
Android可用SSR，SSRR等https://github.com/shadowsocksrr/shadowsocksr-android/releases
电脑端可用SSR等
**Brook配置过程**
参考https://doub.io/brook-jc1/
使用一键脚本
系统要求：CentOS 6+ / Debian 6+ / Ubuntu 14.04 +
安装步骤
执行下面的代码下载并运行脚本。

wget -N --no-check-certificate https://raw.githubusercontent.com/ToyoDAdoubi/doubi/master/brook.sh && chmod +x brook.sh && bash brook.sh
运行脚本后会出现脚本操作菜单，选择并输入 1 就会开始安装。
进入下载脚本的目录并运行脚本：
```
./brook.sh
然后选择你要执行的选项即可。

 Brook 一键管理脚本 [vx.x.x]
 ---- Toyo | doub.io/brook-jc3 ----
 
 0. 升级脚本
————————————
 1. 安装 Brook
 2. 升级 Brook
 3. 卸载 Brook
————————————
 4. 启动 Brook
 5. 停止 Brook
 6. 重启 Brook
————————————
 7. 设置 账号配置
 8. 查看 账号信息
 9. 查看 日志信息
10. 查看 链接信息
————————————
 
 当前状态: 已安装 并 已启动
 
 请输入数字 [0-10]:
其他操作
启动：/etc/init.d/brook start

停止：/etc/init.d/brook stop

重启：/etc/init.d/brook restart

查看状态：/etc/init.d/brook status

安装目录：/usr/local/brook

配置文件：/usr/local/brook/brook.conf

日志文件：/usr/local/brook/brook.log
（注意正常情况下，日志是不会记录使用信息的，只会记录报错）
```
**brook客户端**
ios： app store 上目前还有，只是没怎么更新。
其他客户端：https://github.com/txthinking/brook/releases