import scrapy


class CarSpider(scrapy.Spider):
    name = 'car'
    allowed_domains = ['www.autohome.com.cn']
    start_urls = ['https://car.autohome.com.cn/price/brand-15.html']  # 当url的后缀名为html时不能有斜杠 / 存在

    def parse(self, response):
        print('========代码执行===========')
