
---
title: (16) python补充
date: 2018-11-14 22:01:49
tags:
categories: python基础
---
```
num2 = 100
sum1 = lambda num1 : num1 + num2 
num2 = 10000
sum2 = lambda num1 : num1 + num2 

print( sum1( 1 ) )#10001
print( sum2( 1 ) )#10001
```
lambda 表达式中的 num2 是一个自由变量，在运行时绑定值，而不是定义时就绑定，这跟函数的默认值参数定义是不同的。
**打印乘法表**
**占位符**
```
#方法1
for i in range(1, 10):
    for j in range(1, i+1):
 # end='' 意思是末尾不换行，加空格
        print('{}x{}={}\t'.format(i, j, i*j), end='') 
    print()

#方法2
for m in range(1, 10):
    for n in range(1, m+1):
        print('%d*%d=%d\t'%(n,m,n*m), end='')
 
    print()
```
**while 与for (待补充)**



**从键盘获取输入信息：input**
在 Python 中可以使用 input 函数从键盘等待用户的输入
用户输入的 任何内容 Python 都认为是一个 字符串

**格式化输出：print**
如果希望输出文字信息的同时，一起输出 数据，就需要使用到 格式化操作符
% 被称为 格式化操作符，专门用于处理字符串中的格式
包含 % 的字符串，被称为 格式化字符串
% 和不同的 字符 连用，不同类型的数据 需要使用 不同的格式化字符
>格式化字符   含义
%s	   字符串
%d	   有符号十进制整数，%06d 表示输出的整数显示位数，不足的地方使用 0 补全
%f	  浮点数，%.2f 表示小数点后只显示两位
%%	  输出 %

**随机数生成**
```
import random
#导入模块后，可以直接在 模块名称 后面敲一个 . 然后按 Tab 键，会提示该模块中包含的所有函数
#random.randint(a, b) ，返回 [a, b] 之间的整数，包含 a 和 b

random.randint(12, 20)  # 生成的随机数n: 12 <= n <= 20   
random.randint(20, 20)  # 结果永远是 20   
random.randint(20, 10)  # 该语句是错误的，下限必须小于上限。
```
随机数的小游戏

```
import random

# 从控制台输入要出的拳 —— 石头（1）／剪刀（2）／布（3）
player = int(input("请输入您要出的拳 石头（1）／剪刀（2）／布（3）："))

# 电脑 随机 出拳 —— 先假定电脑只会出石头，完成整体代码功能
computer = random.randint(1, 3)

print("玩家选择的拳头是 %d - 电脑出的拳是 %d" % (player, computer))

# 比较胜负
# 1 石头 胜 剪刀
# 2 剪刀 胜 布
# 3 布 胜 石头
# if (()
#        or ()
#        or ()):
if ((player == 1 and computer == 2)
        or (player == 2 and computer == 3)
        or (player == 3 and computer == 1)):

    print("欧耶，电脑弱爆了！")
# 平局
elif player == computer:
    print("真是心有灵犀啊，再来一盘")
# 其他的情况就是电脑获胜
else:
    print("不服气，我们决战到天明！")
```
```
import random
guess_list = ["石头", "剪刀", "布"]
win_combination = [["布", "石头"], ["石头", "剪刀"], ["剪刀", "布"]]

while True:
    computer = random.choice(guess_list)
    people = input('请输入：石头,剪刀,布\n').strip()
    if people not in guess_list:
        continue
    elif computer == people:
        print ("平手，再玩一次！")
    elif [computer, people] in win_combination:
        print ("电脑获胜，再玩，人获胜才能退出！")
    else:
        print ("人获胜！")
        break
```
**函数**
```    
def print_code(code):
    print(code)
    #return None
print_code('python')  # python

def add(x,y):
    result=x+y
    return result
a = add(1,2)
print(a)  # 3

def add1(x,y):
    result = x + y
    print(result)
add1(1,2)  # 3

def add2(x,y):
    result = x + y
    print('%d + %d = %d'%(x,y,x+y))
add2(1,2)  # 1 + 2 = 3
```
####多值参数
有时可能需要 一个函数 能够处理的参数 个数 是不确定的，这个时候，就可以使用 多值参数。

**python 中有 两种 多值参数：**
>参数名前增加 一个 * 可以接收 元组
参数名前增加 两个 ** 可以接收 字典

**一般在给多值参数命名时，习惯使用以下两个名字**
>*args —— 存放 元组 参数，前面有一个 *
**kwargs —— 存放 字典 参数，前面有两个 **

```
def demo(num, *args, **kwargs):

    print(num)
    print(args)
    print(kwargs)


demo(1, 2, 3, 4, 5, name="小明", age=18, gender=True)
#1
#(2, 3, 4, 5)
#{'name': '小明', 'age': 18, 'gender': True}

demo(1,(2,3,4,5),{"name":"小明", "age":18, "gender":True})
#1
#((2, 3, 4, 5), {'name': '小明', 'age': 18, 'gender': True})
#{}

demo(1,(2,3,4,5), name="小明", age=18, gender=True)
#1
#((2, 3, 4, 5),)
#{'name': '小明', 'age': 18, 'gender': True}
```
**元组和字典的拆包**
在调用带有多值参数的函数时，如果希望：
将一个 元组变量，直接传递给 args
将一个 字典变量，直接传递给 kwargs
就可以使用 拆包，简化参数的传递，拆包 的方式是：
在 元组变量前，增加 一个 *
在 字典变量前，增加 两个 *
```
def demo(*args, **kwargs):

    print(args)
    print(kwargs)

# 需要将一个元组变量/字典变量传递给函数对应的参数
gl_nums = (1, 2, 3)
gl_xiaoming = {"name": "小明", "age": 18}

# 会把 num_tuple 和 xiaoming 作为元组传递个 args
demo(gl_nums, gl_xiaoming)
#((1, 2, 3), {'name': '小明', 'age': 18})
#{}
demo(*gl_nums, **gl_xiaoming)
#(1, 2, 3)
#{'name': '小明', 'age': 18}
```

**函数的返回值**
```
# Python 专有，利用元组交换两个变量的值
a, b = b, a
```


#面向对象(补充)
