import scrapy
from ..items import DemoItem
import scrapy, re, json, sys
import pandas as pd
from ..items import DemoItem

#重构爬虫文件，保留爬取到的域名以及对应的html文件，同时添加一列属性表明该网页是否用于被感染的代码。
#添加模仿用户行为的代码之后再进行爬取，观察爬取到的网页是否为网页的源代码
class WebSpider(scrapy.Spider):
    name = 'webspider'
    data = []
    data_temp = []
    data = pd.read_csv('/home/zyc/PycharmProjects/Test/top-1m.csv')
    for i in range(10):
        data.loc[i, 'domain'] = "http://" + data.loc[i, 'domain']
        data_temp.append(data.loc[i, 'domain'])
    # data_temp.append("hello")
    # data_temp.append("world")
    #print(data_temp)
    #allowed_domains = ['posthemes.com/']
    #data_temp即为要检索的从alexa提取出的网址名字
    #start_urls = data_temp  这里是根据提取出的csv文件来进行爬取
    start_urls = ['http://adamsnaturals.com/',
                  'http://www.soufeel.com.cn/',
                  'https://woodpeckerfurniture.com/',
                  'https://www.swisstgallery.com/',
                  'http://cmi-co.com/',
                  'http://www.canderediamonds.com/',
                  'http://www.angzcommerz.com/',
                  'https://www.tarrianalee.co.uk',
                  'https://www.halloweenhallway.com',
                  'http://www.goftogoonews.com/UserFiles/media/4f81cxeo/womens_nike_free_5.0_2014_nike_free_5.0_sale_which_nike_free.asp?/yos459g'
                  ]

    def parse(self, response):
        WebPage = response.body
        #soup = BeautifulSoup(WebPage,"lxml")
        item = DemoItem()
        item['html'] = WebPage
        item['infect'] = 1
        #这里用0代表默认了这个网页是没有被感染的
        item['domain'] = response.url
        #print(item['html'])
        yield item
        '''
        scripts = soup.find_all(name="script")
        for script in scripts:
            print(script)
        '''