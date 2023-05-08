# _*_coding :utf-8 _*_
# @Time :2022/5/26 14:16
# @File : 练习12
# @Project : python-base

from selenium import webdriver
from lxml import etree
import time

"""
crawl说明：该脚本只能爬取文字内容，让该网站所有文字不再恶意收费，减少我的   
"""
url = input('请输入您想要的资源的网址：')
path = 'chromedriver.exe'
browser = webdriver.Chrome(path)
# url = 'http://www.creditsailing.com/CeHuaShu/1408780.html'
browser.get(url)

# 点击全文阅读
content_content = browser.find_element_by_xpath('//b[@class="btn"]')
content_content.click()

# 获取网页源码 page_source
tree = browser.page_source

# 滑到底部获取完整资源
# for i in range(1, 110):
#     time.sleep(0.01)
#     js_button = 'document.documentElement.scrollTop=%d000' % i
#     browser.execute_script(js_button)

# 爬取想要的文字
# 用xpath解析
tree = etree.HTML(tree)
print(tree)  # 控制台输出 <Element html at 0x1f7fbe977c0>
fp_title = tree.xpath('//div[@class="left_one"]/h1/text()')
word = tree.xpath('//div[@class="left_one"]//p/text()')
# fp_title = tree.xpath('//div[@class="newsDetail"]/h1/text()')
# word = tree.xpath('//div[@class="jz_fix_ue_img"]//p/text()')

# 创建一个新文件
with open('./file_storage/高考升学网/%s.txt' % (fp_title[0]), 'a', encoding="utf-8") as fp:
    for i in range(len(word)):
        fp.write(word[i] + '\n')
        print(word[i])

a = '😁😁😁😁😁'
print("大功告成\n" + a * 9)
