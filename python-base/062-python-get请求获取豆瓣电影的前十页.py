# _*_coding :utf-8 _*_
# @Time :2022/5/12 8:27
# @File : 062-python-get请求获取豆瓣电影的前十页
# @Project : python-base

# 前十页网址
# https://movie.douban.com/j/chart/top_list?type=5&interval_
# id=100:90&action=&start=0&limit=20
# https://movie.douban.com/j/chart/top_list?type=5&interval_
# id=100:90&action=&start=20&limit=20
# https://movie.douban.com/j/chart/top_list?type=5&interval_
# id=100:90&action=&start=40&limit=20

# page： 1   2   3   4
# start：0  20   30   40
# 规律：start = （page-1）*20

# 下载豆瓣电影前十页的数据，存入本地

import urllib.request
import urllib.parse

def create_request(page):
    url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100:90&action=&'
    data = {
            'start': (page-1)*20,
            'limit': 20
    }
    data = urllib.parse.urlencode(data)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0'
               }
    url = url + data
    # print(url)
    request = urllib.request.Request(url=url, headers=headers)
    return request

def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content

def download(content):
    fp = open('file_storage/豆瓣电影' + str(page) + '.json', 'w', encoding='utf-8')
    fp.write(content)
    fp.close()




# 程序的入口：

start_page = int(input('请输入起始页码：'))
end_page = int(input('请输入结束页码：'))

for page in range(start_page, end_page + 1):
    request = create_request(page)
    content = get_content(request)
    download(content)









































