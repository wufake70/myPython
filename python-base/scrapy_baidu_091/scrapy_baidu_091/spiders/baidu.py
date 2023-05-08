import scrapy


class BaiduSpider(scrapy.Spider):
    # 爬虫的名字， 用于运行爬虫的时候，使用的值
    name = 'baidu'
    # 允许访问的域名
    allowed_domains = ['www.baidu.com']
    # 起始的url地址  指的是第一次要访问的域名
    # start_url是在allow_domain的前面加上协议头，后面写成路径的形式
    start_urls = ['http://www.baidu.com/']

    # 执行了start_urls之后，执行的方法，方法中的response 就是返回的那个对象
    def parse(self, response):
        print('hello 你好好  科技委；粉底加快科教文化人软胶囊 world')

