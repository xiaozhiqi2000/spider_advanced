# -*- coding: utf-8 -*-

# import the spiders you want to run
from spiders.example1 import Example1Spider

# scrapy api imports
from twisted.internet import reactor
from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings
from scrapy.utils.project import get_project_settings

settings = get_project_settings()

crawler = CrawlerProcess(settings)

crawler.crawl(Example1Spider)

crawler.start()















# vim: set ts=4 sw=4 sts=4 tw=100 et:
