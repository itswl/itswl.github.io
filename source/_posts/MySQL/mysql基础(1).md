
---
title: mysql基础(1)
date: 2019-01-14 21:57:47
tags:
categories: mysql学习
---



**windows安装过程参考之前的文章**
https://www.jianshu.com/p/e35185ec3294

## MySQL语法基础
### 创建表
![](https://upload-images.jianshu.io/upload_images/14597179-e5337691cb52df57.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![](https://upload-images.jianshu.io/upload_images/14597179-6f81961566f3b52a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
**-- 为注释，不会被执行**
![](https://upload-images.jianshu.io/upload_images/14597179-f5e3b6d515a3c27f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
#### 使用查询语句建表
```
-- 新建数据库
CREATE DATABASE`school`;

-- 使用数据库
USE `school`;

-- 创建表格
-- id
-- name
-- nickname
-- sex
-- in_time
CREATE TABLE `students`(
	`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	`name` VARCHAR(20) NOT NULL,
	`nickname` VARCHAR(20) NULL,
	`sex` CHAR(1) NULL,
	`in_time` DATETIME NULL
) DEFAULT CHARSET 'UTF8MB4';
-- PRIMARY KEY 主键是用来唯一定位记录的
-- 建议不使用任何业务相关的字段作为主键

-- 在students表中添加一个class id
ALTER TABLE `school`.`students`
ADD COLUMN `class id` int NULL AFTER `id`;
```
### 插入数据
![](https://upload-images.jianshu.io/upload_images/14597179-bcf9fc45ccef45c3.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
```
-- 插入students表   
-- now():mysql中当前时间
INSERT INTO `students` VALUE(1,'weilai','imwl','男',now());

-- 可以选择性插入
INSERT INTO `students`(`name`,`nickname`,`sex`,`in_time`) VALUES('weilai','imwl','男',now());

-- 插入多行数据
INSERT INTO `students`(`name`,`nickname`,`sex`,`in_time`) VALUES
('weilai2','imwl','男',now()),
('weilai','imwl','男',now()),
('weilai','imwl','男',now()),
('weilai','imwl','男',now());
```
### 查询数据
![得按照上面的先后顺序，不能颠倒](https://upload-images.jianshu.io/upload_images/14597179-53f0c41769e97f51.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
```
-- 查询数据库
-- * 表示所有的
SELECT * FROM `students`;
-- 只查询name 和 nickname
SELECT `name`,`nickname` FROM `students`;
-- 只查询name 和 nickname,同时性别为男的(查询表中不显示男)
SELECT `name`,`nickname` FROM `students` WHERE `sex`='男';
-- 在上面基础上id倒序
SELECT `id`,`name`,`nickname` FROM `students` WHERE `sex`='男'
ORDER BY `id` DESC;
-- 在上面基础上分页
-- 0，2  : 从第1条数据开始，显示2条
SELECT `id`,`name`,`nickname` FROM `students` WHERE `sex`='男'
ORDER BY `id` DESC LIMIT 0,2;
-- 1,2 : 从第2条数据开始，显示2条
SELECT `id`,`name`,`nickname` FROM `students` WHERE `sex`='男'
ORDER BY `id` DESC LIMIT 1,2;
```
### 修改数据
![](https://upload-images.jianshu.io/upload_images/14597179-55179cbdc79cdbb5.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
**where 很重要，不然就是改动整张表的数据**
```
-- 修改
-- 将所有的性别改女
UPDATE `students` SET `sex`='女';
-- 将name为weilai 的性别回男
UPDATE `students` SET `sex`='男' WHERE `name` = 'weilai';
-- 将name为weilai 的性别为男,nickname改为没有昵称
UPDATE `students` SET `sex`='男',`nickname`='没有昵称' WHERE `name` = 'weilai';
-- 将id <3 的性别改为女
UPDATE `students` SET `sex`='女' WHERE `id` < 3

```
### 删除数据
![](https://upload-images.jianshu.io/upload_images/14597179-bbe41919edbb6dee.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
 
```
-- 删除数据  
-- 删除students表中，性别为女的数据
DELETE FROM `students` WHERE `sex` = '女'
-- 删除students表中全部数据
DELETE FROM `students`
```
444
