# _*_coding :utf-8 _*_
# @Time :2022/5/19 19:51
# @File : 练习005-使用selenium爬取百度图片
# @Project : python-base


import os
from selenium import webdriver
import urllib.request
from lxml import etree
import time
import urllib.parse
from selenium.webdriver.chrome.options import Options

# headless基本配置无界面浏览器
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
chrome_options.binary_location = path
# 实例化了一个浏览器对象(一定要传入浏览器的驱动程序)
wd = webdriver.Chrome(chrome_options=chrome_options)

word = input('请输入您要搜索的thing：')
word_1 = urllib.parse.quote(word)

# 打开网站
wd.get('https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=index&fr=&hs=0'
       '&xthttps=000000&sf=1&fmq=&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word='
       + word_1 + '&oq=%E6%9D%8E%E6%99%BA%E6%81%A9&rsp=-1')

# UA伪装请求头
header = {
   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                 'Chromeh/81.0.4044.138 Safari/537.36 '
}

# 获取返回的源码 ，.page_source
# 此时获取的网页源码只有第一页的数据
# page_text = wd.page_source

# 类型字符串
# print(page_text)
# print(type(page_text))

# 执行一个js脚本，
# for循坏模拟手动滑动页面
for t in range(0, 10):
    # print(t)
    # 获取的数据直接与接收到数据包有关
    time.sleep(0.5)
    scroll_bottom = 'document.documentElement.scrollTop=%d0000' % (t)
    wd.execute_script(scroll_bottom)
time.sleep(3)


# 网页标签中的<div class="imgpage">会随着页面的向下滑动而增加--懒加载技术
page_text = wd.page_source
tree = etree.HTML(page_text)
picture = tree.xpath('//div[@class="imgpage"]//img//@src')
# 获取图片链接成功
#print(picture)
# 判断图片的数量
print(len(picture))


# 使用 os 创建一个文件夹  ==============
new_folder = './%s/%s/' % ('file_storage', word)
if not os.path.exists(new_folder):  # 是否存在这个文件夹
    print('ok，创建文件夹成功')
    os.makedirs(new_folder)  # 如果没有这个文件夹，那就创建一个
# =========================================

# 遍历链接并下载
for i in range(1, len(picture)):
    # print(picture[i])
    if 'data' in picture[i]:
        print('该link太长了，跳过')
    else:
        url = str(picture[i])
        # print(type(url))

        urllib.request.urlretrieve(url, new_folder + str(i) + '.jpeg')
        print('一下载第' + str(i) + '图片了')

print('代码结束，大功告成！！')
























