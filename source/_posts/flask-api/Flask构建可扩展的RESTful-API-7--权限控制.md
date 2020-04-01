
---
title: Flask构建可扩展的RESTful-API-7--权限控制
date: 2018-12-18 18:36:16
tags:
categories: flask-api
---


# 7.1 删除模型的注意事项

1.204 的HTTP状态码代表的是NO CONTENT，无内容。所以如果状态码是204，那么无论返回什么，前端都接受不到，但是我们要尽量返回格式化的信息，让前端能够判断，为此，我们可以使用状态码202，并且添加一个特殊的error_code=-1 来代表删除操作

2.由于我们的删除是逻辑删除，使用get的方法会一直可以查询出当前用户，这里我们应该使用filter_by()，传入status=1，好在，我们之前已经在基类重写了filter_by()，所以我们只需要调用filter_by()传入id即可
app\api\v1\user.py
```
@api.route('/<int:uid>', methods = ['DELETE']) 
@auth.login_required
def delete_user(uid):
    with db.auto_commit():
        # user = User.query.get_or_404(uid)   #软删除后，用get 还是能查询到，所以改写
        user = User.query.filter_by(id=uid).first_or_404()
        user.delete()     #  软删除
    # return 'delete sucess'
    return DeleteSuccess()

```
app\libs\erro_code.py
```
class DeleteSuccess(Success):
    code = 202
    error_code = 1
```
3.防止超权现象 id=1的用户，不能删除id=2的用户，为了解决这个问题，我们的uid不能由用户传入，而是应该从他传入的token中取出来。由于我们之前做token验证的时候，已经把取出来的信息存入到了flask的g中，所以我们只需要从g中取出来做判断即可
```
@api.route('', methods = ['DELETE'])   
@auth.login_required
def delete_user():
    uid = g.user.uid   #  防止超权，从token中读取  已存储在 g 变量中 ，g 变量线程隔离。
                    # 对于管理员来说，可以超权，删除别的用户

    with db.auto_commit():

        # user = User.query.get_or_404(uid)   #软删除后，用get 还是能查询到，所以改写
        user = User.query.filter_by(id=uid).first_or_404()
        user.delete()     #  软删除
    # return 'delete sucess'
    return DeleteSuccess()
```
> 两个知识点
1.g.user.uid之所以可以这样用.的方式获取uid，是因为我们在向g中存储user的时候，使用的是namedtuple，而不是dict，不然我们就只能g.user['uid']这样获取了  
> 2.即使两个用户同时访问这个接口，我们也不会出错，g会正确的指向每一个请求的user，这是因为g是线程隔离的

4.我们是需要一个超级管理员用户的试图函数super_delete_user，可以通过传入uid来删除指定用户的。但是对这两个接口，普通用户应该只能访问delete_user，而超级管理员都能够访问。

首先我们需要创建一个管理员用户，不过管理员用户不能通过公开API来创建，而应该直接在数据库里创建，但是这又涉及到一个问题，就是直接在数据库里创建，密码不好生成。所以最好的方式是创建一个离线脚本文件.也可以普通注册，改auth为2
```
from app import create_app
from app.models.base import db
from app.models.user import User

app = create_app()
with app.app_context():
    with db.auto_commit():
        # 离线脚本，创建一个超级管理员
        user = User()
        user.nickname = 'Super'
        user.password = '123456'
        user.email = '999@qq.com'
        user.auth = 2
        db.session.add(user)

# 直接运行就能创建
```
这个脚本不仅仅可以生成管理员，还可以使用它生成大量的假数据，测试数据




# 7.2 权限管理方案

通过之前的分析，我们可以发现，我们之前的get_user，实际上应该是super_get_user，而我们应该在多添加一个get_user作为普通用户的获取方法
```
@api.route('/<int:uid>', methods=['GET'])
@auth.login_required
def super_get_user(uid):
    user = User.query.filter_by(id=uid).first_or_404(uid)
    return jsonify(user)

@api.route('', methods = ['GET'])   
@auth.login_required
def get_user():
    uid = g.user.uid 
    user = User.query.filter_by(id=uid).first_or_404()
    return jsonify(user)
```
### 1.不太好的权限管理方案

我们只要可以在视图函数中获取到用户的权限，就可以根据权限来判断，用户的身份，来做出不同的控制。

要做到这一点，我们只需要在生成令牌的时候，将is_admin的字段写入到token中。然后再视图函数中取出这个字段来进行不同的判断就好了。

这样的方案有两个缺点： 1.代码太啰嗦了，每个视图函数都需要做这样的判断。 2.我们把全新想的太简单了，我们这个项目只有管理员和普通用户两种，但是真正的权限应该有各种分组，每个分组每个用户都有不同的权限，如果这样，再在视图函数里进行控制基本上是不可能

### 2.比较好的权限管理方案

假如说我们在代码里做三张表（Mysql，Redis，配置文件），每一张表都记录着某一种权限，现在假如某一个请求过来了。当用户访问@auto.login的接口的话，他必须要带有一个token令牌中的，而我们是可以从token中读取到当前的权限种类的，并且我们是可以知道他所访问的接口的。我们可以拿权限种类和接口做匹配，然后来做判断。 这样做还有一个很好的优势，是我们可以在进入方法前进行权限判断，如果不能够访问根本就不会进入该方法。

![image](http://upload-images.jianshu.io/upload_images/14597179-c5171f4d51fe6475?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240) 





# 7.3 Scope权限管理的实现

## 遇到的坑
用的之前生成的token，当时token并没有写入scope,所以报错重新生成就好了。

### 1.编码实现

根据上一小节的编写，我们来动手编写权限管理方案

#### 1.1 scope配置

app/libs/scope.py
```
class AdminScope:
    allow_api = ['v1.super_get_user']  # 因为是注册在Blueprint上，所以endpoint 前缀为 v1 

class UserScope:
    allow_api = ['v1.get_user']

    # 判断当前访问的endpoint是否在scope中
def is_in_scope(scope, endpoint):
    # 反射获取类
    scope = globals()[scope]()  # globals使用类的名字动态创建对象
    if endpoint in scope.allow_api:
        return True
    else:
        return False
```
#### 1.2 生成令牌

app/models/user.py
```
    @staticmethod
    def verify(email, password):
        user = User.query.filter_by(email=email).first_or_404()   # 查询出当前用户
        if not user.check_password(password):  # 检验密码
            raise AuthFailed()   #抛出异常
        scope = 'AdminScope' if user.auth == 2 else 'UserScope'  # 判断用户作用域，假设只有两个作用域
        return {'uid': user.id,'scope': scope}  #成功，返回uid   # 返回scope
```
app/api/v1/token.py
```
from app.libs.redprint import Redprint

from flask import current_app
from app.libs.enums import ClientTypeEnum
from app.models.user import User
from app.validators.forms import ClientForm
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

from flask import jsonify


api = Redprint('token') # 实例化一个Redprint

@api.route('', methods=['POST'])  # 路由注册
# 返回token的试图函数，这里稍微破坏一下REST的规则，由于登录操作密码安全性较高，使用GET的话会泄漏
def get_token():
    form = ClientForm().validate_for_api()   # 同注册过程，不同client 区分
    promise = {
        ClientTypeEnum.USER_EMAIL: User.verify,  #验证 # 在 user中编写 verify
        # ClientTypeEnum.USER_MINA: __register_user_by_MINA 
    }
    # 拿到用户信息
    identity = promise[form.type.data](
        form.account.data,
        form.secret.data
    )

    # 调用函数生成token
    expiration = current_app.config['TOKEN_EXPIRATION']  #过期时间
    token = generator_auth_token(identity['uid'],
                                form.type.data,
                                identity['scope'],
                                expiration=expiration)
    t = {
            'token': token.decode('ascii')  # 因为是byte
        }
    return jsonify(t), 201  # 返回 json 字典

def generator_auth_token(uid, ac_type, scope=None,expiration=7200):
    """生成令牌  ，拿到uid,client类型，权限作用域，过期时间"""
    s = Serializer(current_app.config['SECRET_KEY'],expires_in=expiration)  # expires_in 生成令牌的有效期
    return s.dumps({
                    'uid': uid,
                    'type': ac_type.value,
                    'scope': scope
                })  # 将想写入的信息以字典形式写入令牌
```
#### 1.3 验证令牌
```
# 编写一个验证token的装饰器

from flask_httpauth import HTTPBasicAuth

from flask import current_app, g, request
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, BadSignature, \
          SignatureExpired

from collections import namedtuple

from app.libs.erro_code import AuthFailed, Forbidden
from app.libs.scope import is_in_scope

auth = HTTPBasicAuth()

User = namedtuple('User', ['uid', 'ac_type', 'scope'])

# @auth.verify_password
# def verify_password(account, password):

#   # 需要在HTTP请求的头部设置一个固定的键值对
#   # key=Authorization,value=basic base64(account:psd)
#   #    imwl@live.com:12345678   编码后 aW13bEBsaXZlLmNvbToxMjM0NTY3OA==
#   #  key=Authorization,value=basic aW13bEBsaXZlLmNvbToxMjM0NTY3OA==
#     return True

@auth.verify_password
def verify_password(token, password):
    user_info =  verify_auth_token(token) # token 赋值给 user_info
    if not user_info:
        return False
    else:
        g.user = user_info  # g 变量 ,代理模式
        return True


def verify_auth_token(token):
    s = Serializer(current_app.config['SECRET_KEY'])
    try:
        data = s.loads(token)   # 解密 token
    # token不合法抛出的异常
    except BadSignature:
        raise AuthFailed(msg='token is valid', erro_code=1002)
    # token过期抛出的异常
    except SignatureExpired:
        raise AuthFailed(msg='token is expired', erro_code=1003)

    uid = data['uid']
    ac_type = data['type']   # 生成令牌的时候写入了 uid ac_type
    scope = data['scope']
    # 也可在这拿到当前request的视图函数
    allow = is_in_scope(scope ,request.endpoint) # request.endpoint  拿到当前视图函数的endpoint 判断是否有权限。
    if not allow:
        raise Forbidden()
    return User(uid, ac_type, scope)   # 定义对象式 接口返回回去 ,scope 先返回为空字符串

```




# 7.4 Scope优化

#### 1.支持权限相加

假如我们的UserScope的权限是A，B，C。而AdminScope的权限是A，B，C，D。按照我们的写法，我们的A，B，C就需要些两遍。况且这只是一个简单的例子，实际情况下会更复杂。所以我们需要实现一种方法，可以让AdminScope的allow_api可以和UserScope的allow_api相加得到新的allow_api。

```
class UserScope:
    allow_api = ['v1.A','v1.B']

class SuperScope:    # 相加操作
    allow_api = ['v1.C','v1.D']

    def __init__(self):
        self.add(UserScope())
# 这个方法可以将其他的Scope合并到当前Scope。省去重复代码的编写
    def add(self, other):
        self.allow_api = self.allow_api + other.allow_api

```
#### 2.支持权限链式相加

现在我们只能讲AdminScope和UserScope的权限相加，如果还想再加上其他的Scope，就需要链式的操作
```
class AdminScope:
    allow_api = ['v1.super_get_user']  # 因为是注册在Blueprint上，所以endpoint 前缀为 v1 

class UserScope:
    allow_api = ['v1.A','v1.B']

class SuperScope:    # 相加操作
    allow_api = ['v1.C','v1.D']

    def __init__(self):
        self.add(UserScope()).add(AdminScope())
        

    def add(self, other):
        self.allow_api = self.allow_api + other.allow_api
        return self  # 将self return不然第二段调用为None.add(),报错
```
#### 3.所有子类支持相加

add方法不应该写在具体的Scope类中，因为这样就只有当前Scope类有该功能了。应该将add方法写在基类Scope中
```
class Scope:
    allow_api = []

    def add(self, other):
        self.allow_api = self.allow_api + other.allow_api
        return self


class AdminScope(Scope):
    allow_api = ['v1.super_get_user']  # 因为是注册在Blueprint上，所以endpoint 前缀为 v1 
    def __init__(self):
        self.add(UserScope())


class UserScope(Scope):
    allow_api = ['v1.A','v1.B']


class SuperScope(Scope):    # 相加操作
    allow_api = ['v1.C','v1.D']

    def __init__(self):
        self.add(UserScope()).add(AdminScope())
        
#  重复问题，得去重SuperScope为['v1.C', 'v1.D', 'v1.A', 'v1.B', 'v1.super_get_user', 'v1.A', 'v1.B']
#  要是能直接相加就好了      self + UserScope() + AdminScope()

```
#### 4.运算符重载

现在我们一直使用add()方法，太啰嗦了，我们可以修改我们的代码，使得我们可以使用+号来完成add()方法的功能。 要完成这个功能，就要使用到运算符重载的技术
```
class Scope:
    allow_api = []
    # def add(self, other):
# 运算符重载，支持对象相加操作
    def __add__(self, other):
        self.allow_api = self.allow_api + other.allow_api
        return self


class AdminScope(Scope):
    allow_api = ['v1.super_get_user']  # 因为是注册在Blueprint上，所以endpoint 前缀为 v1 
    def __init__(self):
        self + UserScope()


class UserScope(Scope):
    allow_api = ['v1.A','v1.B']


class SuperScope(Scope):    # 相加操作
    allow_api = ['v1.C','v1.D']

    def __init__(self):
        self + UserScope() + AdminScope()
```
#### 5.去重

我们现在的scope，编写完成之后，由于可能会连续相加，会有很多重复的试图函数，如SuperScope()中会出现两次v1.A,现在我们就需要将这些重复的试图函数去除掉。我们只需要使用set这个数据结构，就可以完成。
```
class Scope:
    allow_api = []
    # def add(self, other):
# 运算符重载，支持对象相加操作
    def __add__(self, other):
        self.allow_api = self.allow_api + other.allow_api
        self.allow_api = list(set(self.allow_api)) # 先转化为set，后转为list 从而去重
        return self

```
也可以直接定义的时候，就定义成集合,例如：`allow_api = {'v1.C','v1.D'}`

以上全部代码
```
class Scope:
    allow_api = []
    # def add(self, other):
# 运算符重载，支持对象相加操作
    def __add__(self, other):
        self.allow_api = self.allow_api + other.allow_api
        self.allow_api = list(set(self.allow_api)) # 先转化为set，后转为list 从而去重
        return self


class AdminScope(Scope):
    allow_api = ['v1.super_get_user']  # 因为是注册在Blueprint上，所以endpoint 前缀为 v1 
    def __init__(self):
        self + UserScope()


class UserScope(Scope):
    allow_api = ['v1.A','v1.B']


class SuperScope(Scope):    # 相加操作
    allow_api = ['v1.C','v1.D']

    def __init__(self):
        self + UserScope() + AdminScope()

        
   # 判断当前访问的endpoint是否在scope中
def is_in_scope(scope, endpoint):
    # 反射获取类
    scope = globals()[scope]()  # globals使用类的名字动态创建对象
    if endpoint in scope.allow_api:
        return True
    else:
        return False
```

#### 6.模块级别的Scope

现在我们的Scope都是试图函数级别的，加入我们的user下面有100个试图函数，我们就需要把这100个全都加入进来，我们可以想办法，让我们的Scope支持可以添加一个模块下的视图函数。

我们可以添加一个变量，allow_moudle，来标示允许通过的模块。然后现在我们的is_in_scope只是简单的判断endpoint是否在scope.allow_api中，endpoint默认的形式是blueprint.view_func 的形式，我们可以自定义endpoint为blueprint.moudle_name+view_func这样的形式，这样我们我们就可以在is_in_scope进行模块的判断

修改红图的注册：
```
class Scope:
    allow_api = []
    allow_moudle = []
    # def add(self, other):
# 运算符重载，支持对象相加操作
    def __add__(self, other):
        self.allow_api = self.allow_api + other.allow_api
        self.allow_api = list(set(self.allow_api)) # 先转化为set，后转为list 从而去重
        return self


class AdminScope(Scope):
    allow_api = ['v1.super_get_user']  # 因为是注册在Blueprint上，所以endpoint 前缀为 v1 
    def __init__(self):
        self + UserScope()


class UserScope(Scope):
    allow_api = ['v1.A','v1.B']


class SuperScope(Scope):    # 相加操作
    allow_api = ['v1.C','v1.D']
    allow_moudle = ['v1.user']

    def __init__(self):
        self + UserScope() + AdminScope()



        

    # def add(self, other):
    #     self.allow_api = self.allow_api + other.allow_api
    #     return self  # 将self return不然第二段调用为None.add(),报错
# 提取到基类中，每个都继承这个基类



    # 判断当前访问的endpoint是否在scope中
def is_in_scope(scope, endpoint):
    # 反射获取类
    scope = globals()[scope]()  # globals使用类的名字动态创建对象
    splits = endpoint.split('+')
    red_name = splits[0]
    if endpoint in scope.allow_api:
        return True
    # v1.view_func  改为v1.moudle_name+view_func  # 改写endpoint
    # 从Redprint 入手  v1.red_name +view_func
    '''
    从   endpoint = options.pop("endpoint", f.__name__)
    改为 endpoint = self.name + '+' + options.pop("endpoint", f.__name__) # 改成Redprint+视图函数名字
            '''
    if red_name in scope.allow_moudle:
        return True
    else:
        return False
```
```
class Scope:
    allow_api = []
    allow_moudle = []
    # def add(self, other):
# 运算符重载，支持对象相加操作
    def __add__(self, other):
        self.allow_api = self.allow_api + other.allow_api
        self.allow_api = list(set(self.allow_api)) # 先转化为set，后转为list 从而去重

        self.allow_moudle = self.allow_moudle + other.allow_moudle
        self.allow_moudle = list(set(self.allow_moudle))   # 模块级别的相加操作
        return self


class AdminScope(Scope):
    allow_api = ['v1.user+super_get_user','v1.user+super_delete_user']  # 因为是注册在Blueprint上，所以endpoint 前缀为 v1 
    
    # allow_moudle = ['v1.user']
    def __init__(self):
        self + UserScope()


class UserScope(Scope):
    allow_api = ['v1.user+get_user','v1.user+delete_user']


# class SuperScope(Scope):    # 相加操作
#     allow_api = ['v1.C','v1.D']
#     allow_moudle = ['v1.user']

#     def __init__(self):
#         self + UserScope() + AdminScope()



        

    # def add(self, other):
    #     self.allow_api = self.allow_api + other.allow_api
    #     return self  # 将self return不然第二段调用为None.add(),报错
# 提取到基类中，每个都继承这个基类



    # 判断当前访问的endpoint是否在scope中
def is_in_scope(scope, endpoint):
    # 反射获取类
    scope = globals()[scope]()  # globals使用类的名字动态创建对象
    splits = endpoint.split('+')
    red_name = splits[0]
    if endpoint in scope.allow_api:
        return True
    # v1.view_func  改为v1.moudle_name+view_func  # 改写endpoint
    # 从Redprint 入手  v1.red_name +view_func
    '''
    从   endpoint = options.pop("endpoint", f.__name__)
    改为 endpoint = self.name + '+' + options.pop("endpoint", f.__name__) # 改成Redprint+视图函数名字
            '''
    if red_name in scope.allow_moudle:
        return True
    else:
        return False
```
**模块级别的权限控制一定得特别注意**
#### 7.支持排除

如果一个模块又100个视图函数，UserScope需要访问98个，AdminScope需要访问所有，那么UserScope的编写就太麻烦了，我们可以让我们的Scope 支持排除操作，这样UserScope就可以添加AdminScope的全部，然后再排除掉他不能访问的两个就好了
```

class Scope:
    allow_api = []
    allow_moudle = []
    forbidden = []
    # def add(self, other):
# 运算符重载，支持对象相加操作
    def __add__(self, other):
        self.allow_api = self.allow_api + other.allow_api
        self.allow_api = list(set(self.allow_api)) # 先转化为set，后转为list 从而去重

        self.allow_moudle = self.allow_moudle + other.allow_moudle
        self.allow_moudle = list(set(self.allow_moudle))   # 模块级别的相加操作

        self.forbidden = self.forbidden + other.forbidden
        self.forbidden = list(set(self.forbidden)) 
        return self


class AdminScope(Scope):
    # allow_api = ['v1.user+super_get_user','v1.user+super_delete_user']  # 因为是注册在Blueprint上，所以endpoint 前缀为 v1 
    
    allow_moudle = ['v1.user']
    # def __init__(self):
    #     self + UserScope()


class UserScope(Scope):
    forbidden =  ['v1.user+super_get_user','v1.user+super_delete_user']
    # allow_api = ['v1.user+get_user','v1.user+delete_user']
    def __init__(self):
        self + AdminScope()




# class SuperScope(Scope):    # 相加操作
#     allow_api = ['v1.C','v1.D']
#     allow_moudle = ['v1.user']

#     def __init__(self):
#         self + UserScope() + AdminScope()



        

    # def add(self, other):
    #     self.allow_api = self.allow_api + other.allow_api
    #     return self  # 将self return不然第二段调用为None.add(),报错
# 提取到基类中，每个都继承这个基类



    # 判断当前访问的endpoint是否在scope中
def is_in_scope(scope, endpoint):
    # 反射获取类
    scope = globals()[scope]()  # globals使用类的名字动态创建对象
    splits = endpoint.split('+')
    red_name = splits[0]
    if endpoint in scope.forbidden:   # 排除
        return False

    if endpoint in scope.allow_api:
        return True
    # v1.view_func  改为v1.moudle_name+view_func  # 改写endpoint
    # 从Redprint 入手  v1.red_name +view_func
    '''
    从   endpoint = options.pop("endpoint", f.__name__)
    改为 endpoint = self.name + '+' + options.pop("endpoint", f.__name__) # 改成Redprint+视图函数名字
            '''
    if red_name in scope.allow_moudle:
        return True
    else:
        return False
# 首先判断是否在要排除的列表里

```
