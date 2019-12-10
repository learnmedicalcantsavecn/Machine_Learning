# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NewsDataGeneratorItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class GlobalTimesItems(scrapy.Item):
    category = scrapy.Field()  # 分类
    title = scrapy.Field()  # 标题
    content = scrapy.Field()  # 内容
    pass
