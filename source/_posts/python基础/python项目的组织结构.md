---
title: (5) python项目的组织结构
date: 2018-11-14 21:59:11
tags:
categories: python基础
---
包、模块、类→函数、变量

**序列解包**
```
# a=1
# b=2
# c=3
# d,e,f=4,5,6  
```
**定义一个函数**
```
def damage(skill1,skill2): 
    damage1 = skill1*3
    damage2 = skill2*2+10
    return damage1,damage2 (不return，就是返回none)


skill1s,skill2s=damage(2,3)
print(skill1s,skill2s)
```
```
def add(x,y):
    result=x+y
    return result
    
def print_code(code):
    print(code)
    return

a=add(1,2)
print_code('python')
print(a)
```
**函数参数**
```
def print_student_files(name, gender,age,adress):
    print("I'm "+name)
    print("I'm "+age+'years old')
    print("I'm "+ gender)
    print("I'm living in "+adress)

print_student_files('weilai','man','18','hubei')

def print_student_files1(name, gender='man',age=18,adress='hubei'):
    print("I'm "+name)
    print("I'm "+str(age)+ 'years old')
    print("I'm "+gender)
    print("I'm living in "+adress)

print_student_files1('weilai','woman',18,'hubei')
#重点：
#1）必须参数:形参(例如name)，实参('weilai','man',18,'hubei')
#2）关键字参数
#3)默认参数：大多数情况下，函数的参数选取的的是一种默认值，可选用默认参数
# 注意事项:1、形参没有给默认值的，函数调用时得给一个实参
#         2、非默认参数不能放在默认参数之后（调用时，同理）
#         3、参数顺序得与默认参数顺序相同（关键字参数有时，可不遵守顺序）
#         4、给了默认参数，函数调用时优先使用实参
```
**import**
```
import _init_
print(_init_.b)

# 注意事项：import 与 from import
#         1）如 print t包C7.py中的a
#         import t.c7 ~ print（t.c7.a）   等价于from t.c7 import a ~print（a）
#         等价于from t import c7.a ~print（c7.a）
#         2)import t.c7 ~ print（t.c7.a） 等价于import t.c7 as m ~print（m.a）


#         3）包和模块不会被重复导入
        # 4）避免循环导入
        # 5）from t.c7 import * (导入C7中所有的变量)
        # 6）from t.c7 impor _all_=['a','c'] (导入C7中'a','c'两个变量） 
```
**if**
```
mood=True 
if mood:
    print('go to left')
else :
    print('go to right')
```
```
a=1
b=2
c=3
d,e,f=4,5,6   #序列解包
if d<a:
    print('go to left')
elif d<b:
    print('go to left')
elif d<c:
    print('go to left')
elif d<e:
    print('go to left')
```

**for**
```
a=[1,2,3,4,5]
for x in a:
    if x==3:
        break 
    print(x)

    #     continue
    # print(x)

a = [['apple','orange','banana'],(1,2,3)]
for x in a:
    for y in x: 
        print(y)
    print(x)


for x in range(0,10):
    print(x)
for x in range(0,10,2):
    print(x)
```
 注意事项：
        1)break和continue区别：break到3就停止，continue跳过3继续
       2）注意print()函数的位置，对结果的影响
       3）递归用while，遍历用for
