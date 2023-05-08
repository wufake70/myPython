# _*_coding :utf-8 _*_
# @Time :2022/9/11 18:54
# @File : urls
# @Project : python_Django
from django.urls import path
from .views import *

urlpatterns = [
    path('add/', add),
    path('select/', select),
    path('update/', update),
    path('delete/', delete),


]