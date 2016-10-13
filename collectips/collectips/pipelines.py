# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
'''
mysql> CREATE DATABASE IF NOT EXISTS ippool DEFAULT CHARACTER SET utf-8;
mysql> CREATE TABLE IF NOT EXISTS `proxy` (  `IP` varchar(255) NOT NULL DEFAULT '',
                                            `PORT` varchar(255) NOT NULL DEFAULT '',
                                            `TYPE` varchar(255) DEFAULT NULL,
                                            `GET_POST` varchar(255) DEFAULT NULL,
                                            `POSITION` varchar(255) DEFAULT NULL,
                                            `SPEED` varchar(255) DEFAULT NULL,
                                            `LAST_CHECK_TIME` varchar(255) DEFAULT NULL,
                                            PRIMARY KEY (`IP`,`PORT`) ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
'''
import pymysql
import json

class JsonPipeline(object):

    def __init__(self):
        self.file = open('/home/tomcat/workplace/spider_advanced/collectips/collectips/xici.json', 'wb')

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item


class CollectipsPipeline(object):

    def process_item(self, item, spider):

        DBKWARGS = spider.settings.get('DBKWARGS')
        con = pymysql.connect(**DBKWARGS)
        cur = con.cursor()
        sql = ("insert into proxy(IP,PORT,TYPE,POSITION,SPEED,LAST_CHECK_TIME)"
               "values(%s,%s,%s,%s,%s,%s)")
        lis = (item['IP'],item['PORT'],item['TYPE'],item['POSITION'],item['SPEED'],item['LAST_CHECK_TIME'])
        try:
            cur.execute(sql,lis)
        except Exception,e:
            print "Insert error:",e
            con.rollback()
        else:
            con.commit()
        cur.close()
        con.close()
        return item









