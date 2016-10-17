# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql.cursors

from project32.items import CommitItem
from project32.items import BriefItem
from project32.items import InfoItem

class SQLPipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(host = 'localhost', port = 3306, 
                                        user = '12306',
                                        password = '12306',
                                        db = '12306-train',
                                        charset = 'utf8')
        self.cursor = self.conn.cursor()
        self.brief_sql = "INSERT IGNORE INTO `train_briefs` VALUES\
                    (%s, %s, %s, %s, %s)"
        self.info_sql = "INSERT IGNORE INTO `train_infos` VALUES\
                    (%s, %s, %s, %s, %s, %s, null, %s)"
        self.turn_sql = "INSERT IGNORE INTO `turns` VALUES\
                    (%s, %s)"

    def process_item(self, item, spider):
        try:
            if isinstance(item, CommitItem):
                self.conn.commit()
            elif isinstance(item, BriefItem):
                self.cursor.execute(self.brief_sql, (item["code"], 
                    item["train_no"],
                    item["start"], item["end"], item["turn"]))
            elif isinstance(item, InfoItem):
                self.cursor.execute(self.info_sql, (item["train_no"], 
                    item["no"],
                    item["station"],
                    item["start_time"], item["arrive_time"],
                    item["stopover_time"], item["turn"]))
            else:
                self.cursor.execute(self.turn_sql, (item["id"],
                    item["mark"]))
                self.conn.commit()
        except Exception, e:
            spider.logger.warning("excute sql fail.")
            spider.logger.warning(str(e))
        
