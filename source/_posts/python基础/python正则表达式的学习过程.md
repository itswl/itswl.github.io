---
title: (7) python正则表达式的学习过程
date: 2018-11-14 21:59:42
tags:
categories: python基础
---

```python
 #优先使用内置函数
a = 'C|C++|Java|C#|Python|Javascript'
print(a.index('Python')>-1)
print('Python' in a)         
#利用内置函数判断字符串'python'是否在a中
```

正则表达式是一个特殊的字符序列，帮助检测一个字符串是否与所设定字符序列相匹配。.可快速检索文本、实现一些替换文本的操作。
例如:
1、检查一串数字是否是电话号码.
2、检测一个字符串是否符合email
3、把一个文本里指定的单词替换为另外一个单词。
#用正则表达式
```python
import re                      #   引入re 模块 

a = 'C|C++|Java|C#|Python|Javascript'

r = re.findall('Python',a)           #findall 方法  
print(r)
if len(r) > 0:
    print('字符串中包含Python')
else:
    print('No')                    
 ```      
  正则表达式不仅可以用来检测字符串，也可以用来替换字符串。
```python
import re                       
a = 'C0C++7Java12C#9Python67\nJavascript8'
 #用r来提取a中的数字
r = re.findall('\d',a)      #\d 来表示数字（0-9）
print(r)
#用s来提取a中的非数字
s = re.findall('\D',a)      #\D 来表示非数字的字符
print(s)
```
上面'python'是普通字符，'\d','\D'属于元字符
正则表达式就是由普通字符和元字符等组合在一起的。

**字符集**
虽然可以提取字符串，但提取出来的都是一个一个字符。只能匹配单一的字符（单个字母，数字）
```python
import re
a = 'abc,acc,adc,aec,adfc,ahc,afc'
r = re.findall('a[cf]c',s)   #提取afc 或acc,普通字符a,c定界，元字符c，f
#[]里表示或。[cf] c或f.[cdf] c或d或f  [^cfd]取反，不是c和d和f。[c-f]取c到f。
print(r) 
```
**概括字符集**
 \d即 [0-9]
\D所有的非数字
\w单词字符 '[A-Za-z0-9]和下划线_ 
\W 非单词字符，
\s 空白字符(空格/制表符/换行符)
\S 非空白字符
.  匹配除换行符之外其他所有的字符
```python
import re
a = 'C0C++7Java12C#9Python67Javascript8\n\r &^'
r = re.findall('\d',a) 
print(r)
#可自行验证
```
**数量词,贪婪与非贪婪**
```python
import re
a = 'C0C++7Java12C#9Python67Javascript8\n\r &^'
r = re.findall('\w{3}',a)  #提取出来的\w 3个一组
s = re.findall('[A-Za-z]{3}',a)
t = re.findall('[A-Za-z]{3,7}',a)#3到7个一组，优先选择7个
#贪婪 与 非贪婪
#python默认使用贪婪  按最大的匹配
u = re.findall('[A-Za-z]{3,7}?',a)#非贪婪  按最小的匹配，即3个一组
print(r)  
print(s)
print(t)
print(u)
```
**问号，星号，加号的使用方法**
```python
import re
a = 'pytho0python1pythonn2'

r =  re.findall('python*',a)  #['pytho', 'python', 'pythonn']
s =  re.findall('python+',a)
t =  re.findall('python?',a)
print(r)
print(s)
print(t)
```
1、 *  对*前的字符匹配0次或无限多次
2、+  对+前的字符匹配1次或无限多次
3、 ?   对?前的字符匹配0次或1次    与贪婪中的?是不同的

**边界匹配**
```python
import re 
qq = '100001'
#qq位数4-10位数
r =  re.findall('^\d{4,10}$',qq)  #^从字符串开头匹配 ， $从字符串末尾匹配
#即开头到结尾得在4-10之间
print(r)
```
**组**
```python
import re
a = 'PythonPythonPythonPythonPythonPython'
r =  re.findall('(Python){2}',a)
print(r)#['Python', 'Python', 'Python']
```

**匹配模式**   （函数中的第三个参数）
re.I 忽略匹配中的大小写
re.S 匹配所有的字符，包括换行符
```
import re
a = 'C0C++7Java12C#\n9Python67Javascript#8'
r =  re.findall('c#',a,re.I)
r =  re.findall('c#.{1}',a,re.I|re.S)   #  |  且
print(r)#['C#']
print(r1)#['C#\n']
```
**re.sub简单用法**     
```python
import re
a = 'C0C++C#7Java12C#\n9Python6C#7JavascriptC#8'
r =  re.sub('C#','GO',a,0)  #无限次替换
s =  re.sub('C#','GO',a,1)  #只替换一次
t =  a.replace('C#','GO')    #python内置函数
print(r)
print(s)
print(t)
```
**re.sub高阶用法**
```
import re
a = 'C0C++C#7Java12C#\n9Python6C#7JavascriptC#8'

def convert(value):
    print(value)
#<re.Match object; span=(5, 7), match='C#'>
#<re.Match object; span=(14, 16), match='C#'>
#<re.Match object; span=(25, 27), match='C#'>
#<re.Match object; span=(38, 40), match='C#'>
#所以用value.group()
    matched = value.group()
    return '!!' + matched +'!!'

r =  re.sub('C#',convert,a)
print(r)
```
**把函数作为传递参数**
```
import re
s = 'A1b2c3d4e5f6g7h8i9'

def convert1(value):
    print(value)
    matched1 = value.group()
    if int(matched1) >=6:
        return '9'
    else:
        return '0'

s =  re.sub( r'\d',convert1,s)
print(s)
```
**match和search**
match和search方法类似, 但有些许区别, 顾明思议
match是匹配的意思, 从第一个字符开始匹配, 匹配不到就返回
search是搜索的意思, 如果第一个字符匹配不到, 会继续往后匹配, 直到字符结束
```
import re
s = 'A1b2c3d4e5f6g7h8i9'
r = re.match(r'\d',s)    
r1 = re.search(r'\d',s)

print(r) #None
print(r1)#<re.Match object; span=(1, 2), match='1'>
```
**group()的用法**
```
import re

s = 'life is short,i use python'
r = re.search('life.*python',s)
r1 = re.search(('life.*python'),s) #与上行一样
r2 = re.search('life(.*)python',s)
print(r.group())
print(r1.group())
print(r2.group(0))  #全文匹配
print(r2.group(1))  #括号内匹配
r3 = re.findall('life(.*)python',s)
print(r3)
```
```
import re

s = 'life is short,i use python,I love python'
r = re.search('life(.*)python(.*)python',s)
print(r.group())#life is short,i use python,I love python
print(r.group(0))#life is short,i use python,I love python
print(r.group(1))# is short,i use (第一组)
print(r.group(2))#,I love（第二组）
print(r.group(0,1,2))   #用元组的方式表达出来#('life is short,i use python,I love python', ' is short,i use ', ',I love ')
print(r.groups())  #只会表示出（.*）的内容#(' is short,i use ', ',I love ')
```
