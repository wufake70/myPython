# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Test01Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # 声明相关字段
    detail = scrapy.Field()
    img = scrapy.Field()
    price = scrapy.Field()
    name = scrapy.Field()
    shop = scrapy.Field()

    pass
