# _*_coding :utf-8 _*_
# @Time :2022/10/10 23:00
# @File : 006_爬取京东-手机
# @Project : python-crawl
import csv
import pprint
import queue
import re
import time
import requests
from lxml import etree
from multiprocessing.pool import ThreadPool


def fun1(page):
    ii = page
    url = 'https://search.jd.com/Search?keyword=房子出售&enc=utf-8&wq=房子出售&pvid=9c7c182de1014846b64edcfc7c728f48&page=' + str(
        page)

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "zh,zh-CN;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        # "Accept-Encoding": "gzip, deflate, br",
        "Referer": "https://www.jd.com/",
        "DNT": "1",
        "Connection": "keep-alive",
        "Cookie": "__jda=122270672.1649328199567358221371.1649328199.1661604255.1665413687.17; shshshfpb=mUaEIkzg1GwiZPb8PXUuV_Q; shshshfp=12423ff35c7cb58c3f76d54f42852e61; shshshfpa=b072f2fd-950a-f3fe-5830-7f2b6082c9ac-1649328517; __jdu=1649328199567358221371; unpl=JF8EAMdnNSttXB9UBx8CTxAZGFVVWw8MQ0cGaWVXUFVaH1AFHFJLQBF7XlVdXhRLFh9vZhRXXlNPUQ4ZBisSEXteXVdZDEsWC2tXVgQFDQ8VXURJQlZAFDNVCV9dSRZRZjJWBFtdT1xWSAYYRRMfDlAKDlhCR1FpMjVkXlh7VAQrAhwXGEleXV5VAE8QBW1jDFdeWElSBSsyHCIge1pWW1gLSycCX2Y1FgkEQ1YGEwoZXxBMWFxcXgFLHwtrYANWWVFIVwUZBBsiEXte; __jdb=122270672.4.1649328199567358221371|17.1665413687; __jdc=122270672; __jdv=76161171|baidu-pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_5e1351e38b904c59a473c593e516aac0|1665413686848; areaId=12; ipLoc-djd=12-904-0-0; shshshsID=31909c0df0303ed1745f89d711acaa15_2_1665413747240; jsavif=1; jsavif=1; qrsc=1; rkv=1.0",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "same-site",
        "TE": "trailers",
    }

    response = requests.get(url, headers=headers).content.decode('utf-8')

    a = etree.HTML(response)

    li = a.xpath('//div[@class="p-img"]')

    # time.sleep(0.01*page)
    for i in range(1, len(li)+1):
        img = a.xpath(f'//li[@class="gl-item"][{i}]//div[@class="p-img"]/a/img/@data-lazy-img')  # img标签 懒加载 无法匹配src 属性
        price = a.xpath(f'//li[@class="gl-item"][{i}]//div[@class="p-price"]//strong//i/text()')
        name = ','.join(a.xpath(f'//li[@class="gl-item"][{i}]//div[@class="p-name p-name-type-2"]//em/text()')).strip()
        shop = a.xpath(f'//li[@class="gl-item"][{i}]//a[@class="curr-shop hd-shopname"]/@title')
        # print(f'{page}\n{img}\n{price}\n{name}\n{shop}\n', end='\n')
        if img and price and name and shop:
            # ls.append({"id": (page - 1)*30+i, "name": name, "img": img[0], "price": price[0], "shop": shop[0]})
            save_csv_data([{"id": (page - 1)*30+i, "name": name, "img": img[0], "price": price[0], "shop": shop[0]}], header)

    # if page == i_:
    #     global IsOver
    #     IsOver = True
    #     print('测试')

    print(f'这是第 {ii} 页数据')
    print(len(ls))


def save_csv_headers(h):
    with open('006_手机详情.csv', 'w', encoding='utf-8', newline="") as fp:
        writer = csv.DictWriter(fp, h)
        writer.writeheader()
        # fp.close()


def save_csv_data(d, h):
    with open('006_电脑详情.csv', 'a', encoding='utf-8', newline="") as fp:
        writer = csv.DictWriter(fp, h)
        # writer.writeheader()
        writer.writerows(d)


if __name__ == "__main__":

    # ls = []
    # print('正在爬取......')
    # for i_ in range(1, 21):
    #     fun1(i_)
    # print(f'共有 {len(ls)} 条数据，等待写入文件......')
    #
    # headers = ('id', 'name', 'img', 'price', 'shop')
    # data = ls
    # save_csv(headers, data)

    header = ('id', 'name', 'img', 'price', 'shop')
    save_csv_headers(header)

    print('开始请求......')
    th = ThreadPool(32)
    # ls = []
    # IsOver = False

    for i_ in range(1, 201):
        th.apply_async(fun1, args=(i_,))

    th.close()
    th.join()

    # while IsOver:
    #     print('999999999999999999999')
    #     data = ls
    #     save_csv(headers, data)
    #     break




