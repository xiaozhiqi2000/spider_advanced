#!/usr/bin/env python
# -*- coding:utf-8 -*-

import scrapy

class XiaoHuarSpider(scrapy.spiders.Spider):
    name = "xiaohua"   # app的名字

    # allowed_domains = ["xiaohuar.com"]

    start_urls = [
        "http://www.xiaohuar.com/hua/",
    ]

    def parse(self, response):
        """
        这个方法不能改名,固定
        :param response:
        :return:
        """
        # print(response, type(response))
        # from scrapy.http.response.html import HtmlResponse
        # print(response.body_as_unicode())

        current_url = response.url   # 当前的url
        body = response.body    # 请求的内容
        unicode_body = response.body_as_unicode()  # 编码

        print body