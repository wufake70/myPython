# _*_coding :utf-8 _*_
# @Time :2022/8/4 8:33
# @File : 测试_003
# @Project : python_NCRE

# client.py
import socket


client = socket.socket(family=socket. AF_INET, type=socket.SOCK_STREAM)
host = socket.gethostname()
client.connect(('192.168.80.152', 9999))


while True:
    data = input("客户端发送数据：").strip()

    client.send(data.encode("utf-8"))
    if data == "end":
        client.close()
        break

