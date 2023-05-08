# _*_coding :utf-8 _*_
# @Time :2022/9/22 8:39
# @File : 013_auth系统
# @Project : python_Django


"""
一、auth系统
    1.auth系统中的表
    user: user是auth模块中维护用户信息的关系模式(继承了models.Model)，
        数据库中该表被命名为auth_user。

    group: user对象中有一个名为 groups 的多对多 字段，
        多对多关系 由 auth_user_groups 数据表维护，
        group对象可以通过user_set反向查询用户组中的用户。

    permission: Django的auth系统 提供了 模型级的 权限控制，
            即可以 检查用户是否对某个数据表拥有
            增（add），改（change），删（delete）权限



    2.auth认证系统功能:
    create_user     创建用户
    authenticate    验证登录
    login           记住用户的登录状态
    logout          退出登录
    is_authenticated 判断用户是否登录
    login_required  判断用户是否登录的装饰器

    3.




二、登录注册实现（使用auth系统）
    1.使用内置的auth_user表来存储用户注册信息。
        from .form import RegisterFrom

        # 导入认证系统 的模型类
        from django.contrib.auth.models import User, Group, Permission
        # 导入 auth系统的 登录，退出，验证 方法
        from django.contrib.auth import login, logout, authenticate

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
                        # 添加 auth系统的 (普通)用户
                        # User.objects.create_user(username=name, password=pwd, email=email)
                        # 添加 超级用户
                        User.objects.create_superuser(username=name, password=pwd, email=email)
                        return HttpResponse('用户注册成功')

                    else:
                        return HttpResponse('注册失败，请确认两次密码是否一致')


    2.使用auth系统中的login，logout，authenticate实现登录，退出，和验证登录。
        # 登录
        class Login(View):
            def get(self, request):
                return render(request, 'app_register/login.html')

            def post(self, request):
                username = request.POST.get('user')
                pwd = request.POST.get('pwd')

                # 使用 auth系统的验证方法
                user = authenticate(username=username, password=pwd)

                # if exist == pwd:
                if user:

                    # 使用auth系统 login 保持登录状态
                    login(request, user)

                    return redirect(reverse('home'))

                else:
                    return HttpResponse('密码错误或该用户不存在!!!')

        # 退出
        def out(request):
            # 使用auth系统 logout 退出登录状态
            logout(request)
            # return render(request, 'app_register/home.html')  这只是渲染页面
            return redirect(reverse('home'))  # 重定向: 跳转到指定路由，执行 相关视图函数(包含页面渲染)

    3.给 特定页面设置 （登录）访问权限，
    如果用户没有登录，就没有权限 访问该页面，
    并且跳转到登录页面。
    设置跳转页面
    在settings.py 中 添加 LOGIN_URL = '/db_002/login/'

    主要是 给视图函数或类视图 添加装饰器
        ①视图函数 添加装饰器
            # 导入装饰器
            from django.contrib.auth.decorators import login_required

            # 使用装饰器
            @login_required
            def home(request):
                .....

        ②类视图 添加 装饰器
        法一:(在路由中设置)
            # 导入装饰器
            from django.contrib.auth.decorators import login_required
            # login_required(类名称.as_view())
            path('file/', login_required(Upload.as_view()), name='fileupload')

        法二:(在视图文件中)
            # 导入装饰器
            from django.contrib.auth.decorators import login_required
            from django.utils.decorators import method_decorator
            # 对类视图 直接添加，注意 name='dispatch' 必填
            @method_decorator(login_required, name='dispatch')
            class Upload(View):
                ......

        法三: (对类视图 get请求方式添加装饰器)
            # 导入装饰器
            from django.contrib.auth.decorators import login_required
            from django.utils.decorators import method_decorator
            # 对类视图 get请求方式添加装饰器
            @method_decorator(login_required)
            def get(self, request):
                ......

    4.实现 登录后自动跳转到用户 试图访问的页面
        ①类视图 中 get请求
        思路: 声明一个变量 next_url，当用户 正常路由到 登录页面，参数为None (登陆成功后，重定向到家目录)；
            当用户 是被重定向到 路由页面时，获取url 中next参数 并赋给 next_url。
            最后，将next_url 参数传到 前端模板。
        def get(self, request):
            next_url = request.GET.get('next')
            if next_url:
                return render(request, 'app_register/login.html', context={'next': next_url})
            return render(request, 'app_register/login.html')

        ②前端登录模板，接收 参数
        <input type="hidden" name="next" value="{{ next }}">

        ③提交数据，判断 next 参数的值，
        def post(self, request):
            username = request.POST.get('user')
            pwd = request.POST.get('pwd')

            # 使用 auth系统的验证方法
            user = authenticate(username=username, password=pwd)
            if user:

                # 使用auth系统 login 保持登录状态
                login(request, user)
                next_url = request.POST.get('next')
                print(next_url)
                if next_url:  # 如果参数的值存在， 重定向到相关页面
                    return redirect(next_url)

                return redirect(reverse('home'))

            else:
                return HttpResponse('密码错误或该用户不存在!!!')

三、权限的实现

    1.权限分配设置
    # 查看 权限表
    select * from auth_permission;

    # 导入装饰器
    from django.contrib.auth.decorators import permission_required

    # 使用方法
    # 将装饰器 放在 对应的视图函数上，
    # 如果没有权限 就自动跳转默认 登录页面，
    # 可以 设置 login_url 参数，跳转至点页面
    @permission_required('appname.权限名称', login_url=None)





# 注意:
# 1. 如果使用 auth表 来保存用户信息(并进行注册登录)，可以使用 request.user 来获取 用户名



















"""






























