import scrapy
from scrapy.http import Request
from scrapy.selector import Selector
from urllib.parse import urljoin
from doubanTop250.items import Doubantop250Item,DoubanItemLoader
# from urllib import parse
# url = parse.urljoin("a","b")
# 会提取 a 中的主域名，再拼接 b 地址。如果 b url 中有域名，则不会发生其他改变。如果没有，则会与 a url 进行拼接

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
    #
    # def parse(self, response):
    #     # 默认回调函数
    #     pass
    #
    # def close(self,reson):
    #     # 关闭时调用
    #     pass







    # 每当网页数据 download 下来，就会发送到这里进行解析
    # 然后返回一个新的链接，加入 request 队列
    def parse(self, response):
        # print(response.request.headers['User-Agent'])
        # print(response.body)
        # self.logger.info(response.body)
        item = Doubantop250Item()
        selector = Selector(response)
        print(response.xpath('/html/body/div[3]/div[1]/h1'))
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
            item['title'] = fullTitle.strip()
            item['movieInfo'] = ';'.join(movieInfo).strip()
            item['star'] = star.strip()
            item['quote'] = quote.strip()
            yield item

        # scrapy 的高级用法
        # item_loader = DoubanItemLoader(item=Doubantop250Item, response=response)
        # item_loader.add_css('title', 'html.ua-mac.ua-ff65 body div#wrapper div#content h1')
        # item_loader.add_xpath("star", '//div[@class="info"]/div[@class="bd"]/div[@class="star"]/span/text()')
        # item_loader.add_xpath("quote", '//div[@class="info"]/div[@class="bd"]/p[@class="quote"]/span/text()')
        # item_loader.add_xpath("movieInfo", '//div[@class="info"]/div[@class="bd"]/p/text()')
        # print(item_loader)
        # yield item_loader
        # from w3lib.html import remove_tags


        # nextLink = selector.xpath('//span[@class="next"]/link/@href').extract()
        print("=========================================")
        # print(nextLink)
        print("=========================================")
        # 第10页是最后一页，没有下一页的链接
        # if nextLink:
        #     nextLink = nextLink[0]
        #     yield Request(urljoin(response.url, nextLink), callback=self.parse)
