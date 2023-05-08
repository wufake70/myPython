from appium import webdriver
# import 
import time
# from selenium.webdriver.common.by import By

info = {
    'platformName':'android',
    'platformVersion':'11.0',
    'deviceName':'815c1faf',
    # 'deviceName':'Z81QAFYHG7XQ2',

    # 'appPackage':'com.android.settings',
    # 'appActivity':'.Settings',      
          
    'noReset':True
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',info)

# time.sleep(3)

# 1.跳转 短信界面
# driver.start_activity('com.android.mms','.ui.ConversationList')

# 2.获取当前的包名和界面名
# c_p, c_a = driver.current_package, driver.current_activity
# print("当前包名为: %s\n当前界面名为: %s" % (c_p,c_a))

# 3.关闭app和驱动程序(driver)
# driver.close_app()      # 关闭后 driver对象 还在，不会报错
# driver.quit()         # 关闭后 driver对象 不存在了
# c_p, c_a = driver.current_package, driver.current_activity
# print("当前包名为: %s\n当前界面名为: %s" % (c_p,c_a))

# 4.安装和卸载、判断是否安装
# 判断 学习通是否安装 ，。。。。
isTure = driver.is_app_installed('com.chaoxing.mobile')
# if isTure:
#     driver.remove_app('com.chaoxing.mobile')
#     print('已卸载')
# else:
#     # driver.install_app('电脑端路径')
#     print('已安装')
    
# 5.将应用 置于后台 5秒 在返回前台
# driver.background_app(5)

# 6.坐标点击 tap
# driver.tap([(500,1000)],3)
# print("99999")

# 7.scroll 有惯性 可以传入 duration；drag_and_drop 惯性 很小
# e = driver.find_element_by_xpath("//*[@text='桌面与锁屏']")
# e2 = driver.find_element_by_xpath("//*[@text='设置']")
# driver.scroll(e,e2,6000)


# 8.息屏/亮屏
# driver.lock()
# driver.unlock()

# 9.按键模拟
# driver.press_keycode(26)        # 电源键
# driver.press_keycode(4)         # home键
# driver.press_keycode(3)         # 返回键     
# driver.press_keycode(82)        # 菜单键 在不同 界面 不一样
# driver.press_keycode(7)         # 搜索键 在桌面使用
# driver.long_press_keycode(26,5)

# 10.截屏
# driver.get_screenshot_as_file(r"c:\Users\yui\Desktop\screen.png")

# 11.获取和设置手机网络
# msg = driver.network_connection
# print(msg)
# driver.set_network_connection(2)

"""
+--------------------+------+------+---------------+
            | Value (Alias)      | Data | Wifi | Airplane Mode |
            +====================+======+======+===============+
            | 0 (None)           | 0    | 0    | 0             |
            +--------------------+------+------+---------------+
            | 1 (Airplane Mode)  | 0    | 0    | 1             |        飞行模式
            +--------------------+------+------+---------------+
            | 2 (Wifi only)      | 0    | 1    | 0             |
            +--------------------+------+------+---------------+
            | 4 (Data only)      | 1    | 0    | 0             |        只用流量
            +--------------------+------+------+---------------+
            | 6 (All network on) | 1    | 1    | 0             |
            +--------------------+------+------+---------------+
"""

# 12.操作手机的通知栏
# driver.open_notifications()
# time.sleep(4)
# driver.back()


# 13.高级手势
from appium.webdriver.common.touch_action import TouchAction
t_a = TouchAction(driver)   # 创建对象
# t_a.tap(None,500,1000)    # 实现轻敲
# t_a.perform()
# t_a.press(None,500,1200).wait(3000).release().perform() # 因为这些方法 返回的都是 self，可连续调用
# t_a.tap(driver.find_element_by_xpath("//*[contains(@text,'测验')]")).perform()


# 切换输入法


driver









