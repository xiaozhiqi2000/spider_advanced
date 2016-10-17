# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class CommitItem(scrapy.Item):
    pass

class TurnItem(scrapy.Item):
    id = scrapy.Field()
    mark = scrapy.Field()

class BriefItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    code = scrapy.Field()
    train_no = scrapy.Field()
    start = scrapy.Field()
    end = scrapy.Field()
    turn = scrapy.Field()

class InfoItem(scrapy.Item):
    train_no = scrapy.Field()
    no = scrapy.Field()
    station = scrapy.Field()
    start_time = scrapy.Field()
    arrive_time = scrapy.Field()
    stopover_time = scrapy.Field()
    seat_type = scrapy.Field()
    turn = scrapy.Field()

