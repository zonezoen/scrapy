import scrapy
from scrapy.http import Request
from scrapy.selector import Selector
from urllib.parse import urljoin
from bs4 import BeautifulSoup


# import sys
# sys.path.append("/Users/zone/Desktop/zone/work/featureTest/mScrapy/doubanTop250")

class FtxSpider(scrapy.spiders.Spider):

    urlList = []

    def __init__(self):
        name = "宝安"
        page = 3
        for index in range(page):
            if index == 0:
                self.urlList.append(self.baseUrl + self.urlDir[name])
            else:
                self.urlList.append(self.baseUrl + self.urlDir[name] + "i3" + str(index + 1) + "/")


    baseUrl = "http://sz.zu.fang.com"

    urlDir = {
        "不限": "/house/",
        "宝安": "/house-a089/",
        "龙岗": "/house-a090/",
        "南山": "/house-a087/",
        "福田": "/house-a085/",
        "罗湖": "/house-a086/",
        "盐田": "/house-a088/",
        "龙华区": "/house-a013080/",
        "坪山区": "/house-a013081/",
        "光明新区": "/house-a013079/",
        "大鹏新区": "/house-a013082/",
        "惠州": "/house-a013058/",
        "东莞": "/house-a013057/",
        "深圳周边": "/house-a016375/",
    }


    name = "ftx"
    allowed_domains = ["fang.com"]
    start_urls = [urlList.pop(0)]


    def parse(self, response):
        self.logger.info("==========================")
        # self.logger.info(response.cookies)
        # self.logger.info(response.body)
        # print(response.body)

        self.logger.info("==========================")
        selector = Selector(response)
        dds = selector.xpath('//dd[@class="info rel"]')
        # print(dds)
        print("print => dd => p")
        for dd in dds:
            ps = dd.xpath('p')
            print("=====================")
            # # roomMsg = ps[1].xpath('text()').extract().split("|")
            # # rentMsg 这样处理是因为有些信息未填写完整，导致对象报空
            # # area = roomMsg[2].strip()[:len(roomMsg[2]) - 2]
            # print(ps[0].xpath('text()').extract())
            # # print(roomMsg[1].xpath('text()').extract())
            # # print(int(float(area)),)
            # # print(int(ps[len(ps) - 1].xpath('text()').extract()[:len(ps[len(ps) - 1].xpath('text()').extract()) - 3]))
            # print(ps[2].xpath('text()').extract())
            # print(ps[3].xpath('text()').extract())
            # print(ps[2].xpath('text()').extract())
            # # print(roomMsg[3])

            for p in ps:
                print(p.xpath('text()').extract())

        yield Request(self.urlList.pop(0), callback=self.parse)

        # soup = BeautifulSoup(response.body, "html.parser")
        # divs = soup.find_all("dd", attrs={"class": "info rel"})  # 获取需要爬取得 div
        #
        # for div in divs:
        #     ps = div.find_all("p")
        #     try:  # 捕获异常，因为页面中有些数据没有被填写完整，或者被插入了一条广告，则会没有相应的标签，所以会报错
        #         for index, p in enumerate(ps):  # 从源码中可以看出，每一条 p 标签都有我们想要的信息，故在此遍历 p 标签，
        #             text = p.xpath('text()').extract()
        #             print(text)  # 输出看看是否为我们想要的信息
        #         print("===================================")
        #         # 爬取并存进 MongoDB 数据库
        #         roomMsg = ps[1].text.split("|")
        #         # rentMsg 这样处理是因为有些信息未填写完整，导致对象报空
        #         area = roomMsg[2].strip()[:len(roomMsg[2]) - 2]
        #         rentMsg = self.getRentMsg(
        #             ps[0].xpath('text()').extract().encode("gb2312"),
        #             roomMsg[1].strip().encode("gb2312"),
        #             int(float(area)).encode("gb2312"),
        #             int(ps[len(ps) - 1].xpath('text()').extract()[:len(ps[len(ps) - 1].xpath('text()').extract()) - 3]).encode("gb2312"),
        #             ps[2].xpath('text()').extract().encode("gb2312"),
        #             ps[3].xpath('text()').extract().encode("gb2312"),
        #             ps[2].xpath('text()').extract()[:2].encode("gb2312"),
        #             roomMsg[3].encode("gb2312"),
        #         )
        #         self.logger.info(rentMsg)
        #     except:
        #         continue
