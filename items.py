# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CpwsAhItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    date = scrapy.Field()
    court = scrapy.Field()
    caseno = scrapy.Field()
    ptext = scrapy.Field()
    content = scrapy.Field()
    pass
