# _*_coding :utf-8 _*_
# @Time :2022/8/12 9:04
# @File : 18_多进程和多线程
# @Project : python_ubuntu_progress

import multiprocessing
import threading
import time
from datetime import datetime

now = datetime.now().strftime('%H:%M:%S')


def fun():
    print('内部开始---', datetime.now().strftime('%H:%M:%S'))
    time.sleep(4)
    print('内部结束---', datetime.now().strftime('%H:%M:%S'))


if __name__ == '__main__':
    p1 = multiprocessing.Process(target=fun,daemon=False)
    p1.start()
    # p1.join()  # 会等待 子进程 执行结束
    print('外部开始---', datetime.now().strftime('%H:%M:%S'))
    p1.join()    # 会等待 子进程 执行结束,在执行主进程 代码，
    #                 # 共执行4+3=7 秒
    # 注意: 进程或线程添加 join 方法之后，会等待子任务结束，
    # 如果没有结束则会阻塞，直到子任务结束，
    # 因此join一般都是放在程序的最后面

    # p1.terminate() 终止子进程
    # print('nihao')
    time.sleep(3)
    print('外部结束---', datetime.now().strftime('%H:%M:%S'))

    print('主进程对象', multiprocessing.current_process())
    print('主进程名字', multiprocessing.current_process().name)
    print('主进程id', multiprocessing.current_process().pid)

    print('子进程对象', p1)
    # <Process name='Process-1' pid=8956 parent=10148 started> started 表示子进程 已开启
    # 注意: 进程没启动前，pid 为None，
    # 线程 是在 进程内 运行的
    print('子进程名字', p1.name)
    print('子进程id', p1.pid)
    print('进程生命周期', p1.is_alive())
    # 返回布尔值，进程开启时为True，可用判断 一个子进程 是否 开启。

    # 守护模式，主进程结束，子进程自动结束与 terminate 效果一样
    # p1 = multiprocessing.Process(target=fun, daemon=True)





























