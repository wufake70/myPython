# _*_coding :utf-8 _*_
# @Time :2022/9/9 17:04
# @File : 002_路由及应用的创建
# @Project : python_Django


"""
一、url 路由
    1.URL (uniform resource locator) 统一资源定位符
    是 对 可以从互联网上得到的资源的位置和访问方法的一种简洁的表示，
    是互联网上标准资源的地址，互联网的每一个文件都有一个唯一url，
    它包含的信息支出 文件的 位置以及浏览器应该怎么处理它

    2.设置 路由, 尖括号
    尖括号转换器 的匹配模式:
        str 匹配除了路径分隔符(/)之外的非空字符串，这是 默认的形式
        int 只匹配正整数 包含 0；
        slug 匹配字母、数字、即横杆，下划线组成的字符串
        uuid 匹配格式化的uuid（设备标识符），
        path 匹配任何非空字符串，包含路径分隔符(/)

    3.使用正则 设置 更加 详细的路由
    re_path(r'^test3/(?P<name>[A-z\d_]{5,10})/(?P<age>\d{1,2})', test1)

    4.主路由 分配 多个子路由
        ① 在 主目录的setting文件里，将新的 app(的名字) 添加到 INSTALLED_APPS的 列表内。

        ② urls.py 导入 include函数,如 from django.urls import include

        ③ 对应着 修改 app模块 的 urls.py(自行创建)、views.py 文件

    5.kwargs 可以传递额外的参数到 views.py文件中(使用include时 )，
    需要统一给下面的url一些参数的时候 显得尤其有用。
    注意: 加入该参数 必须要接收，否则报错。

    6.name
    给每一个匹配的url 地址取名字

    页面重定向
        用户访问 老的url地址(article)  重定向到 新的页面(new_article)
        def article(request):
            # 重定向到 new_article 的视图函数
            # return redirect(reverse(new_article))

            # 重定向到 name 为 new_article 的URL地址上,
            # reverse  反向解析
            return redirect(reverse('new_article'))

    注意: 需要导入 redirect、reverse模块
    from django.shortcuts import reverse, redirect


二，Django html模板 (css img javascript在Django项目中 都是 static 文件)
    1.在 项目 目录下创建一个templates 目录用来存放所有的html的模板 文件，
    2.在templates 目录里面在新建 各个以 app 名字命名的目录，用来存放 各个 app中模板文件。

    3.新建的项目 需要到 settings.py 中 配置 路径
        TEMPLATES

    4.渲染模板 的方法
        ① 直接将html的字符串 硬编码 HttpResponse中 （不用）
        ② django.template.loader 定义了函数以加载 模板
        导入 html文件（from django.template.loader import get_template）
        ③ 使用 render 进行渲染 （常用）

"""























