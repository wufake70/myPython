# _*_coding :utf-8 _*_
# @Time :2022/9/11 10:31
# @File : 005_自定义过滤器和标签
# @Project : python_Django

"""
一、自定义 模板过滤器
    目录结构
    1.在项目文件 下 创建个名为 common的Python包(即 文件夹)，在该目录创建 __init__.py 的文件。
    2.将common加入到settings.py 中的INSTALLED_APP 列表中，
    3.在common 里 创建目录 templatetags，在该目录下 创建 __init__.py文件 用于写 自定义过滤器 源码。
    4.开始编写 自定义过滤器 源码(在custom_filter.py中)

    from django import template
    register = template.Library()  # 生成一个注册器

    # 自定义 转小写 的过滤器
    @register.filter('my_lower')    # 注册方法二
    def my_lower(values):
        return values.lower()
    # register.filter(my_lower)   # 注册方法一

    # 数值 相减
    @register.filter
    def my_reduce(values, values2):
        return values - values2

    # 列表排序



    5.在 模板html中 使用 自定义过滤器
    {% load custom_filter %} (顶部加载 custom_filter.py 文件即可)


二、自定义 标签
    两种标签 django.template.Library.simple_tag()   简单 自闭和标签
            django.template.Library.inclusion_tag() 包含标签

    1~3 同上
    4.开始编写 自定义过滤器 源码(在custom_tags.py中)
    from django import template
    import datetime
    register = template.Library()  # 生成一个注册器

    # 显示当前时间 的标签
    @register.simple_tag   注册一个简单标签
    def current_time(str1='%Y年%m月%d日 %H时%M分%S秒'):
        now = str1
        return datetime.datetime.now().strftime(now)

    # 使用视图函数 传过来的数据
    @register.simple_tag(takes_context=True)
    def current_time1(context):
        now = context.get('format')
        return datetime.datetime.now().strftime(now)

    # 包含标签
    需要在模板目录下 另写一个 html文件 show_tags.html,
    <lu>
    {% for i in choice %}
        <li>{{ i }}</li>
    {% endfor %}
    </lu>

    在custom_tags.py中
    @register.inclusion_tag('app_book/show_tags.html')
    def show_result(ls):   不能传入组合和数据类型
        ls = ['a', 'b', 'c', 'd']
        return {'choice': ls}


    5.模板html文件 导入 {% load custom_tags %}















"""































