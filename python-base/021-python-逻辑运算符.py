# _*_coding :utf-8 _*_
# @Time :2022/5/7 21:39
# @File : 020-python-逻辑运算符
# @Project : python-base

# 逻辑运算符 （and 与   or 或    not 非）

# and(与）：两边的值都为true时，就返回true
# 结果为True
print(1 < 3 and 2 > 1)
# 结果为False
print(0 > 2 and 9 > 3)


# or(或）：两边的值都为False时，就返回False
# 结果为True
print(0 < 3 or 1 > 9)
# 结果为False
print(0 < -1 or 9 > 10)

# not（非）：取反
# 结果为False
print(not(1 == 1))
