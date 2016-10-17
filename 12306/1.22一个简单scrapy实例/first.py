# -*- coding: utf-8 -*-
import scrapy

class FirstSpider(scrapy.Spider):
    name = 'simple spider'
    start_urls = ['http://stackoverflow.com/']

    def parse(self, response):
        print "------------------"
        print response.url
        print response.headers
        print response.body

