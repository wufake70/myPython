# _*_coding :utf-8 _*_
# @Time :2022/8/13 15:29
# @File : 19_生产者与消费者模型
# @Project : python_ubuntu_progress

"""基本概念"""
# 模型:  生产者—(入队)—》队列 —(出队)—》消费者
# 生产者 不断 产生问题 放入队列
# 队列存储 问题
# 消费者 从队列 取出 任务，解决任务

# 注意: 从程序员的角度来看，
# 生产者是用户，消费者是程序员

import threading
import queue
import random
import time
import multiprocessing


# 建立 消费者模型
# 继承 多线程模块，一个线程作为 消费者，一个线程作为生产者
class Consumer(threading.Thread):
    def __init__(self, q):
        super().__init__()  # 继承父类的初始化方法
        self.q = q          # 定义 队列的属性

    # 重写 线程自带的 run方法，
    # 调用start()方法时， 会自动调用
    def run(self):
        while True:     # 循环不断从队列中获取任务
            time.sleep(1)
            self.q = q.get()   # 从队列里 取出元素
            print('消费者消费了', self.q)


# 建立 生产者模型
class Producer(threading.Thread):
    def __init__(self, q):
        super().__init__()  # 继承父类的初始化方法
        self.q = q  # 定义 队列的属性

    # 重写 线程自带的 run方法，
    # 调用start()方法时， 会自动调用
    def run(self):
        while True:  # 循环不断向队列中添加任务
            time.sleep(1)
            item = random.randint(1, 100)
            self.q = q.put(item)  # 从队列里 取出元素
            print('生产者生产了', item)


if __name__ == "__main__":
    q = queue.Queue()  # 队列 存储 资源

    p1 = Producer(q)
    c1 = Consumer(q)
    # c1.start()
    # p1.start()
    # 生产者和消费者模型 是解决 线程争夺资源的 一种方法，

    # 进程 也可以使用 生产者和消费者模型,
    # 但是 进程 并存在资源争夺
    # 多进程模块自带 队列 对象
    q2 = multiprocessing.Queue()
    q2.put(1)
    print(q2.get())



































