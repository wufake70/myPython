# _*_coding :utf-8 _*_
# @Time :2022/9/9 21:08
# @File : urls
# @Project : python_Django

from django.contrib import admin
from django.urls import path
from .views import *


# 子路由 book应用 设置
urlpatterns = [
    path('index/', index),
    path('login/<name>/<password>/', login)

]

























