# _*_coding :utf-8 _*_
# @Time :2022/5/21 20:57
# @File : 088-python-requests-cookie登录
# @Project : python-base

import requests
from lxml import etree

# 登录页面的url地址
url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0'
           }
response = requests.get(url=url, headers=headers)
content = response.text
print(content)

# 解析页面源码，然后获取重要参数（被设置为隐藏域）_VIEWSTATE, __VIEWSTATEGENERATOR
tree = etree.HTML(content)
VIEWSTATE = tree.xpath('//input[@id="__VIEWSTATE"]/@value')
VIEWSTATEGENERATOR = tree.xpath('//input[@id="__VIEWSTATEGENERATOR"]/@value')
# 解析后得到的数据类型为列表型
print(VIEWSTATE[0])
print(VIEWSTATEGENERATOR[0])

# 获取验证码图片
code = tree.xpath('//img[@id="imgCode"]/@src')
# print(code[0])
code_url = 'https://so.gushiwen.cn' + code[0]
# print(code_url)

# 获取验证码的图片链接，下载到本地，观察后人工填写
# 注意：不能使用urlretrieve,进行下载
session = requests.session()
# 这里的session与下面的下载图片的session是同步的
response_code = session.get(code_url)
# 注意此时需要使用二进制的数据（即比特类型），用来下载图片
content_code = response_code.content  # content 返回比特类型数据
# wb模式就是将二进制写入文件中
# 注意：open函数只能创建文件 不能创建文件夹，文件夹要使用 os库
with open('./file_storage/code.jpg', 'wb')as fp:
    # 在这里可以将图片的链接给打印出来以方便直接 查看验证码图片
    print('file:///C:/Users/yui/Desktop/my-python/python-base/file_storage/code.jpg')
    fp.write(content_code)
    fp.close()

im_gcode = input('请输入您的验证码：')

# 模拟登录
url_post = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
data_post = {
'__VIEWSTATE': VIEWSTATE,
'__VIEWSTATEGENERATOR': VIEWSTATEGENERATOR,
'from': 'http://so.gushiwen.cn/user/collect.aspx',
'email': '13765450541',
'pwd': 'zxcvbnm',
'code': im_gcode,
'denglu': '登录',
}

# 这里的session与上面的下载图片的session是同步的
response_post = session.post(url=url, headers=headers, data=data_post)
content_post = response_post.text
with open('./file_storage/gushiwendengluyemian.html', 'w', encoding='utf-8')as fp:
    fp.write(content_post)
    fp.close()
# 这里也直接把登录页面的文件 本地地址 给打印出来，注意：创建文件名的时候尽量用英文来写，因为url编码会对中文进行编码（对中文不友好）
print('file:///C:/Users/yui/Desktop/my-python/python-base/file_storage/gushiwendengluyemian.html')






















