import datetime

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

"""
模板变量 将后台的数据传入前端


"""


# 模板变量 类
class Person:
    def __init__(self, name, password):
        self.name = name
        self.password = password

    def say(self):
        pass
        return 'hello'


# 模板变量 类对象
sun = Person('孙悟空', '666666')
# user = '孙悟空'
# pwd = '666666'

# 模板变量 字符串
success = '登录成功！！'
error = "登录失败！！"

# 列表
friend_list = ['唐僧', '猪八戒', '沙和尚', '白龙马', ]

# 字典
sun_info = {
    'name': '孙悟空',
    'gender': '男',
    'age': 30,
    'friend': friend_list
}


# 这里是book 视图函数
def index(request):
    return HttpResponse('这里还是 book项目')


# 用户登录验证
def login(request, name, password):
    # 登录 验证
    if name == sun.name and password == sun.password:

        return render(request, 'app_book/login.html',
                      # 返回相应 数据(前端)
                      context={
                          'message': success,
                          'user': sun.name,  # 传入类对象的信息
                          'user_say': sun.say,  # 传入类对象的函数
                          'friend': friend_list,
                          'info': sun_info,
                          'string': 'moran',
                          'string2': 'ABCDE',
                          'string3': 'l o v e',
                          'string4': 'this is python',
                          'string5': '>',
                          'xx': None,
                          'age': 90,
                          'null': '',
                          'num1': 200,
                          'num2': 39,
                          'num3': 3.1415926,
                          'now': datetime.datetime.now(),
                          'html': '<h1>this is a html</h1>',
                          'format':  '%H:%M:%S'


                      })
    else:
        return render(request, 'app_book/error.html',
                      context={
                          'message': error
                      })

