# _*_coding :utf-8 _*_
# @Time :2022/8/14 6:53
# @File : python_并发池
# @Project : python_ubuntu_progress

import threading
import time
import queue


"""
一、可重复利用的的线程
二、线程池的实现
三、内置池 (直接导入)
四、使用池实现并发服务器
"""

"""  一、可重复利用的的线程  


class MyThread(threading.Thread):
    def __init__(self):
        super().__init__()
        self.q = queue.Queue()  # 创建一个 队列对象，接收任务函数
        self.daemon = True  # 设置成守护模式,主线程结束，子线程自动结束
        self.start()    # 实例化 直接 开启线程

    # 重写run方法
    def run(self):
        while True:         # 实现 一个线程 循环执行多个任务
            func, args, kwargs = self.q.get()  # 从队列中取出 任务函数,
            #                                    当队列为空时，再次get就会阻塞
            func(*args, **kwargs)           # 执行任务函数
            self.q.task_done()

    def submit(self, func, args=(), kwargs={}):  # 当参数 不确定时，使用 不定长传参
        self.q.put((func, args, kwargs))    # 相对列内 提交任务函数

    # 重写 join方法
    def join(self):
        self.q.join()
        # 判断队列是否为空，
        # 不为空，就说明 子线程还在执行任务，
        # 主线程阻塞 等待任务执行完成。
        # 为空，就说明子线程 全部任务执行完成
        # 继续执行 主线程代码，
        # 由于开启 守护模式 主线程 结束，子线程也结束。

# 任务一
def func1():
    time.sleep(1)
    print('任务一完成')

# 任务二
def func2(*args, **kwargs):
    time.sleep(1)
    print('任务二完成', args, kwargs)


if __name__ == '__main__':
    mt = MyThread()     # 实例化 一个新建的类对象，即创建一个可重复使用的线程
    mt.submit(func1)    # 将任务函数 添加到 该线程的 任务队列里
    mt.submit(func2, args=('hello world', ), kwargs={'str': '你好世界！'})

    mt.join()
    # 因为 设置成守护模式，这里需要调用 join方法，
    # 等待子线程结束
    # 但是 子线程 执行完最后一个任务，
    # 再次get 就会 造成子线程阻塞(队列造成的)，
    # 同时 造成主线程阻塞，
    # 则需要重写 线程模块的join 方法。

    # ### 线程的重复利用，一个线程 执行多个任务(任务存储在队列)
    # ### 提高 线程的利用率
"""

"""   二、线程池: 多个可重复利用的线程。"""

"""
class MyPool:
    def __init__(self, n):
        self.q = queue.Queue()
        for i in range(n):      # n参数 表示 要开启几个线程
            threading.Thread(target=self.run, daemon=True).start()

    def run(self):
        while True:     # 实现 一个线程 循环执行多个任务
            func, args, kwargs = self.q.get()  # 从队列中取出 任务函数,
            #                                    当队列为空时，再次get就会阻塞
            func(*args, **kwargs)  # 执行任务函数
            self.q.task_done()

    def submit(self, func, args=(), kwargs={}):  # 当参数 不确定时，使用 不定长传参
        self.q.put((func, args, kwargs))  # 相对列内 提交任务函数

    # 重写 join方法
    def join(self):
        self.q.join()


def func1():
    time.sleep(1)
    print('任务一完成')


def func2(*args, **kwargs):
    time.sleep(1)
    print('任务二完成', args, kwargs)


if __name__ == '__main__':
    tm = MyPool(6)   # 实例化线程池对象 开启六个线程
    tm.submit(func1)
    tm.submit(func2, args=('hello',), kwargs={'str': 'world'})
    tm.submit(func1)
    tm.submit(func2, args=('hello',), kwargs={'str': 'world'})
    tm.submit(func1)
    tm.submit(func2, args=('hello',), kwargs={'str': 'world'})
    # 相对列内 添加 六个 任务
    # 每个线程 平均下来 执行一个任务
    tm.join()
    
    注意: 从生产者和消费者模型来看 并发池
          主线程 类似于生产者，产生任务，存储在队列
          子线程 类似于消费者，从队列取出任务，并解决任务。
          
"""












