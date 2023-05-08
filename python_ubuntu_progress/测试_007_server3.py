# _*_coding :utf-8 _*_
# @Time :2022/8/5 23:01
# @File : 测试_007_server3
# @Project : python_ubuntu_progress

import socket
import selectors     # io 多路复用选择器（事件驱动）
import datetime

# selectors.DefaultSelector()         # 使用默认的复用器，根据不同的操作系统
import time

epoll_select = selectors.EpollSelector()  # linux  常用 复用器epoll

server = socket.socket()
server.setblocking(False)
server.bind(('127.0.0.1', 9001))
server.listen(4)

# 任务函数二 接收 客户端的消息
def receive(conn):
    # print(7)
    ip, port = conn.getpeername()           # 获取 对应的ip 和 端口号
    now = datetime.datetime.now().strftime('%H:%M')
    message = conn.recv(1024)
    de_message = message.decode('utf-8')
    if de_message == 'exit':                    # 客户端 正常退出
        epoll_select.unregister(conn)           # 删除掉 已注册的 任务，关闭 对应的 对等套接字
        conn.close()                            # 可以不用
        print(f"{ip},{now}:退出聊天室")
        return
    elif de_message == '':                      # 防止 客户端 被叉掉，进入循环
        epoll_select.unregister(conn)           # 删除掉 已注册的 任务，关闭 对应的 对等套接字
        conn.close()                            # 需要 删除 已注册的任务 ，才关闭 对等套接字，否则在此运行客户端 会 KeyError: "<socket.socket fd=5, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 9998), raddr=('127.0.0.1', 36228)> (FD 5) is already registered"
        print(f"{ip},{now}:退出聊天室")
        return

    try:
        print(f"{ip},{now}:", de_message)
    except OSError as e:
        print(e)
        pass


# 任务函数1，接收客户端响应 连接
def accept(server):
    conn, addr = server.accept()
    print(addr[0],addr[1], '连接成功')
    # print(conn)  # <socket.socket fd=5, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 9998), raddr=('127.0.0.1', 59992)>

    # 复用器, 注册任务 监听 已连接用户端的消息 调用接收数据的 任务函数
    epoll_select.register(conn, selectors.EVENT_READ, receive)


# 复用器 注册任务，监听服务套接字，有没有客户端链接
epoll_select.register(server, selectors.EVENT_READ, accept)

print('等待客户端连接……')
while True:
    event = epoll_select.select()       # 多路复用器一直查询(阻塞状态)，有没有 注册任务(对等套字节，用户端数据)发生，
    # print(event)
    # 对等连接事件 [(SelectorKey(fileobj=<socket.socket fd=4, family=AddressFamily.AF_INET,type=2049, proto=0, laddr=('127.0.0.1', 9999)>, fd=4, events=1, data=<function accept at 0x7fe5dab9fea0>), 1)]
    # 客户端消息事件 [(SelectorKey(fileobj=<socket.socket fd=5, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 9998), raddr=('127.0.0.1', 56254)>, fd=5, events=1, data=<function receive at 0x7f00be7a6488>), 1)]
    for key, mask in event:         # 元祖拆包
        # print(key)
        func = key.data
        # print(func)                 # <function accept at 0x7f975fd64b70>
        func(key.fileobj)               # 执行对等链接套接字 accept函数 / 执行receive函数
        #  print(key.fileobj) 对等连接事件 # <socket.socket fd=4, family=AddressFamily.AF_INET, type=2049, proto=0, laddr=('127.0.0.1', 9999)>
        # 客户端消息事件 fileobj=<socket.socket fd=5, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 9998), raddr=('127.0.0.1', 56254)>
        # 客户端消息事件 中的 fileobj 与 receive函数 中的conn 参数 是一样的


"""
1.多路复用器 阻塞状态？
2.多路复用器 接收到相关 任务响应，执行相关代码时，任然会错过 用户端响应？
3.更及时的接收 用户端的响应 或数据（比较于 非阻塞）
4.bug 客户端代码启动后，直接 叉掉，服务端 进入循环状态
5.fd 是什么意思？         文件描述符，用于区分 不同的 IO流
6.epoll_select.register(conn, selectors.EVENT_READ, receive) conn 和 receive 什么关系
8. 需要 删除 已注册的任务 ，才能关闭 对等套接字 否则 在运行客户端 会报错 KeyError: "<socket.socket fd=5, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 9998), raddr=('127.0.0.1', 41752)> (FD 5) is already registered"
7.客户端 退出了，需要 conn.close() 关闭 对链接套接字？  是的
9.客户端消息事件 中的 fileobj 与 receive函数 中的conn 参数 是一样的？

"""





























