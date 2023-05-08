# _*_coding :utf-8 _*_
# @Time :2022/7/31 20:45
# @File : Python_操作MySQL
# @Project : python_ubuntu_progress

import pymysql
import openpyxl
import pprint


# l链接数据库
# test_con = pymysql.connect(host='localhost', user='admin', password='qwe123', db='students2')
# 注意: 这里的host，如果用的是远程解释器，只要填localhost即可；如果是本地解释器，就需要填入 远程的 ip地址
test_con = pymysql.connect(host='localhost', user='admin', password='qwe123')
test_con.select_db('test')          # 跟换数据库
print(test_con)
print('=' * 60)

# 获取游标
test_cur = test_con.cursor()
print(test_cur)
print('=' * 60)

# ##执行相关的 SQL语句


# #查找 并 接收 数据
# test_1 = test_cur.execute('SELECT * FROM stu_tab;', args=None)      # 执行 SQL命令;报错时，可以返回 SQL报错的信息
# print(test_1)                         # test_cur.execute()方法只会返回 受影响的行数
# result = test_cur.fetchall()          # fetchall()  将接收所有数据,以元祖形式

# result = test_cur.fetchone()          # fetchone() 只会返回一行数据,没有就会返回None；
"""  输出所有数据
for i in range(test_1):
    result = test_cur.fetchone()
    print(result)

while 1:
    result = test_cur.fetchone()
    if result is None:
        break
    print(result)
"""

# result = test_cur.fetchmany(test_1)                    # 填入多少数值，就返回多少行，超过也不报错。
# pprint.pprint(result)

# #创建新的数据库
# test_2 = test_cur.execute('CREATE DATABASE test DEFAULT CHARSET=UTF8;', args=None)

# 多次 执行SQL语法        （添加 索引
# test_3 = test_cur.execute('SET @index:=0; ', args=None)
# test_4 = test_cur.execute(' SELECT @index:=@index+1 ,id,name,age FROM stu_tab1;', args=None)
# print(test_cur.fetchall())

# #创建 数据表
# test_5 = test_cur.execute("""CREATE TABLE `数理学院团员信息表` (
# id INT PRIMARY KEY,
# `缴费金额` INT DEFAULT 0,
# `姓名` VARCHAR(19),
# `手机号码` VARCHAR(11) NOT NULL UNIQUE KEY,
# `身份证` VARCHAR(18) NOT NULL UNIQUE KEY,
# `学院班级` VARCHAR(20) DEFAULT '未定义')
# DEFAULT CHARSET=UTF8;""", args=None)

# #将excel 中的数据 填入到 数据表中
"""
excel = openpyxl.load_workbook(r"C:\ Users\yui\Desktop\001.xlsx")
sheet = excel['Sheet1']
# print(len(sheet['A']))
for i in range(2, len(sheet['A'])):
    # print(sheet[f'{i}'][0].value)
    # print(f"{sheet[f'{i}'][0].value},{type(sheet[f'{i}'][1].value)},{type(sheet[f'{i}'][2].value)},{sheet[f'{i}'][3].value},{sheet[f'{i}'][4].value},{sheet[f'{i}'][5].value}")
    a_1 = sheet[f'{i}'][0].value
    a_2 = sheet[f'{i}'][1].value
    a_3 = sheet[f'{i}'][2].value
    a_4 = sheet[f'{i}'][3].value
    a_5 = sheet[f'{i}'][4].value
    a_6 = sheet[f'{i}'][5].value
    test_6 = test_cur.execute(f"INSERT INTO `数理学院团员信息表` VALUE ({a_1},{a_2},'{a_3}','{a_4}','{a_5}','{a_6}')")


test_con.commit()               # 填入数据后 提交并保存
"""
"""
# #私密信息加密                   中文表（或字段） 全部使用 反引号包围
test_7 = test_cur.execute('UPDATE `数理学院团员信息表` SET `手机号码`=MD5(`手机号码`),`身份证`=MD5(`身份证`)')
test_con.commit()
test_cur.close()
"""