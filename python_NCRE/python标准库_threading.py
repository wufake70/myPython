# _*_coding :utf-8 _*_
# @Time :2022/7/28 23:33
# @File : python标准库_threading
# @Project : python_NCRE
import datetime
import threading
import time


def fun(a, b=88):
    print(a)
    print(b)


# 调用threading.Thread() 函数 生成 Thread对像
thread_1 = threading.Thread(target=print, args=['你好', '世界'], kwargs={'sep': '&'})
# 开启新线程
thread_1.start()

# 创建线程 同时 向目标函数传参
# 规则:
# 常规参数(必备参数，默认参数) 可以作为一个列表 传给 Thread（）中的 args
# 关键字 参数 可以作为一个 字典 kwargs
thread_2 = threading.Thread(target=fun, args=['nihao', 'shijie'])
thread_2.start()

# 关键字 作为字典 传参
thread_3 = threading.Thread(target=fun, kwargs={'a': 'hello world', 'b': '9999'})
thread_3.start()

# 注意: target=函数名 而不是 调用函数
# 多线程的 并发问题
# 可以创建多个 线程 ，让他们同时运行。但是多线程可能会导致 所谓的并发问题
# 如果这些线程 同时读写相同的 变量，导致相互干扰，就会发生 并发问题。
# 当创建一个 新的 线程对象时，要确保其目标函数只使用该函数 局部变量，避免并发问题；



