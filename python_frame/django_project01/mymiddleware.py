# _*_coding :utf-8 _*_
# @Time :2022/9/21 8:42
# @File : mymiddleware
# @Project : python_Django
from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin


class MyException(MiddlewareMixin):
    # 发送请求 过程中，执行的中间件
    def process_request(self, request):
        # 获取请求的信息
        # print(request.method)
        # print(request.path)
        # print(request.is_ajax())

        # 在执行中间件时 就返回响应，后面的 视图函数就没有执行的机会
        # return HttpResponse('请求错误')
        return None


































