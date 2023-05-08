# _*_coding :utf-8 _*_
# @Time :2022/6/25 17:26
# @File : 作业_006_文件
# @Project : python_base_payment

import os
import sys
from _datetime import datetime

print('============第一题============')
# 1.批量生成5月的txt文件，2022-5-.txt 2022-5-31.txt
# 创建一个新文件夹
# 判断当前文件家是否存在
if not os.path.exists('./作业_006'):
    os.mkdir('./作业_006')

for i in range(1, 32):
    # 创建新的txt文件要在，write模式下
    # %02d 表示再数值不够两位数用零补齐
    with open('./作业_006/2022-5-%02d.txt' % i, 'w') as p:
        p.close()

print('=============第二题============')
# 2.生成上免得文件之后，再一次再每个文件中写入文件名

for i in range(1, 32):
    with open('./作业_006/2022-5-%02d.txt' % i, 'w') as p:
        p.write('2022-5-%02d.txt' % i)
        p.close()
print('已经写入文件名')

print('===========第三题===========')
# 3.将上面生成的所有文件之后加上  '_NEW’
# 2022-5-1.txt  2022-5-31_NEW.txt

for i in range(1, 32):
    #    with open('./作业_006/2022-5-%02d.txt' % i, 'a') as p:  不能再打开文件时，对该文件改名
    # 通过os.system()使用dos命令
    # os.system('calc.exe')
    # os.system(r'move .\作业_006\2022-5-%02d.txt .\作业_006\2022-5-%02d_NEW.txt' % (i, i))
    # 也可使用os.rename(path, new path)
    os.rename(r'.\作业_006\2022-5-%02d.txt' % i, r'.\作业_006\2022-5-%02d_NEW_new.txt' % i)

print('=============第四题============')
# 4.假如有一个文件中，有一段文字中存在错别字，找到他，并将他修改为正确的文字

# 新建一个测试txt文本
with open('./作业_006/测试.txt', 'w') as p:
    p.write('''233可以看到，通过7998移动文件指针的位置，再借助 read() 和 write() 函数，就可以轻松实现，读取文件中指定位置的数据（或者向文件中的指定位置写入数据）。

注意，当向文件中写入数据时，如果不是文件的尾部，写入位置的原有88595数据不会自行向后移动，新写入的数据会将文件中处于该位置的数据直接覆盖掉。

实现对文件指针的58移动，文件对象提供了 tell() 函数895898和 seek() 函数。tell() 函数用于判断文件指针当前所处的位置，而 seek() 函数用于移动文件指针到文件的指定位置
''')

# 该文本中错字为数字
# 修改就是将他们删除
with open('./作业_006/测试.txt', 'r')as p:
    # 将文本的全部内容读取完，并存入变量 a 中
    a = p.read()
    # print(a)
    # 遍历字符串的每一个字府
    for i in range(0, len(a)):
        # 对照表
        b = '1234567890'
        # 判断字符串是不是数字类的
        if a[i] not in b:
            # 将修改后数据存入新的文件中
            with open('./作业_006/测试(修改版).txt', 'a') as f:
                f.write(a[i])
print('文本已修改')

input('回车快速删除：')

os.system(r'rd /q /s .\作业_006')










