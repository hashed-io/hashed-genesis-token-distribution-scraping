
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
    name = scrapy.Field()
    relay_chain = scrapy.Field(input_processor = MapCompose(remove_tags), output_procesor = TakeFirst())
    market_supply = scrapy.Field(input_processor = MapCompose(remove_tags, format_item), output_procesor = TakeFirst())
    circulation_supply = scrapy.Field()
    market_cap = scrapy.Field()

    token_distribution = scrapy.Field(input_processor = MapCompose(remove_tags, format_item), output_procesor = TakeFirst())

    link = scrapy.Field()