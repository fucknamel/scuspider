# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScuspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    num1 = scrapy.Field()
    num2 = scrapy.Field()
    name_en = scrapy.Field()
    name_ch = scrapy.Field()
    value = scrapy.Field()
    _type = scrapy.Field()
    grades = scrapy.Field()
    pass
