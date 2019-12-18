# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from pymongo import MongoClient

import json, codecs

class DemoPipeline(object):
    def __init__(self, databaseIp='0.0.0.0', databasePort=27017, user="simple", password="test",
                 mongodbName='tutorial'):
        client = MongoClient(databaseIp, databasePort)
        self.db = client[mongodbName]
        self.db.authenticate(user, password)

    def process_item(self, item, spider):
        postItem = dict(item)  # 把item转化成字典形式
        self.db.scrapy.insert(postItem)  # 向数据库插入一条记录
        return item  # 会在控制台输出原item数据，可以选择不写


class CsdnspiderPipeline(object):
    def process_item(self, item, spider):
        return item


class JsonWithEncodingCSDNPipeline(object):
    def __init__(self):
        self.file = codecs.open('papers.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        writeTime = json.dumps("日期：" + str(item['writeTime']), ensure_ascii=False) + "\n"
        title = json.dumps("标题：" + str(item['title']), ensure_ascii=False) + "\n"
        link = json.dumps("链接：" + str(item['link']), ensure_ascii=False) + "\n"
        readers = json.dumps("阅读次数：" + str(item['readers']), ensure_ascii=False) + "\t"
        comments = json.dumps("评论数量：" + str(item['comments']), ensure_ascii=False) + "\n\n"
        line = writeTime + title + link + readers + comments
        print(1)
        line1 = "test"
        self.file.write(line)
        self.file.write(line1)
        return item

    def spider_closed(self, spider):
        self.file.close()

class WebPipeline(object):
    def __init__(self, databaseIp='0.0.0.0', databasePort=27017, user="simple", password="test",
                 mongodbName='tutorial'):
        client = MongoClient(databaseIp, databasePort)
        self.db = client[mongodbName]
        self.db.authenticate(user, password)

    def process_item(self, item, spider):
        postItem = dict(item)  # 把item转化成字典形式
        self.db.inject_data.insert(postItem)  # 向数据库插入一条记录
        return item  # 会在控制台输出原item数据，可以选择不写