from appium import webdriver
# from selenium.webdriver.common.by import By


info = {
    # 手机使用的系统名
    'platformName':'android',
    # 手机使用的系统版本号
    'platformVersion':'11.0',
    # adb连接的手机设备号
    'deviceName':'815c1faf',  #(序列号) 当使用网络adb 连接时 可写 "ip:port"   
    # 'deviceName':'192.168.0.39:5669',
    # 'udid':'192.168.0.39:5669',    ##### 在虚拟机(vmos)中 必须使用 "udid"


    # 设置界面
    # # 指定打开的应用包名
    'appPackage':'com.android.settings',
    # # 指定打开的应用进程名
    'appActivity':'.Settings',      

    # 微信主界面
    # 'appPackage':'com.tencent.mm',
    # 'appActivity':'.ui.LauncherUI' ,
    
          
    # 禁止初始化操作（避免删除登录信息）
    'noReset':True
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',info)

# driver.quit()  脚本停止


# 注意事项: 必须打开开发者模式
#           必须启用 "usb调试"
#               OPPO 手机 需要 启用 "禁止权限监控" 
#               魅族













