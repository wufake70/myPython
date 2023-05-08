# _*_coding :utf-8 _*_
# @Time :2022/9/10 20:57
# @File : 004_Django模板标签
# @Project : python_Django

"""
一、常用的html模板标签
    1.if 流程控制语句(<br> 表示换):
        <br> if 流程控制
    {% if string == 'moran1' %}
        <br> 1.hello world
    {% else %}
        <br> 你好 世界！！
    {% endif %}
    注意: 不支持逻辑运算符 not or and


    2.for循环
    {% for i in friend %}
    <br> {{ i }} 模板变量 ，获取数据
        {{ forloop.counter }} 获取下标
    {% endfor %}

    {% empty %} 当组合元素为 空时 直接跳到 该标签

    3.{% load ... %} 加载第三方标签

    4.{% url 'name' 'params'  %} 用于 a 标签的href 的属性，跳转页面
    param 带参路由

    5.{% autoescape off%} 批量关闭 自动转义

    6.{% comment %}
    {% endcomment %}  批量注释


二、模板的继承与引用
    父模板 html
    <title>{% block title %}父模板{% endblock %}</title> 编写标题的 继承
    </head>
    <body>
    {% block head %}
        网页头部的统一内容
    {% endblock %}

    {% block content %}
        网页内容的统一内容
    {% endblock %}

    {% block foot %}
        网页底部的统一内容
    {% endblock %}
    </body>

    继承父模板 html
    {% extends 'app_book/base1.html' %}  模板标签

    {% block title %} 重写标题
    修改 页面的 标题
    {% endblock title %}

    {% block head %}  重写内容 头部
    {% block.super %}  在继承父模板的基础上 修改
    修改网页 头部的内容
    {% include '....' %}  导入另外一个html文件 的内容
    {% endblock head %}

    注意:
        1.extend必须是模板中的第一个出现的标签
        2.子模板中的所有内容，必须出现在父模板定义好的 block中
        (必须要在 {% block ... %}标签内编写代码)，
        否则Django将不会渲染
        3.在重写模板的内容 基础上，继承父模板的内容 使用{% block.super %}








"""



























