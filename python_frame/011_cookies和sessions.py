# _*_coding :utf-8 _*_
# @Time :2022/9/19 10:40
# @File : 011_cookies和sessions
# @Project : python_Django


"""
状态保持
    1.http协议是无状态的: 每次请求都一次全新的请求，不会记得之前的通信的状态
    2.客户端与服务器端的一次通信，就是一次 会话实现 状态保持的方式，
    在客户端或服务器端存储与会话有关的数据。
    3.村粗方式包括cookies，session，会话一般指session对象
    4.使用cookies，所有数据存储在客户端，注意不要存储 敏感信息
    5.session方式，所有数据存储在服务器端(即数据库)，在客户端cookies中存储 session_id(加密过后)
    ***6.状态保持的目的是 在一段时间内 跟踪请求者的状态，可以实现 跨页面访问 当前请求者的数据。

一、cookies
    保存 用户一些简单的信息（可在浏览器 直接找到）

    views.py文件
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

    注意: cookies 的设置、删除 都是通过 响应对象（HttpResponse） 去操作


二、sessions
    1.视图文件 views.py 代码
        # 家目录
        def home(request):

            username = request.session.get('username', '未登录')
            return render(request, 'app_register/home.html', context={'x': username})


        # 登录
        class Login(View):
            def get(self, request):
                return render(request, 'app_register/login.html')

            def post(self, request):
                username = request.POST.get('user')

                # 会自动存入数据库(django_session)
                # session 在数据库 会自动加密
                request.session['username'] = username

                request.session.set_expiry(0)
                # 会话过期时间 set_expiry(value)
                # 如果没有指定 默认两个星期后 过期
                # 如果 是整数 时间单位是 秒
                # 如果 是 0 ，关闭浏览器 过期
                # value 为None，name永不过期
                # session 过期 并不会在 数据库被删除

                return redirect(reverse('home'))

        # 退出
        def out(request):
            request.session.flush()

            # return render(request, 'app_register/home.html')  这只是渲染页面
            return redirect(reverse('home'))
            # 重定向: 跳转到 指定路由，执行 相关视图函数(包含页面渲染)

    2.路由文件 urls.py 代码
    path('home/', home, name='home'),
    path('login/', Login.as_view(), name='login'),
    path('out/', out, name='out')

    3.模板代码
    ①home.html
     登录: {{ x }}  <br>
    <a href="{% url 'login' %}">登录</a> &emsp;
    <a href="{% url 'out' %}">退出</a>
     <script src=""></script>

     ②login.html
     <form action="./" method="post"> {% csrf_token %}
    <input type="text" name="user"> <br>
    <input type="submit" name="登录">
    </form>



三、注册登录实现思路:
    1.创建模型类(数据数据表)     =====》映射生成数据表
    models.py.py 文件
    # 创建用户注册的模型类
    class Users(models.Model):

        name = models.CharField(max_length=50, unique=True)
        pwd = models.CharField(max_length=50)
        email = models.EmailField()

    2.创建登录模板(html)    ===》创建注册模板(html)

    3.创建注册的视图函数(views.py)
    from  .models import Users
    from .form import RegisterFrom

    class Register(View):
        def get(self, request):
            form = RegisterFrom()
            return render(request, 'app_register/register2.html', context={'form': form})

        def post(self, request):
            # 获取 form表单中的数据
            form = RegisterFrom(request.POST)

            # 需要先 判断 表单数据 是否有效
            if form.is_valid():
                name = form.cleaned_data.get('name')
                pwd = form.cleaned_data.get('pwd')
                pwd_repeat = form.cleaned_data.get('pwd_repeat')
                email = form.cleaned_data.get('email')

                # 判断密码和确认密码 相同
                if pwd == pwd_repeat:
                    Users.objects.get_or_create(name=name, pwd=pwd, email=email)
                    return HttpResponse('用户注册成功')

                else:
                    return HttpResponse('注册失败，请确认两次密码是否一致')

    3.1重写 登录的视图函数(类视图)，
    class Login(View):
        def get(self, request):
            return render(request, 'app_register/login.html')

        def post(self, request):
            username = request.POST.get('user')
            pwd = request.POST.get('pwd')

            # 验证 用户名和密码 是否 对应
            exist = Users.objects.get(name=username).pwd
            if exist == pwd:

                # 登录成功后 将相关数据 存入数据库(django_session)
                # session 在数据库 会自动加密
                request.session['username'] = username

                request.session.set_expiry(0)
                # 会话过期时间 set_expiry(value)
                # 如果没有指定 默认两个星期后 过期
                # 如果 是整数 时间单位是 秒
                # 如果 是 0 ，关闭浏览器 过期
                # value 为None，name永不过期
                # session 过期 并不会在 数据库被删除

                return redirect(reverse('home'))

            else:
                return HttpResponse('密码错误或该用户不存在!!!')



    4.配置路由(urls.py)
    path('register/', Register.as_view(), name='register')



"""
































