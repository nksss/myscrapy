# -*- coding: utf-8 -*-
import scrapy

import re
from myScrapy.items import MyscrapyItem

class DemoSpider(scrapy.Spider):
    name = 'demo'
    allowed_domains = ['how2j.cn']
    start_urls = ['https://how2j.cn/stage/33.html']

    def parse(self, response):
        html = response.xpath('//a[@class="list-group-item moduleItemLeft"]/span')
        for each in html:
            item = MyscrapyItem()
            name = each.xpath('./text()').extract()
            item['name'] = name[0]
            yield item

