import pandas as pd
import re
import db_test
from pymongo import MongoClient

data_temp = [] #存放了要进行检索的关键字
data = pd.read_csv('/home/zyc/可查询的关键字.csv')
data_df = pd.DataFrame(data)
# for i,row in data_df.iterrows():
#     #这里i是序号,row是数据内部所含的内容
#     print(row['可检索关键词'])
#     #print(i)

#连接数据库

mongo = db_test.MyMongoDB()
# mongo.findAll()
# mongo.my_set.find()
for temp in mongo.my_set.find():
    #对数据库的内容进行遍历，然后经过提取的各个关键进行正则表达式的分析。
    #print(temp['html'])
    temp_str = str(temp['html'])#把html转换为字符串我下一步的检索关键字做准备
    temp_domain = str(temp['domain'])
    for i,row in data_df.iterrows():
        #对可检索关键词的遍历，确保对每一个html都检索了每一个关键词
        temp_re = row['可检索关键词']
        match_web = re.search(temp_re,temp_str)
        if match_web:
            mongo.update({"domain": temp_domain}, {"$set": {"inject": "1"}})
            print("数据已更新")
        else:
            print(temp_domain)
            print("no match")




#可通过['']的方式来获取数据库中存放的html文件，在经过扫描后如何有问题需要对数据库中对应的部分进行修改。
#print(temp['html'])
# temp_str = str(temp)
# matchWeb = re.search('html',temp_str)
#print(temp_str[96:100])
#只要找到这个网页里是有我们寻找的关键字即可
# pattern = re.compile(r'([a-z]+) ([a-z]+)', re.I)   # re.I 表示忽略大小写
# m = pattern.match('Hello World Wide Web')
# print m                               # 匹配成功，返回一个 Match 对象
