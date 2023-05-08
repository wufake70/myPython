# _*_coding :utf-8 _*_
# @Time :2022/5/9 18:07
# @File : 047-python-文件的打开和关闭
# @Project : python-base

"""
1.打开/创建文件(注意：该方式不能创建文件夹）
    使用open函数，可以到开一个已经存在的文件，或者创建一个新文件
    格式：open（文件路径，访问模式）
    访问模式：r 读取、w 存储。

2.关闭文件(close)

"""
# 创建一个新文件
# open('test.txt', 'w')

# 向文件中写如内容
fp = open('test.txt', 'w')
fp.write('hello world')

# 文件的关闭
fp1 = open('test2.txt', 'w')
fp1.write('hello!!')
fp1.close()











































