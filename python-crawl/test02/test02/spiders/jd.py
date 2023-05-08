import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import Test02Item
from lxml import etree


class JdSpider(CrawlSpider):
    name = 'jd'
    # 允许的域名
    allowed_domains = ['jd.com']
    start_urls = ['https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&wq=%E6%89%8B%E6%9C%BA&pvid=8858151673f941e9b1a4d2c7214b2b52']

    rules = (
        # 链接提取 的规则(编写正则);       callback:   对应的回调函数
        Rule(LinkExtractor(allow=r'//item.jd.com/.*?\.html'), callback='parse_item', follow=False),
    )

    # 回调函数
    # 会逐个 请求上面所获取的 链接
    def parse_item(self, response):
        # 打印当前的 url
        # print(response.url)
        # print('000')

        itme = Test02Item()
        content = etree.HTML(response.text)
        itme['name'] = content.xpath('//div[@class="sku-name"]/text()')
        itme['img'] = content.xpath('//img[@id="spec-img"]/@data-origin')

        return itme



