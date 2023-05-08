import datetime
import socket  # 套接字模块
import multiprocessing  # 多进程模块
import threading  # 多线程模块


# 数据处理的任务
def handle(conn, addr,ip_port):  # 对等连接套接字中的conn
    # 加入while循环去处理数据
    while True:
        """
        recv_data = conn.recv(1024).decode('utf-8')  # 服务端接收到的客户端的数据
        if recv_data:  # 如果有数据就打印，并发送给客户端
            now = datetime.datetime.now().strftime('%H:%M')
            print(f'ip:{addr[0]},time:{now},', recv_data)
            conn.send(recv_data.encode('utf-8'))    # 会发给 客户端
        else:  # 没有数据就把conn关闭，并结束循环
            conn.close()
            break
        """
        message = conn.recv(1024).decode('utf-8')
        now = datetime.datetime.now().strftime('%H:%M')
        if not message:
            print(f'ip:{addr[0]},time:{now}:…退出聊天室…')
            conn.close()
        else:
            print(f'ip:{addr[0]},time:{now}:{message}')
            # 发送给 其他 客户端
            if len(ip_port) >= 2:
                conn.sendto(message.encode('utf-8'), ip_port[1])
                # NameError: name 'ip_port' is not defined


# 不断生成对等连接套接字，等待客户端接入
if __name__ == "__main__":
    server = socket.socket()  # 创建服务端套接字对象
    server.bind(('127.0.0.1', 9998))  # 服务端绑定的ip及端口
    server.listen(10)  # 限制最大监听数
    print("……等待客户端链接……")
    ip_port = []        # 保存已建立连接的 ip和port
    while True:
        conn, addr = server.accept()
        now = datetime.datetime.now().strftime('%H:%M')
        print(f'iP:{addr[0]},time:{now}: 连接成功……')
        ip_port.append(addr)
        # conn.setblocking(False)
        # 实例化一个进程对象帮我们做事情
        p1 = multiprocessing.Process(target=handle, args=(conn,addr,ip_port))
        p1.start()

        # 实例化一个线程对象帮我们做事情
        # t1 = threading.Thread(target=handle , args=(conn,))
        # t1.start()
