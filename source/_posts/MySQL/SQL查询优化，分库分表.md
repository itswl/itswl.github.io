
---
title: SQL查询优化，分库分表
date: 2020-03-18 21:57:47
tags:
categories: mysql学习
---

# 一、SQL查询优化（**`重要`**）

## 1.1 获取有性能问题SQL的三种方式

1.  通过用户反馈获取存在性能问题的SQL；
2.  通过慢查日志获取存在性能问题的SQL；
3.  实时获取存在性能问题的SQL；

### 1.1.2 慢查日志分析工具

**相关配置参数：**

```
slow_query_log # 启动停止记录慢查日志，慢查询日志默认是没有开启的可以在配置文件中开启(on)
slow_query_log_file # 指定慢查日志的存储路径及文件，日志存储和数据从存储应该分开存储

long_query_time # 指定记录慢查询日志SQL执行时间的阀值默认值为10秒通常,对于一个繁忙的系统来说,改为0.001秒(1毫秒)比较合适
log_queries_not_using_indexes #是否记录未使用索引的SQL

```

  **常用工具：**`mysqldumpslow`和`pt-query-digest`

```
pt-query-digest --explain h=127.0.0.1,u=root,p=p@ssWord  slow-mysql.log
```

## 1.1.3 实时获取有性能问题的SQL（**推荐**）

![image.png](https://upload-images.jianshu.io/upload_images/14597179-108def45b4274a2b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


```
SELECT id,user,host,DB,command,time,state,info
FROM information_schema.processlist
WHERE TIME>=60
```

  查询当前服务器执行超过`60s`的`SQL`，可以通过脚本周期性的来执行这条`SQL`，就能查出有问题的`SQL`。

## 1.2 SQL的解析预处理及生成执行计划（**`重要`**）

### 1.2.1 查询过程描述（**`重点！！！`**）

![image.png](https://upload-images.jianshu.io/upload_images/14597179-5dc87722917e561f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


[**上图原文连接**](https://processon.com/chart_image/5aab1fcbe4b0f68cc019053a.png?_=1521169284173)

#### 通过上图可以清晰的了解到MySql查询执行的大致过程：

1.  发送`SQL`语句。
2.  查询缓存，如果命中缓存直接返回结果。
3.  `SQL`解析，预处理，再由优化器生成对应的查询执行计划。
4.  执行查询，调用存储引擎API获取数据。
5.  返回结果。

### 1.2.2 查询缓存对性能的影响（**建议关闭缓存**）

**第一阶段：**
**相关配置参数：**

```
query_cache_type # 设置查询缓存是否可用
query_cache_size # 设置查询缓存的内存大小
query_cache_limit # 设置查询缓存可用的存储最大值（加上sql_no_cache可以提高效率）
query_cache_wlock_invalidate # 设置数据表被锁后是否返回缓存中的数据
query_cache_min_res_unit # 设置查询缓存分配的内存块的最小单
```

> **缓存查找是利用对大小写敏感的`哈希查找`来实现的**，Hash查找只能进行全值查找（sql完全一致），如果缓存命中，检查用户权限，如果权限允许，直接返回，查询不被解析，也不会生成查询计划。

#### **`在一个读写比较频繁的系统中，建议关闭缓存，因为缓存更新会加锁`**。将`query_cache_type`设置为`off`,`query_cache_size`设置为`0`。

### 1.2.3 **第二阶段：**MySQL依照执行计划和存储引擎进行交互

  **这个阶段包括了多个子过程：**

![](https://upload-images.jianshu.io/upload_images/14597179-bb44338f81085e38.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)



![](https://upload-images.jianshu.io/upload_images/14597179-2b8b416a6222bf5a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![](https://upload-images.jianshu.io/upload_images/14597179-fe5d84ef10a6fa4d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


#### **`一条查询可以有多种查询方式`**，查询优化器会对每一种查询方式的（存储引擎）统计信息进行比较，找到成本最低的查询方式，**`这也就是索引不能太多的原因`**。

## 1.3 会造成MySQL生成错误的执行计划的原因

1、统计信息不准确
2、成本估算与实际的执行计划成本不同

![](https://upload-images.jianshu.io/upload_images/14597179-75fdacdb25eccc88.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


3、给出的最优执行计划与估计的不同

![](https://upload-images.jianshu.io/upload_images/14597179-6ddff26864a8687f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


4、MySQL不考虑并发查询
5、会基于固定规则生成执行计划
6、MySQL不考虑不受其控制的成本，如存储过程，用户自定义函数

## 1.4 MySQL优化器可优化的SQL类型

> 查询优化器：对查询进行优化并查询mysql认为的成本最低的执行计划。 为了生成最优的执行计划，查询优化器会对一些查询进行改写

  可以优化的sql类型

  1、重新定义表的关联顺序；

![](https://upload-images.jianshu.io/upload_images/14597179-2d05194901f2f95e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


  2、将外连接转换为内连接；

  3、使用等价变换规则；

![](https://upload-images.jianshu.io/upload_images/14597179-e415cccfa34dd5f9.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


  4、优化count(),min(),max()；

![](https://upload-images.jianshu.io/upload_images/14597179-409bf29b8984f5b1.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


  5、将一个表达式转换为常数；
  6、子查询优化；

  ![](https://upload-images.jianshu.io/upload_images/14597179-2b8e7d1a457ebd7f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


  7、提前终止查询，如发现一个不成立条件(如`where id = -1`)，立即返回一个空结果；

  8、对in()条件进行优化；

## 1.5 查询处理各个阶段所需要的时间

### 1.5.1 使用profile(目前已经不推荐使用了)

```
set profiling = 1; #启动profile,这是一个session级的配制执行查询

show profiles; # 查询每一个查询所消耗的总时间的信息

show profiles for query N; # 查询的每个阶段所消耗的时间

```

### 1.5.2 performance_schema是5.5引入的一个性能分析引擎（5.5版本时期开销比较大）

启动监控和历史记录表：`use performance_schema`

```
update setup_instruments set enabled='YES',TIME = 'YES' WHERE NAME LIKE 'stage%';

update set_consumbers set enabled='YES',TIME = 'YES' WHERE NAME LIKE 'event%';

```

![](https://upload-images.jianshu.io/upload_images/14597179-5a68e6460cfd4b93.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![](https://upload-images.jianshu.io/upload_images/14597179-d85ebe9b118c2b02.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


## 1.6 特定SQL的查询优化

### 1.6.1 大表的数据修改

![](https://upload-images.jianshu.io/upload_images/14597179-7308bd9300d15310.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


![](https://upload-images.jianshu.io/upload_images/14597179-c3ffa1d09d4c9f9c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


### 1.6.2 大表的结构修改

![](https://upload-images.jianshu.io/upload_images/14597179-ba5584f9907539cd.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

1.  利用主从复制，先对从服务器进入修改，然后主从切换
2.  （推荐）

> 添加一个新表（修改后的结构），老表数据导入新表，老表建立触发器，修改数据同步到新表， 老表加一个排它锁（重命名）， 新表重命名， 删除老表。

![](https://upload-images.jianshu.io/upload_images/14597179-6ca18587e28be637.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


**修改语句这个样子：**

```
alter table sbtest4 modify c varchar(150) not null default ''

```

**利用工具修改：**

![](https://upload-images.jianshu.io/upload_images/14597179-7239a84cec0180b6.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


# ## 1.6.3 优化not in 和 <> 查询

  **子查询改写为关联查询：**

![](https://upload-images.jianshu.io/upload_images/14597179-5e4c1522cdb5a9d9.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


# 二、分库分表

## 2.1 分库分表的几种方式

> 分担读负载 可通过 一主多从，升级硬件来解决。

### 2.1.1 把一个实例中的多个数据库拆分到不同实例（集群）

![](https://upload-images.jianshu.io/upload_images/14597179-da7140ceb6ffa592.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


    **拆分简单,不允许跨库。但并不能减少写负载。**

### 2.1.2 把一个库中的表分离到不同的数据库中

![](https://upload-images.jianshu.io/upload_images/14597179-f3ff87b0f2ee2b0c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


    **该方式只能在一定时间内减少写压力。**

    以上两种方式只能暂时解决读写性能问题。

### 2.1.3 数据库分片

> 对一个库中的相关表进行水平拆分到不同实例的数据库中

![](https://upload-images.jianshu.io/upload_images/14597179-6ff65dacf21a21f5.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


#### 2.1.3.1 如何选择分区键

1.  分区键要能尽可能避免跨分区查询的发生
2.  分区键要尽可能使各个分区中的数据平均

#### 2.1.3.2 分片中如何生成全局唯一ID

![](https://upload-images.jianshu.io/upload_images/14597179-82271ac4944e9cf2.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


#### [**扩展：表的垂直拆分和水平拆分**](https://www.kancloud.cn/thinkphp/mysql-design-optimalize/39326)
