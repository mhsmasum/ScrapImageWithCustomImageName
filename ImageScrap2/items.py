# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Imagescrap2Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class ImdbItem(scrapy.Item):
    
    # images = scrapy.Field()
    # image_urls = scrapy.Field()
    # title = scrapy.Field()

    host= scrapy.Field()
    s=scrapy.Field()
    count = scrapy.Field()
    src_link = scrapy.Field()
    