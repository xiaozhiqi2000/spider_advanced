# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql.cursors

from project28.items import CommitItem
from project28.items import BriefDeltaItem
from project28.items import StationItem

class SQLPipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(host = 'localhost', port = 3306, 
                                        user = '12306',
                                        password = '12306',
                                        db = '12306-train',
                                        charset = 'utf8')
        self.cursor = self.conn.cursor()
        self.update_brief = "UPDATE `train_briefs` SET \
                    `seat_type` = %s WHERE `code` = %s"
        self.station_sql = "INSERT IGNORE INTO `train_stations` VALUES\
                    (%s, %s)"
        self.tickets_sql = "INSERT IGNORE INTO `train_tickets` VALUES\
                    (%s, %s, %s, %s, %s, %s, %s, %s,\
                    %s, %s, %s, %s, %s, %s)"

    def process_item(self, item, spider):
        try:
            if isinstance(item, CommitItem):
                self.conn.commit()
            elif isinstance(item, BriefDeltaItem):
                self.cursor.execute(self.update_brief, (item["seat_type"], 
                    item["code"]))
            elif isinstance(item, StationItem):
                self.cursor.execute(self.station_sql, (item["name"], 
                    item["code"]))
            else:
                self.cursor.execute(self.tickets_sql, (item["train_no"],
                    item["start"], item["end"], item["swz"],
                    item["tz"], item["zy"], item["ze"],
                    item["gr"], item["rw"], item["yw"],
                    item["rz"], item["yz"], item["wz"],
                    item["qt"]))
        except Exception, e:
            spider.logger.warning("excute sql fail.")
            spider.logger.warning(str(e))
        
