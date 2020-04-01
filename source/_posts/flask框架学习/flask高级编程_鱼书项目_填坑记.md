
---
title: flask高级编程_鱼书项目_填坑记
date: 2018-11-14 23:07:07
tags:
categories: flask
---

详细过程可以去我的个人博客上查看，另有flask构建可扩展restful-api过程.
[个人博客](https://itswl.github.io)，gitbook 下

## 本文主要是记录我在鱼书项目遇到的问题
很多bug都是因为一点小小的原因导致的，所以以后还得仔细。

### 1. 数据库表不能添加数据
#### 产生场景
localhost:2333/register 注册用户信息，提交后出现如下提示:

![错误提示](https://upload-images.jianshu.io/upload_images/14597179-1528e2b9e557b92f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

#### 产生原因
![](https://upload-images.jianshu.io/upload_images/14597179-718df0c5743d901f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
自己粗心，之前已经有添加_password,后来又在末尾加了_password,导致数据表生成不了password,所以在/register 注册后，出现bug。

#### 解决过程
在数据库user表中查询不到password字段，于是到model/user.py中查看到自己多写了一遍_password 代码，删除后成功。

### 2. 搜索isbn成功，搜索关键字时失败
![搜索关键字](https://upload-images.jianshu.io/upload_images/14597179-2b3d3a0dab7cc02b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![搜索isbn](https://upload-images.jianshu.io/upload_images/14597179-3f28623f8aa5351a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

#### 产生原因
![/book/search/](https://upload-images.jianshu.io/upload_images/14597179-d1f859099f3fc488.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
restful 格式 为 `search?q= xxx`,重构代码后。route修改有问题。

#### 解决过程
![/book/search](https://upload-images.jianshu.io/upload_images/14597179-58d225465cbbc2a0.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
修改后正常，还是得细心。
**注意事项**
chrome 浏览器有缓存，修改后，即使网址 为 `.../book/search?q=xxx`,也会跳转成` .../book/searc/q=xxx`导致出错，清空一下浏览数据就可以了。

### 3. 路由问题
#### 产生场景
注册后，重定向产生Bug
![错误提示](https://upload-images.jianshu.io/upload_images/14597179-82cceb823e1c0a8a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
#### 产生原因
flask_login 中的重定向格式为web.login，这一段可能是我输入有误吧。直接给出了解决方案。
#### 解决过程
![](https://upload-images.jianshu.io/upload_images/14597179-b2c8fbaea6278e9e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

将web/login 更改为web.login

### 4. 有关于前端的问题

因为最初 的时候，有一段前端代码得注释，当时不熟悉这一块，我还是按照python 中的方法，在前面加`#`号处理的，结果有问题，后来才发现不应该这样做。很久以前的问题了，当时也没保存，所以没有具体图片。当时的解决方案是把那些要注释掉的前端代码全部删除掉了。

### 5. flask调试
调试端口号默认为5000。
`localhost:5000`，之前没仔细查看，一直在生产模式下调试，还一直进不了断点0.0

### 6. 新增个人中心

![](https://upload-images.jianshu.io/upload_images/14597179-2729a25d4234a7e5.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

代码如下
```
@web.route('/personal')
def personal_center():
    cur_user = User.query.get_or_404(current_user.id)  
# 从数据库中查询出当前用户数据
    user = cur_user.summary  
 # summary返回一个自定义的字典，详情在user模型下
    # b = a.summary
    return render_template('personal.html', user=user)  # 网页模板下

```
![summray](https://upload-images.jianshu.io/upload_images/14597179-7b7877d24f287d9a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![前端代码](https://upload-images.jianshu.io/upload_images/14597179-2ce000dcf082291d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


因为 user 是一个字典形式，从而得到数据。

### 7. 新增修改密码
之前没有看前端代码，所以password字段有问题，更改后，成功
```
@web.route('/change/password', methods=['GET', 'POST'])
@login_required 
def change_password():
    form = ChangePasswordForm(request.form)

    if request.method == 'POST' and form.validate():
        if current_user.check_password(form.old_password.data):
            current_user.change_password(form.password1.data)
            flash('您的密码已重置，请使用新密码登录')
            return redirect(url_for('web.login'))
        flash('密码更改失败')
    return render_template('auth/change_password.html')
```
![前端代码](https://upload-images.jianshu.io/upload_images/14597179-0b0796b6c1bb8427.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
把 前端代码中的原密码改成old_password,新密码，确认新密码改为password1,password2 就可以了。
暴露的问题，对前端这一块不熟。

###8 . 新增API搜索的图书保存的mysql中
最初使用的如下方式，一点都不优雅，后更改
```
    @classmethod
    def insert_into_sql(cls, books):
        for b in books:    # 优化后如上
            with db.auto_commit():
                try:
                    if Book.query.filter_by(isbn=b.isbn).first():
                        continue
                    book = Book()
                    book.title = b.title
                    book.author = b.author
                    book.binding =b.binding
                    book.publisher = b.publisher
                    book.price = b.price
                    book.pages = b.pages
                    book.isbn = b.isbn
                    book.summary = b.summary
                    book.image = b.image
                    db.session.add(book)
                except sqlalchemy.exc.DataError:
                    pass
```
如下：
```
    @classmethod
    def insert_into_sql(cls, books):
        # book model 写入
        import sqlalchemy
        for b in books: # books是一个列表，每个元素是一个Book实例化后的对象
            # print(111111111111, b.pages)
            if Book.query.filter_by(isbn=b.isbn).first():  # 因为重复的isbn不能添加
                        continue
            with db.auto_commit():
                book = Book()
                book.set_attrs(b.__dict__)  # [b1, b2, b3] 
                # 类实例化后的一个对象 b.author b.title
                db.session.add(book)
```
base模型的部分代码：
```
class Base(db.Model):
    __abstract__ = True
    create_time = Column('create_time',Integer)
    status = Column(SmallInteger, default=1)

    def __init__(self):
        self.create_time = int(datetime.now().timestamp())

    def set_attrs(self, attrs_dict):
        for key, value in attrs_dict.items():
            if hasattr(self, key) and key != 'id':
                setattr(self, key, value)
```

#### 详细解释
这一块，考虑的点特别多。因为从API拿来的数据，并不是很可靠。所以有一些数据为None,或者超出了长度，用以前的代码可能会报错
```
    def __init__(self, data):
        self.title = data['title']
        self.author = '、'.join(data['author'])
        self.binding = data['binding']
        self.publisher = data['publisher']
        self.image = data['image']
        # self.price = '￥' + data['price']  
# 因为价格可能为NONE,str不能和NONE相加，会报错。
# '￥'去掉，因为api中部分带货币单位
        self.price = data['price'] 

        self.isbn = data['isbn']
        self.pubdate = data['pubdate']

# summuy长度最多取1000.
        self.summary = data['summary'][:1000] if data['summary'] else ''
        self.pages = data['pages'].replace('页', '') if data['pages'] else None

    @property
    def intro(self):
        intros = filter(lambda x: True if x else False,
                        [self.author, self.publisher, self.price])
        return ' / '.join(intros)

```
以上是在view_modles 下book.py做的处理。要细心，多进行代码优化。



web/book.py部分代码
```
@web.route("/book/search")
def search():
    """
    搜索书籍路由
    """
    # 实例化我们自定义的SearchForm，需要传入一个字典作为要校验的参数
    form = SearchForm(request.args)
    # validate()方法返回True/False来标示是否校验通过
    books = BookCollection()
    # if not form.validate():
    #     # errors为错误信息提示（上面定义的message）
    #     flash("搜索的关键字不符合要求，请重新输入关键字")
    #     return render_template('search_result.html', books=books)
    # 从form中获取校验后的参数，不从request里拿，
#因为我们可能会对数据进行预处理或者默认值的给定
    q = form.q.data.strip()
    page = form.page.data
    isbn_or_key = is_isbn_or_key(q)
    yushu_book = YuShuBook()
    if form.validate():
        if isbn_or_key == 'isbn':
            yushu_book.search_by_isbn(q)
            books.fill(yushu_book,q)
            # print(11111, books.books)
            # for b in books.books:
            #     print('title', b.title)
            #     print('author', b.author)
        # result = YuShuBook.search_by_isbn(q)
        # result = BookViewModel.package_single(result,q) 
        else:
            yushu_book.search_by_key(q,page)        
        # result = YuShuBook.search_by_keyword(q,page)
        # result = BookViewModel.package_collection(result,q)
    # return jsonify(result)
            books.fill(yushu_book,q)
        Book.insert_into_sql(books.books)   # 搜索的信息保存到SQL中
    else:
        flash("搜索的关键字不符合要求，请重新输入关键字")

    # return jsonify(books)  
# TypeError: Object of type BookCollection is not JSON serializable
    # return json.dumps(books, default=lambda o: o.__dict__)
    return render_template('search_result.html', books=books)
```
