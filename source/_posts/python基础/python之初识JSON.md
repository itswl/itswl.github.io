---
title: (8) python之初识JSON
date: 2018-11-14 21:59:58
tags:
categories: python基础
---

**JSON是一种轻量级的数据交换格式**
**JSON 是一种数据格式**
**字符串是 JSON的表现形式**
**符合JSON格式的字符串叫做 JSON字符串**
json易于阅读，易于解析，网络传输效率高    跨语言交换数据
 json.loads()解码(反序列化),json.dumps()编码(序列化)
```
import json   #反序列化

json_str = '{"name":"weilai","age":18,"a":true}'     #JSON字符串格式，双引号
json_str1 = '[{"name":"weilai","age":18,"a":false},{"name":"weilai","age":18}]'

student = json.loads(json_str)      #将一个JSON编码的字符串转换回一个Python数据结构
student1 = json.loads(json_str1)     

print(type(student))  #字典格式  {'name': 'weilai', 'age': 18, 'a': True}
print(type(student1)) #列表形式  [{'name': 'weilai', 'age': 18, 'a': False}, {'name': 'weilai', 'age': 18}]

print(student)  
print(student1)
print(student['age']) 
print(student['name']) 
```

**序列化**
```
import json

student = [
            {'name': 'weilai', 'age': 18,'a': False},
            {'name': 'weilai', 'age': 18}
          ]

json_str = json.dumps(student)
print(type(json_str))  #<class 'str'>
print(json_str)        #[{"name": "weilai", "age": 18, "a": false}, {"name": "weilai", "age": 18}]
```
**JSON对象，json, json字符串**

**在python中没有JSON对象**

**json 是对ecmascript的一种实现  与Javascript相同**

**json 是一种中间数据类型，有自己的数据类型，与JavaScript相似**

**rest  服务的标准格式**
