from json import loads
from requests import get
from os import makedirs, path


def base_url():
    query = input('请键入关键字:')
    start = input('请键入获取数值:')
    url = f'https://vt.sm.cn/api/pic/list?query={query}&tag=&limit=20&start={start}&databucket=default&ad=on&hid' \
          f'=ZWwq0EVuH0F4ykI6Y5dSluXLlvw7hhdz&from=wm850032&fr=&uid=7224ce7c4ca4fa9734fd3a904611d13f%7C54691003951%7C' \
          f'%7C1647355696 '
    return url, start, query


def request_1(url):
    # 该url只返回20个图片数据 url = f'https://vt.sm.cn/api/pic/list?query={
    # query}&tag=&limit=20&start=0&databucket=default&ad=on&hid=ZWwq0EVuH0F4ykI6Y5dSluXLlvw7hhdz&from=wm850032&fr
    # =&uid=7224ce7c4ca4fa9734fd3a904611d13f%7C54691003951%7C%7C1647355696'

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "DNT": "1",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Origin": "https://vt.quark.cn",
        "Referer": "https://vt.quark.cn/"
    }
    response_1 = get(url, headers)

    return response_1


dic_1 = []


def img_dic(response_1, dic_1=[]):                                # 使用json模块加载数据
    try:
        # print(response.text)                              # 字符串类型
        response_1 = loads(response_1.text)              # 将字符串对象加载成为 python 对象
        # pprint.pprint(response_1)                         # 查看字典数据结构 方便获取资源url
        dic = response_1['data']['hit']['imgInfo']['item']  # itme 对应的值为列表类型
        # pprint.pprint(dic)
        dic_1 += dic
    except KeyError as error:
        print(error, '数据达不到预期值')
        
    return dic_1


def save_pic(dic,):
    dir_name = input('请设置新文件夹名字:')
    if not path.exists(r'.\%s' % dir_name):
        makedirs(r'.\%s' % dir_name)
    else:
        print('该文件夹已存在')
    for i in dic:
        with open(r'.\%s\%03d_%s.jpeg' % (dir_name, dic.index(i)+1, i['title']),  'wb') as fp:
            data = get(i['bigPicCache']).content
            print(f'正在写入图片数据{dic.index(i)+1:*>10}')
            fp.write(data)
    

def moro_url(url, start, query):
    for i in range(int(start) // 20):
        print(f'正在发送请求数据包{i+1:*>10}')
        start = 20 * i + 1
        url = f'https://vt.sm.cn/api/pic/list?query={query}&tag=&limit=20&start={start}&databucket=default&ad=on&hid' \
          f'=ZWwq0EVuH0F4ykI6Y5dSluXLlvw7hhdz&from=wm850032&fr=&uid=7224ce7c4ca4fa9734fd3a904611d13f%7C54691003951%7C' \
          f'%7C1647355696 '
        response = request_1(url)
        dic = img_dic(response)
    
    save_pic(dic)


a = base_url()
moro_url(a[0], a[1], a[2])
