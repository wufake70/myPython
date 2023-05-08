from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


# 设置 子路由 movie模块的 视图
def index(request):
    return HttpResponse('这里是 movie模块')