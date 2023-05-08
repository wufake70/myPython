# _*_coding :utf-8 _*_
# @Time :2022/7/13 16:19
# @File : 测试_001
# @Project : python_NCRE

import pywifi
from pywifi import const  # 引用一些定义
import time

wifi = pywifi.PyWiFi()
iface = wifi.interfaces()[0]
print(iface.name())  # wlan设置的描述属性 Intel(R) Wi-Fi 6 AX201 160MHz
print(iface.scan())  # 扫描WiFi接口（AP ,access point 接口)
print(len(iface.scan_results()))  # 接口数量
print(iface.scan_results())


iface.add_network_profile()
print(iface.network_profiles())  # 返回已连接 WiFi 内存地址

