# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.conf import settings
import pymongo


class MongodbPipeline(object):

    def __init__(self):
        host = "localhost"
        port = 27017
        db_name = "house_rent"
        col = "rent_58"
        client = pymongo.MongoClient(host=host, port=port)
        db = client[db_name]
        self.collection = db[col]

    def process_item(self, item, spider):
        data = dict(item)
        self.collection.insert(data)
        print('[yeah!!!]insert into mongoDB seccessfully')
        return item
