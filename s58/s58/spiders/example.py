#!/usr/bin/python3

# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from s58.items import S58Item
import sys
import string
sys.stdout=open('output.txt','w')

class TuSpider(CrawlSpider):
	name = "s58"
	allowed_domains = ["58.com"]
	start_urls = ('http://hz.58.com/binjiang/chuzu/',)

	rules = (
		Rule(SgmlLinkExtractor(allow=('hz.58.com/', )), callback='parse_item'),
		Rule(SgmlLinkExtractor(allow=('jinpai.58.com/', )), callback='parse_item'),
		)

	def parse_item(self, response):
		sel = Selector(response)
		items = []
		item = TuItem()
		print(response.text.encode('utf-8'))
		try:
			print('try:')
			item['prices'] = sel.xpath("//span[@class='price']").extract()[0].encode('utf-8')
			print (item['prices'])
			item['houseTypes'] = sel.xpath("//ul[@class='house-info-list']/li[2]/span").extract()[0].encode('utf-8')
			print (item['houseTypes'])
			item['locations'] = sel.xpath("//ul[@class='house-info-list']/li[4]/span").extract()[0].encode('utf-8')
			print (item['locations'])
			item['briefs'] = sel.xpath('//h2').extract()[0].encode('utf-8')
			print (item['briefs'])
			item['links'] = response.url.encode('utf-8')
			print (item['links'])
			items.append(item)
		except Exception as e:
			print("xpath error" + str(e))
			pass

		return items
