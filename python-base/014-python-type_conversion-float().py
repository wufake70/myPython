# _*_coding :utf-8 _*_
# @Time :2022/5/7 16:15
# @File : 014-python-type_conversion-float()
# @Project : python-base


"""
应用场景：
       当我们在带爬虫的时候，大部分都是字符串类型的
"""
# 将浮点型字符串转换为浮点数，方法：float().
a = '13.22'
print(a)
print(type(a))
a = float(a)
print(a)
print(type(a))


# 将整转换为浮点型。注意：转换是在整数后加上点零
b = 444
print(b)
print(type(b))
b = float(b)
print(type(b))
print(b)









