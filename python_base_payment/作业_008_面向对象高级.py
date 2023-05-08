# _*_coding :utf-8 _*_
# @Time :2022/6/28 9:26
# @File : 作业_008_面向对象高级
# @Project : python_base_payment

import time
import decimal

print('=============第一题================')


# 1.测试列表推导式和不用列表推导式哪一种速度更快
# 上下文协议


class RunTime:
    # with关键字一出来，就立马执行 __enter__(self)
    def __enter__(self):
        self.st = time.time()
        return self.st

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.et = time.time()
        self.ut = self.et - self.st
        print(f'执行{self.ut}时间')

    pass


with RunTime():
    # 列表推导式
    ls_1 = [i for i in range(1000000)]
    # print(ls_1)

with RunTime():
    # 不使用列表推导式
    for i in range(1000000):
        pass

print('=============第二题===============')
# 2.range不可以使用小数做步长，实现一个可迭代对象，可以用小数步长


class Item:
    # 在初始化方法中设置，起始值、结束值、步长
    def __init__(self, s, end, step=1):
        self.s = s
        self.end = end
        self.step = step

    # 让实例变成可迭代对象
    def __iter__(self):
        return self

    # 变成迭代器
    def __next__(self):
        # 使用decimal高精度模块，进行浮点数计算
        a = self.s
        self.s += decimal.Decimal(str(self.step))
        if self.s > self.end:
            # 抛出异常，停止迭代
            raise StopIteration
        # return self.s 起始值为 1
        return a


# 可实现小数作为步长的迭代器
ls = Item(0, 7, 0.7)
# ls_1 = range(0,5,1)
for i in Item(3, 8, 1.020):
    print(i)
