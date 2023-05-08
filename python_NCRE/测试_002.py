# _*_coding :utf-8 _*_
# @Time :2022/7/25 14:33
# @File : 测试_002
# @Project : python_NCRE
import socket

# print(socket.gethostbyname('127.0.0.1'))
client = socket.socket()

try:
    client.connect(('192.168.80.152', 9998))

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












