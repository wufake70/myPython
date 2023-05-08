# _*_coding :utf-8 _*_
# @Time :2022/9/8 20:03
# @File : 001_创建虚拟环境和安装Django
# @Project : python_frame

"""
1.创建虚拟环境
    查看当前的有哪些 虚拟环境: workon。
    创建虚拟环境: mkvirtualenv -p /usr/bin/python3 envname(自定名称)
    进入虚拟环境: workon envname
    退出虚拟环境: deactivate
    删除虚拟环境: rmvirtualenv envname

2.安装Django
    pip install django
    指定稳定的版本下载
    pip install django==2.1.7 -i https://pypi.douban.com/simple
    查看当前Python环境下的第三方库: pip list

3.创建一个Django项目
    django-admin startproject projectname
    自动生成一个文件夹，
    子文件 manage.py Django的管理器
    子文件夹 projectname 中
        __init__.py
        settings.py     配置文件
        urls.py         路由文件
        wsgi.py         部署服务器

4.pycharm 同步Django项目
    注意: 同步路径

5.开启 Django服务
    方法一: linux 命令启动
    ① 将 settings.py文件中的 ALLOWED_HOSTS = [],改成 ALLOWED_HOSTS = ["*"],
    表示 这个Django项目 允许 所有的 ip 访问。

    ② 开启服务：cd 进入 Django的项目文件夹  python manage.py runserver 0.0.0.0:8000
    ctrl+c 打断 进程

    方法二: pycharm 启动
    配置 pycharm
    https://ke.qq.com/webcourse/2929935/
    103042396#taid=10177917148247311&vid=5285890816232911799
    码趣视频 40 分钟

6.视图

7.路由

8.创建  应用app
    一个项目里面 可以对应多个模块(即 app)
    方法一,linux 命令行创建
        python manage.py startapp app-name

    方法二，pycharm创建
    .......

9.修改 后端的文件(如settings.py )都会 导致 Django服务 停止(也可能 会自动刷新)，
    但是修改 模板html文件 不会是 框架服务停止。




"""


























