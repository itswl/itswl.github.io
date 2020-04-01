---
title: (15) python中的None
date: 2018-11-14 22:02:15
tags:
categories: python基础
---

**None 表示空  不同于** 空字符串 空的列表 0 False

**类型不同，值不同**
```
print(type(None)) <class 'NoneType'>None是None类
a=''
b=False
c=[]
print(a==None)  #False
print(b==None) #False
print(c==None) #False  #值不相等
```
**深入**
```
def fun():
    return None

a = fun()
if not a:
    print('S')
else:
    print('F')

if a is None:
    print('S')
else:
    print('F')
#S
#S
```
```
def fun():
    return None

a = []
if not a:
    print('S')
else:
    print('F')

if a is None:
    print('S')
else:
    print('F')
#S
#F
```
**类中默认非空**
```
class Test():
    pass

test = Test()
if test:
    print('S')
else:
    print('F')
#S
```
**类中为空的情况**
```
class Test():
    def __len__(self):
        return 0 #(只能为int类型)

test = Test()
if test:
    print('S')
else:
    print('F')
#F
```
```
class Test():
    def __len__(self):
        return 0 #(只能为int类型)

test = Test()
print(bool(None)) #False
print(bool({}))#False
print(bool([]))#False
print(bool(test))#False
```
**由__bool__决定True or False,与__len__无关**
(即print 只有 bool call  True,或者bool call False ))
```
class Test():

    def __bool__(self):
        print('bool called')
        return False#(/True)

    def __len__(self):
        print('len called')
        return True #(只能为int类型)

print(bool(Test()))
#bool called
#False#(/True)
```
