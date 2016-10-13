#!/usr/bin/env python
# -*- coding:utf-8 -*-

import scrapy
import os
import urllib

class XiaoHuarSpider(scrapy.spiders.Spider):
    name = "s2"   # 爬虫app的名字

    allowed_domains = ["xiaohuar.com"]

    start_urls = [
        "http://www.xiaohuar.com/hua/",
    ]

    def parse(self, response):
        """
        这个方法不能改名,固定
        """
        # current_url = response.url   # 当前的url
        # body = response.body    # 请求的内容
        # unicode_body = response.body_as_unicode()  # 有编码的内容
        #
        # print(response, type(response))
        # print(body)
        # print("xxxxx".center(60,"*"))
        # print(unicode_body)

        # 第一种定义查找的方式,不过这种很快会过期
        from scrapy.selector import HtmlXPathSelector
        hxs = HtmlXPathSelector(response)
        # extract()只是获取对象的具体，没有extract()则获取的是对象
        # items = hxs.select('//div[@class="item_list infinite_scroll"]/div//img/@src').extract()
        # print items
        items = hxs.select('//div[@class="item_list infinite_scroll"]/div')


        # 第二种,优先使用这种
        from scrapy.selector import Selector
        items = Selector(response=response).xpath('//div[@class="item_list infinite_scroll"]/div')


        print items
        for i in range(len(items)):
            srcs = hxs.select('//div[@class="item_list infinite_scroll"]/div[%d]//div[@class="img"]/a/img/@src' % i).extract()
            names = hxs.select('//div[@class="item_list infinite_scroll"]/div[%d]//div[@class="img"]/span/text()' % i).extract()
            schools = hxs.select('//div[@class="item_list infinite_scroll"]/div[%d]//div[@class="img"]/div[@class="btns"]/a/text()' % i).extract()
            if srcs and names and schools:
                print names[0],schools[0],srcs[0]
                ab_src = "http://www.xiaohuar.com" + srcs[0]
                # file_name = names[0] + '.' + srcs[0].split(".")[-1]
                file_name = str(i) + '.' + srcs[0].split(".")[-1]


                # file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),file_name)
                # print os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
                file_path = os.path.join('/home/tomcat/workplace/spider_advanced/spider1/image/',file_name)
                urllib.urlretrieve(ab_src,file_path)



























