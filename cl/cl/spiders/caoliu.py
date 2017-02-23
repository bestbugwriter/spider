# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from cl.items import ClItem
from scrapy.selector import Selector

class CaoliuSpider(CrawlSpider):
    name = 'caoliu'
    allowed_domains = ['cl.lxrfg.com']
    b = lambda x : "http://cl.lxrfg.com/thread0806.php?fid=20&search=&page=" + str(x)
    start_urls = [b(x) for x in range(1,89)]

    rules = (
        Rule(LinkExtractor(allow=r'.*htm_data/.*\.html'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        items = []
        item = ClItem()
        sel = Selector(response)
        try:
            item['title'] = sel.xpath('//h4').extract()[0].encode('utf8')
            l = sel.xpath('//div[@class="tpc_content do_not_catch"]//text()').extract()
            item['content'] = ''.join(l).encode('utf8')
            item['date'] = sel.xpath('//tr[@class="tr1"]/th//div[@class="tipad"]/text()').extract()[1].encode('utf8')
            item['url'] = response.url.encode('utf8')
            items.append(item)
        except Exception as e:
            print("parse_item: " + str(e))
            pass

        return items
