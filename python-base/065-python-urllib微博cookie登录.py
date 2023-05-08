# _*_coding :utf-8 _*_
# @Time :2022/5/12 16:32
# @File : 065-python-urllib微博cookie登录
# @Project : python-base


# 使用场景：数据采集的时候，需要绕过登录，然后进入到某个页面
import urllib.request
import urllib.parse
import json

url = 'https://m.weibo.cn/profile/info?uid=6602743011'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0',
 'accept': 'application/json, text/plain, */*',
 #'accept-encoding': 'gzip, deflate, br',
 'accept-language': 'zh-CN,zh;q=0.9',
 'cookie': 'WEIBOCN_FROM=1110006030; SUB=_2A25PeLazDeRhGeBI61AW9C3Myj2IHXVsgtr7rDV6PUJbkdANLWnDkW1NRqfjTWRl4SHMdyJCMPJF8SWZnMzUFBVP; _T_WM=24938002797; MLOGIN=1; XSRF-TOKEN=7166bb; M_WEIBOCN_PARAMS=luicode%3D20000174%26lfid%3D231016_-_selffans%26uicode%3D20000174',
 'mweibo-pwa': '1',
 'referer': 'https://m.weibo.cn/profile/6602743011',
 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
 'sec-ch-ua-mobile': '?0',
 'sec-ch-ua-platform': '"Windows"',
 'sec-fetch-dest': 'empty',
 'sec-fetch-mode': 'cors',
 'sec-fetch-site': 'same-origin',
 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36',
 'x-requested-with': 'XMLHttpRequest',
 'x-xsrf-token': '5ff9fa'
           }
request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request)
# content = response.read()的类型为比特（<class 'bytes'>）
# decode()方法会将content 比特类型转化为字符串类型
content = response.read().decode('utf-8')
# 此时的content的类型为字符串，但仍对中文不太友好
print(type(content))
print(content)

# headers 中的  （'accept-encoding': 'gzip, deflate, br'）要记得注释掉,
# headers 中的 token（令牌）也很重要，（'x-xsrf-token': 'a0024b'），注意：token具有时效性
# headers 中的 'referer': 'https://m.weibo.cn/profile/6602743011'，也是一种反扒手段。
# referer（涉及）的作用（防盗链）：判断当前路径是不是又上一个路径进来的，一般情况下，用于图片的防盗链

fp = open('file_storage/中文你好哦.txt', 'w', encoding='utf-8')
fp.write(content)
fp.close()



































