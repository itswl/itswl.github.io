---
title: (4) python中流程控制语句
date: 2018-11-14 21:58:54
tags:
categories: python基础
---

**条件语句**
if elif else都是关键字，需要能读和写

基本格式：
```
  if 条件语句1：
    执行语句块1
  elif 条件语句2：
    执行语句块2
  else：
    执行语句块3
```
执行过程：
```
a.先判断条件语句1是否为True，如果为True就执行冒号后边的执行语句块1，整个条件结构就执行完了;如果是False，就去判断条件语句2是否为True。
b.如果是True就执行执行语句块2，再执行其他语句;如果是False,就直接执行语句块3，再执行其他语句。
```
注意：冒号后边语句块和冒号所在得语句要保持一个缩进。

**if**
判断条件语句的值是否为True，如果为True，就只执行执行语句块。否则就直接执行if语句后面的其他语句。
```
  if 条件语句：
      执行语句块
  
  age=20
  要求判断年龄是否大于18，如果大于18就输出'成年人'
  if age>18:
      print('成年人')
  
  练习：判断一个数是否是偶数，如果是就打印'xxx是偶数'
  n=18
  if n%2==0:
      print('%d是偶数'%(n))
```
2.if-else
判断条件语句是否为True，如果为True，就执行语句块1;否则就执行语句块2.
```
  if 条件语句：
      执行语句块1
  else：
      执行语句块2
  n=17
  if n%2==0:
      print('%d是偶数'%(n))
  else:
      print('%d是奇数'%(n))
  练习：输入一个数，如果这个数大于10，就输出他的2倍值。否  则输出这个数的2次幂。
  input():从控制台获取键盘输入的一个字符串，以回车结束。
  
  inputvalue=input('请输入一个数：')
  print(inputvalue)
  n=int(inputvalue)
  比较运算符和+以及*，在运算的时候，两边可以都是字符串，也可以都是数字，但是不可以一样一个。
  if n>10:
  num=n*2
      print(num)
  else:
  num=n**2
      print(num)
```
3.if-elif-elif-else
总结:

a.如果要求中需要多个判断，可以使用多个elif的if语句。
b.一个if/elif/else语句中可以嵌套其他的if语句。
```
（1）给一个成绩，判断成绩是优秀(90-100)、良好(80-89)、        中等(60-79)、不及格(60以下)
方法一：
grade=96
if grade>=90:
    if grade>100:
        print('成绩有误')
    else:
        print('优秀')
elif grade>=80:
    print('良好')
elif grade>=60:
      print('中等')
elif grade>=0:
      print('不及格')
else:
      print('成绩有误')
方法二：
grade=67
if 100>=grade>=90:
  print('优秀')
elif 90>grade>=80:
  print('良好')
elif 80>grade>=60:
  print('中等')
elif 60>grade>=0:
  print('不及格')
else:
  print('成绩有误')
  
（2）给个年龄，判断年龄处于：婴儿（0-1岁）、儿童（2-4         岁）、少年（5-12岁）、青年（13-18岁）、成年（19-40）、       中年（41-60）、老年（60以上）
age=1
if age<2:
  if age<=0:
      print('年龄输入错误')
  else:
      print('婴儿')
elif age<5:
  print('儿童')
elif age<13:
  print('少年')
elif age<19:
  print('青年')
elif age<41:
  print('成年')
elif age<61:
  print('中年')
else:
  print('老年')
说明：Python中没有switch语法。

pass：占位，防止因为没有写块结构而出现语法错误。

if n==10:
    pass
```
**转换函数**

1.int()
int():将其他的数据转换成int类型的数据
```
num=12.56
print(int(num))    # 12 将浮点数转换成整数（直接去掉小数部分）
bool1=True
print(int(bool1))  # 1 将布尔值转换成整数，True->1  False->0
str1='123'
print(int(str1))   # 123 只有纯数字字符串或者纯数字字符串前有正负号的字符串才能转换成相应的整数。
```
2.flot()
flot():将其他数据转换成浮点型
3.bool()
bool()：将其他的数据转换成布尔值

数字转换成布尔，非0是True，0是False。
```
print(bool(12))     # True
print(bool(-12.3))  # True
print(bool(0))      # False
字符串转换成布尔，除了空串是False，其他的都是True。

print(bool('abc'))  # True
print(bool(''))     # False
```
注意：在if或者while循环后的条件语句，可以不是结果为True/False的表达式，也可以是值是其他类型的表达式.判断的是时候就看这个值转换成bool后的结果是True还是False。
```
if 10:
  print('aaa')   # aaa （10转换成bool后是True) 
if 0:
  print('aaa')   #  （0转换成bool后是False）
```
练习：判断一个字符串是否是空串，如果不是就直接打印这个字符       串，否则打印“空串”
```
方法1：
str1=''
if str1:
  print(str1)
else:
  print('空串')
方法2：
str1='abc'
if str1!='':
  print(str1)
else:
  print('空串')
```
4.str()
str()：将其他的数据转换成字符串。所有的数据类型都可以转换成字符串。
**循环**
python中循环：for循环、while循环（一个操作需要重复执行多次，这个时候就要考虑使用循环）
**for循环**
python中的for循环只有for-in循环：
```
格式：
for 变量名 in 列表：
  循环体
执行过程：使用变量去依次获取列表中的数据直到获取完为止;没获取一个数据，执行一次循环体。

循环次数：由列表中的数据的个数决定。

去获取字符串中的每一个字符
str1='abcdef'
for char in str1:
  print(char)

去统计字符串中'a'出现的次数
str1='avaadafvaavafaaa'
n=0
for char in str1:
  if char=='a':
      n=n+1       
print(n)
range（）函数：可以生成一个数值范围
````
```
打印1-100
for n in range(1,101):
  print(n)
用法1：range(n),生成0~n-1的值
for x in range(9):
  print(x)
````
用法2：range(m,n),生成m~n-1的数
```
for n in range(5,9):
  print(n)
打印0-100之间所有的偶数
for x in range(101):
  if x%2==0:
      print(x)
```
用法3：range(m,n,step):从m开始每step取一个数，取到n前       一个数为止。
```
for x in range(1,8,2):
  print(x)   # 1,3,5,7 

不通过字符串相乘，打印10次“=”,并且打印在同一行。
for _ in range(10):
  print('=',end=' ')
```
求1+2+3...+100
```
n=0
for x in range(1,101):
  n=n+x
print(n)
```
注意：如果循环中的变量取到的值没有意义，循环只是单纯的控制次数，这个时候for后面的变量名一般用“_”代替。

**while循环**
``` 
格式：
 while 条件语句：
    循环体
```
执行过程：判断条件语句结果是否为True，如果为True就执行一次循环体。执行完循环体后再判断条件语句是否为True，如果为True继续执行循环体。重复这个过程，直到条件语句结果为False

for循环可以实现的操作，while循环都可以

打印1-100
```
方法1：
x=0
while x<100:
  x+=1
  print(x) 
方法2：
x=1
while x<=100:
  print(x)
  x+=1
```
计算1+2+3+...+100
```
x=0
n=0
while n<100:
  n+=1
  x+=n
  print(x)
```
求1-100中所有偶数的和
```
方法1：
n=0
x=0
while n<=100:
  if n%2==0:
      x=x+n
      n=n+1
  print(x)
方法2：
n=0
x=0
while n<100:
  n+=2
  x=x+n
print(x)
```
**break和continue**
1、break
break是一个让循环提前结束的关键字

如果在for循环或者while循环中遇到了break，那么循环就在break的位置直接结束。结束后程序执行循环后边的代码。

练习:找到1000~9999中第一个能够被13整除的数，打印出来
```
for x in range(1000,10000):
  if x%13==0:
      print(x)
      break    
  
for x in range(1,100):
  if x==50:
      break
      print(x)     # 1 2 3 ...  49
```
用while循环实现：不断的让用户去输入数字，直到用户输入的数字是0为止。最后在打印之前输入的数的和。

input()函数：程序执行到input()函数的时候，程序就会停下来，等待用户从键盘输入并且以回车结束，然后才会往下执行。

注意：break只能写在循环中
```
  sum1=0
  while True:
  num=int(input(">>>"))   # 获取键盘输入的内容，并且转换成int类型
      sum1+=num   # 将当次输入的数字加起来
      if num==0:   #  判断输入的数字是否是0，如果是就让循环结束
          break   
      print(num)
  print(sum1)
```
for循环的特点：次数确定，可以在序列中取数据

while循环：循环次数不确定的（while True + break）

randint(m,n):产生一个m到n的随机整数

产生随机数：random模块是python内置用来产生随机数的模块，里面提供了很多产生随机数的函数。

  猜数字：随机生成一个整数。用户输入数字。如果用户输入的数字大于这个随机数就提示：“大了”;如果用户输入的数小于随机数就提示：“小了”。直到用户输入的数和这个随机数大小一样游戏结束。
```
  import random
  num=random.randint(0,100)   # 产生一个0到100的随机数
  n=0
  while True:
  num1=int(input("请输入你猜的数字："))
  n=n+1
  if num1>num:
      print('大了')
  elif num1<num:
      print('小了')
  else:
      print('恭喜你，猜对了！')       
      print('一共猜了：%d次'%(n),end='  ')
      if n<=5:
          print('你太棒了，只猜了%d次就猜对了'%(n))
      else:
          print('下次加油！')
      break
```
2、continue
continue:结束当次循环，进入下次循环
```
  for x in range(1,10):
      print('=')
      continue   # 遇到continue就不再执行循环体后面的内容，直接进入下一次循环的判断
      print(x)
  ````
  求1~100中所有奇数的和
```
  sum=0
  for x in range(1,100):
      if x%2==0:
          continue
      sum=sum+x
  print(sum)
  ```
  打印100~999中十位数上不是3的所有数：
```
  for x in range(100,1000):
      if x//10%10==3:
          continue
      print(x)   
 ``` 
  统计输入的数字中，偶数的个数。如果输入0，就结束。（必须使用continue）
```
  flag=True
  n=0
  while True:
      num=int(input('请输入一个数：'))  # 输入数据
      if num%2==1:  # 判断是否是奇数
          continue
      if num==0:
          flag=False
      n=n+1
  print(n)
````
**else**
python中循环语句后面可以加else语句。这个else语句会在循环结束后执行。
```
 for 变量 in 序列：
  循环体
 else：
  循环结束后会执行的语句块
 ```
```
 1*2*3...*10
 sum1=1
 for x in range(1,11):
  sum1*=x
 else:
  print(sum1)
```
注意：如果再循环语句中使用break，那么else语句不会执行。（continue不存在这个问题）

  1*2*3...*10，当乘积大于10000就不在执行
```
  sum1=1
  for x in range(1,11):
      if sum1*x>10000:    
          break
      sum1*=x
  print(sum1)
  else:
      print(sum1)  # 如果在循环中执行了break，那么else中的语句不会执行
```
**多重循环**
在循环体里面可以有其他的循环语句，结构为：
```
 for 变量 in 序列：
     for 变量1 in 序列2：
      循环体2
  其它的循环语句
 
 for 变量 in 序列：
  其他的循环语句1
  while 条件语句：
      循环体2
  其他的循环语句2
 
 while 条件语句1：
  while 条件语句2：
      循环体2
  其他的循环语句2
```
例如：
```
  如果n=5 打印
  1
  12
  123
  1234
  12345

  n=5
  for x in range(1,n+1):   # 控制行数
      for b in range(1,x+1):  # 控制当前行的数值
          print(b,end='')
      print()   # 一行结束换行

  *****
  ****
  ***
  **
  *
  n=5
  for x in range(1,n+1):
      for b in range(x,n+1):
          print('*',end='')
      print()
  
  n=10
  for x in range(1,n+1):
      for b in range(x,n+1):
          print('*',end='')
      print()
```
参考了简书中某人的记录，但找不到具体是谁了。侵删。
