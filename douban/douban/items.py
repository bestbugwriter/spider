# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
	bookName = scrapy.Field()
	bookPrice = scrapy.Field()
	bookAuthor = scrapy.Field()
	bookScore = scrapy.Field()
	bookPageNum = scrapy.Field()
	bookBrief = scrapy.Field()
	bookISBN = scrapy.Field()
	bookTag = scrapy.Field()
	pass

class DouyouItem(scrapy.Item):
	username = scrapy.Field()
	content = scrapy.Field()