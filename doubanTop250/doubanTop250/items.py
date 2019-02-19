# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose, Join
class DoubanItemLoader(ItemLoader):
    default_output_processor = TakeFirst()


# input_processor = Join(',')
# input_processor = MapCompose(remove_tags)

class Doubantop250Item(scrapy.Item):
    title = scrapy.Field()  # 电影名字
    star = scrapy.Field()  # 电影评分
    quote = scrapy.Field()  # 脍炙人口的一句话
    movieInfo = scrapy.Field()  # 电影的描述信息，包括导演、主演、电影类型

    # def get_insert_sql(self):
    #     sql = """
    #     insert into ladou_job(title,url) VALUES (%s,%s)
    #     """
    #     params = (self["title"],["url"])
    #     return sql,params













