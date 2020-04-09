---
title: mysql基础(3)
date: 2019-01-14 21:57:47
tags:
categories: mysql学习
---


### 多表联查
![多表联查](https://upload-images.jianshu.io/upload_images/14597179-1fa4f7a5a63d4bb1.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![投影查询 简写](https://upload-images.jianshu.io/upload_images/14597179-b63431d5c819503c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![加where](https://upload-images.jianshu.io/upload_images/14597179-d745bdc83fac0f8e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

**使用多表查询可以获取M x N行记录**（M,N为两个表各自的行数）
**多表查询的结果集可能非常巨大，要小心使用。**

### 内连接
```
mysql>   SELECT  s.id, s.name,`s`.`class id`, s.nickname,s.sex,c.name,s.in_time,s.is_vaild FROM students s INNER JOIN class c ON `s`.`class id` = c.id;
+----+---------+----------+-----------+------+--------------+---------------------+----------+
| id | name    | class id | nickname  | sex  | name         | in_time             | is_vaild |
+----+---------+----------+-----------+------+--------------+---------------------+----------+
|  7 | weilai  |      202 | imwl      | 男   | 二年二班     | 2018-12-27 22:05:41 |        1 |
|  8 | weilai  |      202 | imwl      | 男   | 二年二班     | 2018-12-27 22:05:41 |        2 |
|  9 | weilai  |      202 | imwl      | 男   | 二年二班     | 2018-12-27 22:05:41 |     NULL |
| 10 | weilai2 |      201 | imwl      | 男   | 二年一班     | 2018-12-27 22:05:41 |     NULL |
| 12 | name1   |      201 | nickname1 | 女   | 二年一班     | NULL                |     NULL |
| 13 | name2   |      201 | nickname2 | 男   | 二年一班     | NULL                |     NULL |
| 19 | 2       |      301 | i         | 男   | 三年一班     | 2019-02-27 12:02:04 |     NULL |
| 20 | 3       |      301 | m         | 女   | 三年一班     | 2019-02-27 12:02:04 |     NULL |
| 21 | 4       |      302 | w         | 男   | 三年二班     | 2019-02-27 12:02:04 |     NULL |
| 22 | 5       |      302 | l         | 男   | 三年二班     | 2019-02-27 12:02:04 |     NULL |
+----+---------+----------+-----------+------+--------------+---------------------+----------+

```
**INNER JOIN查询的写法是：**

先确定主表，仍然使用`FROM <表1>`的语法；
再确定需要连接的表，使用`INNER JOIN <表2>`的语法；
然后确定连接条件，使用`ON <条件...>`，这里的条件是`s.class id = c.id`，表示`students`表的`class id`列与`class`表的`id`列相同的行需要连接；
**可选：**加上`WHERE`子句、`ORDER BY`等子句。

### 小结
`JOIN`查询需要先确定主表，然后把另一个表的数据“附加”到结果集上；

`INNER JOIN`是最常用的一种`JOIN`查询，它的语法是`SELECT ... FROM <表1> INNER JOIN <表2> ON <条件...>；`

`JOIN`查询仍然可以使用`WHERE`条件和`ORDER BY`排序。
  ##  补充知识
假设查询语句是：

```
SELECT ... FROM tableA ??? JOIN tableB ON tableA.column1 = tableB.column2;

```

我们把tableA看作左表，把tableB看成右表，那么INNER JOIN是选出两张表都存在的记录：

![inner-join](http://upload-images.jianshu.io/upload_images/14597179-09046e20094fd1a3?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

LEFT OUTER JOIN是选出左表存在的记录：

![left-outer-join](http://upload-images.jianshu.io/upload_images/14597179-50bdf5c6968d8023?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

RIGHT OUTER JOIN是选出右表存在的记录：

![right-outer-join](http://upload-images.jianshu.io/upload_images/14597179-73c084a179aae278?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

FULL OUTER JOIN则是选出左右表都存在的记录：

![full-outer-join](http://upload-images.jianshu.io/upload_images/14597179-3720c7085052d139?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
