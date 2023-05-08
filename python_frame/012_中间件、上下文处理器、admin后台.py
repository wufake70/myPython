# _*_coding :utf-8 _*_
# @Time :2022/9/21 8:20
# @File : 012_中间件、上下文处理器、admin后台
# @Project : python_Django


"""
一、中间件(mymiddleware)
    定义: 是一个轻量级、底层的 "插件"系统，
    可以介入 Django的请求 和 响应处理过程，
    修改Django的输入或输出。

    Django中的 中间件 就是一个类，在请求和结束后，
    Django会根据自己的规则在合适的时机执行 中间件中响应的方法。

    在Django项目中的 settings.py ，有一个MIDDLEWARE CLASSES变量，
    其中每一个元素就是一个中间件。

    使用 (内置)中间件:
    1.在项目的主目录下 创建一个 mymiddleware.py 文件
    2.mydiddleware.py中的代码
    from django.utils.deprecation import MiddlewareMixin  # 导入相关类，方便继承
    class MyException(MiddlewareMixin):
        # 发送请求 过程中，执行的中间件
        def process_request(self, request):
            # 获取请求的信息
            print(request.method)
            print(request.path)
            print(request.is_ajax())

            # 在执行中间件时 就返回响应，后面的 视图函数就没有执行的机会
            # return HttpResponse('请求错误')
            return None

    3.在settings.py中 MIDDLEWARE CLASSES 变量 注册 中间件
    'django_project01.mymiddleware.MyException'



二、上下文处理器(就是创建模板变量)
    引入: 在模板中 想要使用的变量 是 通过视图函数中的 context 这个上下文参数 传递进来的，
    每一个模板(html) 需要什么参数就传什么参数。
    但是 该参数 只能 供当前模板使用 ，对其他的模板不管用

    如何创建 上下文处理器:   (使得 登录的信息 在每一个页面 都可展示)
    1.在项目主目录文件下 创建 Context_Processor.py 文件

    2.在该py文件 创建一个函数，注意: 必须传入request参数，必须返回一个字典类型的对象
    def context_processor(request):
        user = request.session.get('username', '未登录')
        if user != '未登录':
            return {'user': user}

        else:
            return {}
            注意: 这里一定要返回空 字典，否则后面 登录 admin后台管理 时，
            会报错 AttributeError: 'str' object has no attribute 'pk'

    3.将其注册到 settings.py TEMPLATES变量 的 'context_processors' 键名 对应的 键值
    'django_project01.Context_Processor.context_processor'


三、admin后台 管理
    1.运行命令，创建一个管理账号
    python manage.py createsuperuser

    2.然后按提示 输入用户名，邮箱，密码

    3.注册模型类
    注册哪个app(模块)的模型类 就在 哪个模块项目下 的admin.py文件下 编写代码。
    from django.contrib import admin
    # 导入模型类
    from .models import Users

    # 模型类管理
    class UsersAdmin(admin.ModelAdmin):
        pass

    # 注册模型类
    admin.site.register(Users)

    4.自定义管理 页面
    Django 提供了admin.ModelAdmin类
    通过定义ModelAdmin的子类，来定义模型在Admin界面的显示方式。
    列表页属性:
    list_display----显示字段，可以点击 列头进行排序
    list_filter-----过滤字段，过滤框会出现在右侧
    search_fields---搜索字段，搜索框会出现在上侧
    list_per_page---分页，分页框会出现在下侧

    添加、修改也属性
    fields-----属性的先后顺序
    fieldsets--属性的分组

    在 admin.py 中编写
    # 学院类 页面显示管理类
    class AcademyAdmin(admin.ModelAdmin):
        # 显示 学院表的 a_id、a_name字段，
        list_display = ['a_id', 'a_name']
        # 设置 字段 可以 点击
        list_display_links = ['a_id', 'a_name']
        # 字段内容 搜索
        search_fields = ['a_name']
        # 分页显示 数据
        list_per_page = 2

    # 将对应的显示管理类 注册到相应的模型类
    admin.site.register(Academy, AcademyAdmin)




    注意:
    创建超级用户 保存在 数据库的 auth_user 数据表中
    使用  SELECT * FROM auth_user/G; （/G 格式化输入出）
     SELECT * FROM auth_user\G; 如果 是通过ssh远程，使用反斜杠

     如果保错 AttributeError: 'str' object has no attribute 'pk'
     请将 自定义的 上下文处理器中的 函数返回值 设为 空字典。














"""
