from selenium import webdriver
from time import sleep

# 有窗口访问百度
driver=webdriver.Firefox()
driver.get("http://www.baidu.com")

# 设置浏览器窗口大小
driver.set_window_size(500, 500)

# 搜索
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
sleep(2)

# 通过javascript设置浏览器窗口的滚动条位置
js="window.scrollTo(100,1600);"
driver.execute_script(js)
sleep(3)

driver.quit()
#
# #无窗口访问浏览器
#
# from selenium.webdriver.firefox.options import Options
# from selenium import webdriver
#
# url = 'https://www.baidu.com'
#
# # 设置chrome为无界面浏览器
# options = Options()
# options.add_argument('--headless')
#
# # 打开浏览器
# browser = webdriver.Firefox(options=options)
# #browser = webdriver.Firefox()
# # 利用get请求请求浏览器的一个网页
# browser.get(url=url)
#
# # 打印输出这个网页的源代码
# print(browser.page_source)
#
# # 设置浏览器窗口大小
# browser.set_window_size(500, 500)
#
# # 搜索
# browser.find_element_by_id("kw").send_keys("selenium")
# browser.find_element_by_id("su").click()
# sleep(2)
#
# # 通过javascript设置浏览器窗口的滚动条位置
# js="window.scrollTo(100,450);"
# browser.execute_script(js)
# sleep(3)
#
# # 关闭浏览器
# browser.close()
#
# # 杀死chrome浏览器的连接桥(chromedriver)的进程
# browser.quit()

