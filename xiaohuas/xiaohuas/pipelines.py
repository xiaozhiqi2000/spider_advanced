# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class Spider1Pipeline(object):
    def process_item(self, item, spider):

        #item['school']
        print "start".center(60,"*")
        print item
        print "end".center(60,"*")
        import os
        import urllib

        ab_src = "http://www.xiaohuar.com" + item['src']
        print ab_src
        file_name = item['name'] + '.jpg'
        file_path = os.path.join('/home/tomcat/workplace/spider_advanced/spider1/image/', file_name)
        urllib.urlretrieve(ab_src, file_path)


        return item
