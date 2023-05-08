# _*_coding :utf-8 _*_
# @Time :2022/5/18 16:38
# @File : 081-python-selenium交互
# @Project : python-base


from selenium import webdriver
path = 'msedgedriver.exe'
browser = webdriver.Edge(path)
url = 'https://www.baidu.com/'
browser.get(url)

# 导入定时器
import time
# 睡眠两秒
time.sleep(2)
# 获取百度输入框的对象
input = browser.find_element_by_id('kw')
# 在输入框中输入周杰伦
input.send_keys('周杰伦')
# 在点击按钮搜索
button = browser.find_element_by_id('su')
button.click()
time.sleep(1)
# 在滑动此时的页面到底部
js_botton = 'document.documentElement.scrollTop=5000'
browser.execute_script(js_botton)
time.sleep(1)
# 获取下页的路径
next = browser.find_element_by_xpath('//a[@class="n"]')
# 点击下一页
next.click()
# 回到上一页
time.sleep(1)
browser.back()
time.sleep(1)
browser.forward()
time.sleep(1)
# 退出浏览器
browser.quit()



































