# _*_coding :utf-8 _*_
# @Time :2022/6/23 20:30
# @File : 测试_003
# @Project : python_base_payment

import requests
import re
from tqdm import tqdm # 进度条展示

url = 'https://vd.l.qq.com/proxyhttp'
data = {"buid":"vinfoad","adparam":"pf=in&ad_type=LD%7CKB%7CPVL&pf_ex=pc&url=https%3A%2F%2Fv.qq.com%2Fx%2Fcover%2Fj3czmhisqin799r.html&refer=https%3A%2F%2Fv.qq.com%2Fx%2Fsearch%2F&ty=web&plugin=1.0.0&v=3.5.57&coverid=j3czmhisqin799r&vid=z002615k57t&pt=&flowid=e9b3e49b2593efd194cbcd24030ed803_10201&vptag=www_baidu_com%7Cvideo%3Aposter_tle&pu=-1&chid=0&adaptor=2&dtype=1&live=0&resp_type=json&guid=4b4e192e83f4abaf8b68df3e4f5be769&req_type=1&from=0&appversion=1.0.166&uid=522810848&tkn=fbYfeWDCLKtAaOd_OGvCNg..&lt=qq&platform=10201&opid=5FE180427A4C883F69CADDED665CE99B&atkn=49C1A486316C8D269AC65AAC080CFB29&appid=101483052&tpid=1&rfid=86c3f668da63d8bc7aab3fbc1eb7378a_1633763084","vinfoparam":"spsrt=1&charge=0&defaultfmt=auto&otype=ojson&guid=4b4e192e83f4abaf8b68df3e4f5be769&flowid=e9b3e49b2593efd194cbcd24030ed803_10201&platform=10201&sdtfrom=v1010&defnpayver=1&appVer=3.5.57&host=v.qq.com&ehost=https%3A%2F%2Fv.qq.com%2Fx%2Fcover%2Fj3czmhisqin799r.html&refer=v.qq.com&sphttps=1&tm=1633767536&spwm=4&logintoken=%7B%22main_login%22%3A%22qq%22%2C%22openid%22%3A%225FE180427A4C883F69CADDED665CE99B%22%2C%22appid%22%3A%22101483052%22%2C%22access_token%22%3A%2249C1A486316C8D269AC65AAC080CFB29%22%2C%22vuserid%22%3A%22522810848%22%2C%22vusession%22%3A%22fbYfeWDCLKtAaOd_OGvCNg..%22%7D&vid=z002615k57t&defn=fhd&fhdswitch=0&show1080p=1&isHLS=1&dtype=3&sphls=2&spgzip=1&dlver=2&drm=32&hdcp=0&spau=1&spaudio=15&defsrc=2&encryptVer=9.1&cKey=W5agxKnJ7N56KJEItZs_lpJX5WB4a2CdS8kEIo8rVaqtHEZQ1c_W6myJ8hQXnmDDG8ErEJDMLjvm2vPBr-xE-uhvZyEMY131vUh1H4pgCXe2OphM_H32Jqtu2hFoqfA-un0sVBkIXYfWkOdABnbLUo4RgzSXkBHF3N3K7dNKPg_56X9JO3gwBMyBeAex05x8SbbQKY5AXaDVSM7hsBQ8XEeHzIEGJzlCt94ONgPYVSRkZqo51NVr_Bs8h4-UNLT0jG-obbyNs2IJhrZ4JUBeuGEk8zAOhE9HTZPNDViLRIyt2mNDud09qSLLKl4XAj3CE6i26P6BRyAy1_qatijXkm9J1hs3ZYC7dgYmAZD6BE9UGX4hkziTy-Y8cCBppeEBGSaj9w&fp2p=1&spadseg=3"}

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36'
}
response = requests.post(url=url, json=data, headers=headers)

html_data = response.json()['vinfo']
# 正则表达式
m3u8_url = re.findall("url(.*?),", html_data)[3].split('"')[2]
m3u8_data = requests.get(url=m3u8_url).text
m3u8_data = re.sub('#EXTM3U', '', m3u8_data)
m3u8_data = re.sub('#EXT-X-VERSION:\d', '', m3u8_data)
m3u8_data = re.sub('#EXT-X-MEDIA-SEQUENCE:\d', '', m3u8_data)
m3u8_data = re.sub('#EXT-X-TARGETDURATION:\d+', '', m3u8_data)
m3u8_data = re.sub('#EXT-X-PLAYLIST-TYPE:VOD', '', m3u8_data)
m3u8_data = re.sub('#EXTINF:\d+\.\d+,', '', m3u8_data)
m3u8_data = re.sub('#EXT-X-ENDLIST', '', m3u8_data).split()

for ts in tqdm(m3u8_data):
    ts_url = 'https://apd-57c5d150c8b9788baf40ea4f65feddf8.v.smtcdns.com/moviets.tc.qq.com/A2k4JuW9ATia8thdFQ6y5HWRUGLqAr4L5fk9KFbAUEI8/uwMROfz2r5xgoaQXGdGnC2df64gVTKzl5C_X6A3JOVT0QIb-/doVi4hWq0sqexPo_ylKYxVIJdr9zz2VweWbcY7x70kRnbVNPvBaoTsjwfOq1uojOtsRKJ8r3372HRaTOVg4VyKOFFvzjq2EeMdpleIIyTv0tb-C3CzXmkZz-34hK4Fc-r4mZK55L9W1RqJMpsvrORZr_sqpqvGZrrRq830get0NLJGkeAQ9SBg/' + ts
    ts_content = requests.get(url=ts_url).content

with open('霸王别姬.mp4', mode='ab') as f:
    f.write(ts_content)
print('下载完成')






























