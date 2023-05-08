# _*_coding :utf-8 _*_
# @Time :2022/8/14 13:42
# @File : 测试_010_server6_进程
# @Project : python_ubuntu_progress

import socket
import datetime
from multiprocessing.pool import ThreadPool
from multiprocessing import Pool, cpu_count


def receive_message(conn, addr):    # 处理客户端数据
    while True:
        message = conn.recv(1024).decode('utf-8')
        now = datetime.datetime.now().strftime('%H:%M')
        if not message:
            print(f'ip:{addr[0]}:{addr[1]},time:{now}:…退出聊天室…')
            conn.close()
        else:
            print(f'ip:{addr[0]}:{addr[1]},time:{now}:{message}')


def accept_process(server):
    tp = ThreadPool(cpu_count()*2)
    # 一般来说 ，可以开启线程是 CPU核心的两倍
    while True:
        conn, addr = server.accept()
        now = datetime.datetime.now().strftime('%H:%M')
        print(f'iP:{addr[0]}:{addr[1]},time:{now}: 连接成功……')
        # 设置线程池 处理客户端发来的 数据
        tp.apply_async(receive_message, args=(conn, addr))
        # tp.close()   这里不需要 停止 向线程池中 添加 任务函数
        # tp.join()    等待所有的子线程 结束任务
        # break


def s():   # 用于测试
    print(888)


if __name__ == "__main__":
    server = socket.socket()  # 创建服务端套接字对象
    server.bind(('127.0.0.1', 9004))  # 服务端绑定的ip及端口
    server.listen(10)  # 限制最大监听数
    print("……等待客户端链接……")

    n = cpu_count()     # 获取CPU核心数（8）
    pro_pool = Pool(n)  # 实例化进程池对象 并开启最合适的进程数(8)
    # 给进程池添加 建立对等套接字任务(共8个)
    pro_pool.apply_async(accept_process, args=(server,))
    pro_pool.apply_async(accept_process, args=(server,))
    pro_pool.apply_async(accept_process, args=(server,))
    pro_pool.apply_async(accept_process, args=(server,))
    pro_pool.apply_async(accept_process, args=(server,))
    pro_pool.apply_async(accept_process, args=(server,))
    pro_pool.apply_async(accept_process, args=(server,))
    pro_pool.apply_async(accept_process, args=(server,))

    # 最后一个 任务 print(888),用于测试 进程池里，
    # 有几个进程在 执行任务，实际上 在建立对等套接字任务里，
    # 执行的是while 循环，每一个进程 只能执行一个任务
    # 最后一个任务 无法执行
    pro_pool.apply_async(s)    #

    pro_pool.close()
    pro_pool.join()  # 等所有的子进程 结束任务

"""
一个进程池 
"""












