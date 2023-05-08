# _*_coding :utf-8 _*_
# @Time :2022/8/13 8:23
# @File : 19_进程隔离和线程资源分配
# @Project : python_ubuntu_progress

import multiprocessing
import threading
import time

""" 一、进程(通信)隔离"""

"""
def func():
    global var
    var += 1
    time.sleep(3)
    print(var)


def func2(space1):
    space1['num'] += 1
    print(space1)


if __name__ == "__main__":      # 如果使用了 if __name__ == "__main__":
    var = 10                    # 则所有 非 创建类(class)，非 创建函数(def)的代码 
                                # 都要写在 之下

    # 创建一个进程公共空间 管理器
    space = multiprocessing.Manager()
    space1 = space.dict()  # 开辟公共空间字典类型
    space1.update({'num': 10})  # 向公共space1 空间添加值
    
    # 进程隔离
    # p1 = multiprocessing.Process(target=func)
    # p1.start()
    # p1.join()
    # print(var)  # 主进程 和子进程存在隔离，var 并没有 改变

    
    p2 = multiprocessing.Process(target=func2, args=(space1,))
    p2.start()
    p2.join()       # 主进程 输出 11
    print(space1)
    p2.join()       # 主进程 输出 10，主进程 通常 比子进程快
    # 注意: 如果 进程任务函数 传的参数 是字典，必须使用 join 方法
    #       join()的位置 也影响 主进程 输出
"""

"""二、线程共享资源"""
"""
由于 线程是在 进程中的，不存在隔离
但是 线程存在 资源争夺 问题。

"""


def fun1():
    global var
    # 添加 锁
    lock.acquire()
    for i in range(1000000):
        var += 1
    # 打开锁
    lock.release()


def fun2():
    global var
    lock.acquire()
    for i in range(1000000):
        var -= 1
    lock.release()


if __name__ == "__main__":
    var = 1

    # 定义 一把锁
    lock = threading.Lock()

    t1 = threading.Thread(target=fun1)
    t2 = threading.Thread(target=fun2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(var)      # 当循环的 次数 很大时，
                    # 打印的 值不是可预期的
                    # 该结果 是由线程争夺进程资源 造成的

# 解决 线程争夺资源问题
# 1.互斥锁 保护资源，频繁加锁和解锁，会降低程序效率

# 2.队列 queue  (生产者和消费者模型 即线程池)























