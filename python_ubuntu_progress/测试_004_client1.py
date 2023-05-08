# _*_coding :utf-8 _*_
# @Time :2022/8/3 21:05
# @File : 测试_004
# @Project : python_ubuntu_progress

import socket
import time

client = socket.socket()

client.connect(('127.0.0.1', 9999))         # 链接服务主机

time.sleep(8)
client.send('你好'.encode('utf_8'))         # 发送消息
client.close()
