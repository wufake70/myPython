# _*_coding :utf-8 _*_
# @Time :2022/8/3 21:43
# @File : 测试_006
# @Project : python_ubuntu_progress

import socket
import time
import multiprocessing


def sd():
    while True:
        ins = input(':')            # 在控制台 输入与输出 看起来美观
        if not ins:
            client.send('exit'.encode('utf-8'))  # 客户端退出连接
            client.close()
            break
        ins_b = ins.encode(encoding='utf_8')
        client.send(ins_b)
        # receive()
        # message = client.recv(1024).decode('utf-8')
        # print(message)


def receive(client):          # 接收服务端数据
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            time.sleep(0.09)
            print(f'服务端:{message}')

        except OSError as e:
            print(e)
            # 由于套接字没有连接并且(当使用一个 sendto 调用发送数据报套接字时)
            # 没有提供地址，发送或接收数据的请求没有被接受
            pass


if __name__ == "__main__":
    client = socket.socket()
    try:
        client.connect(('127.0.0.1', 9004))
        print('…服务器连接成功…')

    except ConnectionRefusedError as e:
        print('无法链接服务器，请稍后重试')

    except Exception as e:
        print(e)
        print('未知异常，请联系管理员')

    else:
        p1 = multiprocessing.Process(target=receive, args=(client,))
        p1.start()

        sd()

    finally:
        client.close()

























