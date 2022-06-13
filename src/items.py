
# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, MapCompose
from w3lib.html import remove_tags

def format_item(value):
    output = ""

    value.pop(0)
    value.pop(0)
    value.pop(0)
    value.pop(0)

    for k in len(value):
        output += value[k]

    return output


class SrcItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # category = scrapy.Field(input_processor = MapCompose(remove_tags), output_procesor = TakeFirst())
    # subcategory = scrapy.Field(input_processor = MapCompose(remove_tags), output_procesor = TakeFirst())

    # product_key = scrapy.Field()
    # name = scrapy.Field(input_processor = MapCompose(remove_tags), output_procesor = TakeFirst())
    # link = scrapy.Field()
    # price = scrapy.Field(input_processor = MapCompose(remove_tags), output_procesor = TakeFirst())

    # weight = scrapy.Field()
    # stock = scrapy.Field()
    # subProductName = scrapy.Field()
    # subProductPrice = scrapy.Field()
    name = scrapy.Field()
    market_supply = scrapy.Field(input_processor = MapCompose(remove_tags, format_item), output_procesor = TakeFirst())
    circulation_supply = scrapy.Field()
    market_cap = scrapy.Field()

    token_distribution = scrapy.Field(input_processor = MapCompose(remove_tags, format_item), output_procesor = TakeFirst())

    link = scrapy.Field()