# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql.cursors

from project24.items import CommitItem

class StationSQLPipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(host = 'localhost', port = 3306, 
                                        user = '12306',
                                        password = '12306',
                                        db = '12306-train',
                                        charset = 'utf8')
        self.cursor = self.conn.cursor()
        self.sql = "INSERT IGNORE INTO `stations` (`bureau`, `station`,\
                `name`, `address`, `passenger`, `luggage`,\
                `package`) VALUES\
                (%s, %s, %s, %s, %s, %s, %s)"

    def process_item(self, item, spider):
        if isinstance(item, CommitItem):
            try:
                self.conn.commit()
            except Exception, e:
                spider.logger.warning("commit fail.")
        else:
            try:
                self.cursor.execute(self.sql, (item["bureau"], item["station"],
                    item["name"], item["address"],
                    item["passenger"], item["luggage"],
                    item["package"]))
            except Exception, e:
                spider.logger.warning("insert item fail.")
        
