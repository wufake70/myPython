# _*_coding :utf-8 _*_
# @Time :2022/5/15 8:24
# @File : 爬取IU图片
# @Project : python-base

import urllib.request
import urllib.parse

from lxml import etree


# kw = input('请输入相关信息：')


def create_request():
#   data中的关键字 q，必须要与原url中的关键字一样
#     data = {
#         'q': kw,
#     }

    data = {
'tn': 'baiduimage',
'ipn': 'r',
'ct': '201326592',
'cl': '2',
'lm': '-1',
'st': '-1',
'fm': 'index',
'fr': '',
'hs': '0',
'xthttps': '111110',
'sf': '1',
'fmq': '',
'pv': '',
'ic': '0',
'nc': '1',
'z': '',
'se': '1',
'showtab': '0',
'fb': '0',
'width': '',
'height': '',
'face': '0',
'istype': '2',
'ie': 'utf-8',
'word': '李智恩',
'oq': '李智恩',
'rsp': '-1',
}
#   data向url传参时，要记得转码
    data = urllib.parse.urlencode(data)
    url = 'https://image.baidu.com/search/index?' + data
    print(url)

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'Accept-Language': 'zh-CN,zh;q=0.9',
'Cache-Control': 'max-age=0',
'Connection': 'keep-alive',
'Cookie': '__yjs_duid=1_2422155ec3376ed49006cc141c69e0a01645605020450; BAIDUID=31A5761E3E87B3E18CC1131B24410AB5:FG=1; BIDUPSID=31A5761E3E87B3E18CC1131B24410AB5; PSTM=1649747485; H_WISE_SIDS=110085_127969_179350_184716_188332_189755_191254_194085_195622_197241_197471_197711_198260_199155_199580_201193_201536_202652_203190_203310_203316_203504_204123_204261_204701_204711_204864_204902_205218_205240_205484_205569_205807_205909_206006_206196_206729_206734_206929_207236_207471_207729_207830_207864_208113_208268_208343_208522_208687_208721_209282_209395_209488_209512_209521_209568_209575_209931_209944_209981_210163_210357_210653_210670_210737_210842_210890_210892_210894_210900_210906_211113_211181_211242_211302_211442_211457_8000059_8000100_8000118_8000131_8000136_8000165_8000173_8000178_8000179_8000186; BDUSS_BFESS=EdWMkprREJYMHlQOGFZN20xRmhsd3B4N2R3LU4xTk5LOGpkMzg3REw5b2lyNlZpSUFBQUFBJCQAAAAAAQAAAAEAAAAi0eFCeXVra29vb2tnZwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACIifmIiIn5iR; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BA_HECTOR=2ha50ka0a4a0a40l9r1h7ucpq0r; BAIDUID_BFESS=2ABC9363F5F2FD6F9F58DBA367186A65:FG=1; BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm; userFrom=null; BDRCVFR[-pGxjrCMryR]=mk3SLVN4HKm; BDRCVFR[X_XKQks0S63]=mk3SLVN4HKm; ab_sr=1.0.1_ZmM1MDEzN2QxZDNlZDQ0MDA0MjU3MzM2OGVkYTEzZjZjYTdkZTcxMTYwZGRjNTFjMzRiMzVmYTIzODQxODIwYTlmNTU5OTg2ZDNhOWRkNzhjNmU4YWRmOGEwYzdlYmQzNTViMmQyZjg1ZDJkY2FlZDU2NTI1OTk5OTJkZjYzNzhjMDM0NmJiZGU3MGVjNTgzNWEwMWVlMTlkMzUzODk2Yw==; firstShowTip=1',
'Host': 'image.baidu.com',
'Referer': 'https://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&dyTabStr=MCwzLDIsMSw2LDUsNCw4LDcsOQ%3D%3D&word=%E6%9D%8E%E6%99%BA%E6%81%A9',
'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Windows"',
'Sec-Fetch-Dest': 'document',
'Sec-Fetch-Mode': 'navigate',
'Sec-Fetch-Site': 'same-origin',
'Sec-Fetch-User': '?1',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36',
    }

    request = urllib.request.Request(url=url, headers=headers)
    return request

def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
#    print(content)
    return content

def download(content):
    fp = open('file_storage/百度图片.html', 'w', encoding='utf-8')
    fp.write(content)
    fp.close()


#    print(content)
#    tree = etree.HTML(content)
#    print(tree)
# 用xpath查找图片的名字和地址
#    name_list = tree.xpath('//ul[@class="imglist clearfix pageNum0"]//a[@style]//text()')
#    src_list = tree.xpath("//img/@src")

#    print(name_list)
#    print(len(name_list))
#    print(src_list)

    # for i in range(1, len(src_list)+1):
    #       url = 'https://' + src_list[i]
    #       print(str(i+1) + "." +url)


request = create_request()
content = get_content(request)
download(content)

























