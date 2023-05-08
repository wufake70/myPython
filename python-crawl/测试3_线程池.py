# _*_coding :utf-8 _*_
# @Time :2022/10/12 14:40
# @File : 测试3
# @Project : python-crawl
from multiprocessing.pool import ThreadPool   # 从进程模块导入线程池
from multiprocessing.pool import Pool        # ....导入内置进程池
import time


def func1():
    # time.sleep(3)
    # ls.append(1)
    # print('任务一完成')
    global a
    for i in range(0, 10000000):
        a += 1
    print(a)


def func2(*args, **kwargs):
    # time.sleep(3)
    # print('任务二完成', args, kwargs)
    # ls.append(1)
    global a
    for i in range(0, 10000000):
        a -= 1
    print(a)


if __name__ == '__main__':
    # ls = []
    a = 0
    th = ThreadPool(2)

    # for i in range(0, 1000000):
    #     th.apply_async(func1)
    #     th.apply_async(func2)

    th.apply_async(func1)
    th.apply_async(func2)

    th.close()
    th.join()

    # time.sleep(20)
    # print(len(ls))
    # print(a)


