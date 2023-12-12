import scrapy
from lxns_test_task.items import EstateItem

class EstatesSpider(scrapy.Spider):
    name = "estates"
    start_urls = [
        "https://www.sreality.cz/api/en/v2/estates?category_main_cb=1&category_type_cb=1&locality_country_id=10001&per_page=500"
    ]

    def parse(self, response):
        json_response = response.json()
        for estate in json_response["_embedded"]["estates"]:
            estateItem = EstateItem()
            estateItem["id"] = estate["hash_id"]
            estateItem["name"] = estate["name"]
            estateItem["price"] = estate["price"]
            estateItem["locality"] = estate["locality"]
            estateItem["image_urls"] = [href['href'] for href in estate["_links"]["images"]]
            
            yield estateItem
        
        
        