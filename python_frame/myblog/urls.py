# _*_coding :utf-8 _*_
# @Time :2022/9/14 13:52
# @File : urls
# @Project : python_Django

from django.contrib import admin
from django.urls import path, include, re_path
from .views import *

urlpatterns = [
    path('base/', base),
    path('index/', index, name='blog_index'),
    path('add/', add, name='add'),
    path('list/', article_list, name='list'),
    path('detail/<blog_id>/', detail, name='blog_detail'),
    path('delete/<blog_id>/', delete, name='blog_delete'),
    path('edit/<int:blog_id>/', edit, name='blog_edit'),
    # re_path('myblog\\/edit\\/(?P<blog_id>[^/]+)\\/(?P<user>[^/]+)\\/\\Z', edit, name='blog_edit')

    # 分页
    path('page/', page)
]


















