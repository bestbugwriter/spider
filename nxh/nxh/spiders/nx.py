# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from nxh.items import NxhItem
from scrapy.selector import Selector
from scrapy.utils.response import get_base_url
from scrapy.utils.url import urljoin_rfc

class NxSpider(CrawlSpider):
    name = 'nx'
    allowed_domains = ['lars.mec.ua.pt']
    start_urls = ['http://lars.mec.ua.pt/public/Media/ResearchDevelopmentProjects/HaarFeatures_RoadFilms/']

    rules = (
        Rule(LinkExtractor(allow='.*/public/Media/ResearchDevelopmentProjects/HaarFeatures_RoadFilms/.*'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        i = []
        item = NxhItem()
        sel = Selector(response)
        try:
            base_url = get_base_url(response)
            relative_url = sel.xpath('//img/@src').extract()
            item['image_urls'] = [urljoin_rfc(base_url, ru) for ru in relative_url]
            i.append(item)
        except Exception as e:
            print("parse_item: " + str(e))
            pass

        return item
