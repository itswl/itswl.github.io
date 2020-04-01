---
title: (10) python中的枚举
date: 2018-11-14 22:00:48
tags:
categories: python基础
---
**在python中，枚举的本质是一个类，所有枚举类都是Enum的子类**
**枚举值不能动态更改且标签唯一，标签唯一但是数值不唯一。如果数值不唯一，相当于起别名**

**表示类型的三种方式**
```
from enum import Enum

class VIP(Enum):       #所有枚举类都是Enum的子类
    YELLOW = 1     #常量是不能更改的   用大写表示（约定的，python中没有真的常量）
    GREEN = 2   
    RED =  'str'
    BLACK = 4
    PINK = 1     # 其实就是YELLOW = 1， 可以看作YELLOW 的别名，
    #YELLOW = 1  #会报错，不能同时有两个YELLOW Attempted to reuse key: 'YELLOW'
  #  GREEN = 6  #会报错，不能继续使用GREEN这个标签 Attempted to reuse key: 'GREEN'

#class Common():
  #  YELLOW = 1       
#VIP.YELLOW =6         #会报错，枚举中的值不能被更改
print(VIP.PINK)
print(VIP.YELLOW)    #VIP.YELLOW   (不关心取值)
print(VIP.PINK)      #VIP.YELLOW   可以看作YELLOW 的别名
print(type(VIP.YELLOW))   #<enum 'VIP'>  枚举类型
print(VIP.YELLOW.name)   #YELLOW 获取标签名字
print(type(VIP.YELLOW.name))  #<class 'str'> 字符串类型

print(VIP['YELLOW'])  #VIP.YELLOW

print(VIP.YELLOW.value)  #1   获取值

#枚举类型、枚举的名字、枚举的值

for v in VIP:   #遍历枚举类型(并不会把别名打印出来)
    print(v)    #VIP.YELLOW
                #VIP.GREEN
                #VIP.RED
                #VIP.BLACK 

#枚举的比较运算
#枚举不可以进行大小比较，但可以进行等值比较，身份比较
result = VIP.YELLOW == VIP.PINK  #枚举之间的等值比较  #True
result1 = VIP.YELLOW == 1    #False
#result = VIP.YELLOW >= VIP.PINK  #枚举不能进行大小比较报错 
                                 #'>=' not supported between instances of 'VIP' and 'VIP'
result2 = VIP.YELLOW is VIP.PINK #True   身份比较
print(result)  
print(result1)
print(result2)  


class VIP1(Enum):       
    YELLOW = 1     
    GREEN = 2   
    RED = '3'
    BLACK = 4
    PINK = 1

result = VIP.YELLOW == VIP1.YELLOW  #Fales  虽然值相等，但其实是两个不同的枚举类型
print(result) 

for v in VIP.__members__.items():   #遍历枚举类型(把别名也打印出来)
    print(v)
'''
('YELLOW', <VIP.YELLOW: 1>)
('GREEN', <VIP.GREEN: 2>)
('RED', <VIP.RED: 3>)
('BLACK', <VIP.BLACK: 4>)
('PINK', <VIP.YELLOW: 1>)
'''

for v in VIP.__members__:
    print(v)   #枚举的名字（包括别名）
'''
YELLOW
GREEN
RED
BLACK
PINK
'''

a = 1
a = VIP(a)         #把a变成一个枚举类型
print(a)   #VIP.YELLOW     


from enum import IntEnum #(枚举的值得是int类型)
from enum import IntEnum,unique #(枚举的值得是int类型,且不能重复)

class VIP2(IntEnum):       
    YELLOW = 1     
    GREEN = 2   
#    RED = 'str'  #会报错,(枚举的值得是int类型)
    BLACK = 4
    PINK = 1    

@unique
class VIP3(IntEnum):       
    YELLOW = 1     
    GREEN = 2   
#    RED = 'str'  #会报错,(枚举的值得是int类型)
    BLACK = 4
  #  PINK = 1       #会报错,取值重复



#枚举  是单例模式    #23种设计模式        实践中
```
