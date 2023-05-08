# _*_coding :utf-8 _*_
# @Time :2022/9/11 15:17
# @File : Django操作数据库
# @Project : python_Django


"""
一、Django 的ORM 模型
    简介ORM(Object Relational Mapping),对象关系映射
    ORM封装 Python代码 执行SQL语句 操作数据库
    优势: 不用直接编写SQL代码，只需要像操作 对象一样 从数据库操作数据。

    Django模型映射关系:
    模型类====》数据表
    类属性====》表的字段名

    注意:
    1.模型类必须都写在项目app 下的models.py 文件下。
    2.模型如果需要映射到数据库，其所在的app 必须被安装
    (即 在settings.py文件中 INSTALLED_APP列表中 注册)
    3.一个数据表 对应 一个模型类，表中的字段，对应 模型中的类属性


二、数据库的链接配置、模型的创建与映射
    1.在 settings.py 文件 中配置数据库信息
    DATABASES = {
        'default': {     # 如果没有指定 数据库，默认使用 该数据库
                'ENGINE': 'django.db.backends.mysql',   # 数据库引擎
                # 登录数据库
                'USER': 'admin',                        # 用户名
                'PASSWORD': 'qwe123',                   # 密码
                'NAME': 'MY_Django001',                 # 数据库名
                'HOST': '192.168.0.198',                # IP地址
                'PORT': 3306,                           # 端口
        },

        'db2': {
        'ENGINE': 'django.db.backends.mysql',   # 数据库引擎
        # 登录数据库
        'USER': 'admin',                        # 用户名
        'PASSWORD': 'qwe123',                   # 密码
        'NAME': 'Myblog',                 # 数据库名
        'HOST': '192.168.0.198',                # IP地址
        'PORT': 3306,                           # 端口
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        }  # mysql使用严格模式，不指定会有警告信息
    },
    }

    注意: 如果需要 每个 模块配一个数据库，
        ① 则要在setting.py 中配置 数据库路由表
        # test_django为项目名，database_router为路由文件名，DatabaseAppsRouter为路由中创建的类名
        DATABASE_ROUTERS = ['django_project01.database_router.DatabaseAppsRouter']
        # 设置 数据库路由表
        DATABASE_APPS_MAPPING = {
            'myblog': 'db2',
            'Online_Course': 'db3'
        }

        ② 还要 在项目的主目录下 新建 py文件
        # 自动配置 数据库路由表，
        # app 应用会根据指定的路由 来选择 对应数据库 保存数据
        # (而不是 使用默认的 数据库)
        from django.conf import settings

        DATABASE_MAPPING = settings.DATABASE_APPS_MAPPING  # 在setting中定义的路由表


        class DatabaseAppsRouter(object):
            def db_for_read(self, model, **hints):
                if model._meta.app_label in DATABASE_MAPPING:
                    return DATABASE_MAPPING[model._meta.app_label]
                return None

            def db_for_write(self, model, **hints):

                if model._meta.app_label in DATABASE_MAPPING:
                    return DATABASE_MAPPING[model._meta.app_label]
                return None

            def allow_relation(self, obj1, obj2, **hints):

                db_obj1 = DATABASE_MAPPING.get(obj1._meta.app_label)
                db_obj2 = DATABASE_MAPPING.get(obj2._meta.app_label)
                if db_obj1 and db_obj2:
                    if db_obj1 == db_obj2:
                        return True
                    else:
                        return False
                return None

            def allow_syncdb(self, db, model):

                if db in DATABASE_MAPPING.values():
                    return DATABASE_MAPPING.get(model._meta.app_label) == db
                elif model._meta.app_label in DATABASE_MAPPING:
                    return False
                return None

            def allow_migrate(self, db, app_label, model_name=None, **hints):
                if db in DATABASE_MAPPING.values():
                    return DATABASE_MAPPING.get(app_label) == db
                elif app_label in DATABASE_MAPPING:
                    return False
                return None



    2.在 Django虚拟环境下 下载 pymysql 模块
    3.在主目录下的 __init__.py文件添加下面
    两行代码
    import pymysql
    pymysql.install_as_MySQLdb()

    4.在新建的app 项目下 进入models.py文件

    # 创建模型类， 模型类 对应表(即 创建表)
    class User(models.Model):
        id = models.AutoField(primary_key=True)     # 创建id字段，并赋予主键约束
        name = models.CharField(max_length=50)      # .....
        age = models.IntegerField()
        # 如果 新增字段 必须要用默认值
        gender = models.CharField(max_length=2, default='男')

        def __str__(self):  # 使用查询方法时，数据的展示方法
            return 'User<id=%s,name=%s,age=%s>' % (self.id, self.name, self.age)


    5.将模型类(数据表) 映射 到数据库
        ① 创建 映射文件
        python manage.py makemigrations db_001
        ② 将映射文件中的 映射数据 提交 到数据库
        python manage.py migrate db_001
        **(也可以 指定对应的数据库 python manage.py migrate myblog --database=db2)

    6.如果有新增字段 gender 直接去修改 models.py文件
    在 对应 模型类下 增加字段，必须要有默认值，
    然后使用 "将模型类映射到数据库" 的第二行命令
    python manage.py migrate db_001。

    注意:
    这里删除数据表，不能在 linux上 直接操作(因为 Django 是通过 映射文件 创建数据表的，
    直接删除表，启动Django服务时，映射文件无法 映射 到 该表，报错)，
    方法:
    可以 再对应 模块下的 models.py 文件 注释 对应的 模型类(其 对应数据表)，
    然后通过 '将模型类 映射到数据库' 的两行命令
    python manage.py makemigrations db_001、
    python manage.py migrate db_001,
    使用 映射文件生效, 最后 删除 数据表 。


三、数据的增删改查
在 该模块 目录下 的视图文件中 编写 操作数据库的代码

# 在视图文件中 导入模型文件中的 模型类(数据表，要操作哪张表 ，就导入哪个模型类)
from .models import User, FieldTest

# 向数据表中 添加 数据
def add(request):

    # 方法一
    # moran = User(name='moran', age=18, city='长沙')
    # moran.save()    # 保存

    # 方法二
    # wufake = User()
    # wufake.name = 'wufake'
    # wufake.age = 24
    # wufake.city = '贵阳'
    # wufake.gender = '男'
    # wufake.save()

    # 方法三，自动保存
    # User.objects.create(name='孙悟空', age=20, city='花果山', gender='男')

    # 方法四，不会 增加 重复数据
    User.objects.get_or_create(name='孙悟空', age=20, city='花果山', gender='男')
    User.objects.get_or_create(name='猪八戒', age=33, city='高老庄', gender='男')
    return HttpResponse('数据保存成功！！')



# 查找数据
def select(request):
    # all() 返回 所有数据，以列表方式 保存
    # result = User.objects.all()
    # result = [[i.id, i.name, i.age, i.gender] for i in result]

    # filter() 条件查询
    # result = User.objects.filter(name='moran')
    # result = [[i.id, i.name, i.age, i.gender] for i in result]
    # 名字包含 ‘孙’的
    result = User.objects.filter(name__contains='孙').values()
    # name__startswith = '孙'，匹配以'孙'开头
    # name__endswith = '孙'，匹配以'孙'结尾

    # get()  只能查询唯一的 一个(id字段)，如果 多个重复报错
    # result = User.objects.get(id=2)

    # 查询第一条
    # result = User.objects.first()
    # result = [[result.id, result.name, result.age, result.gender]]

    # 排除查询
    # result = User.objects.exclude(name='猪八戒')

    # 排序查询
    # result = User.objects.order_by('age')
    # result = User.objects.order_by('-age')  # 逆序排列
    # result = [[i.id, i.name, i.age, i.gender] for i in result]

    # 数值范围查询
    # result = User.objects.filter(age__gte=19)   # 大于等于 19岁
    # result = User.objects.filter(age__in=[18, 20])   # 等于18,20岁的

    # ##查询完并以 字典形式 返回数据, values方法
    # result = User.objects.filter(age__range=(20, 30)).values()   # 在 25~30岁

    # result = [[i.id, i.name, i.age, i.gender] for i in result]
    return HttpResponse(result)


# 修改数据
    def update(request):
        # 方法一，先查询，在修改
        # result = User.objects.last()
        # result.name = '沙和尚'
        # result.save()

        # 方法二
        User.objects.filter(id=1).update(name='成龙')

        return HttpResponse('数据修改成功')


# 删除数据
    def delete(request):
        # 先查找获取数据，再删除
        User.objects.get(id=1).delete()

        return HttpResponse('删除成功')











"""


































