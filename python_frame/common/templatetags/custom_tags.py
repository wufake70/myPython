# _*_coding :utf-8 _*_
# @Time :2022/9/11 11:46
# @File : custom_tags
# @Project : python_Django

from django import template
import datetime

register = template.Library()  # 生成一个注册器


# 显示当前时间 的标签
@register.simple_tag
def current_time(str1='%Y年%m月%d日 %H时%M分%S秒'):
    now = str1
    return datetime.datetime.now().strftime(now)


@register.simple_tag(takes_context=True)
def current_time1(context):
    now = context.get('format')
    return datetime.datetime.now().strftime(now)


# 包含标签
@register.inclusion_tag('app_book/show_tags.html')
def show_result(ls):

    return {'choice': ls}

























