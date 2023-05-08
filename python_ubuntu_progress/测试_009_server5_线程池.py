# _*_coding :utf-8 _*_
# @Time :2022/8/14 11:09
# @File : 009_server5_线程池
# @Project : python_ubuntu_progress

import socket
import datetime
from multiprocessing.pool import ThreadPool
from multiprocessing import Pool, cpu_count


def receive_message(conn, addr):
    while True:
        message = conn.recv(1024).decode('utf-8')
        now = datetime.datetime.now().strftime('%H:%M')
        if not message:
            print(f'ip:{addr[0]}:{addr[1]},time:{now}:…退出聊天室…')
            conn.close()
        else:
            print(f'ip:{addr[0]}:{addr[1]},time:{now}:{message}')


if __name__ == "__main__":
    server = socket.socket()  # 创建服务端套接字对象
    server.bind(('127.0.0.1', 9003))  # 服务端绑定的ip及端口
    server.listen(10)  # 限制最大监听数
    print("……等待客户端链接……")

    n = cpu_count()  # 获取 CPU核心数
    tm = ThreadPool(n)  # 开启 最合适的线程数
    while True:
        conn, addr = server.accept()
        now = datetime.datetime.now().strftime('%H:%M')
        print(f'iP:{addr[0]}:{addr[1]},time:{now}: 连接成功……')
        tm.apply_async(receive_message, args=(conn, addr))
        # 主线程 执行 创建对等连接套接字
        # 线程池 里面 执行对 客户端数据的 处理

        # ##线程池并发服务器 与多线程并发服务器的区别:
        # 线程池…是开启 多个线程 共同完成 所有任务
        # 多线程…一个线程 只执行 一个任务,多个任务 需要开启 多个线程。







