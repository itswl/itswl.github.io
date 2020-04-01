---
title: (2) python基本数据类型总结
date: 2018-11-14 21:58:19
tags:
categories: python基础
---

![python基本数据类型总结](https://upload-images.jianshu.io/upload_images/14597179-d367ffa3f9bbc505.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
**整数int与浮点数float**
整数运算永远是精确的，浮点数的运算可能会有四舍五入。
2/2结果为1.0
// 表示整除   2//2结果为1   
3//2也是1  并不是四舍五入，而是只保留整数部分
1.23x10^9和 12.3x10^8相等
1.23x10^9就是1.23e9，或者12.3e8，0.000012可以写成1.2e-5
**进制**
python中默认为10进制。
2进制用0b表示，例如0b10即为2。
8进制用0o表示，例如0o10即为8。
16进制用0x表示，例如0x10即为16。（8,9,a,b,c,d,e,f,0x10)
```
bin()  #转化为2进制
oct()  #转化为8进制
int()  #转化为10进制
hex()  #转化为16进制
```
**布尔值bool**
```
bool()
bool(0)
bool('')
bool([])
bool({})
bool(None)
```
只有bool(0)和bool()括号中为空才表示Fasle。bool(’0‘)等表示True

**序列**
字符串 str  可用单引号，双引号或者三引号表示例如'str' 或"str "或者'''str'''

其中三引号常用方式如下
```
'''
line1
line2
  .
  .
'''
```
在字符串前面加一个R/r 表示原始字符串
```
print(r'\t\r')   #  \t\r
```
一些转义字符（特殊的字符）
```
\n          #换行       无法“看见”的字符
\'           #单引号   与语言本身有冲突的字符
\t          #横向制表符
\r          #回车
\n         #换行
\\          #表示\
```
元组 tuple  ( )与列表list  [ ]

元组与列表在python中的唯一区别就是：元组是不可变的，列表是可变的。(元组和字符串是不可变的)
```
a = 'hello'
a=a+'world'
print(a)  #'helloworld'    a变成了一个新的字符串，而不是改变了字符串

#列表可变
b=[1,2,3]
b.append(4)
print(b)  #[1,2,3,4]

#改变的是列表不是元组
c =  (1,2,3,[4,5,['a','b','c']])
c[3][2][1] = 'd'
c[3][0]='6'
c[3][1]=7
#c[2]=8   #会报错，因为元组不能被改变'tuple' object does not support item assignment
print(c)  #(1, 2, 3, ['6', 7, ['a', 'd', 'c']])  改变的是列表  而不是 元组
 ```
在你有一些不确定长度的相同类型队列的时候使用列表；在你提前知道元素数量的情况下使用元组，因为元素的位置很重要。
```
#元组
(1,2,3) 
((1,2,3),(4,'hello',True))
(1,2,[3,4],{5,6},{(1,2,3):10,'hello':11,100:'hello'})
()   #空元组
(1,)  #一个元素的元组
#列表
[1,2,3]
[[1,2,3],[4,'hello',True],(1,2,3),{7,8}{(1,2,3):10,'hello':11,100:'hello'}]
```


序列可以进行加法，与整数相乘，切片操作
```
#与整数相乘
'python'*3   # 'pythonpythonpython'
((1,2,3),(4,'hello',True))*2  # ((1, 2, 3), (4, 'hello', True), (1, 2, 3), (4, 'hello', True))
[[1,2,3],[4,'hello',True],(1,2,3)]*2 #[[1, 2, 3], [4, 'hello', True], (1, 2, 3), [1, 2, 3], [4, 'hello', True], (1, 2, 3)]
#同类型相加
'hello'+'world'   # 'helloword'
((1,2,3),(4,'hello',True))+(7,8,9)  #((1, 2, 3), (4, 'hello', True), 7, 8, 9)
[[1,2,3],[4,'hello',True],(1,2,3)]+[4,5,6] #[[1, 2, 3], [4, 'hello', True], (1, 2, 3), 4, 5, 6]
#切片
'hello world'[0]       # 'h'   从0开始
'hello world'[-1]      # 'd'   从末尾往前数1
'hello world'[1:4]    # 'ell'  从1开始，4前一位结束
'hello world'[0:-2]    # 'hello wor'  从开头到末尾减去2位
'hello world'[:-5]     # 'hello '  从开头到末尾减去5个字符  
'hello world'[1:-2]   #'ello wor'    从1到末尾减去2位
'hello world'[6:100]    # 'world'  超过，从第6位取到末尾
'hello world'[6:]     # 'world'  从第6位取得末尾
'hello world'[-1:2]   #'’‘  空字符串，不能这样做
```
**集合set {}和字典dict {}**
集合和字典的特点是   **无序，不重复**
set()表示空集合
{}  表示空字典
```
-   #可以用来求两个集合的差集
+  #可以用来求两个集合的交集
|   #可以用来求两个集合的合集
```
字典是通过key访问value{key1:value1,key2:value2}
key**不能重复,类型为int,str，tuple**
value可以为任意数据
