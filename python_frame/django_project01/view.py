# _*_coding :utf-8 _*_
# @Time :2022/9/9 15:14
# @File : view
# @Project : python_Django

from django.http import HttpResponse
from django.shortcuts import reverse, redirect, render

"""
视图
"""


# 视图函数
def index(request):

    # 用户 访问后，发送 响应
    return HttpResponse('hello world')


def test1(request, name, age, ):
    return HttpResponse(f'姓名:{name}\n年龄:{age}')


# 用户 访问 旧的URL地址，重定向到新的页面
def article(request):
    # 重定向到 new_article 的视图函数
    # return redirect(reverse(new_article))
    # 重定向到 name 为 new_article 的URL地址上
    return redirect(reverse('new_article'))


# 新的url 地址
def new_article(request):
    return HttpResponse('这是新的 资源')



from django.template.loader import get_template


# 渲染 页面 小米商城
def mi_shop(request):
    # 获取 模板文件
    t = get_template('./app_mi_shop/1.html')
    # 进行页面渲染，必须变量接收
    t = t.render()
    return HttpResponse(t)


# clock
def clock(request):
    # t = get_template('./app_movie/14钟表.html')
    # t = t.render()
    return render(request, './app_clock/14钟表.html')


# 注册
def register(request):
    return render(request, './app_register/register.html')


def threeD(request):
    return render(request, '3D/15_3D效果.html')










