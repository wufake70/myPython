# _*_coding :utf-8 _*_
# @Time :2022/6/6 15:19
# @File : 练习017
# @Project : python-base

import requests
from lxml import etree
import os

# 专爬 https://www.mmm131.com

# 关键词搜索
kw = input('请输入关键词：')
kw = kw.encode('gbk')  # 将字符串进行gbk编码，以便于下面的url传参
# print(kw)
url_search = 'https://www.mmm131.com/search/'  # 注意：URL编码中对中文一切字符不友好，包括 （！ ， ？）
data_search = {
    'keyword': kw,  # 坑点：这里所用的URL编码是gbk（不是utf-8）  %D7%E3%C7%F2（足球）
}

header_search = {
    'Host': 'www.mmm131.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    # 'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Content-Length': '52',
    'Origin': 'https://www.mmm131.com',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Referer': 'https://www.mmm131.com/xinggan/709_3.html',
    'Cookie': 'searchtime=1654514770; Hm_lvt_672e68bf7e214b45f4790840981cdf99=1654493919; Hm_lpvt_672e68bf7e214b45f4790840981cdf99=1654515231',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',

}

response = requests.post(url=url_search, data=data_search, headers=header_search)
# 在此有个坑点，此网站使用字符集（charset）为gbk，需要将源码的原始数据（即二进制数据）进行解码（decode（'gbk'））
content = response.content  # content获取的是二进制数据 ，text直接将源码进行解码（默认情况下用的是Unicode字符集中的utf-8编码规则），因此 就会出现汉字乱码
# print(type(content))
content = content.decode('gbk')
# print(content)  成功获取有效数据

# 解析源码，获取页码总数
tree = etree.HTML(content)
YM = tree.xpath('//ul[@class="newpage"]/a')  # 获取页码总数

# 获取相关的url和标题
for page in range(1, len(YM) + 1):
    url_search = 'https://www.mmm131.com/search/?'  # 注意：URL编码中对中文一切字符不友好，包括 （！ ， ？）
    params_search = {
        'key': kw,
        'page': page
    }
    header_search = {

        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': 'searchtime=1654521094; Hm_lvt_672e68bf7e214b45f4790840981cdf99=1654493813,1654499351,1654500784,1654518200; Hm_lpvt_672e68bf7e214b45f4790840981cdf99=1654521091',
        'Host': 'www.mmm131.com',
        'Referer': 'https://www.mmm131.com/search/',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36',

    }

    response = requests.get(url=url_search, params=params_search, headers=header_search)
    # 在此有个坑点，此网站使用字符集（charset）为gbk，需要将源码的原始数据（即二进制数据）进行解码（decode（'gbk'））
    content = response.content  # content获取的是二进制数据 ，text直接将源码进行解码（默认情况下用的是Unicode字符集中的utf-8编码规则），因此 就会出现汉字乱码
    # print(type(content))
    content = content.decode('gbk')
    # print(content)  成功获取有效的页面源码
    tree_2 = etree.HTML(content)  # 获取标题和链接
    title = tree_2.xpath('//ul[@class="e2"]//li/a[@target="_blank"]//text()')
    href = tree_2.xpath('//ul[@class="e2"]//li/a[@target="_blank"]/@href')
    # 便利并打印以供选择
    for i in range(len(title)):
        print(title[i])
        print(href[i])


data_love = input('请输入以上任何一个链接的重要参数：')

# 定义下载图片函数
def Download(data_love):
    # 创建一个专属文件夹
    pic_name = input('请为图片设置名称：')
    new_folder = r'.\porn_pic_box\%s'  % pic_name
    if not os.path.exists(new_folder):  # 判断文件夹是否重复
        os.makedirs(new_folder)
        print('新文件夹创建成功！！')
    for i in range(1, 51):

        header = {
            'Host': 'img1.hnllsy.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0',
            'Accept': 'image/avif,image/webp,*/*',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Referer': 'https://www.mmm131.com/',  # referer 图片防盗链
            'Sec-Fetch-Dest': 'image',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Site': 'cross-site',
        }

        url_base = 'https://img1.hnllsy.com/pic/%s/%s.jpg' % (data_love, str(i))

        response = requests.get(url=url_base, params=None, headers=header)
        content = response.content

        with open(r'.\porn_pic_box\%s\%s.jpg' % (pic_name, str(i)), 'wb') as fp:
            # 注意：转义字符报错
            fp.write(content)
            fp.close()
            print('这是第%s张美图，别着急' % str(i))

    print('大功告成')


for n in range(99):
    data_love = input('请输入以上任何一个链接的重要参数：')
    Download(data_love)
