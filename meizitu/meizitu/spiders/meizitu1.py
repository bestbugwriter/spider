# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from meizitu.items import MeizituItem
from scrapy.selector import Selector

class Meizitu1Spider(CrawlSpider):
    name = 'meizitu1'
    allowed_domains = ['meizitu.com']
   
    ba = lambda x : "http://www.meizitu.com/a/list_1_" + str(x) + ".html"
    start_urls = [ba(x) for x in range(1,89)]

    rules = (
        Rule(LinkExtractor(allow='http://www.meizitu.com/a.*'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        i = []
        item = MeizituItem()
        sel = Selector(response)
        try:
            item['image_urls'] = sel.xpath('//div[@class="postContent"]/p/img/@src').extract()
            i.append(item)
        except Exception as e:
            print("parse_item: " + str(e))
            pass

        return item
