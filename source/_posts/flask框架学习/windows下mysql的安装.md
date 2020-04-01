---
title: windows下mysql的安装
date: 2018-11-14 23:01:57
tags:
categories: flask
---



1. 先去官网下载点击的MySQL的下载：https://dev.mysql.com/downloads/mysql/

2. 下载完成后解压 

3. 配置系统环境变量

4. 复制解压后的mysql到C盘或者其他磁盘下

5. 系统的环境变量的path里添加一个mysql的配置 ，指向mysql的bin目录

6.  配置初始化的my.ini文件的文件
解压后的目录并没有的my.ini文件，没关系可以自行创建在安装根目录下添加的my.ini（新建文本文件，将文件类型改为的.ini），写入基本配置： 
```
[mysqld]
# 设置3306端口
port=3306
# 设置mysql的安装目录
basedir=C:\Program Files\MySQL
# 设置mysql数据库的数据的存放目录
datadir=C:\Program Files\MySQL\Data
# 允许最大连接数
max_connections=200
# 允许连接失败的次数。
max_connect_errors=10
# 服务端使用的字符集默认为UTF8
character-set-server=utf8
# 创建新表时将使用的默认存储引擎
default-storage-engine=INNODB
# 默认使用“mysql_native_password”插件认证
#mysql_native_password
default_authentication_plugin=mysql_native_password
[mysql]
# 设置mysql客户端默认字符集
default-character-set=utf8
[client]
# 设置mysql客户端连接服务端时默认使用的端口
port=3306
default-character-set=utf8
 ```
7. 安装服务
在安装时，尽量用管理员身份运行CMD，否则在安装时可能会报错，会导致安装失败的情况。进入CMD直接进入的mysql的目录。在MySQL的安装目录的仓目录下执行命令：

`mysqld --initialize --console`
![root@localhost: 0?qRk)L6AjyT 冒号后面为密码](https://upload-images.jianshu.io/upload_images/14597179-03673a273b1803c8.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


 

8.  安装服务`mysqld --install`,  启动MySQL的服务`net start mysql`

![安装并启动服务](https://upload-images.jianshu.io/upload_images/14597179-3d46a184c40a6b9f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


9. 改密