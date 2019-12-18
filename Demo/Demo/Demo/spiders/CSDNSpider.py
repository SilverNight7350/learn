from importlib import reload

import scrapy, re, json, sys
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.spiders import Rule

from ..items import DemoItem
from scrapy.spiders import CrawlSpider
from bs4 import BeautifulSoup



# 导入爬取一般网站常用类class scrapy.contrib.spiders.CrawlSpider和规则类Rule
from bs4 import BeautifulSoup


# 设置编码格式

add = 0


class CSDNPaperSpider(scrapy.spiders.CrawlSpider):
    name = "csdnSpider"
    allowed_domains = ["csdn.net"]
    # 定义爬虫的入口网页
    start_urls = ["https://blog.csdn.net/fly_yr/article/list/1"]
    # 自定义规则
    rules = [Rule(LxmlLinkExtractor(allow=('/article/list/\d{,2}')), follow=True, callback='parseItem')]

    # 定义提取网页数据到Items中的实现函数
    def parse(self, response):
        global add
        items = []
        data = response.body
        soup = BeautifulSoup(data, "html5lib")
        print(soup)
        # 找到所有的博文代码模块
        sites = soup.find_all(name='div', attrs={"class", "article-item-box csdn-tracking-statistics"})
        for site in sites:
            item = DemoItem()
            # 标题、链接、日期、阅读次数、评论个数
            item['title'] = site.find(name='span', attrs={"class", "article-type type-1 float-none"}).a.get_text()
            item['link'] = site.find('span', "link_title").a.get('href')
            item['writeTime'] = site.find('span', "link_postdate").get_text()
            item['readers'] = re.findall(re.compile(r'\((.*?)\)'), site.find('span', "link_view").get_text())[0]
            item['comments'] = re.findall(re.compile(r'\((.*?)\)'), site.find('span', "link_comments").get_text())[0]
            add += 1
            print(2)
            items.append(item)
        print("The total number:", add)
        return items

