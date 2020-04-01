---
title: (12) python中的装饰器
date: 2018-11-14 22:00:43
tags:
categories: python基础
---

**对修改是封闭的，对扩展是开放的**
####在原有函数上调用时加时间
```
import time

def a():
    print('This is a function') 

def b():
    print('Hello world') 

def print_current_time(abc):
    print(time.time())
    abc()

print_current_time(a)
print_current_time(b)
```
**等同于**
```
import time

def a():
    print('This is a function') 

def b():
    print('Hello world') 

def print_current_time(abc):
    print(time.time())
    abc()

print(time.time())
a()
print(time.time())
b()
```
**更改了内部实现，不够优雅**

####装饰器
```
import time

def decorator(func):
    def wrapper():
        print(time.time())
        func()
    return wrapper

def f1():
    print('This is a function') 

f = decorator(f1)
f()
```
**修改一下**
 ```
import time

def decorator(func):
    def wrapper():
        print(time.time())
        func()
    return wrapper

@decorator   #@装饰器名字
def f1():
    print('This is a function') 

f1()   #并没有改变原有函数的调用方式
#这才是装饰器  意义所在
```
**进一步优化，支持不同个数的参数**
```
import time

def decorator(func):
    def wrapper(*args):
        print(time.time())
        func(*args)
    return wrapper

@decorator   #@装饰器名字
def f1(func_name):
    print('This is a function'+ func_name) 

@decorator
def f2(func_name1,func_name2,func_name3):
    print('hello world'+ func_name1) 
    print('hello world'+ func_name2) 
    print('hello world'+ func_name3) 

f1('tset func')   
f2('tset func1','tset func2','tset func3')
```
**进一步优化，加入关键字参数**
```
import time

def decorator(func):
    def wrapper(*args,**kw):
        print(time.time())
        func(*args,**kw)
    return wrapper

@decorator   #@装饰器名字
def f1(func_name):
    print('This is a function'+ func_name) 

@decorator
def f2(func_name1,func_name2,func_name3):
    print('hello world'+ func_name1) 
    print('hello world'+ func_name2) 
    print('hello world'+ func_name3) 

@decorator
def f3(func_name1,func_name2,**kw):
    print('hello world'+ func_name1)
    print('hello world'+ func_name2)
    print(kw)


f1('tset func')   
f2('tset func1','tset func2','tset func3')
f3('tset func1','tset func2',a = 1,b = 2,c = '123')
```

**装饰器也可以用来控制访问**
**一个函数上就可以加多个装饰器**
