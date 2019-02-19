# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from scrapy.http import Request
from urllib.parse import urljoin


class JdSpiderSpider(scrapy.Spider):
    name = 'jd_spider'
    allowed_domains = ['jd.com']
    start_urls = ['https://shouji.jd.com/shoujisort.html']

    def parse(self, response):
        selector = Selector(response)
        # print(selector.extract())
        print(selector.css('.title-name'))
        nextLink = 'https://sale.jd.com/act/8yaD0qZuE6VFk.html'
        yield Request(urljoin(response.url, nextLink), callback=self.detail, dont_filter=True)

    def detail(self, response):
        selector = Selector(response)
        print(selector.extract())
        # print(response.extract())
