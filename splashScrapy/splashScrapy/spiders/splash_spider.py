import scrapy
from scrapy_splash import SplashRequest
from bs4 import BeautifulSoup


class Spider(scrapy.Spider):
    name = 'qq'
    allowed_domains = ['qq.com']
    start_urls = [
        'https://y.qq.com/portal/search.html#page=1&searchid=1&remoteplace=txt.yqq.top&t=song&w=%E5%91%A8%E6%9D%B0%E4%BC%A6']

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url=url, callback=self.parse)

    def parse(self, response):
        soup = BeautifulSoup(response.body, "html5lib")
        self.logger.info("======================= 数据 =============================")
        self.logger.info(soup.find_all(name='a', attrs={"class": "mod_tab__item js_tab", "data-tab": "song"})[0].text)
        self.logger.info("======================= 数据 =============================")
        self.logger.info(response.xpath('/html/body/div[1]/div/ul[1]/li[1]/a/text()').extract_first())
        self.logger.info("======================= 数据 =============================")
        self.logger.info(response.xpath('/html/body/div[3]/div/div/div[3]/a[1]/text()').extract_first())
        self.logger.info("======================= 数据 =============================")
