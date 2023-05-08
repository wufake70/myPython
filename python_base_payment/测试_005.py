import requests
from selenium import webdriver
import time


url = 'https://www.8090g.cn/?url=https://v.qq.com/x/cover/mzc00200p51jpn7/z0043cus21w.html?ptag=10523'
url = 'https://jx.quanmingjiexi.com/?url=https://www.iqiyi.com/v_1obcoxn2g7w.html?vfm=2008_aldbd&fv=p_02_01'
path = 'chromedriver.exe'
# path_1 = 'msedgedriver.exe'

browser = webdriver.Chrome()

browser.get(url)

frame = browser.find_element_by_tag_name('iframe')
browser.switch_to.frame(frame)
# frame_2 = browser.find_element_by_id('WANG')
# browser.switch_to.frame(frame_2)
# frame_3 = browser.find_element_by_id('iframepage')
# browser.switch_to.frame(frame_3)
# frame_4 = browser.find_element_by_id('WANG')
# browser.switch_to.frame(frame_4)



time.sleep(4)


response_1 = browser.page_source
print(response_1)

























