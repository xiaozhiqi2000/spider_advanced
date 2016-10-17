# -*- coding: utf-8 -*-
import scrapy
import json

class ProvincesSpider(scrapy.Spider):
    name = 'provinces spider'
    start_urls = ['https://kyfw.12306.cn/otn/userCommon/allProvince']

    def parse(self, response):
        j = json.loads(response.body)
        print "------------------"
        print response.url
        print response.headers
        for prov in j["data"]:
            print prov["chineseName"]

