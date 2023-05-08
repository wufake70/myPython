import scrapy


class TcSpider(scrapy.Spider):
    name = 'tc'
    allowed_domains = ['https://bj.58.com/tech/?PGTID=0d000000-0000-021e-5d4f-6c9f36a95fee&ClickID=1']
    start_urls = ['https://bj.58.com/tech/?PGTID=0d000000-0000-021e-5d4f-6c9f36a95fee&ClickID=1']

    def parse(self, response):
        # 接收字符串数据
        content = response.test
        # print(content)

        # 接收比特类型数据（二进制）数据
        content = response.body
        # print(content)

        # scrapy框架中不用导入任何库
        # 进入了反爬页面，需要点击认证
        # location = response.xpath('//div')
        # print('==================')
        # print(location)
        #
