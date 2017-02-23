# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.http import Request, FormRequest

from douban.items import DoubanItem
from douban.items import DouyouItem

class DoubansSpider(CrawlSpider):
    name = 'doubans'
    allowed_domains = ['douban.com']
    start_urls = ['https://www.douban.com/doumail/']

    rules = (
        Rule(LinkExtractor(allow='https://www.douban.com/doumail/.+'), callback='parse_item', follow=True),
    )

    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Connection':'keep-alive'
        }

    from_data = {
        'source':'index_nav',
        #'redir':'https://www.douban.com/',
        'form_email':'123456@qq.com',
        'form_password':'12345',
        #'captcha-solution':'basket'
        #'captcha-id':'uWRX2BEQrMmdAsVavgeWUEQU:en'
        #'login':'登录'
    }

    login_url = "https://accounts.douban.com/login"

    def start_requests(self):
        return [Request(self.login_url, meta = {'cookiejar' : 1}, headers = self.headers, callback = self.post_login)]

    def post_login(self, response):
        print 'post login'
        return [FormRequest.from_response(response, meta = {'cookiejar' : response.meta['cookiejar']}, headers = self.headers,
            formdata = self.from_data, callback = self.after_login, dont_filter = True)]

    def after_login(self, response):
        print 'after login'
        for url in self.start_urls :
            yield FormRequest(url,meta = {'cookiejar':response.meta['cookiejar']},
                            headers = self.headers,
                            callback = self.parse_item
                            )

    def parse_item(self, response):
        sel = Selector(response)
        i = []
        item = DouyouItem()

        item['username'] = sel.xpath('//div[@id="status-unread-anchor"]/div[@class="content"]/div/text()').extract()[0]
        item['content'] = sel.xpath('//div[@id="status-unread-anchor"]/div[@class="content"]/p/text()').extract()[0]
        i.append(item)

        print(item)
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i
