# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from db_handler import DbHandler

class EstatesPipeline:
    def __init__(self):
        self.db = DbHandler()
        self.db.connect()
        self.db.create_items_table()
        
    def process_item(self, item, spider):
        self.db.insert_item(item)

    def open_spider(self, spider):
        self.db.delete_items()

    def close_spider(self, spider):
        self.db.disconnect()