# _*_coding :utf-8 _*_
# @Time :2022/5/14 9:19
# @File : 071-解析获取百度网站的百度一下
# @Project : python-base

from lxml import etree
import urllib.request
import json

# 获取网页源码
# 解析 服务器响应的数据

url = 'https://www.baidu.com'
headers = {
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'Accept-Language': 'zh-CN,zh;q=0.9',
'Cache-Control': 'max-age=0',
'Connection': 'keep-alive',
'Cookie': '__yjs_duid=1_2422155ec3376ed49006cc141c69e0a01645605020450; BAIDUID=31A5761E3E87B3E18CC1131B24410AB5:FG=1; BIDUPSID=31A5761E3E87B3E18CC1131B24410AB5; PSTM=1649747485; ORIGIN=2; ISSW=1; ISSW=1; Hm_lvt_aec699bb6442ba076c8981c6dc490771=1649747516; BAIDUID_BFESS=C851B9E82BA1D9BC2AB15B1D30D94EDD:FG=1; H_WISE_SIDS=110085_127969_179350_184716_188332_189755_191254_194085_195622_197241_197471_197711_198260_199155_199580_201193_201536_202652_203190_203310_203316_203504_204123_204261_204701_204711_204864_204902_205218_205240_205484_205569_205807_205909_206006_206196_206729_206734_206929_207236_207471_207729_207830_207864_208113_208268_208343_208522_208687_208721_209282_209395_209488_209512_209521_209568_209575_209931_209944_209981_210163_210357_210653_210670_210737_210842_210890_210892_210894_210900_210906_211113_211181_211242_211302_211442_211457_8000059_8000100_8000118_8000131_8000136_8000165_8000173_8000178_8000179_8000186; BD_UPN=12314753; COOKIE_SESSION=1292_0_1_2_1_3_1_0_0_2_14_2_0_0_0_0_1651132922_0_1652264131%7C3%230_0_1652264131%7C1; BDUSS_BFESS=EdWMkprREJYMHlQOGFZN20xRmhsd3B4N2R3LU4xTk5LOGpkMzg3REw5b2lyNlZpSUFBQUFBJCQAAAAAAQAAAAEAAAAi0eFCeXVra29vb2tnZwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACIifmIiIn5iR; BA_HECTOR=a0ag24a184802g8ked1h7s90m0r; Hm_lvt_9f14aaa038bbba8b12ec2a4a3e51d254=1652433964; BD_HOME=1; H_PS_PSSID=36426_31253_34812_36423_36166_34584_35978_36055_36419_26350_36348_36315',
'Host': 'www.baidu.com',
'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Windows"',
'Sec-Fetch-Dest': 'document',
'Sec-Fetch-Mode': 'navigate',
'Sec-Fetch-Site': 'none',
'Sec-Fetch-User': '?1',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36'
}

request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')

# print(type(content))
# print(content)

tree = etree.HTML(content)
print(tree)
# 返回值类型为列表类型，
search = tree.xpath('//ul[@class="s-news-rank-content"]//span[@class="title-content-title"]//text()')

# print('今天的百度热词是：')
fp = open('file_storage/百度热条.txt', 'a')
fp.write('此刻的百度热条是：')
for i in range(0, 10):
#  list index out of range ，超过了list的范围
    fp.write('\n'*2 + str(i+1) + '.' + search[i])
    print(str(i))

fp.close()





































