
---
title: 爬虫整理（一）使用re和urllib
date: 2018-12-25 11:05:31
tags:
categories: python练习
---



### 完整代码
```
from urllib.request import urlopen


html = urlopen(
    "https://morvanzhou.github.io/static/scraping/basic-structure.html").read(
        
    ).decode('utf-8')
print(html)


import re
res = re.findall(r"<title>(.+?)</title>", html)
print("\nPage title is: ", res[0])


res = re.findall(r"<p>(.*?)</p>", html, flags=re.DOTALL) 
print("\nPage paragraph is: ", res[0])


res = re.findall(r'href="(.*?)"', html)
print("\nAll links: ", res)
```
## 正文
### 使用re和urllib
```
from urllib.request import urlopen
# if has Chinese, apply decode()
html = urlopen(
    "https://morvanzhou.github.io/static/scraping/basic-structure.html"
).read().decode('utf-8')  
print(html) # 打开，读取，转换可显示中文，最后打印出来
```
**结果显示**
![print(html)](https://upload-images.jianshu.io/upload_images/14597179-3fc7bec17b3ab982.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
#### 接下来，使用re筛选数据
```
import re
res = re.findall(r"<title>(.+?)</title>", html) 
print(res)  # ['Scraping tutorial 1 | 莫烦Python'] # 列表
print(res[0]) # Scraping tutorial 1 | 莫烦Python
res = re.findall(r"<p>(.*?)</p>", html)
print(res)  # []

res = re.findall(r"<p>(.*?)</p>", html, flags=re.DOTALL) 
# re.DOTALL if multi line
prnt(res)
print(res[0]) 
```
![以上五个的print数据](https://upload-images.jianshu.io/upload_images/14597179-c0284891771dc42d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

```
res = re.findall(r'href="(.*?)"', html)
print("\nAll links: ", res)
```
![筛选链接](https://upload-images.jianshu.io/upload_images/14597179-3141c3afe0a3e428.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

