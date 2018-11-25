# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LagouscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()  # 职位名称(python工程师)
    company = scrapy.Field()  # 公司名称（xxx有限公司）
    welfare = scrapy.Field()  # 福利（餐补、下午茶、带薪年假）
    salaryMin = scrapy.Field()  # 工资下限（9k）
    salaryMid = scrapy.Field()  # 工资下限（9k+15k）/2
    salaryMax = scrapy.Field()  # 工资上限（15k）
    experience = scrapy.Field()  # 工作经验（经验3-5年）
    education = scrapy.Field()  # 教育程度（本科）
    companyType = scrapy.Field()  # 公司类型（移动互联网/信息安全）
    companyLevel = scrapy.Field()  # 公司级别（上市公司）
    companySize = scrapy.Field()  # 公司人数规模（150-500人）
    pass
