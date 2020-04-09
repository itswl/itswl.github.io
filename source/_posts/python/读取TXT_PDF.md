
---
title: 读取TXT_PDF
date: 2018-12-25 11:26:55
tags:
categories: python练习
---

这个是我学习爬取TXT和PDF的代码，前半段是读取TXT，后半段是读取PDF，PDF中使用了第三方库，pdfminer3k,使用pip安装即可。
`pip install pdfminer3k`。PDF其中注释掉的为读取网络上的PDF文档。
代码如下：

```
from urllib import request

from pdfminer.pdfdevice import PDFDevice
from pdfminer.pdfinterp import PDFPageInterpreter, PDFResourceManager
from pdfminer.pdfparser import PDFDocument, PDFParser
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams


# html = request.urlopen(
# 'https://en.wikipedia.org/robots.txt'
# ).read().decode('utf-8')
# print(html)   # 读取txt


# fp = open('./practice/byte-of-python-chinese-edition.pdf','rb')  # 获取文档对象
fp = request.urlopen('https://q.stock.sohu.com/newpdf/201831703172.pdf')  # 读取网络pdf
parser = PDFParser(fp)   # 创建一个与文档关联的解释器
doc = PDFDocument() # 文档对象

# 链接解释器和文档对象
parser.set_document(doc)
doc.set_parser(parser)

# 初始化文档
doc.initialize()   # 可接收文档密码

resource = PDFResourceManager()  # 创建PDF资源管理器

laparam = LAParams()   # 参数分析器

device = PDFPageAggregator(resource,laparams=laparam)
# 创建一个聚合器

interpreter = PDFPageInterpreter(resource,device)
# 创建 PDF页面解释器

# 使用文档对象得到页面的集合
for page in doc.get_pages():
    # 使用页面解释器来读取
    interpreter.process_page(page)

    # 使用聚合器来获取内容
    layout = device.get_result()

    for out in layout:
        if hasattr(out,'get_text'):   # 有没有这个属性
            print(out.get_text())


```
