#coding:utf-8

'''
sudo apt-get install python-dev python-pip libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev
pip install scrapy (最好在virtualenv中进行)
运行命令：scrapy runspider stackoverflow_spider.py -o abc.csv,有JSON,CSV,XML格式
具体的抓取过程：
1)使用start_urls作为初始url生成Request,并默认把parse作为它的回调函数
2)在parse中采用css选择器获得目标URL,并注册parse_question作为目标URL的回调函数
'''

import scrapy

class StackOverflowSpider(scrapy.Spider):
    # 爬虫的名字
    name = 'stackoverflow'
    # 爬取的URL
    start_urls = ['http://stackoverflow.com/questions?sort=votes']

    def parse(self, response):
        for href in response.css('.question-summary h3 a::attr(href)'):
            full_url = response.urljoin(href.extract())
            yield scrapy.Request(full_url, callback=self.parse_question)

    def parse_question(self, response):
        yield {
            'title': response.css('h1 a::text').extract_first(),
            'votes': response.css('.question .vote-count-post::text').extract_first(),
            'body': response.css('.question .post-text').extract_first(),
            'tags': response.css('.question .post-tag::text').extract(),
            'link': response.url,
        }











