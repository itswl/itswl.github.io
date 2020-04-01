---
title: (11) python之函数式编程
date: 2018-11-14 22:00:48
tags:
categories: python基础
---
**函数式编程是一种思维，闭包只是其一种体现**

**匿名函数**
```
#例如 x+y

#普通函数
def add(x,y):
  return x+y

#匿名函数
lambda x,y:x+y 
```
**三元表达式**
```
# x,y   x大于y，取x 否则，取y
# x > y ? x:y  (其他语言中)
# x if x > y else y #python中
#条件为真时返回的结果 if 条件判断 else 条件为假时的返回结果 
x = 1
y = 4
r = x if x > y else y
print(r) #4
```
**map类**
```
list_a = [1,2,3,4,5,6,7,8]

def square(x):
    return x * x

r = map(square,list_a)
print(r)  #<map object at 0x0000026BCECDE9E8>#map类
print(list(r)) #[1, 4, 9, 16, 25, 36, 49, 64]
#map:将集合里每个元素传到square里去，并且映射到新的集合中

#也可以用for
def square1(x):
    return x * x
for x in list_a:
    x = square1(x)
    print(x)#1, 4, 9, 16, 25, 36, 49, 64
```
**map常用方法**
```
list_a = [1,2,3,4,5,6,7,8]

r = map(lambda x:x * x,list_a)
print(list(r))#[1, 4, 9, 16, 25, 36, 49, 64]
```
```
list_a = [1,2,3,4,5,6,7,8]
list_b = [1, 4, 9, 16, 25, 36, 49]

s = map(lambda x,y:x * x + y,list_a,list_b)  #map中传入多个list
print(list(s))  #[2, 8, 18, 32, 50, 72, 98] 长度取决于列表少的那个
```
**reduce** 连续计算，连续计算，连续调用lambda
```
from functools import reduce
list_a = [1,2,3,4,5,6,7,8]
r = reduce(lambda x,y:x + y,list_a,10) #初始值为10
 #10+1,得到11，11+2,得到13.....等一系列计算
print(r) #46
```
```
#初始值为50，从0累加到99
from functools import reduce
a = range(0,100)
r = reduce(lambda x,y:x+y,a,50)
print(r) 
```
**map/reduce编程模型 映射 归纳 
并行计算
函数式编程**

**filter  过滤**
```
list_a = [1,1,0,0,1,1,0,1,0]
# r = filter(lambda x: True if x==1 else False, list_a)
r = filter(lambda x:x,list_a) #因为0代表False
print(list(r))
```
