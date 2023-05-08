# _*_coding :utf-8 _*_
# @Time :2022/8/4 20:25
# @File : python标准库_socket
# @Project : python_NCRE

import socket

"""     向服务器发送消息
### 服务器代码
# 创建服务器套接字对象，通过这个socket对象完成连接
server = socket.socket()            默认协议 tcp

# 给服务器端套接字 绑定 本机ip 和端口
server.bind(('127.0.0.1', 8889))
# 设置最大监听数量
server.listen(5)

#### 等待客户端链接,accept() 方法 创建与客户端链接的 对等链接套接字
# 注意: accept会阻塞 程序，等待客户端链接，连接后继续运行
conn, addr = server.accept()  # 元祖拆包
# print(server.accept()) print(conn)         # 返回链接信息 <socket.socket fd=440, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 8889), raddr=('127.0.0.1', 1385)> 
# print(addr)         返回 ('127.0.0.1', 1385) 

####recv()方法 接收客户端数据数据
# recv也会阻塞程序，等待连接的客户端把数据传输过来，继续往后执行
message = conn.recv(1024).decode('utf-8')

print(message)
conn.close()                # 关闭链接
server.close()              # 关闭 套字节


#### 客户端 代码

import socket

client = socket.socket()

client.connect(('127.0.0.1', 8889))         # 链接服务主机
client.send('你好'.encode('utf_8'))         # 发送消息
client.close()
"""

"""  多人聊天室代码
####        服务器代码
import socket
import datetime
from collections import deque  # deque,这个对象类似于list列表，不过可以操作它的“两端”

server = socket.socket()
server.setblocking(False)           # 设置成非阻塞
server.bind(('127.0.0.1', 9999))  # 只能连接本机ip(解释器所在的主机) 或者用 回环地址127.0.0.1
server.listen(5)
connections = deque()

print('等待客户端链接……')
while True:
    try:                # 设置成非阻塞时 需要使用异常，防止报错终止程序
        # conn, addr = server.accept()  # 对等链接套字节，并拆包
        # c_ip, c_port = addr     # 元祖拆包，获取ip和port
        accept = server.accept()
        conn, addr = accept
        c_ip, c_p = addr

    except BlockingIOError as e:        # BlockingIOError: [WinError 10035] 无法立即完成一个非阻止性套接字操作。
        pass
    else:               # 没有异常，直接运行
        print('...客户端连接成功', f'ip:{c_ip},加入聊天室')

        conn.setblocking(False)     # 非阻塞
        connections.append(accept)    # 将客户端的链接对象 保存到列表

    now = datetime.datetime.now().strftime('%H:%M')     # 时间的 格式化输出

    for i in connections:
        try:  # 设置成非阻塞时 需要使用异常，防止报错终止程序
            message = i.recv(1024)      # 接收 客户端数据，注意用变量保存，方便后面使用
            if not message:     # 判断返回的数据 内容是否为空
                continue
            print(f'ip:{i[1][0]},time:{now}:', message.decode('utf-8'))
        except BlockingIOError as e:
            pass


####    客户端代码
import socket
client = socket.socket()
try:
    client.connect(('127.0.0.1', 9999))
except ConnectionRefusedError as e:
    print('无法链接服务器，请稍后重试')
except Exception as e:
    print('未知异常，请联系管理员')
else:
    while True:
        ins = input('请输入：')
        if not ins:
            break
        ins_b = ins.encode(encoding='utf_8')
        client.send(ins_b)
finally:
    client.close()


"""
























