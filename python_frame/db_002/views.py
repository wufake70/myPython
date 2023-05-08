import os.path
from time import sleep

from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .models import Academy, Student, StuInfo, Course


# 添加数据
def add(request):
    # 学院添加
    # 设置a_id的起始值 为 100001，后面一次增加
    Academy.objects.get_or_create(a_id=100001, a_name='计算机学院', )
    Academy.objects.get_or_create(a_name='数理学院', )
    Academy.objects.get_or_create(a_name='经济管理学院', )
    Academy.objects.get_or_create(a_name='机电学院', )

    # 学生添加
    Student.objects.get_or_create(s_id=10001, s_name='陈冠希', a_id=100001)
    Student.objects.get_or_create(s_name='罗志祥', a_id=100002)
    Student.objects.get_or_create(s_name='吴亦凡', a_id=100003)
    Student.objects.get_or_create(s_name='王力宏', a_id=100004)
    Student.objects.get_or_create(s_name='李易峰', a_id=100001)
    Student.objects.get_or_create(s_name='郑爽', a_id=100002)
    Student.objects.get_or_create(s_name='成龙', a_id=100003)
    Student.objects.get_or_create(s_name='李连杰', a_id=100004)

    # 学生详情表
    StuInfo.objects.get_or_create(stu_id_id=10001, age=50, gender=1)
    StuInfo.objects.get_or_create(stu_id_id=10002, age=39, gender=1)
    StuInfo.objects.get_or_create(stu_id_id=10003, age=30, gender=1)
    StuInfo.objects.get_or_create(stu_id_id=10004, age=40, gender=1)
    StuInfo.objects.get_or_create(stu_id_id=10005, age=35, gender=1)
    StuInfo.objects.get_or_create(stu_id_id=10006, age=30, gender=0)
    StuInfo.objects.get_or_create(stu_id_id=10007, age=60, gender=1)
    StuInfo.objects.get_or_create(stu_id_id=10008, age=60, gender=1)

    # 课程表
    Course.objects.get_or_create(c_id=1001, c_name='Python')
    Course.objects.get_or_create(c_name='Web')
    Course.objects.get_or_create(c_name='C++')
    Course.objects.get_or_create(c_name='Java')

    # 课程与学生 中间表(对于模型类来说，我们无法直接操作 中间表)
    # c_all = Course.objects.all()  获取 全部课程
    # 单独 获取 课程
    py = Course.objects.get(c_id=1001)
    web = Course.objects.get(c_id=1002)
    c__ = Course.objects.get(c_id=1003)
    java = Course.objects.get(c_id=1004)

    # 获取 全部 学生
    s_all = Student.objects

    # 通过 主键 找外键（表），给学生添加课程
    s_all.get(s_name='吴亦凡').course_set.add(py, c__)
    s_all.get(s_name='陈冠希').course_set.add(py, web)
    s_all.get(s_name='罗志祥').course_set.add(py, java, c__)
    s_all.get(s_name='王力宏').course_set.add(web, c__)
    s_all.get(s_name='李易峰').course_set.add(py, web, c__)
    s_all.get(s_name='郑爽').course_set.add(java, web, c__)
    s_all.get(s_name='成龙').course_set.add(web, c__)
    s_all[7].course_set.add(py, web, c__, java)

    return HttpResponse('数据添加成功')


# 查询
def query_data(request):
    pass
    # ##一对多的查找  (学院 对 学生)

    stu = Student.objects.get(s_name='陈冠希')  # 注意: 只能使用 get方法
    # 直接通过 外键 查找 外键表 “.外键名”
    stu_academy = stu.a.a_name

    # 反向查找 与该主键关联的表，".外键表名_set"  set==》一对多
    # 查找一个学院 所有的学生， .student_set.all()
    # all_stu = Academy.objects.get(a_id=100003).student_set.all()
    all_stu = Academy.objects.get(a_id=100003).student_set.get(s_name='成龙')

    # 一对一 查找  （学生 对 学生详情）
    stu = Student.objects.get(s_id=10001)
    # 反向查找 与该主键关联的表， ".外键表名" ==》一对一
    stu_info = stu.stuinfo

    # 多对多 查找
    # 单独 获取 课程
    py = Course.objects.get(c_id=1001)
    web = Course.objects.get(c_id=1002)
    c__ = Course.objects.get(c_id=1003)
    java = Course.objects.get(c_id=1004)

    # 获取 全部 学生
    s_all = Student.objects.all()
    # 反向查找 与该主键关联的表，".外键表名_set"，获取某个学生 课程情况
    result = s_all[0].course_set.all()

    # 获取 一个课程 的学生人数
    # 通过 外键 查找 主键表  ".外键名"
    result = py.stu.all()

    return HttpResponse(result)


# 数据删除
def delete(request):
    pass
    # 移除某个学生的 某个课程。
    stu = Student.objects.get(s_id=10001)
    py = Course.objects.get(c_id=1001)
    # result = stu.course_set.get(c_name='Python')
    # result = stu.course_set.remove(py)  # 返回None

    # 清空某个学生的 课程。
    # result = stu.course_set.all()
    result = stu.course_set.clear()  # 返回None
    return HttpResponse(result)


# 数据修改; add 可以 添加，也可修改。
def modify(request):
    pass
    # 学生转专业
    stu = Student.objects.get(s_id=10002)
    stu_academy = stu.a  # 数理学院
    # academy = Academy.objects.get(a_name='机电学院')
    # 给该学院 加该学生，即可完成转专业 (一对多)
    # academy.student_set.add(stu)
    # stu_academy = stu.a
    # return HttpResponse(stu_academy)
    return HttpResponse(stu_academy)


# 多表(联结)查询 (多表无关联 查询)=======》filter()
def more_query(request):
    # 查询 计算机学院 所有 学生 的 详细信息，（学院表，学生表，学生信息表）
    result = StuInfo.objects.filter(stu_id__a__a_name='计算机学院')

    # 查询 有Python课程 的学生 的学院表，(课程表，学生表，学院表)
    result = Academy.objects.filter(student__course__c_name='Python')

    # 查询 郑爽 的课程信息表
    result = Course.objects.filter(stu__s_name='郑爽')
    return HttpResponse(result)
    # return HttpResponse(academy)


# 聚合与关联查询
# 导入 相关 函数
from django.db.models import Count, Max, Min, Avg, Sum, OrderBy, F, Q


def select(request):
    pass
    # 聚合 查询
    # aggregate()是QuerySet的 一个终止句，他返回一个包含一些键值对的字典

    # 求年龄 总和,返回值为 字典形式 使用中括号 ['键名'] 进行取值。
    result = StuInfo.objects.all().aggregate(Sum('age'))
    result = f"所有学生的年龄总和:{result}"

    # 求平均年龄
    result = StuInfo.objects.all().aggregate(Avg('age'))
    result = f"所有学生的平均年龄:{result['age__avg']}"

    # 求统计 个数
    result = StuInfo.objects.filter(age__gte=40).aggregate(Count('age'))
    result = f"age大于等于 40的个数:{result['age__count']}"

    # 求最大
    result = StuInfo.objects.all().aggregate(Max('age'))
    result = f"年龄最大的:{result['age__max']}"

    # 分组查询 annotate()
    # 安学院分组，并显示 学院的名字
    result = Student.objects.values('a__a_name').annotate(count=Count('a'))

    # F查询 对表中字段操作
    # 查询 学生ID 小于等于 学院ID 的数据
    result = Student.objects.filter(s_id__lte=F('a'))

    # Q查询
    # 查询 学生名字 为 郑爽 或 成龙 的学生
    result = Student.objects.filter(Q(s_name='郑爽') | Q(s_name='成龙'))

    return HttpResponse(result)


# HttpRequest(请求)对象
def index(request):
    print(request)  # <WSGIRequest: GET '/db_002/index/'>
    print(request.path)  # /db_002/index/   不包含 ip和端口
    print(request.method)  # GET
    print(request.encoding)  # None

    return render('ok')


"""
def post(request):
    
    POST 方式
    post属性
    QueryDict类型的对象，包含post请求方式的 所有参数
    参数 与form表单中 的控件（name属性，value属性）对应，
    name属性 为 键名，
    value属性 为 键值。
    
    user = request.POST.get('user_name')
    pwd = request.POST.get('pwd')
    print(user)
    print(pwd)
    print(request)
    print(request.path)
    print(request.method)
    print(request.encoding)
    return render(request, 'app_register/register.html')


def get(request):
    
    GET 方式
    get属性
    QueryDict类型的对象，包含get请求方式的所有参数
    与 url请求地址 中的参数 对应，位于 '？' 后面参数的格式是 键值对
    key1=value1.....,多个参数之间 用 '&' 链接，

    
    user = request.GET.get('user_name')
    # pwd = request.GET.get('pwd')
    # 当请求参数 一键多值(a=111&a=222)时，get方法只能获取最后一个值，
    # 此时 可以使用 getlist方法 获取全部值(列表形式)
    pwd = request.GET.getlist('pwd')
    print(user)
    print(pwd)
    print(request)
    print(request.path)
    print(request.method)
    print(request.encoding)
    return render(request, 'app_register/register.html')
"""

# 类视图
from django.views import View


class Hello(View):
    def get(self, request):
        user = request.GET.get('user_name')
        # pwd = request.GET.get('pwd')
        # 当请求参数 一键多值(a=111&a=222)时，get方法只能获取最后一个值，
        # 此时 可以使用 getlist方法 获取全部值(列表形式)
        pwd = request.GET.getlist('pwd')
        print(user)
        print(pwd)
        print(request)
        print(request.path)
        print(request.method)
        print(request.encoding)
        return render(request, 'app_register/register.html')

    def post(slef, request):
        # user = request.POST.get('user_name')
        # pwd = request.POST.get('pwd')
        # print(user)
        # print(pwd)
        # print(request)
        # print(request.path)
        # print(request.method)
        # print(request.encoding)
        # return render(request, 'app_register/register.html')
        pass


from django_project01.settings import MEDIA_ROOT
import os

from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator


# 文件上传
@method_decorator(login_required, name='dispatch')
class Upload(View):
    # @method_decorator(login_required)
    def get(self, request):
        return render(request, 'app_register/文件上传.html')

    # @method_decorator(permission_required(login_url='www.baidu.com'))
    def post(self, request):
        # 获取 上传的文件（name 属性）
        file = request.FILES.get('file')

        # 拼接路径
        f_name = os.path.join(MEDIA_ROOT, file.name)
        print(f_name)
        with open(f_name, 'wb+') as f:
            for i in file.chunks():  # 读取文件 内容
                f.write(i)

        return HttpResponse('文件上传成功')


# cookies设置
import datetime


def set_cookies(request):
    response = HttpResponse('设置cookies')
    # response.set_cookie('name1', 1111111111)  # 默认 关闭浏览器就过期
    response.set_cookie('name', 'wufake', max_age=100)  # 设置过期时间
    # response.set_cookie('name', 'wufake', expires=datetime.datetime(2022, 10, 1))  # 设置过期日期

    return response


def get_cookies(request):
    cookies = request.COOKIES
    ck = cookies.get('name')
    return HttpResponse(f'欢迎{ck}回来')


def delete_cookies(request):
    response = HttpResponse('删除cookies')
    response.delete_cookie('name')

    return response


# 家目录
@login_required
def home(request):
    username = request.session.get('username', '未登录')
    return render(request, 'app_register/home.html', context={'x': username})


# 登录
class Login(View):
    def get(self, request):
        next_url = request.GET.get('next')
        if next_url:
            return render(request, 'app_register/login.html', context={'next': next_url})
        return render(request, 'app_register/login.html')

    def post(self, request):

        username = request.POST.get('user')
        pwd = request.POST.get('pwd')

        # 验证 用户名和密码 是否 正确
        # exist = Author.objects.get(name=username).pwd
        # exist = User.objects.get(username=username).password

        # 使用 auth系统的验证方法
        user = authenticate(username=username, password=pwd)

        # if exist == pwd:
        if user:

            # 登录成功后 将相关数据 存入数据库(django_session)
            # session 在数据库 会自动加密
            # 将 username 存入 session 中
            request.session['username'] = username

            # request.session.set_expiry(0)
            # 会话过期时间 set_expiry(value)
            # 如果没有指定 默认两个星期后 过期
            # 如果 是整数 时间单位是 秒
            # 如果 是 0 ，关闭浏览器 过期
            # value 为None，name永不过期
            # session 过期 并不会在 数据库被删除

            # 使用auth系统 login 保持登录状态
            login(request, user)

            next_url = request.POST.get('next')
            # print(next_url)
            if next_url:
                return redirect(next_url)
            return redirect('blog_index')
            # return redirect(reverse('home'))

        else:
            return HttpResponse('密码错误或该用户不存在!!!')


# 退出
def out(request):
    # request.session.flush()

    # 使用auth系统 logout 退出登录状态
    logout(request)

    # return render(request, 'app_register/home.html')  这只是渲染页面
    return redirect(reverse('blog_index'))  # 重定向: 跳转到指定路由，执行 相关视图函数(包含页面渲染)


# 注册页面
from myblog.models import Author
from .form import RegisterFrom

# 导入认证系统 的模型类
from django.contrib.auth.models import User, Group, Permission
# 导入 auth系统的 登录，退出，验证方法
from django.contrib.auth import login, logout, authenticate
# 导入 auth系统的 登录认证
from django.contrib.auth.decorators import login_required


class Register(View):
    def get(self, request):
        form = RegisterFrom()
        return render(request, 'app_register/register2.html', context={'form': form})

    def post(self, request):
        # 获取 form表单中的数据
        form = RegisterFrom(request.POST)

        if form.is_valid():
            name = form.cleaned_data.get('name')
            pwd = form.cleaned_data.get('pwd')
            pwd_repeat = form.cleaned_data.get('pwd_repeat')
            email = form.cleaned_data.get('email')

            # 判断密码和确认密码 相同
            if pwd == pwd_repeat:
                # 用户表用来 对应 文章表
                Author.objects.get_or_create(name=name, pwd=pwd)

                # 添加 auth系统的 (普通)用户
                User.objects.create_user(username=name, password=pwd, email=email)

                # 添加 超级用户
                # User.objects.create_superuser(username=name, password=pwd, email=email)

                # return HttpResponse('用户注册成功')
                return redirect('login')
            else:
                return HttpResponse('注册失败，请确认两次密码是否一致')

