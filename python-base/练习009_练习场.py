# _*_coding :utf-8 _*_
# @Time :2022/5/21 10:28
# @File : 练习009
# @Project : python-base

import requests

from bs4 import BeautifulSoup

import os



path = r'.\防盗链.jpg'

size = os.path.getsize(path)   # 返回的值的单位为字节（即B）
print(size)

# break 的作用 终止当前循环体内的代码 （他可以结束当前和上一级函数，上上一级的函数仍然可以执行）

for ii in range(1000):
    print(ii)
    for i in range(101):
        print('%d%s%d' % (ii, '+', i))
        if i == 10:
            # break 打印出11后就停止当前两个函数
            continue
        print(i)