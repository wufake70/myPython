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
        'default': {
                'ENGINE': 'django.db.backends.mysql',   # 数据库引擎
                # 登录数据库
                'USER': 'admin',                        # 用户名
                'PASSWORD': 'qwe123',                   # 密码
                'NAME': 'MY_Django001',                 # 数据库名
                'HOST': '192.168.0.198',                # IP地址
                'PORT': 3306,                           # 端口
        }
    }

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


    5.将模型类映射到数据库
        ① 创建 映射文件
        python manage.py makemigrations db_001
        ② 将映射文件中的 映射数据 提交 到数据库
        python manage.py migrate db_001

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










"""


































