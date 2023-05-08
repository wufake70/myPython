# _*_coding :utf-8 _*_
# @Time :2022/9/13 10:16
# @File : urls
# @Project : python_Django
from django.urls import path
from .views import *

from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('add/', add),
    path('query/', query_data),
    path('delete/', delete),
    path('modify/', modify),
    path('more_query/', more_query),
    path('select/', select),  # 聚合查询
    path('index/', index),   # Httprequest对象
    # path('post/', post),
    # path('get/', get),


    # 类视图的路由
    path('chassview/', Hello.as_view(), name='class view'),

    # 文件上传
    # path('file/', login_required(Upload.as_view()), name='fileupload'),
    path('file/', Upload.as_view(), name='fileupload'),

    # cookies设置
    path('setcookies/', set_cookies),
    path('getcookies/', get_cookies),
    path('deletecookies/', delete_cookies),

    # session
    # 家目录
    path('home/', home, name='home'),
    path('login/', Login.as_view(), name='login'),
    path('out/', out, name='out'),

    # 注册
    path('register/', Register.as_view(), name='register'),
    # path('register/', Register, name='register')

    #



]