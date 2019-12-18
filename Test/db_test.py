# -*- coding:utf-8 -*-
from pymongo import MongoClient

settings = {
    "ip":'0.0.0.0',   #ip
    "port":27017,           #端口
    "db_name" : "tutorial",    #数据库名字，没有则自动创建
    "set_name" : "data",   #集合名字，没有则自动创建
    "user" : "simple",
    "password" : "test"

}
#set_name相当于是表的样子

class MyMongoDB(object):
    def __init__(self):
        try:
            self.conn = MongoClient(settings["ip"], settings["port"])
        except Exception as e:
            print(e)
        self.db = self.conn[settings["db_name"]]
        self.db.authenticate(settings["user"],settings["password"])
        self.my_set = self.db[settings["set_name"]]
    #插入
    def insert(self,dic):
        self.my_set.insert(dic)
        print("插入成功")
    #更新
    def update(self,dic,newdic):
        self.my_set.update(dic,newdic)
        print("更新成功")
    #删除
    def delete(self,dic):
        self.my_set.remove(dic)
        print("删除成功")
    #查找
    def dbFind(self,dic):
        data = self.my_set.find(dic)
        for result in data:
            print(result)
        print("查找成功")
    #查找全部
    def findAll(self):
        # 查询全部
        for i in self.my_set.find():
            print(i)

if __name__ == "__main__":
    # dic = {"name": "tom", "age": 18}
    # mongo = MyMongoDB()
    #
    # mongo.insert(dic)
    # mongo.findAll()
    #
    # mongo.update({"name": "tom"}, {"$set": {"age": "25"}})
    # mongo.dbFind({"name": "tom"})
    #
    # mongo.delete({"name": "tom"})
    # mongo.findAll()
    mongo = MyMongoDB()
    #mongo.findAll()
    mongo.update({"domain": "http://nic.jot"},{"$set": {"infect": "0"}})
    mongo.findAll()