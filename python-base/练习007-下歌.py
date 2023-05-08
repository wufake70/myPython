# _*_coding :utf-8 _*_
# @Time :2022/5/20 19:03
# @File : 练习007-下歌
# @Project : python-base

import urllib.request
from urllib import request
from bs4 import BeautifulSoup
import re
import requests
import time
# import getpass
import os

# getpass.getuser()，他会返回你当前系统的用户名，比如你当前的用户名是administrator，那么返回字符串adminstrator。
# user_name = getpass.getuser() 但在这里我不需要


class Music(object):
    def __init__(self, baseurl, path):
        head = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
        }
        baseurl = baseurl.replace("#/", "")
        self.baseurl = baseurl
        self.headers = head
        self.path = path

    def main(self):
        html = self.askurl()
        bs4 = self.analysis(html)
        id = self.matching(bs4)
        self.save(id)

    def askurl(self):
        req = request.Request(url=self.baseurl, headers=self.headers)
        response = request.urlopen(req)
        html = response.read().decode("utf-8")
        return html

    def analysis(self, html):
        soup = BeautifulSoup(html, "html.parser")
        bs4 = soup.find_all("li")
        bs4 = str(bs4)
        return bs4

    def matching(self, bs4):
        rule = re.compile(r'href="/song\?id=(\d*?)"', re.S)
        id = re.findall(rule, bs4)
        return id
# 保存
    def save(self, id):
        for i in id:
            print('这是第' + str(i) + '首歌')
            url = "http://music.163.com/song?id=" + i
            req = request.Request(url=url, headers=self.headers)
            response = request.urlopen(req)
            html = response.read().decode("utf-8")
            soup = BeautifulSoup(html, "html.parser")
            bs4 = soup.find_all("title")
            bs4 = str(bs4)
            # 编写一个正则表达式
            rule = re.compile(
                r'<title>(.*?) - (.*?) - 单曲 - 网易云音乐</title>', re.S)
            name = re.findall(rule, bs4)
            name = name[0]
            songname = name[0].replace(r"/", "_")
            singername = name[1].replace(r"/", "_")
            print("正在下载：" + songname + " - " + singername + "……")
            saveurl = "http://music.163.com/song/media/outer/url?id=" + i
            # urllib.request.urlretrieve(saveurl, self.path + songname + " - " + singername + ".mp4") ,无法通过url直接下载
            content = requests.get(url=saveurl, headers=self.headers).content
            # print(type(content))  # content类型为<class 'bytes'>
            with open(self.path + songname + " - " + singername + ".mp4", "wb") as f:
                f.write(content)
            print(songname + " - " + singername + "-----------下载完毕。")
            time.sleep(1)
        return


def getArtistId(content):
    # content = input('请输入歌手名字: ')
    searchUrl = "http://music.163.com/api/search/get/web?csrf_token=hlpretag=&hlposttag=&s=" + \
                content + "&type=100&offset=0&total=true&limit=20"
    result = requests.get(url=searchUrl).json()
    artistList = result['result']['artists'][:3]

    # enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标
    for i, artist in enumerate(artistList):
        number = i + 1
        name = artist['name']
        if 'transNames' in artist:
            name = name + '(' + artist['transNames'][0] + ')'
        print("[" + str(number) + "]: " + name)

    artistNo = int(input('请输入歌手序号: '))
    return artistList[artistNo - 1]['id']


if __name__ == "__main__":
    content = input('请输入歌手的名字：')
    artistid = getArtistId(content)
    artisturl = "http://music.163.com/#/artist?id=" + str(artistid)  # 下载歌手歌曲的url
    path = './file_storage/%s/' % content  # 保存路径

    # 若下载文件夹不存在，则新建
    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path)

    artist_demo = Music(artisturl, path)
    artist_demo.main()
    print("\n全部歌曲下载完毕")