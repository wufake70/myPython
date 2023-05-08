# _*_coding :utf-8 _*_
# @Time :2022/5/14 19:48
# @File : 074-python-解析jsonpath解析淘飘飘
# @Project : python-base

import urllib.request
import json
import jsonpath
#
#
# url = 'https://dianying.taobao.com/cityAction.json?activityId&_ksTS=1652625949812_97&jsoncallback=jsonp98&action=cityAction&n_s=new&event_submit_doGetAllRegion=true'
# headers = {
#
# 'accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
# 'accept-language': 'zh-CN,zh;q=0.9',
# 'cookie': 'miid=632767101766770865; t=5a982bd6620c4d7c04130ea93d04f74d; cookie2=10c01f03ae34155258b5d937842167b8; v=0; _tb_token_=79d6735bee33e; cna=7MicGn9HKlACAXU9BBOm+C3s; xlly_s=1; l=eBETLDCRLBJlD6u8BO5Churza77O2IOb45VzaNbMiInca18RtFZoaOChGtXvSdtxgtCAHEtPjRmeuRLHR3AgCc0c07kqm0WsFxvO.; tfstk=cp8lBgmF_3S79JsDf4_SRzSenpnOZFiPFe82ubqhySTHvT8Vi_Z4bp--iTHsUk1..; isg=BL-_QDFO4XcPNeVrUO4VSUDTTpNJpBNG-wga21GNZG61YN_iVXVolgV-ozCeB-u-',
# 'referer': 'https://dianying.taobao.com/',
# 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
# 'sec-ch-ua-mobile': '?0',
# 'sec-ch-ua-platform': '"Windows"',
# 'sec-fetch-dest': 'empty',
# 'sec-fetch-mode': 'cors',
# 'sec-fetch-site': 'same-origin',
# 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36',
# 'x-requested-with': 'XMLHttpRequest',
# }
#
# request = urllib.request.Request(url=url, headers=headers)
# response = urllib.request.urlopen(request)
# content = response.read().decode('utf-8')
#
# # split切割字符串
# content = content.split('(')[1].split(')')[0]
# # print(content)
# fp = open('file_storage/淘票票.json', 'w', encoding='utf-8')
# fp.write(content)
# fp.close()
#
obj = json.load(open('file_storage/淘票票.json', 'r', encoding='utf-8'))
city_list = jsonpath.jsonpath(obj, '$..regionName')
print(city_list)
























