# _*_coding :utf-8 _*_
# @Time :2022/10/1 10:57
# @File : 测试
# @Project : python_Django
import re

a = None or 1

print('网' == '⽹')

print('局域，英文缩写为'[2] == '局域，英⽂缩写为'[2])
print(ord('网'))
print(ord('⽹'))
print(ord('⼀'))

str1 = "单选题*在***参考模型中，（）选择合适的网间路由和交换结"

a = str1.split('*')
print(a)
print('*' in str1)









