import scrapy
from scrapy.http import Request
from bs4 import BeautifulSoup
from rentHouseScrapy.items import RenthousescrapyItem

class FtxSpider(scrapy.spiders.Spider):
    baseUrl = "http://km.zu.fang.com"
    allUrlList = []
    headUrlList = []
    name = "ftx"
    allowed_domains = ["fang.com"]

    # start_urls = ["http://gz.zu.fang.com/house-a078/"]


    def start_requests(self):
        start_url = self.baseUrl
        return [scrapy.FormRequest(start_url, callback=self.head_url_callback)]
    # 先获取头部 url
    def head_url_callback(self, response):
        self.logger.info("========== head_url_callback ================")

        soup = BeautifulSoup(response.body, "html5lib")
        dl = soup.find_all("dl", attrs={"id": "rentid_D04_01"})  # 获取各地区的 url 地址的 dl 标签
        my_as = dl[0].find_all("a")  # 获取 dl 标签中所有的 a 标签，
        for my_a in my_as:
            if my_a.text == "不限":  # 不限地区的,特殊处理
                self.headUrlList.append(self.baseUrl)
                self.allUrlList.append(self.baseUrl)
                continue
            if "周边" in my_a.text:  # 清除周边地区的数据
                continue
            # print(my_a["href"])
            # print(my_a.text)
            self.allUrlList.append(self.baseUrl + my_a["href"])
            self.headUrlList.append(self.baseUrl + my_a["href"])
        print(self.allUrlList)
        url = self.headUrlList.pop(0)
        yield Request(url, callback=self.all_url_callback, dont_filter=True)

    # 获取非头部 url
    def all_url_callback(self, response): # 解析并拼接所有需要爬取的 url 地址
        self.logger.info("========== all_url_callback ================")

        soup = BeautifulSoup(response.body, "html5lib")
        div = soup.find_all("div", attrs={"id": "rentid_D10_01"})  # 获取各地区的 url 地址的 dl 标签
        span = div[0].find_all("span")  # 获取 dl 标签中所有的 span 标签，
        span_text = span[0].text
        print(span_text)
        for index in range(int(span_text[1:len(span_text) - 1])):
            if index == 0:
                pass
                # self.allUrlList.append(self.baseUrl + my_a["href"])
            else:
                if self.baseUrl == response.url:
                    self.allUrlList.append(response.url + "house/i3" + str(index + 1) + "/")
                    continue
                self.allUrlList.append(response.url + "i3" + str(index + 1) + "/")
        print(self.allUrlList)
        if len(self.headUrlList) == 0:
            url = self.allUrlList.pop(0)
            yield Request(url, callback=self.parse, dont_filter=True)
        else:
            url = self.headUrlList.pop(0)
            yield Request(url, callback=self.all_url_callback, dont_filter=True)

    # 解析一个数据页面
    def parse(self, response):
        self.logger.info("==========================")
        soup = BeautifulSoup(response.body, "html5lib")
        divs = soup.find_all("dd", attrs={"class": "info rel"})  # 获取需要爬取得 div
        for div in divs:
            ps = div.find_all("p")
            try:  # 捕获异常，因为页面中有些数据没有被填写完整，或者被插入了一条广告，则会没有相应的标签，所以会报错
                for index, p in enumerate(ps):  # 从源码中可以看出，每一条 p 标签都有我们想要的信息，故在此遍历 p 标签，
                    text = p.text.strip()
                    print(text)  # 输出看看是否为我们想要的信息
                print("===================================")
                # 爬取并存进 MongoDB 数据库
                roomMsg = ps[1].text.split("|")
                area = roomMsg[2].strip()[:len(roomMsg[2]) - 1]
                item = RenthousescrapyItem()
                item["title"] = ps[0].text.strip()
                item["rooms"] = roomMsg[1].strip()
                item["area"] = int(float(area))
                item["price"] = int(ps[len(ps) - 1].text.strip()[:len(ps[len(ps) - 1].text.strip()) - 3])
                item["address"] = ps[2].text.strip()
                item["traffic"] = ps[3].text.strip()
                if (self.baseUrl+"house/") in response.url: # 对不限区域的地方进行区分
                    item["region"] = "不限"
                else:
                    item["region"] = ps[2].text.strip()[:2]
                item["direction"] = roomMsg[3].strip()
                print(item)
                yield item
            except:
                print("糟糕，出现 exception")
                continue
        if len(self.allUrlList) != 0:
            url = self.allUrlList.pop(0)
            yield Request(url, callback=self.parse, dont_filter=True)
