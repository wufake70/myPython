# _*_coding :utf-8 _*_
# @Time :2022/7/21 0:20
# @File : 测试_001
# @Project : python_ubuntu

import socket
server = socket.socket()
server.setblocking(False)
server.bind(('127.0.0.1', 9999))

server.listen(1)

conn, addr = server.accept()
print('nnn')

conn.setblocking(False)

a = conn.recv(1024)
print(a.decode('utf-8'))

print('nihao')






















