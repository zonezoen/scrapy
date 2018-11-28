import scrapy
from scrapy.http import Request
from scrapy.selector import Selector
from urllib.parse import urljoin
# import sys
# sys.path.append("/Users/zone/Desktop/zone/work/featureTest/mScrapy/doubanTop250")
from doubanTop250.items import Doubantop250Item

class DoubanTop250Spider(scrapy.spiders.Spider):
    # 此处为上面留下的小坑
    name = "douban"
    # 设置允许爬取的域名
    allowed_domains = ["douban.com"]
    # 设置起始 url
    start_urls = ["https://movie.douban.com/top250"]

    # # header信息
    # my_header = {
    #     'Host': 'www.douban.com',
    #     'Referer': 'https://movie.douban.com',
    # }
    #
    # # 表单需要提交的数据
    # form_data = {'user': 'zone', 'pass': 'zone7'}
    #
    # # 自定义信息，向下层响应(response)传递下去
    # customer_data = {'key1': 'value1', 'key2': 'value2'}
    # def start_requests(self):
    #     return [scrapy.FormRequest("https://movie.douban.com/login",
    #                                formdata=self.form_data,  # 表单提交的数据
    #                                headers=self.my_header,
    #                                method='POST',  # GET or POST
    #                                meta=self.customer_data,  # 自定义，向response传递数据
    #                                errback=self.error_handle,
    #                                callback=self.logged_in,
    #                                # 如果需要多次提交表单，且url一样，那么就必须加此参数 dont_filter，防止被当成重复网页过滤掉了
    #                                dont_filter=True
    #                                )]
    #
    # def logged_in(self, response):
    #     # 解析模拟登陆数据
    #     pass






    # 每当网页数据 download 下来，就会发送到这里进行解析
    # 然后返回一个新的链接，加入 request 队列
    def parse(self, response):
        print(response.request.headers['User-Agent'])
        # print(response.body)
        # self.logger.info(response.body)
        item = Doubantop250Item()
        selector = Selector(response)
        Movies = selector.xpath('//div[@class="info"]')
        # //*[@id="content"]/div/div[1]/ol/li[1]/div/div[2]/div[1]/a
        for eachMovie in Movies:
            title = eachMovie.xpath('div[@class="hd"]/a/span/text()').extract()  # 多个span标签
            fullTitle = "".join(title)  # 将多个字符串无缝连接起来
            movieInfo = eachMovie.xpath('div[@class="bd"]/p/text()').extract()
            star = eachMovie.xpath('div[@class="bd"]/div[@class="star"]/span/text()').extract()[0]
            quote = eachMovie.xpath('div[@class="bd"]/p[@class="quote"]/span/text()').extract()
            # quote可能为空，因此需要先进行判断
            if quote:
                quote = quote[0]
            else:
                quote = ''
            item['title'] = fullTitle
            item['movieInfo'] = ';'.join(movieInfo)
            item['star'] = star
            item['quote'] = quote
            # print(fullTitle)

            # print(star)
            # print(quote)
            # print()
            yield item
        nextLink = selector.xpath('//span[@class="next"]/link/@href').extract()
        print("=========================================")
        print(nextLink)
        print("=========================================")
        # 第10页是最后一页，没有下一页的链接
        if nextLink:
            nextLink = nextLink[0]
            yield Request(urljoin(response.url, nextLink), callback=self.parse)
