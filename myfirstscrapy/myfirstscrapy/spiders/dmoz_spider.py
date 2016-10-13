# -*- coding: utf-8 -*-
import scrapy
from myfirstscrapy.items import MyfirstscrapyItem

class DmozSpiderSpider(scrapy.Spider):
    name = "dmoz_spider"
    allowed_domains = ["dmoz.org"]
    start_urls = (
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    )

    def parse(self, response):
        # 爬取上面两个URL的源代码
        # filename = response.url.split('/')[-2] + '.html'
        # with open(filename,'wb') as fp:
        #     fp.write(response.body)

        lis = response.xpath("/html/body/div[@id='main-content']/div[@id='doc']/section[@class='results sites']/div[@id='sites-section']/div[@id='site-list-content']/div[@class='site-item '][1]/div[@class='title-and-desc']/*")

        for li in lis:
            item = MyfirstscrapyItem()
            item['title'] = li.xpath('a/dev/text()').extract()
            item['link'] = li.xpath('a/@href').extract()
            item['desc'] = li.xpath('dev/text()')












