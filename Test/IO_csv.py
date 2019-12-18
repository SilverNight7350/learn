import pandas as pd
data = []
data_temp = []
data_temp1 = []
data = pd.read_csv('/home/zyc/PycharmProjects/Test/top-1m.csv')
for i in range(100):
    data.loc[i,'domain'] = "http://" + data.loc[i,'domain']
    data_temp.append(data.loc[i,'domain'])
# data_temp.append("hello")
# data_temp.append("world")
data_temp1 = data_temp
print(data_temp1)


# data = pd.read_csv('/home/zyc/可查询的关键字.csv')
# for i in range(30):
#     data_temp.append(data.loc[i,'可检索关键词'])
# print(data_temp[1])
