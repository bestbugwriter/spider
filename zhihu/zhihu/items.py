# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhihuItem(scrapy.Item):
    url = scrapy.Field()  #保存抓取问题的url
    title = scrapy.Field()  #抓取问题的标题
    description = scrapy.Field()  #抓取问题的描述
    answer = scrapy.Field()  #抓取问题的答案
    name = scrapy.Field()  #个人用户的名称
    pass

class ZhihuUserItem(scrapy.Item):
    username = scrapy.Field()
    name = scrapy.Field()
    brief = scrapy.Field()
    url = scrapy.Field()
    thanks = scrapy.Field()
    agree = scrapy.Field()
    sex = scrapy.Field()
    image_urls = scrapy.Field()
    pass
