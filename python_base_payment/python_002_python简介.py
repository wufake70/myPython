# _*_coding :utf-8 _*_
# @Time :2022/6/5 16:20
# @File : python_001_python简介
# @Project : python_base_payment

# 查看python的关键字
import keyword

print(keyword.kwlist)

"""
编译型语言：
使用编译器先将源代码全部编译成机器码，运行时直接运行编译后的机器码。
一次编译，多次执行，效率比较高。但是依赖编译器，跨平台性差。
如C,C++是编译型语言。
编译型语言执行方式

解释型语言：
使用解释器，在运行时，逐行翻译成机器码。
每执行一次源代码，就要翻译一次， 效率较低。依赖解释器，跨平台性好。
如Python是解释性语言。
解释型语言执行方式
"""

# 查看内置函数
print(dir(__builtins__))

# 编辑模式下输出结果，需要使用print（）函数
# 交互模式（interactive mode）下，可直接读取变量的值


# 字符串拼接
# 1. 加号 +
# 2.%s
print('%s' % '兰州交通大学')
print('%d' % 888)
# 3.format（）函数
a = '{1}年{1}月{1}日'.format(2022, 6, 5)  # 大括号里可以填写下标（索引）
a = f'{2022}年{6}月{5}日'  # format（）函数的简写
# print(a)
# 4.join（）函数
b = '.'.join(['2022', '6', '5'])  # 统一用点号“."将列表中每一个数据进行拼接
print(b)

# 字符串的格式化
# %d 格式化整数，针对的是数字
a = '%6d8748' % 33394.3333
# 数字6表示字符串长度，
# 默认情况下超过字符串长度，就会用空格补齐
print(a)
# %f 格式化浮点数，
a = '%08d8885857' % 99999  # 不够用零来补齐
a = '%08d8885857' % 99999
print(a)
# %f ”格式化浮点数
a = '%f' % 88  # 默认情况下保留六位小数
a = '%.1f' % 99  # 保留一位小数
a = '%07.2f' % 99  # 不够长度用零补充，保留两位小数
print(a)

import decimal

# 导入decimal模块进行高精度计算
print(decimal.Decimal('2.2') - decimal.Decimal('2'))

import math

# 导入数学模块
"""
math.ceil() 向上取整
math.floor() 向下取整
math.pi  Π值
math.sqrt() 开平方
"""
print(math.pi)

# 查看对应模块的方法 dir(模块的名字)
import selenium
import json
print(dir(json))
