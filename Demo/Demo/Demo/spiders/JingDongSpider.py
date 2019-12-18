from scrapy import Spider,Request
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

class JingdongSpider(Spider):
    name = 'jingdong'

    def __init__(self):
        options = Options()
        options.add_argument('--headless')
        self.browser = webdriver.Firefox(options=options)
        self.browser.set_page_load_timeout(30)
        self.browser.set_window_size(500,500)#设置浏览器窗口大小

    def closed(self,spider):
        print("spider closed")
        self.browser.close()

    def start_requests(self):
        start_urls = ['https://search.jd.com/Search?keyword=%E6%96%87%E8%83%B8&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&suggest=1.his.0.0&page={}&s=1&click=0'.format(str(i)) for i in range(1,2,2)]
        for url in start_urls:
            yield Request(url=url, callback=self.parse)


    def parse(self, response):
        selector = response.xpath('//ul[@class="gl-warp clearfix"]/li')
        temp = response.body
        print(temp)
        print(len(selector))
        print('---------------------------------------------------')