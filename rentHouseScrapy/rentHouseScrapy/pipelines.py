# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os

base_dir = os.getcwd()

from pymongo import MongoClient
import os

base_dir = os.getcwd()


class MongoPipeline(object):
    # 实现保存到mongo数据库的类，
    collection = 'ftx'  # mongo 数据库的 collection 的默认名字

    def __init__(self, mongo_uri, db_name, db_user, db_pass):
        self.mongo_uri = mongo_uri
        self.db_name = db_name
        self.db_user = db_user
        self.db_pass = db_pass

    @classmethod
    def from_crawler(cls, crawler):
        # scrapy 为我们访问settings提供了这样的一个方法，这里，
        # 我们需要从 settings.py 文件中，取得数据库的URI和数据库名称
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            db_name=crawler.settings.get('DB_NAME'),
            db_user=crawler.settings.get('DB_USER'),
            db_pass=crawler.settings.get('DB_PASS'))

    def open_spider(self, spider):  # 爬虫启动时调用，连接到数据库
        self.client = MongoClient(self.mongo_uri)
        self.zfdb = self.client[self.db_name]
        self.zfdb.authenticate(self.db_user, self.db_pass)

    def close_spider(self, spider):  # 爬虫关闭时调用，关闭数据库连接
        self.client.close()

    def process_item(self, item, spider):
        # if item["region"]:
        self.collection = item["region"]
        if item["region"] =="不限":
            item["region"] = item["address"][0:2]

        # self.zfdb[self.collection].insert({
        #     "title": item["title"].strip(),
        #     "rooms": item["rooms"],
        #     "area": item["area"],
        #     "price": item["price"],
        #     "address": item["address"],
        #     "traffic": item["traffic"],
        #     "region": item["region"],
        #     "direction": item["direction"],
        # })
        return item


# import json
# class JsonPipeline(object):
#     file_name = base_dir + '/rentHouseScrapy/data.json'  # json 文件路径
#
#     def process_item(self, item, spider):
#         file = open(self.file_name, 'r', encoding='utf-8')
#         load_data = json.load(file)
#         load_data.append(item)
#         file = open(self.file_name, 'w', encoding='utf-8')
#         json.dump(load_data, file, ensure_ascii=False)
#         file.close()
#         return item
