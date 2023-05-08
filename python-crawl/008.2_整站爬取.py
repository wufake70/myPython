# _*_coding :utf-8 _*_
# @Time :2022/10/16 13:49
# @File : 008.2_整站爬取
# @Project : python-crawl

"""
整站爬取

scrapy genspider -t crawl jd www.jd.com         (对应)创建爬虫文件


spiders 文件夹下的 爬虫文件
rules = (
        # 链接提取 的规则(编写正则);       callback:   对应的回调函数
        Rule(LinkExtractor(allow=r'//item.jd.com/.*?\.html'), callback='parse_item', follow=False),
    )


对应的回调函数
def parse_item():

    .......



"""



































