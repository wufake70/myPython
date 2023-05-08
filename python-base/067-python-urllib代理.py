# _*_coding :utf-8 _*_
# @Time :2022/5/12 22:40
# @File : 067-python-urllib代理
# @Project : python-base

url = 'https://www.google.com/search?q=ip'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0'
           }
import urllib.request

request = urllib.request.Request(url=url, headers=headers)

# response = urllib.request.urlopen(request)
#
# content = response.read().decode('utf-8')
# fp = open('file_storage/ip.htm', 'w', encoding='utf-8')
# fp.write(content)
# fp.close()




# handler    build_opener     open
proxies = {
     'http': '202.55.5.209:8090'
 }
handler = urllib.request.ProxyHandler(proxies)

opener = urllib.request.build_opener(handler)

response = opener.open(request)

content = response.read().decode('utf-8')

fp = open('file_storage/ip代理.htm', 'w', encoding='utf-8')
fp.write(content)
fp.close()




































