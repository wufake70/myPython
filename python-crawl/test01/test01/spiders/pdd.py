import scrapy


class PddSpider(scrapy.Spider):
    name = 'pdd'
    allowed_domains = ['https://www.pinduoduo.com/']
    start_urls = ['https://www.pinduoduo.com/']

    def parse(self, response):
        print(response.text)
