import scrapy
from scrapy.http import Request
from scrapy.selector import Selector
from urllib.parse import urljoin
from girlScrapy.items import ImgItem
from bs4 import BeautifulSoup


class GirlSpider(scrapy.spiders.Spider):
    name = 'girl'
    start_urls = ["http://www.meizitu.com/a/3741.html"]
    def parse(self, response):
        soup = BeautifulSoup(response.body, 'html5lib')
        pic_list = soup.find('div', id="picture").find_all('img')  # 找到界面所有图片
        link_list = []
        item = ImgItem()
        for i in pic_list:
            pic_link = i.get('src')  # 拿到图片的具体 url
            link_list.append(pic_link)  # 提取图片链接
        item['image_urls'] = link_list
        print(item)
        yield item

