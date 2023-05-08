# _*_coding :utf-8 _*_
# @Time :2022/8/3 21:27
# @File : 测试_005
# @Project : python_ubuntu_progress

import socket
import datetime
import multiprocessing

# from collections import deque       # 相当于两端可操作的列表

server = socket.socket()
server.setblocking(False)           # 非 阻塞
server.bind(('127.0.0.1', 9999))  # 只能连接本机ip(解释器所在的主机) 或者用 回环地址127.0.0.1
server.listen(5)
connections = []  # 使用列表 保存 已连接的客户端，以便于接受 每个客户端数据（消息）


def fun():
    print('等待客户端链接……')
    while True:                    # 轮询 过程， # 1.是否有客户端链接响应、
        try:                                     # 2.已连接的客户端 是否 发来数据
            # conn, addr = server.accept()  # 阻塞
            # c_ip, c_port = addr
            accept = server.accept()
            conn, addr = accept
            c_ip, c_p = addr
            # accept[0].close()
        except BlockingIOError as e:
            pass
        else:
            print('...客户端连接成功', f'ip:{c_ip},加入聊天室')

            conn.setblocking(False)
            connections.append(accept)

            # out_b = conn.recv(1024)  # 阻塞

            # if not out_b:               # 判断是否结束会话
            #     print('退出聊天室')
            #     break
            # out = out_b.decode('utf-8')
        now = datetime.datetime.now().strftime('%H:%M')
        # print(f'{c_ip}:{c_port},当前时间为{now}:\n{out}')
        # print(connections)
        for i in connections:
            # if not i.recv(1024):  # 判断是否 离线
            #     print(f"{c_ip};{c_port},退出聊天室")
            #     break
            try:
                message = i[0].recv(1024)           # conn.recv(1024)
                # ConnectionResetError: [WinError 10054] 远程主机强迫关闭了一个现有的连接。

                de_message = message.decode('utf-8')
                if not message:
                    continue
                elif de_message == 'exit':
                    print(f'ip:{i[1][0]},time:{now}:退出聊天室')
                    i[0].close()        # 关闭对应 对等链接套接字
                    connections.remove(i)

                else:
                    print(f'ip:{i[1][0]},time:{now}:', de_message)

                    # 发送客户端
                    #sendto(de_message.encode('utf-8'),i[1])
                    i[0].sendto('你好'.encode('utf-8'),i[1])

            except BlockingIOError as e:
                pass


if __name__ == "__main__":
    p1 = multiprocessing.Process(target=fun)
    # p1.start()
    fun()

