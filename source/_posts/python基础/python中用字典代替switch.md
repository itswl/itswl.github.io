---
title: (13) python中用字典代替switch
date: 2018-11-14 22:02:16
tags:
categories: python基础
---
**switch语句类型**
```
'''
switch(n)
{
case 1:
  执行代码块 1
  break;
case 2:
  执行代码块 2
  break;
default:
  n 与 case 1 和 case 2 不同时执行的代码
}
'''
```
**例如：**
```
'''
switch (day)
{
case 0:
  x="Today it's Sunday";
  break;
case 1:
  x="Today it's Monday";
  break;
case 2:
  x="Today it's Tuesday";
  break;
case 3:
  x="unknown"
}
'''
```
**python中字典方式**
```
day = 3
switcher = {
    0:'Today it\'s Sunday',
    1:'Today it\'s Monday',
    2:'Today it\'s Tuesday'
}
#day_name =switcher[day]  #并不能显示default
day_name = switcher.get(day,'Unknown')
print(day_name)
```
**函数**
```
day = 3

def get_monday():
    return 'Monday'

def  get_sunday():
    return 'Sunday'

def get_tuesday():
    return 'Tuesday'

def get_default():
    return 'Unknown'

switcher1 = {
    0:get_sunday,
    1:get_monday,
    2:get_tuesday
} 

day_name = switcher1.get(day,get_default)()
print(day_name)
```
