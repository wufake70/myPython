# _*_coding :utf-8 _*_
# @Time :2022/7/20 13:15
# @File : python_WiFi密码本
# @Project : python_NCRE
import json
import os

if not os.path.exists(r'.\WiFi密码类型'):
    os.mkdir(r'.\WiFi密码类型')

ls_num = [chr(i) for i in range(48, 58)]
print(ls_num)           # 数字['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
ls = []
with open(r'.\WiFi密码类型\纯数字(8).txt', 'a') as fp:
    for l_1 in ls_num:
        for l_2 in ls_num:
            for l_3 in ls_num:
                for l_4 in ls_num:
                    for l_5 in ls_num:
                        for l_6 in ls_num:
                            for l_7 in ls_num:
                                for l_8 in ls_num:
                                    ls.append(''.join([l_1, l_2, l_3, l_4, l_5, l_6, l_7, l_8]))
        print('加速中')
    print(len(ls))          # 共一亿个
    ls = json.dumps(ls)     # 将Python 转为 JSON字符串
    print('密码列表加载完了,正在写入')
    fp.write(ls)            # 写入 磁盘（TXT文本） 容量 1一个G ，所耗时间 5分钟左右
"""
运行过程中，程序所占内存 一直飙升 直至 8个g 
Python 暴力破解 WiFi 不可行
"""

print('program over')


















