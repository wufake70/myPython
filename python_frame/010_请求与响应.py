# _*_coding :utf-8 _*_
# @Time :2022/9/17 21:24
# @File : 010_请求与响应
# @Project : python_Django


"""
一、HttpRequest 对象：
    服务器接收到http协议的请求后，会根据 报文 创建HttpRequest对象，
    视图函数 中的一个参数 是HttpRequest对象，
    在django.http 模块中 定义了 HttpRequest对象的 api

    HttpRequest对象包含了，
    path        请求页面的完整路径(字符串)
    method      请求使用的http 方法，常用 get，post （字符串）
    cookies     用于 保存用户登录的状态，保存在客户端（字典）
    session     表示当前的会话，保存在服务端 （类似字典）
    encoding    表示提交数据的编码格式
    files       包含所有 上传 文件
    headers     请求头
    body        请求体

    方法:
    is_ajax     判断请求是否 通过 XMLHttpRequest（Ajax） 发起的


# HttpRequest(请求)对象
def index(request):
    print(request)          # <WSGIRequest: GET '/db_002/index/'>
    print(request.path)     # /db_002/index/   不包含 ip和端口
    print(request.method)   # GET
    print(request.encoding)  # None

    return render('ok')


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



二、类 视图
    在views.py 文件中的 类视图
    class Upload(View):
        def get(self, request):  渲染页面
            return render(request, 'app_register/文件上传.html')

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

    在urls.py 文件中 配置路由
        path('file/', Upload.as_view(), name='fileupload') name 该路由的名字



三，上传文件
    Django在处理 文件上传的时候 ，文件的数据被保存在了request.FILES，
    FILES中的每一个键 为<input type="file", name=""> 中 name。

    设置文件的存储路径
    1.在项目 根目录下 static文件夹 中创建 media文件夹
    2.图片上传后，会被保存到  该文件夹下，
    3.打开setting.py文件，增加 MEDIA_ROOT
        # 配置 音视频，保存的路径 ,注意 是字符串的拼接 不用写 圆括号，中括号
        MEDIA_ROOT = os.path.join(BASE_DIR, 'static/media')

    4.在 views.py 中
        class Upload(View):
            def get(self, request):
                return render(request, 'app_register/文件上传.html')

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

    5. 在 urls.py 中
    path('file/', Upload.as_view(), name='fileupload')

    6.相关模板文件
    <form action="" method="post" enctype="multipart/form-data"> {% csrf_token %}
        <input type="file" name="file">
        <input type="submit" value="提交">
    </form>





四、HttpResponse
    属性：
    content:    表示返回的内容，字符串类型
    charset:    表示response 采用的 编码字符集，字符串类型
    content-type: 表示 指定输出 MIME 类型


    返回数据的响应函数:
    HttpResponse:   返回简单的字符串对象，
    render:         渲染模板
    redirect:       重定向
    JSONResponse:   返回 JSON数据














"""






























