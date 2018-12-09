# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class RenthousescrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    title = scrapy.Field()  # 标题
    rooms = scrapy.Field()  # 房间数
    area = scrapy.Field()  # 平方数
    price = scrapy.Field()  # 价格
    address = scrapy.Field()  # 地址
    traffic = scrapy.Field()  # 交通描述
    region = scrapy.Field()  # 区、（福田区、南山区）
    direction = scrapy.Field()  # 房子朝向（朝南、朝南北）
    pass
