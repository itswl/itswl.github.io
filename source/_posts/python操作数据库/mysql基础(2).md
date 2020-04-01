
---
title: mysql基础(2)
date: 2019-01-14 21:57:47
tags:
categories: mysql学习
---

## 外键
在students表中，通过class id的字段，可以把数据与另一张表（class）关联起来，这种列称为外键。

**在students表中添加一个class id(id的后一列)**
```
ALTER TABLE `school`.`students`
ADD COLUMN `class id` int NULL AFTER `id`;
```
**在数据库school中建立一个班级表**
```
CREATE TABLE `students`(
    `class id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(20) NOT NULL,
) DEFAULT CHARSET 'UTF8';
```
**添加/删除 外键**
```
ALTER TABLE `students`
ADD CONSTRAINT `qe`
-- 外键约束名称，随意取值 
FOREIGN KEY (`class id`)
REFERENCES `class` (`id`);

-- ALTER TABLE `school`.`students` 
-- ADD FOREIGN KEY (`class id`) REFERENCES `school`.`class` (`id`);

-- 删除外键
ALTER TABLE `students`
DROP FOREIGN KEY `qe`;
删除外键约束并没有删除外键这一列。删除列是通过DROP COLUMN ...实现的
```

通过中间表，可以定义了一个“多对多”关系。

**一对一：**一个表的记录对应到另一个表的唯一一个记录

有一些应用会把一个大表拆成两个一对一的表，目的是把经常读取和不经常读取的字段分开，以获得更高的性能。例如，把一个大的用户表分拆为用户基本信息表user_info和用户详细信息表user_profiles，大部分时候，只需要查询user_info表，并不需要查询user_profiles表，这样就提高了查询速度

## 索引
在查找记录的时候，想要获得非常快的速度，就需要使用索引
```
ALTER TABLE `school`.`students` 
ADD INDEX `sex search`(`sex`);   
-- 名称为sex search，使用列 sex 的索引
-- 也可以多列
ALTER TABLE `school`.`students` 
ADD INDEX `search`(`sex`，`name`); 
```
索引的效率取决于索引列的值是否散列，例如sex列，大约一半的记录值是男，另一半是女，因此，对该列创建索引就没有意义。
```
ALTER TABLE `school`.`students` 
DROP INDEX `sex search`;
-- 删除索引
```

**假设name不重复，那么可以创建唯一索引
```
 ADD UNIQUE INDEX `search`(`name`) 
```
**没索引，但对is_vaild进行唯一约束
```
ALTER TABLE students
ADD CONSTRAINT uni_name UNIQUE (is_vaild);
```
**通过对数据库表创建索引，可以提高查询速度。**

**通过创建唯一索引，可以保证某一列的值具有唯一性。**

**数据库索引对于用户和应用程序来说都是透明的。**

## 查询补充
```
SELECT * FROM `students` WHERE  `id` >= 10 AND `sex` != '女'  GROUP BY `id`  HAVING `in_time` ORDER BY `id` DESC LIMIT 0,3;

SELECT  COUNT(*)  num FROM `students` WHERE NOT `id` >= 10 AND `sex` != '女'  ORDER BY `id` DESC LIMIT 0,8 ;

SELECT  AVG(id) num FROM `students` WHERE NOT `id` >= 10 AND `sex` != '女'  ORDER BY `id` DESC LIMIT 0,8 ;
```
![GROUP BY](https://upload-images.jianshu.io/upload_images/14597179-b7ad0cd7670e55c5.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![sql内置函数](https://upload-images.jianshu.io/upload_images/14597179-b4e8a4680f18d4e8.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
4
