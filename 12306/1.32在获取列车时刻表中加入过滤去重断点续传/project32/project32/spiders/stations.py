# -*- coding: utf-8 -*-
import time
import datetime
import json
import urllib

import scrapy
from scrapy.http.request import Request
from project32.items import BriefItem
from project32.items import InfoItem
from project32.items import TurnItem
from project32.items import CommitItem

class ScheduleSpider(scrapy.Spider):
    name = 'ScheduleSpider'
    #start_urls = ['https://kyfw.12306.cn/otn/queryTrainInfo/getTrainName']

    custom_settings = {
            'ITEM_PIPELINES': {
                'project32.pipelines.SQLPipeline': 300,
            },
            'DUPEFILTER_DEBUG': True,
            'DOWNLOADER_MIDDLEWARES': {
                'project32.middle.DownloaderMiddleware': 500,
            },
            'DUPEFILTER_CLASS': "project32.filter.URLTurnFilter",
    }

    def __init__(self, *a, **kw):
        super(ScheduleSpider, self).__init__(*a, **kw)
        turn = int(time.time() / 86400)
        self.turn = turn
#        self.turn = 1
        self.logger.info("this turn %d" % turn)

    def start_requests(self):
        self.logger.info("-------------------------")

        n = datetime.datetime.now()
        turnItem = TurnItem()
        turnItem["id"] = self.turn
        turnItem["mark"] = n.strftime("%Y-%m-%d %H:%M:%S")

        url = "https://kyfw.12306.cn/otn/queryTrainInfo/getTrainName?"

        t = (n + datetime.timedelta(days = 3)).strftime("%Y-%m-%d")
        params = {"date":t}
        
        s_url = url + urllib.urlencode(params)
        yield Request(s_url, callback = self.parse, meta = {"t":t, "turn":self.turn, "item":turnItem})

    def parse(self, response):
        yield response.meta["item"]
        datas = json.loads(response.body)
        url = "https://kyfw.12306.cn/otn/czxx/queryByTrainNo?"
        for data in datas["data"]:
            item = BriefItem() 
            briefs = data["station_train_code"].split("(")
            item["train_no"] = data["train_no"]
            item["code"] = briefs[0]
            briefs = briefs[1].split("-")
            item["start"] = briefs[0]
            item["end"] = briefs[1][:-1]
            item["turn"] = response.meta["turn"]
            yield item

            params = u"train_no=" + data["train_no"] + u"&from_station_telecode=BBB&to_station_telecode=BBB&depart_date=" + response.meta["t"]

            yield Request(url + params, callback = self.parse_train_schedule, meta = {"train_no":data["train_no"], "turn":response.meta["turn"]})

    def parse_train_schedule(self, response):
        stations = json.loads(response.body)

        datas = stations["data"]["data"]
        size = len(datas)
        for i in range(0, size):
            data = datas[i]

            info = InfoItem()
            info["train_no"] = response.meta["train_no"];
            info["no"] = int(data["station_no"])
            info["station"] = data["station_name"]
            info["turn"] = response.meta["turn"]

            if data["start_time"] != u"----":
                info["start_time"] = data["start_time"] + u":00";
            else:
                info["start_time"] = None

            if data["arrive_time"] != u"----":
                info["arrive_time"] = data["arrive_time"] + u":00";
            else:
                info["arrive_time"] = None

            if data["stopover_time"] != u"----":
                info["stopover_time"] = data["stopover_time"] + u":00";
            else:
                info["stopover_time"] = None

            yield info
        yield CommitItem()
          



