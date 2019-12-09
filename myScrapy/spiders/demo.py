# -*- coding: utf-8 -*-
import scrapy

import re
from myScrapy.items import MyscrapyItem
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders.crawl import Rule, CrawlSpider

class DemoSpider(CrawlSpider):
    name = 'demo'
    allowed_domains = ['www.transfermarkt.com']
    start_urls = ['https://www.transfermarkt.com/statistik/saisontransfers']
    # allowed_domains = ['how2j.cn']
    # start_urls = ['https://how2j.cn/stage/33.html']
    rules = (
        Rule(LinkExtractor(restrict_xpaths=u'//li[@class="naechste-seite"]/a'), callback='parse_next', follow=True),
    )

    def parse_next(self, response):
        html = response.xpath('//div[@class="responsive-table"]/div[@class="grid-view"]/table/tbody/tr')
        # html = response.xpath('//a[@class="list-group-item moduleItemLeft"]/span')
        for each in html:
            item = MyscrapyItem()
            name = each.xpath('./td[2]/table[@class="inline-table"]/tr[1]/td[@class="hauptlink"]/a/text()').extract()
            age = each.xpath('./td[3]/text()').extract()
            value = each.xpath('./td[4]/text()').extract()
            # name = each.xpath('./td[2]/table/tbody/tr[2]/td/text()').extract()
            # name = each.xpath('./text()').extract()
            item['name'] = name[0]
            item['age'] = age[0]
            item['value'] = value[0]
            # item['name'] = '111'
            yield item

