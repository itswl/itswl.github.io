---
title: GitHub+Hexo搭建个人网站
date: 2018-11-07 00:03:32
tags:
categories: VPS
---
# 过程
1. **GitHub创建个人仓库**  
  格式**用户名**.github.io
2. **安装Git**
 https://git-scm.com/downloads
3. **安装Node.js** 
 https://nodejs.org/en/download/
4. **安装Hexo**
``npm install -g hexo-cli ``
`hexo init blog`
`hexo new test_my_site`
`hexo g`
`hexo s`
localhost:4000
5. **推送网站**
改站点配置文件
![repo：自己的github网址](https://upload-images.jianshu.io/upload_images/14597179-70886b235322471d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
然后
`hexo clean `
`hexo g `
`hexo d`
https://itswl.github.io
# 1.  GitHub创建个人仓库
https://github.com 点击GitHub中的New repository创建新仓库，仓库名应该为：
**用户名**.http://github.io
这个**用户名**使用你的GitHub帐号名称代替，这是固定写法。
# 2. 安装Git
Git下载地址：https://git-scm.com/downloads
选择对应版本安装即可
![右击会出现这个界面](https://upload-images.jianshu.io/upload_images/14597179-00f3f2b21f8574e1.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

Git Bash here，设置user.name和user.email配置信息：
`git config --global user.name "你的GitHub用户名"`
`git config --global user.email "你的GitHub注册邮箱"`

生成ssh密钥文件：
`ssh-keygen -t rsa -C "你的GitHub注册邮箱"`

然后直接三个回车即可，默认不需要设置密码
然后找到生成的.ssh的文件夹中的id_rsa.pub密钥，将内容全部复制

打开https//github.com/settings/keys 页面，新建new SSH Key

![new SSH Key](https://upload-images.jianshu.io/upload_images/14597179-3c9dbfa11b3932ed.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


Title为标题，任意填即可，将刚刚复制的id_rsa.pub内容粘贴进去，最后点击Add SSH key。

在Git Bash中检测GitHub公钥设置是否成功，输入 `ssh git@github.com` 
![](https://upload-images.jianshu.io/upload_images/14597179-85f173ebe40bee18.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)



如上则说明成功。这里之所以设置GitHub密钥原因是，通过非对称加密的公钥与私钥来完成加密，公钥放置在GitHub上，私钥放置在自己的电脑里。GitHub要求每次推送代码都是合法用户，所以每次推送都需要输入账号密码验证推送用户是否是合法用户，为了省去每次输入密码的步骤，采用了ssh，当你推送的时候，git就会匹配你的私钥跟GitHub上面的公钥是否是配对的，若是匹配就认为你是合法用户，则允许推送。这样可以保证每次的推送都是正确合法的。


# 3.  安装Node.js
Hexo基于Node.js，Node.js下载地址:https://nodejs.org/en/download/
选择对应版本安装。
安装Node.js会包含环境变量及npm的安装，安装后，检测Node.js是否安装成功，在命令行中输入:
`node -v `
检测npm是否安装成功，在命令行中输入
`npm -v` :

![node和npm](https://upload-images.jianshu.io/upload_images/14597179-98b43def7b13f4c9.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
到这了，安装Hexo的环境已经全部搭建完成。

# 4 安装hexo
新建一个博客文件夹，在博客文件夹中，Git bash here

使用npm命令安装Hexo，输入：
``npm install -g hexo-cli ``

这个安装时间较长耐心等待，安装完成后，初始化我们的博客，输入：
`hexo init blog`

为了检测我们的网站雏形，分别按顺序输入以下三条命令：
```
hexo new test_my_site:

hexo g

hexo s
```
完成后，打开浏览器输入地址：
>localhost:4000

可以看出我们写出第一篇博客。

## 常用的Hexo 命令
```
npm install hexo -g #安装Hexo
npm update hexo -g #升级 
hexo init #初始化博客

命令简写
hexo n "我的博客" == hexo new "我的博客" #新建文章
hexo g == hexo generate #生成
hexo s == hexo server #启动服务预览
hexo d == hexo deploy #部署

hexo server #Hexo会监视文件变动并自动更新，无须重启服务器
hexo server -s #静态模式
hexo server -p 5000 #更改端口
hexo server -i 192.168.1.1 #自定义 IP
hexo clean #清除缓存，若是网页正常情况下可以忽略这条命令
```
# 5. 推送网址
上面只是在本地预览，接下来要做的就是就是推送网站，也就是发布网站。
**在blog根目录里的_config.yml文件称为站点配置文件，如下图**

![站点配置文件](https://upload-images.jianshu.io/upload_images/14597179-cceae7be06445f95.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
**根目录里的themes文件夹，里面也有个_config.yml文件，这个称为主题配置文件，如下图**
![主题配置文件](https://upload-images.jianshu.io/upload_images/14597179-6e5f86669c01ab1a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

**下一步将我们的Hexo与GitHub关联起来，打开站点的配置文件_config.yml，翻到最后修改并保存：**

![repo：自己的github网址](https://upload-images.jianshu.io/upload_images/14597179-70886b235322471d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

其实就是给hexo d 这个命令做相应的配置，让hexo知道你要把blog部署在哪个位置，很显然，我们部署在我们GitHub的仓库里。最后安装Git部署插件，输入命令：

```
npm install hexo-deployer-git --save
```

这时，我们分别输入三条命令：

```
hexo clean 
hexo g 
hexo d
```

其实第三条的 hexo d 就是部署网站命令，d是deploy的缩写。完成后，打开浏览器，在地址栏输入你的放置个人网站的仓库路径:
https://itswl.github.io
博客已经上线了，可以在网络上被访问了。
 
