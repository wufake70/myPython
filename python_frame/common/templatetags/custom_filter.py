# _*_coding :utf-8 _*_
# @Time :2022/9/11 10:42
# @File : custom_tags
# @Project : python_Django

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
@register.filter
def my_sort(values):
    values.sort()
    return values















