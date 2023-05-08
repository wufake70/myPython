# _*_coding :utf-8 _*_
# @Time :2022/9/10 10:29
# @File : 003_请求与响应
# @Project : python_Django

"""
一、模板变量
    1.模板变量 在 views.py 中编写，
    2.渲染 html时 使用render中 content参数(字典类型) 传入 相应的数据，
    3.在 html模板中 使用 "{{ 对应的键名 }}" 来获取数据
    4.如果传入的变量 保存的数据 是一个 方法(函数)，html 模板中 获取的数据 是该函数的返回值。
    5.如果传入 组合数据类型 通过 ".+索引" 方式 ，如： {{ friend.3 }}
    6.如果如传入的 字典类型 通过 ".+键名" 方式  ，如： {{ info.friend }}

二、过滤器，对于后端传来的数据 进行修改。
    语法: {{模板变量|...}}
    注意: 不能是随意空格
    1.英文字符转大写 {{ string|upper }}
    2.英文字符转小写，首字母大写 {{ string2|lower|title }}
    3.去除空格后 首字母大写 {{ string3|cut:"" }}
    4.add 用于 数字相加 {{ num1|add:9}}
      字符串与字符串拼接  {{ string|add:string3 }} （join也可以）
    5.设置默认值(对于None，空字符串，空列表，空元祖，空字典都有效) {{xx|default:'null'}}

    6.设置时间格式：
        只要日期{{ now|date }}
        只要时间{{ now|time }}
        24小时制(H) {{ now|date:'Y/m/d/H/i/s' }}
        12小时制(h) {{ now|date:'Y/m/d/h/i/s' }}

    7.length方法
        返回字符串长度 {{ string|length }}
    length_is方法
        判断字符串长度(返回布尔值) {{ string|length_is:9 }}

    8.省略后面字符(保留前四个字符+三个省略号) {{ string4|truncatechars:7 }}
      略后面单词(保留前两个单词) {{ string4|truncatewords:2 }}

    9.字符串切片 字符串切片 {{ string4|slice:'0:4' }}

    10.去除标签 获取文本内容 {{ html|striptags }}
    11.使字符串html标签生效 {{ html|safe }}

    12.操作浮点数(操作浮点数) {{ num3|floatformat:6 }}

    13.自动转义 {{ string5|safe }}

三、配置静态文件(JavaScript，css，img)
    1.在项目文件 下创建一个static 目录，进入该目录 在创建 js，css，img 目录

    2.在 settings.py 进行设置

    3.在每一个html模板 前 加入{% load static %} （导入静态文件）

    4.导入 图片链接 src="{% static 'admin/img/app_clock/表盘.png' %}"








"""













