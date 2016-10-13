#!/usr/bin/env python
# -*- coding:utf-8 -*-

import scrapy
import os
import urllib

class XiaoHuarSpider(scrapy.spiders.Spider):
    name = "s4"   # 爬虫app的名字

    allowed_domains = ["xiaohuar.com"]

    start_urls = [
        "http://www.xiaohuar.com/hua/",
    ]

    def parse(self, response):
        from scrapy.selector import Selector
        items = Selector(response=response).xpath('//div[@class="item_list infinite_scroll"]/div')
        #print items

        for i in range(len(items)):
            srcs = Selector(response=response).xpath('//div[@class="item_list infinite_scroll"]/div[%d]//div[@class="img"]/a/img/@src' % i).extract()
            names = response.selector.xpath('//div[@class="item_list infinite_scroll"]/div[%d]//div[@class="img"]/span/text()' % i).extract()
            schools = response.selector.xpath('//div[@class="item_list infinite_scroll"]/div[%d]//div[@class="img"]/div[@class="btns"]/a/text()' % i).extract()
            if srcs and names and schools:
                try:
                    from xiaohuas import items
                    item = items.Spider1Item()
                    item['name'] = names[0]
                    item['school'] = schools[0]
                    item['src'] = srcs[0]
                   # print item
                    yield item

                except Exception as e:
                    print e


























