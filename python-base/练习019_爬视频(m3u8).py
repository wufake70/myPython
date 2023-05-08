# _*_coding :utf-8 _*_
# @Time :2022/6/9 22:01
# @File : 练习019_爬视频
# @Project : python-base

import re
import requests
import json
import pprint
"""

"""

url = 'https://www.acfun.cn/v/ac34063499'

headers = {
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'zh-CN,zh;q=0.9',
'cache-control': 'max-age=0',
'cookie': 'csrfToken=NIozdDJ-zospfS0Zeolq5QlN; _did=web_901079793BF1E088; safety_id=AAJwJdSYc6WvWiw3hlN8PO0u; cur_req_id=570194230238CC8F_self_4d322017cf564c24132fe69d5190f066; cur_group_id=570194230238CC8F_self_4d322017cf564c24132fe69d5190f066_0; _did=web_901079793BF1E088; webp_supported=%7B%22lossy%22%3Atrue%2C%22lossless%22%3Atrue%2C%22alpha%22%3Atrue%2C%22animation%22%3Atrue%7D; Hm_lvt_2af69bc2b378fb58ae04ed2a04257ed1=1654784637; Hm_lpvt_2af69bc2b378fb58ae04ed2a04257ed1=1654784637; lsv_js_player_v2_main=e4d400',
'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Windows"',
'sec-fetch-dest': 'document',
'sec-fetch-mode': 'navigate',
'sec-fetch-site': 'none',
'sec-fetch-user': '?1',
'upgrade-insecure-requests': '1',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36',
}

response = requests.get(url=url, params=None, headers=headers)
# print(response.text)
html_data = re.findall(r'window.pageInfo = window.videoInfo = (.*?);', response.text)[0]
print(html_data)
html_data = json.dump()


























