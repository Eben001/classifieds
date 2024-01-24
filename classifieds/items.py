# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import Join, MapCompose

def clean(s):
    return s[0].replace("\t", "").replace("\n", "").replace(u'\xa0',u' ').strip("\t")


class ClassifiedsItem(scrapy.Item):
    title = scrapy.Field(output_processor=clean)
    make = scrapy.Field(output_processor=clean)
    model = scrapy.Field(output_processor=clean)
    manfuctured_year = scrapy.Field(output_processor=clean)
    locality = scrapy.Field(output_processor=clean)
    company_name = scrapy.Field(output_processor=clean)