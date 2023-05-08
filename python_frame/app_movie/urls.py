# _*_coding :utf-8 _*_
# @Time :2022/9/9 21:19
# @File : urls
# @Project : python_Django
# 设置路由: 路由名称 和 对应(要执行)的视图函数

from django.contrib import admin
from django.urls import path
from .views import *

# 设置 子路由 movie应用
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('index/', index)

]