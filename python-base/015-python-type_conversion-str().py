# _*_coding :utf-8 _*_
# @Time :2022/5/7 16:50
# @File : 015-python-type_conversion-string
# @Project : python-base


# 将其他类型数据转换为字符串
"""
应用场景：字符串拼接（必须将拼接对象转换为字符串）
     例如：页码与字符串的拼接

"""


# 整型转换为字符串（大部分应用场景）,方法：str();
a = 80
print(type(a))
a = str(a)
print(a)
print(type(a))

# 浮点数转换为字符串一如上；

# 将布尔类型转换为字符串;注意：转换后打印True。False亦是如此
b = True
print(b)
print(type(b))
b = str(b)
print(b)
print(type(b))















































