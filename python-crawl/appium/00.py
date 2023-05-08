"""

安装对应的包文件
pip install pip install Appium-Python-Client -i https://pypi.tuna.tsinghua.edu.cn/simple

"""


# from appium import webdriver
# from selenium.webdriver.common.by import By
import time,re,os
from datetime import datetime


# info = {
#     # 手机使用的系统名
#     'platformName':'android',
#     # 手机使用的系统版本号
#     'platformVersion':'11.0',
#     # adb连接的手机设备号
#     'deviceName':'815c1faf',
#     # # 指定打开的应用包名
#     'appPackage':'com.android.settings',
#     # # 指定打开的应用进程名
#     'appActivity':'.Settings',
#     # 禁止初始化操作（避免删除登录信息）
#     'noReset':True
# }

# driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',info)
# driver.tap([(700, 700)],300)

# driver.set_clipboard_text('你好啊')
# print(driver.get_clipboard_text())

# # driver.quit()


a = [1,333,3,3,3,3]

[a.append(i) for i in [9,9,9,9]]
a.remove(3)
print(a)
print(13 in a)
print(a[-1])

# for i in a: print(a.index(i))
for i in range(2):
    i = 0
    # print(i)

# print('A'.capitalize())
a = 'hello world'
for i in 'orll':
    if i in a: a = a.replace(i,'')

print(a)
print(os.getcwd())
print(os.popen('echo %cd%').read())
print(os.getcwd() + r"\appium\报错图.png")

print(datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))
print(0%3)
a = 'hello world'

print(re.match("h ",a) is None)
print(re.match('\d{1,2}.\d{1,2}','33'))

a = [8,0,82,3]  
a.pop(0)
a.pop(1)
print(a)

b = '99988yhjfdakj'
for i in '998y': b = b.replace(i,'')
print(b)
print(type(' ') == str)
a = ''
print(re.match('\d{0,1}',a))
# exit()
print('abc'.index('a'))
a = ['jioeow\n','fkdak']
for i in a:
    a[a.index(i)] = i.replace('\n','')
print(a)
print('‘' == '’')
print('、'=='、')
