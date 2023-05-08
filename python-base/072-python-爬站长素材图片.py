# _*_coding :utf-8 _*_
# @Time :2022/5/14 15:02
# @File : 072-python-爬站长素材图片
# @Project : python-base

import urllib.request
from lxml import etree


# 站长素材的前十页图片爬取
# 第一页地址：https://sc.chinaz.com/tupian/dadanrenti.html
# 第二页地址：https://sc.chinaz.com/tupian/dadanrenti_2.html

def create_request(page):
    if(page == 1):
        url = 'https://sc.chinaz.com/tupian/dadanrenti.html'
    else:
        url = 'https://sc.chinaz.com/tupian/dadanrenti' + '_' + str(page) + '.html'
#    print(url)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0'
               }
    request = urllib.request.Request(url=url, headers=headers)
    return request

def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content

def download(content):
# 下载图片
    # urllib.request.urlretrieve('图片地址', '文件名')
    tree = etree.HTML(content)
# 用xpath来到所有图片的地址以及相应的名字
# //div[@id="container"]//a/img/@src ，@src： 获取img标签中的src（地址）
# 一般图片的网站都会进行懒加载
    tree_src = tree.xpath('//div[@id="container"]//a/img/@src2')
    tree_name = tree.xpath('//div[@id="container"]//a/img/@alt')
#    print(tree_name)
    for i in range(len(tree_name)):
#   print[i]
        name = tree_name[i]
        src = tree_src[i]
#        print(name, src)
        url = 'https:' + src
        print(name, url)
        #urllib.request.urlretrieve(url, 'file_storage/大胆人体/' + name + '.jpg')






start_page = int(input('请输入开始页码：'))
end_page = int(input('请输入结束页码：'))

for page in range(start_page, end_page+1):
#    print(page)
    request = create_request(page)
    content = get_content(request)
    download(content)






























