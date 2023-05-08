import scrapy
from scrapy.utils import response


class DangSpider(scrapy.Spider):
    name = 'dang'
    allowed_domains = ['category.dangdang.com/cp01.01.02.00.00.00.html']
    start_urls = ['http://category.dangdang.com/cp01.01.02.00.00.00.html']

    def parse(self, response):
         # print('==============执行代码==============')
# pipelines 下载数据
# items  定义数据类型
#       src = //ul[@id="component_59"]/li//img/@src
#       alt = //ul[@id="component_59"]/li//img/@alt
#       price = //ul[@id="component_59"]/li//p[@class="price"]/span[1]/text()
        print('==============执行代码==============')
        li_list = response.xpath('//ul[@id="component_59"]/li')
# 图片懒加载，地址储存再data-original里面
        for li in li_list:
            src = li.xpath('.//img/@data-original').extract_first()
            name = li.xpath('.//img/@alt').extract_first()
            price = li.xpath('.//p[@class="price"]/span[1]/text()').extract_first()
            print(src, name, price)


