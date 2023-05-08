# _*_coding :utf-8 _*_
# @Time :2022/9/26 14:35
# @File : urls
# @Project : python_Django

from django.contrib import admin
from django.urls import path, re_path, include
from .views import *  # "." 表示从当前的目录导入文件

urlpatterns = [
    path('index/', index, name='index'),
    path('upload/', UploadAnswer.as_view(), name='upload'),
    path('aa/', aa),
    path('addcourse/', add_course, name='course'),
    path('search/', SearchAnswer.as_view(), name='Search'),
    path('analysistext/', AnalysisAnswer.as_view()),
    path('search/<answer_id>/', AnswerEdit.as_view(), name='Edit'),
    path('delete/<answer_id>/', delete, name='AnswerDelete'),

    # 搜索 全部课程答案
    path('courseanswer/', SearchCourseAnswer.as_view(), name='SearchCourseAnswer'),
    path('courseanswershow/<course_id>', courseshow)










]












