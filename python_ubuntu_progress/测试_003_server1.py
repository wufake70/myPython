# _*_coding :utf-8 _*_
# @Time :2022/8/3 20:58
# @File : 测试_003
# @Project : python_ubuntu_progress

import socket

# 创建服务器套接字对象，通过这个socket对象完成连接
server = socket.socket()

# 给服务器端套接字 绑定 本机ip 和端口
server.bind(('127.0.0.1', 8889))
# 设置最大监听数量
server.listen(5)

# 等待客户端链接,创建与客户端链接的 对等链接套接字
# 注意: accept会阻塞 程序，等待客户端链接，连接后继续运行
conn, addr = server.accept()  # 元祖拆包
# print(server.accept()) print(conn)         # 返回链接信息 <socket.socket fd=440, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 8889), raddr=('127.0.0.1', 1385)>
# print(addr)         返回 ('127.0.0.1', 1385)

# 接收数据
# recv也会阻塞程序，等待连接的客户端把数据传输过来，继续往后执行
message = conn.recv(1024).decode('utf-8')

print(message)
conn.close()
server.close()























