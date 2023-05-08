# _*_coding :utf-8 _*_
# @Time :2022/8/14 9:57
# @File : 20_并发池_内置池
# @Project : python_ubuntu_progress

from multiprocessing.pool import ThreadPool   # 从进程模块导入线程池
from multiprocessing.pool import Pool        # ....导入内置进程池
import time


def func1():
    time.sleep(1)
    print('任务一完成')


def func2(*args, **kwargs):
    time.sleep(1)
    print('任务二完成', args, kwargs)


if __name__ == '__main__':
    # 内置池的 使用方法:
    tm = Pool(8)    # 实例化 进程池对象，并开启2条线程
    tm.apply_async(func1)
    tm.apply_async(func2, args=('hello',), kwds={'str': 'world'})
    tm.apply_async(func1)
    tm.apply_async(func2, args=('hello',), kwds={'str': 'world'})
    tm.apply_async(func1)
    tm.apply_async(func2, args=('hello',), kwds={'str': 'world'})   #
    # 向队列中添加 六个 任务

    tm.close()  # 停止向 队列中添加 任务)
    tm.join()   # 等待任务执行完毕
    # ###内置的线程、进程池，与自己创建的 效果一样
    






















