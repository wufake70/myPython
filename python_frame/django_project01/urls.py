"""django_project01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from .view import *  # "." 表示从当前的目录导入文件

# 设置路由: 路由名称 和 对应(要执行)的视图函数
urlpatterns = [

    # 网站管理员 设置
    path('admin/', admin.site.urls),

    # path('index/', index),  # 通过路由 调用相应的视图函数
    # path('test1/<name>', test1),  # 必须要有一个 参数(name 接收，该参数要与视图函数 的参数对应)
    # path('test2/<name>/<int:age>', test1)  # 第二个参数 如果不是纯数字 就不可访问。

    # 使用正则 设置 更加 详细的路由(不常用)
    # re_path(r'^test3/(?P<name>[A-z\d_]{5,10})/(?P<age>\d{1,2})', test1)

    # 主路由 分配 两个子路由
    path('book/', include('app_book.urls')),
    path('movie/', include('app_movie.urls')),

    # 重定向
    path('article/', article),  # 旧的路由
    path('new_article/', new_article, name='new_article'),  # 新的路由

    # 渲染 页面，小米商城
    path('mi_shop/', mi_shop),
    # clock
    path('clock/', clock),

    # 注册 页面
    path('register/', register),

    # 给db_001 app模块 分配一个子路由
    path('db_001/', include('db_001.urls')),

    # 给db_002 app模块 分配一个子路由
    path('db_002/', include('db_002.urls')),

    # 子路由 吾论
    path('wulun/', include('myblog.urls')),
    path('3D/', threeD),

    # 子路由 网课答案
    path('onlinecourse/', include('Online_Course.urls'))





]

