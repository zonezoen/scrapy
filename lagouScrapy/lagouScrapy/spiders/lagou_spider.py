import scrapy
from scrapy.http import Request
from scrapy.selector import Selector
from urllib.parse import urljoin
from lagouScrapy.items import LagouscrapyItem
import requests

class LagouSpider(scrapy.spiders.Spider):
    # 要爬取的城市列表
    def getCity(self):
        return [
            "全国",
            "北京",
            "上海",
            "深圳",
            "广州",
        ]

    # "https://www.lagou.com/jobs/positionAjax.json?px=default&city=%E5%B9%BF%E5%B7%9E&needAddtionalResult=false"
    # https://www.lagou.com/jobs/positionAjax.json?px=default&city=%E5%B9%BF%E5%B7%9E&needAddtionalResult=false
    #     first = false
    #     pn = 4
    #     kd = python
    # 要爬取的语言列表
    def getLanguage(self):
        return [
            # "Java",
            # "Python",
            # "C",
            # "机器学习",
            "自然语言",
            "图像识别",
            # "区块链",
            # "精准推荐",
            # "Node.js",
            # "Go",
            # "Hadoop",
            # "Php",
            # ".NET",
            # "Android",
            # "iOS",
            # "web前端",
        ]

    # 经过观察发现，拉钩的 url 随语言和城市的变化如下
    def getUrl(self, language, city):
        url = "https://www.lagou.com/jobs/list_" + language + "?px=default&city=" + city
        return url

    # 获取一个城市，列表中所有语言的 url 列表
    def getCityUrl(self, city):
        urlList = []
        for language in self.getLanguage():
            urlList.append(self.getUrl(language, city))
        return urlList

    name = "lagou"
    allowed_domains = ["lagou.com"]
    # start_urls = ["https://www.lagou.com/jobs/list_python?px=default&city=广州"]

    def start_request(self):
        url = "https://www.lagou.com/jobs/list_python?px=default&city=广州"
        result = requests.get(url)
        cookies = result.cookies
        self.logger.info("====================")
        self.logger.info(cookies)
        self.logger.info("====================")
        # yield scrapy.Request(url=url,
        #                              cookies= cookies,
        #                              headers= headers,
        #                              callback= self.parse,
        #                              dont_filter = True)
        yield scrapy.Request(url=url, cookies=cookies)

    def parse(self, response):
        self.logger.info("body: "+response.body)
        self.logger.info("body: =================")
        self.logger.info("body: =================")
        self.logger.info("body: =================")
        self.logger.info("body: =================")
        # yield Request(urljoin(response.url, nextLink), callback=self.parse)
