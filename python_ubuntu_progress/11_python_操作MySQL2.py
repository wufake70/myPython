# _*_coding :utf-8 _*_
# @Time :2022/8/5 9:02
# @File : python_操作MySQL2
# @Project : python_ubuntu_progress

import pymysql
import pprint


class MyOperateMysql:
    def __init__(self, host, user, password, db=None):
        self.connect = pymysql.connect(host=host, user=user, password=password, db=db)
        self.cursor = self.connect.cursor()  # 获取游标对象
        self.result = None

    def select_DB(self,db):                     # 切换数据库
        self.connect.select_db(db)
        self.cursor = self.connect.cursor()  # 获取游标对象
        self.result = None

    def find(self, command, args=None, onlyOne=True):           # 执行SQL 查找命令,需要返回值
        if onlyOne:
            self.cursor.execute(command, args=args)
            self.result = self.cursor.fetchone()
            return self.result

        else:
            self.cursor.execute(command, args=args)
            self.result = self.cursor.fetchall()
            return self.result

    def execute(self, command, args=None,onlyOne=True):     # 可将查找命令 与 执行命令结合
        self.result = self.cursor.execute(command,args=args)
        # if self.result:
        #     return self.find(command=command,args=args,onlyOne=onlyOne)

    def commit(self):           # 修改数据后，进行提交
        self.connect.commit()


# 实例化 一个对象
test = MyOperateMysql(host='localhost', user='admin', password='qwe123', db='test')

# 查数据 (单条/ 多行数据）
# test_content = test.find('SELECT * FROM `数理学院团员信息表`',onlyOne=False)
# pprint.pprint(test.content)

# 切换数据库
test.select_DB('students2')
# test_content = test.find('SELECT * FROM `stu_tab`', onlyOne=False)
# pprint.pprint(test_content)

# 设置索引 （多行命令执行）
# test.execute('SET @index:=0;')
# 使用find()方法
# test_content = test.find('SELECT @index:=@index+1 "index",name,age,sex FROM stu_tab ORDER BY age', onlyOne=False)
# pprint.pprint(test_content)

# 删除 / 创建数据库
# test.execute('DROP DATABASE test1;')
# test.execute('CREATE DATABASE test1 CHARSET=UTF8;')

# 创建/删除 表
# test.execute("CREATE TABLE `数理学院团员信息表` ( id INT PRIMARY KEY, `缴费金额` INT DEFAULT 0, `姓名` VARCHAR(19),`手机号码` VARCHAR(11) NOT NULL UNIQUE KEY,`身份证` VARCHAR(18) NOT NULL UNIQUE KEY,`学院班级` VARCHAR(20) DEFAULT '未定义') DEFAULT CHARSET=UTF8;")
# test.execute('DROP TABLE `数理学院团员信息表`;')

# 插入数据
# sql语法 insert into 指定的字段要用 圆括号包围
# test.execute('INSERT INTO stu_tab (id,name,sex,age) VALUE (10011,"world","男", 42);')






































