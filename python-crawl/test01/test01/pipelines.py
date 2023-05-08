# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class Test01Pipeline:

    # 处理解析过后的数据
    def process_item(self, item, spider):
        print(item)
        print("-----------------------------------------------------")
        return item
