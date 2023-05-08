# _*_coding :utf-8 _*_
# @Time :2022/6/7 10:17
# @File : 练习018
# @Project : python-base

import requests
import os


def data():
    for i in range(4322, 4350):
        data_love = i
        pic_name = i
        Download(data_love, pic_name)


def Download(data_love, pic_name):
    # 创建一个专属文件夹
    # pic_name = input('请为图片设置名称：')
    new_folder = r'.\porn_pic_box\%s' % pic_name
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
            # print('这是第%s张美图，别着急' % str(i))
            if os.path.getsize(r'.\porn_pic_box\%s\%s.jpg' % (pic_name, str(i))) < 20000:   # 判断文件的大小
                # os.rmdir(r'.\porn_pic_box\%s\%s.jpg' % (pic_name, str(i)))   该方法只能删除文件夹
                break


print('crawl开始了')
data()
