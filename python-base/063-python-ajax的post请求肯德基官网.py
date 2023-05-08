# _*_coding :utf-8 _*_
# @Time :2022/5/12 15:12
# @File : 063-python-ajax的post请求肯德基官网
# @Project : python-base

import urllib.request
import urllib.parse

# 网址分析
# 第一页
# http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cnamecname
# cname: 兰州
# pid:
# pageIndex: 1
# pageSize: 10


# 第二页
# http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname
# cname: 兰州
# pid:
# pageIndex: 2
# pageSize: 10


# 第三页
# http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname
# cname: 兰州
# pid:
# pageIndex: 3
# pageSize: 10




def create_request(i):
    url_base = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'
    data = {
       'cname': '兰州',
        'pid':'',
        'pageIndex': i,
        'pageSize': 10

    }
    data = urllib.parse.urlencode(data).encode('utf-8')


    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0'
               }
    request = urllib.request.Request(url=url_base, data=data, headers=headers)
    return request

def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content

def download(i,content):
    fp = open('file_storage/兰州肯德基站点列表' + str(i) + '.txt', 'w')
    fp.write(content)
    fp.close()
    print('大功告成')


start_page = int(input('请输入开始页码：'))
end_page = int(input('请输入结束页码：'))

for i in range(start_page, end_page + 1):
    request = create_request(i)
    content = get_content(request)
    download(i, content)

































