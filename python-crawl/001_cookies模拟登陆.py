# _*_coding :utf-8 _*_
# @Time :2022/10/8 16:10
# @File : 001_cookies模拟登陆
# @Project : python-crawl

import requests
import pprint


# 通过 headers 传入 cookies
url = 'http://i.mooc.chaoxing.com/space/index?t=1653700682551'
#
# headers = {
# "Cookie": "fid=29385; lv=4; _uid=202644922; uf=da0883eb5260151ec2421b81641f1f22666bb340f9bcbb08fc8262cbd8093e25adb8a61529dc093e4a10871310cdefad6072530a316e7a7e88b83130e7eb4704649a629b576a377ab9a0fbca4fa47fbd4129e2925200b376ea07904cc6d577feb7be6a7fd388f553e7fafd565af53bf2; _d=1664926928892; UID=202644922; vc=A69AB3ACFF121D3B73775D21D8113CE8; vc2=07676F20B154AC0CF9D8461075748420; vc3=fCpv9cRFP5QUr1FzZmwPmK%2Bgv68aMUMAzoFXfys4Fzwq4S%2FTExvpJkyMZS0N0Y7wp9X5qub1dxad6MlWU5kBosvy75axi1qpnWW7AhFZh235gnG5BByKPBaWFojEOq%2Fu2avGHZ0L%2FZIixGHOi0Gbt1vB5%2BwkaA4I0EA6hCCN4GY%3D96b532844cbecf6b4fadf6fb0747bb06; xxtenc=43b8860ad285905a1eebbb1dda40f743; DSSTASH_LOG=C_38-UN_28100-US_202644922-T_1664926928894; JSESSIONID=08502C5CCDA55F8086EC9638654A3BB3; thirdRegist=0"
# }
# response = requests.get(url=url, headers=headers).text


# 单独传入cookies
Cookies = dict()
c_str = 'fid=29385; lv=4; _uid=202644922; uf=da0883eb5260151ec2421b81641f1f22666bb340f9bcbb08fc8262cbd8093e25adb8a61529dc093e4a10871310cdefad6072530a316e7a7e88b83130e7eb4704649a629b576a377ab9a0fbca4fa47fbd4129e2925200b376ea07904cc6d577feb7be6a7fd388f553e7fafd565af53bf2; _d=1664926928892; UID=202644922; vc=A69AB3ACFF121D3B73775D21D8113CE8; vc2=07676F20B154AC0CF9D8461075748420; vc3=fCpv9cRFP5QUr1FzZmwPmK%2Bgv68aMUMAzoFXfys4Fzwq4S%2FTExvpJkyMZS0N0Y7wp9X5qub1dxad6MlWU5kBosvy75axi1qpnWW7AhFZh235gnG5BByKPBaWFojEOq%2Fu2avGHZ0L%2FZIixGHOi0Gbt1vB5%2BwkaA4I0EA6hCCN4GY%3D96b532844cbecf6b4fadf6fb0747bb06; xxtenc=43b8860ad285905a1eebbb1dda40f743; DSSTASH_LOG=C_38-UN_28100-US_202644922-T_1664926928894; JSESSIONID=08502C5CCDA55F8086EC9638654A3BB3; thirdRegist=0'

for i in c_str.split(';'):
    i = i.split('=')
    Cookies[i[0]] = i[1]

# print(c_str)
# pprint.pprint(Cookies)

response = requests.get(url=url, cookies=Cookies).content.decode('utf-8')
print(response)


























