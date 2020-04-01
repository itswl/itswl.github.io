---
title: (6) python中面向对象
date: 2018-11-14 21:59:27
tags:
categories: python基础
---
![变量上为 类变量，实例变量](https://upload-images.jianshu.io/upload_images/14597179-fa443ae94cd458c3.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

有意义的面向对象的代码
类  是面向对象最核心的观念
类、对象
实例化
类最基本的作用：封装
一定要用self,引用 self.
类只负责定义，不会去运行
类和对象。
数据成员
构造函数可以让模板生成不同的对象

**类是现实世界或思维世界中的实体在计算机中的反馈**
**它将数据以及这些数据上的操作封装在一起**

**类 被   实例化后  就成了一个具体的对象** 
**类就像是一个模板，通过类  就可以产生很多对象。**
```
#比如这段代码为  1.py
class Human():
    sum = 0  #在class内部定义变量    类变量 （和类相关联在一起的）
    def __init__(self,name,age):#构造函数 ，
    #文件夹中得含有  _init_.py   模块才会被认为是一个包。包 导入时会优先运行.
    #初始化对象属性  
        self.name = name # 定义实例时需要self，调用实例不需要给self赋参 
        self.age = age   #定义实例变量，实例变量只和对象相关 self.
        #return NONE (构造函数只能返回NONE)  (补充知识)

    def get_name(self):
        print(self.name)

    def do_homework(self):
        print('This is a parent method')
```
```
from 1.py import Human  

class Student(Human):     #Human是Student的父类，Student是Human的子类
  
    def __init__(self,school,name,age):
        self.school = school 

        super(Student,self).__init__(name,age)  #建议以此方式调用父类
        #super 不仅仅可用于构造函数，也可以用于普通的实例方法

        # Human.__init__(self,name,age)   #子类里调用父类构造函数
        #self   用类调用实例方法没意义，所以加self

    #     self.age = age 
  

    def do_homework(self):      #子类和父类同名的话，不会报错，先使用子类
        #super(Student,self).do_homework()  #This is a parent method
        print('English homework')
        
student1 = Student('jinan university','wei',18) #实例化
student1.do_homework() #English homework
print(student1.name) #wei
print(student1.age)#18
#继承   单继承  多继承
```
**定义一个类**
```
class Student():
    name = ''   #在class内部定义变量    类变量 （和类相关联在一起的）
    age = 0   
    #行为 与  特征   
         
    def __init__(self,age,name):        #构造函数(实例化后，会自动调用)
        #初始化对象属性
        self.neme = name 
        self.age = age        #定义实例变量，实例变量只和对象相关 self.

    #    #return NONE (构造函数只能返回NONE)  (补充知识)

    def print_files(self):        #在class内部定义函数
        print('name:'+ self.name)
        print('age:'+ str(self.age))

student = Student()  #类的实例化
student.print_files()  #类下面方法的调用
#  建议 类的实例化以及类下面方法的调用 与类的定义放在不同的模块。
# 定义实例时需要self，调用实例不需要给self赋参 
```
**详解**
```
# 模块
c = 50

def add(x, y):
    c= x+y 
    print(c)

add(1,2)       #3   函数中局部变量的值
print(c)       #50  全局变量的值
 
# 两个print(c)的区别 
# 局部变量不会改变全局变量的值
```

**类和模块要区别对待**

###### '类变量'     和 类  关联在一起的 
######'实例变量'    和 对象 关联在一起的 
```
class Student():        
    sum=0   
    name = 'weilai'   
    age = 0

    def __init__(self,name,age):   
        self.name = name            
        self.age = age

    def marking(self,sorce):         #内部访问
        if sorce < 0:                #建议通过方法 对 类变量赋值
            # sorce =0
            return '不能给同学打负分'
        self.__sorce = sorce
        print(self.name + '同学本次的考试分数为：' + str(self.__sorce))
        return 'hello'
result =  student1.marking(80)#wang同学本次的考试分数为：80
print(result)   #hello
```
```
class Student():        
    sum=0    #   类变量   和类相关
    name = 'weilai'   #在class内部定义变量    类变量
    age = 0           # 类中赋值没有意义的。   #21 ，22 其实是与对象相关，不应出现在这
    # 行为 与  特征   
         
    def __init__(self,name,age):     #构造函数(实例化后，会自动调用),是一个特殊的方法
        #主要是被用来初始化对象属性
        self.name = name            #实例方法操控实例变量
        self.age = age
        print(self.__class__.sum)   
        print(Student.sum)
        self.__class__.sum +=1      #实例方法访问类变量中的sum
        print(Student.sum)
student1 = Student('wang',18)
student2 = Student('li',19)
```
**类方法主要操作和类相关的变量**
**用类调用类方法**
```
class Student():        
    sum=0   
    name = 'weilai'   
    age = 0

    def __init__(self,name,age):   
        self.name = name            
        self.age = age

    @classmethod                  #让其成为类方法     
    def plus_sum(cls):             #sum每运行一次就+1
        cls.sum+=1
        print(cls.sum)

student1 = Student('wang',18)
Student.plus_sum()  #用类调用类方法
student2 = Student('li',19)
Student.plus_sum()
```
**对象调用类方法(python可用但最好不要用)**
```
class Student():        
    sum=0   
    name = 'weilai'   
    age = 0

    def __init__(self,name,age):   
        self.name = name            
        self.age = age

    @classmethod                  #让其成为类方法     
    def plus_sum(cls):             #sum每运行一次就+1
        cls.sum+=1
        print(cls.sum)

student1 = Student('wang',18)
student1.plus_sum()  #用对象调用类方法
student2 = Student('li',19)
student2.plus_sum()
```
**静态方法**
```
class Student():        
    sum=0   
    name = 'weilai'   
    age = 0

    def __init__(self,name,age):   
        self.name = name            
        self.age = age

    @staticmethod                #静态方法
    def add(x):
        print(Student.sum)
        print('this is a static method')
```
**静态方法 能用的地方 基本可以用  类方法替代(最好用类方法)**
**当和类和对象没多大关系的时候,可以使用静态方法**
**静态方法和类方法  均不能访问  实例变量**


**类中赋值没有意义的。**
```
class Student():
    name = 'weilai'
    age = 0

    def __init__(self,name,age): 
        name = name   
        age = age
      
student1 = Student('wang',18)
print(student1.name)   #weilai
print(student1.age)    #0
print(student1.__dict__)    #{}   #__dict__显示student1下所有的变量，即没有变量
# python  会先在  实列变量上寻找 ，寻找不到就会到类变量里寻找，（然后再到父类里寻找）
# 所以即使student1为空，也显示了类变量下的值
#公开的 public    私有的（外部不能访问）private  在方法或变量前加__ 表示私有的
#__init__ 构造函数是python特有的，可以从外部访问
#print(student1._Student__sorce)    表明python中私有只是改了一个名字
```
