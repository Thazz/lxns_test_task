# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class EstateItem(Item):
    id = Field()
    name = Field()
    price = Field()
    locality = Field()
    image_urls = Field()
