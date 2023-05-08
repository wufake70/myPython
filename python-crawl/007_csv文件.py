# _*_coding :utf-8 _*_
# @Time :2022/10/11 17:16
# @File : 007_csv文件
# @Project : python-crawl

import csv

"""
1、  csv文件是大数据文件存储格式的文件，结构与excel不同。
    csv是 一种通用的相对简单的文件格式，支持 大部分软件打开 并编辑。
    
2.   数据写入

3.   数据读取


"""

# 表头
headers = ('name', 'age', 'gender')

# 表数据
student = [
    {"name": "孙悟空", "age": "100", "gender": "男"},
    {"name": "猪八戒", "age": "100", "gender": "男"},
    {"name": "沙和尚", "age": "100", "gender": "男"},
    {"name": "唐僧", "age": "100", "gender": "男"},
]

# with open(r'007—.csv', 'w', encoding='utf-8', newline="") as fp:
#     writer = csv.DictWriter(fp, headers)  # 一定要传入表头
#     writer.writeheader()  # 写入表头
#     writer.writerows(student)  # 写入数据


"""
出现的问题: 使用 utf-8编码 保存为 csv文件，用写字板、excel打开均出现了乱码。
解决:        使用记事本(文本编辑器) 另存为 编码格式改为 'utf-8BOM'

"""

# 数据读取
# with open('007—.csv', 'r', encoding='utf-8', ) as fp:
#     content = csv.DictReader(fp)
#
#     for i in content:  # 直接迭代
#         print(i)






















