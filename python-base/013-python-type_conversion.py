# _*_coding :utf-8 _*_
# @Time :2022/5/7 15:42
# @File : 013-python-type_conversion
# @Project : python-base

# 数据类型转换整型
# 浮点数转换为整型,方法：int()。注意：转换是直接把浮点数除掉
a = 1.92
# float
print(type(a))
# 开始转换
b = int(a)
print(b)
# int
print(type(b))

# 布尔转换为整型，方法：int().注意：转换之后，True为1，False为0；
c = False
d = True
print(c)
print(d)
c = int(c)
d = int(d)
print(c)
print(d)

# 纯整数字字符串转为整型。注意：只能是整数，不能带除数字以外的字符串。
e = '111'
print(e)
e = int(e)
print(e)



































