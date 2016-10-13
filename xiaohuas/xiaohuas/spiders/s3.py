#!/usr/bin/env python
# -*- coding:utf-8 -*-

import scrapy
import os
import urllib

class XiaoHuarSpider(scrapy.spiders.Spider):
    name = "s3"   # 爬虫app的名字

    allowed_domains = ["xiaohuar.com"]

    start_urls = [
        "http://www.xiaohuar.com/hua/",
    ]

    def parse(self, response):

        current_url = response.url   # 当前的url
        body = response.body    # 请求的内容
        unicode_body = response.body_as_unicode()  # 编码

        # 去body中获取所有url
        from scrapy.selector import Selector
        url_list = Selector(response=response).xpath('//a/@href')
        for url in url_list:
            print url
            yield scrapy.Request(url=url,callback=self.parse)



























