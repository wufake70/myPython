# _*_coding :utf-8 _*_
# @Time :2022/7/10 21:42
# @File : 018_百度收藏词
# @Project : python-base


import requests.api
import json
import docx.document

counts = int(input('请输入counts(>=6):'))


def more_url(count):
    url_list = []

    for i in range(1, count):
        base_url = f'https://fanyi.baidu.com/pcnewcollection?req=get&dstStatus=all&order=time&direction=all&page={i}&pagesize=30&gid=2345758&_=1657461863386'
        url_list.append(base_url)
    # print(url_list)
    return url_list


def get_data(url_list):
    list_1 = []  # 数据存储
    for i in url_list:
        headers = {
            "Host": "fanyi.baidu.com",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
            # "Accept-Encoding": "gzip, deflate, br",
            "X-Requested-With": "XMLHttpRequest",
            "DNT": "1",
            "Connection": "keep-alive",
            "Referer": "https://fanyi.baidu.com/collection",
            "Cookie": "BAIDUID=8684ECE112D80EAE49BDD8B2F7239261:FG=1; BIDUPSID=19E45FE34415F4AF958A1FAC08A9578F; PSTM=1649254136; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1657332702,1657350433,1657375022,1657444896; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BDUSS=hQSjZXdGtaU1R2alhMdllMR2VqdXVqTE9oUk40YXpabDlZTFhXV3N-QlQxNTFpSVFBQUFBJCQAAAAAAQAAAAEAAAAi0eFCeXVra29vb2tnZwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFNKdmJTSnZiZT; APPGUIDE_10_0_2=1; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; BA_HECTOR=042g818g8lag8k2521ahb6ng1hckrf217; ZFY=MvbyUQ9a:AHKPd7AyCAMfn0QYASlJx9eYojt4tkXRp7M:C; H_PS_PSSID=36551_36466_36724_36455_36610_36663_36692_36165_36695_36697_36073_36775_36745_36762_36771_36765_26350_22157; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; delPer=0; PSINO=7; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1657461863; BDRCVFR[Fc9oatPmwxn]=mk3SLVN4HKm; ab_sr=1.0.1_ZDgxYzQ0N2ZhNDk2MjFkYWQ4MjMwMGY1N2RlMmY3N2EwNzMzYzA0YzcxNmI5YzZmNTMwOGI3MzQ2ZmJlYWI3Njg5OWM5Njk0M2U2OTMwMzk2NWY3MGRjMmY0N2NkMzYzMDIzYzZmMTQwZGM4OThiYzQxM2QzODc5ZjY0MmFkZjY0YTY0ZDY5ZDY1MjhlMTFlZWNjYjFmYTk5NWM2YmJmMmI4NTViNjE5ZDU1OGJjMGEyNWY5MmRlNTVjMDM4MDYx",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
        }

        response_1 = requests.get(url=i, headers=headers).text  # 返回字符串为 unicode编码
        # print(type(response_1))
        response_2 = json.loads(response_1)  # 用json模块加载成 字典对象
        # print(type(response_2))

        for i_1 in range(0, 15):
            # print(i_1)
            try:
                # 适用漂亮打印查看字典结构
                # pprint.pprint(response_2['pageinfo'][i_1]['fanyisrc'])  # 查询词
                # pprint.pprint(response_2['pageinfo'][i_1]['fanyidst'])  # 查询结果
                word = response_2['pageinfo'][i_1]['fanyisrc']
                # print(type(word))
                translate = response_2['pageinfo'][i_1]['fanyidst']
                # print(type(translate))
                list_1.append(f'{url_list.index(i) * 15 + i_1 + 1: <2}.{word: <20}\t\t\t{translate}')
            except IndexError as E:
                print(E)  # 触发异常 list index out of range, 阻止报错停止

    # pprint.pprint(list_1)
    return '\n'.join(list_1)


def save_doc(list_1):
    doc = docx.Document()  # 创建一个新的空白的word document对象
    doc.add_paragraph(list_1)
    doc.save('我的百度收藏词.docx')


a = more_url(counts)
b = get_data(a)
save_doc(b)