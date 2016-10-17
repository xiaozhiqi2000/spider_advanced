# -*- coding: utf-8 -*-
import json
import urllib

import scrapy
from scrapy.http.request import Request
from project24.items import StationItem
from project24.items import CommitItem

class StationsSpider(scrapy.Spider):
    name = 'StationsSpider'
    #start_urls = ['http://www.google.com']
    start_urls = ['htt://www.12306.cn/mormhweb/kyyyz/']

    custom_settings = {
            'ITEM_PIPELINES': {
                'project24.pipelines.StationSQLPipeline': 300,
            },
    }

    def parse(self, response):
        names = response.css("#secTable > tbody > tr > td::text").extract()
        sub_urls = response.css("#mainTable td.submenu_bg > a::attr(href)").extract()
        for i in range(0, len(names)):
            sub_url1 = response.url + sub_urls[i * 2][2:]
            yield Request(sub_url1, callback = self.parse_station, meta = {'bureau':names[i], 'station':True})

            sub_url2 = response.url + sub_urls[i * 2 + 1][2:]
            yield Request(sub_url2, callback = self.parse_station, meta = {'bureau':names[i], 'station':False})

    def parse_station(self, response):
        datas = response.css("table table tr")
        self.logger.debug(datas)
        # critical
        # error
        # warning
        # info
        # debug
        if len(datas) <= 2:
            self.logger.info('no item ' + response.meta["bureau"] + ' ' + response.meta["station"])
            return
        for i in range(0, len(datas)):
            if i < 2:
                continue
            infos = datas[i].css("td::text").extract()

            item = StationItem()
            item["bureau"] = response.meta["bureau"]
            item["station"] = response.meta["station"]
            item["name"] = infos[0]
            item["address"] = infos[1]
            item["passenger"] = infos[2].strip() != u""
            item["luggage"] = infos[3].strip() != u""
            item["package"] = infos[4].strip() != u""
            yield item
        yield CommitItem()
          



