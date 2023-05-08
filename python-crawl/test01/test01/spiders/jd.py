import scrapy
from lxml import etree
from ..items import Test01Item


class JdSpider(scrapy.Spider):
    name = 'jd'
    allowed_domains = ['https://www.jd.com/']
    # start_urls = ['https://www.jd.com/']
    start_urls = ['https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&wq=%E6%89%8B%E6%9C%BA&pvid=9c7c182de1014846b64edcfc7c728f48']

    def parse(self, response):

        content = response.text
        a = etree.HTML(content)

        li = a.xpath('//div[@class="p-img"]')

        # print(len(li))
        for i in range(1, len(li) + 1):
            item = Test01Item()
            item['detail'] = a.xpath(f'//li[@class="gl-item"][{i}]//div[@class="p-img"]/a[1]/@href')
            item['img'] = a.xpath(f'//li[@class="gl-item"][{i}]//div[@class="p-img"]/a/img/@data-lazy-img')  # img标签 懒加载 无法匹配src 属性
            item['price'] = a.xpath(f'//li[@class="gl-item"][{i}]//div[@class="p-price"]//strong//i/text()')
            item['name'] = ','.join(a.xpath(f'//li[@class="gl-item"][{i}]//div[@class="p-name p-name-type-2"]//em/text()')).strip()
            item['shop'] = a.xpath(f'//li[@class="gl-item"][{i}]//a[@class="curr-shop hd-shopname"]/@title')
            # print(f"{item['detail']}\n{item['img']}\n{item['price']}\n{item['name']}\n{item['shop']}\n', end='\n")

            # 提交数据 给 管道
            yield item
        pass
