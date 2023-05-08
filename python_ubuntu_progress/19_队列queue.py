# _*_coding :utf-8 _*_
# @Time :2022/8/13 15:03
# @File : 19_队列queue
# @Project : python_ubuntu_progress

import queue
import threading

"""   队列操作   """
"""
# 实例化一个队列 对象
q = queue.Queue()
print(q)    # 该对象信息 <queue.Queue object at 0x00000199067343A0>

# 入队 put()    先进先出
q.put(1)
q.put(2)

# 出队 get()    先进先出，每次取出一个，取出一个，队列就少一个，不同于列表
print(q.get())      # 1
# print(q.get())      # 2

# 测试空 empty() 返回 布尔值 / 测试满 full() .....
print(q.empty())

# 队列长度 qsize()  # 返回队列里面的 元素个数
print(q.qsize())

# 限制队列 的元素
q2 = queue.Queue(2)
q2.put(1)
q2.put(2)
# q2.put(3)   当 放入第三个元素时 造成阻塞
print(q2.qsize())
q2.get()
q2.get()
# q2.get()    当 队列为空时，在次取出元素 也会造成阻塞
print(q2.qsize())
"""

# 队列内部 自带队列计数器，
q3 = queue.Queue(2)
# q3.join()     # 等待队列中的元素 被执行完，否则阻塞，
#                 即队列元素不为空是就阻塞
q3.put(1)   # 每次put 多会加一
# q3.get()    # 但是 每次get 计数器 不会减一，使用join 任然会阻塞
q3.put(2)
q3.get()
q3.task_done()  # 必须调用 task_done() 才会减一
q3.get()
q3.task_done()  # 注每次 必须是get后 就调用task_done()，及时减一
q3.join()
print('nihao')

# 通过join方法，可以保证队列为空
























