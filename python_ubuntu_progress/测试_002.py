# _*_coding :utf-8 _*_
# @Time :2022/8/3 11:00
# @File : 测试_002
# @Project : python_ubuntu_progress

import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('127.0.0.1', 1234))
    s.listen(5)
    c, addr = s.accept()

    with c:
        print(addr, 'connected.')

        while True:
            data = c.recv(1024)
            if not data:
                break
            c.sendall(data)






















