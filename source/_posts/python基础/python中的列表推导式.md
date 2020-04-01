---
title: (14) python中的列表推导式
date: 2018-11-14 22:02:15
tags:
categories: python基础
---

#####列表推导式
#####集合字典也可
#####元组也可

```
a=[1,2,3,4,5,6,7,8,9]
b=[i**3 for i in a if i <=5]
print(b)   #b={....}为集合，b(...)为元组，与a{[(...)]},什么的无关。
#为b()时，是一个对象
```

**也可以map filter表示**
```
list_a=[1,2,3,4,5,6,7,8,9]
r=filter(lambda x:x if x<=5 else 0,list_a)
s=map(lambda x:x*x,r)
print(list(s))
```
```
#同上，不建议
list_a=[1,2,3,4,5,6,7,8,9]
r=filter(lambda x:x if x<=5 else 0,list_a)
s=map(lambda x:x**3,filter(lambda x:x if x<=5 else 0,list_a))
print(list(s))
```
#####当为字典时
```
students ={
    'wei':18,
    'lai':19,
    'wan':20
}
b = [key for key,value in students.items()]
print(b)#['wei', 'lai', 'wan']
for x in b:
    print(x)#wei#lai#wan
```
**交换key和value
```
students ={
    'wei':18,
    'lai':19,
    'wan':20
}

b ={value:key for key,value in students.items()}
print(b)#{18: 'wei', 19: 'lai', 20: 'wan'}
```
