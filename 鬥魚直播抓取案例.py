from selenium import webdriver
from lxml import etree
import time 

opt = webdriver.ChromeOptions()
opt.set_headless()
driver = webdriver.Chrome(options=opt)
driver.get('https://www.douyu.com/directory/all')

i = 1
while True:
    pareHtml = etree.HTML(driver.page_source)
    names = pareHtml.xpath('//li/div/a/div[@class="DyListCover-content"]/div[@class="DyListCover-info"]/h2/text()')
    numbers = pareHtml.xpath('//li/div/a/div[@class="DyListCover-content"]/div[@class="DyListCover-info"]/span[@class="DyListCover-hot"]/text()')
    for name,number in zip(names,numbers):
        print("主播名稱:%s , 觀眾人數:%s"%(name,number))
    print("-----正在爬取第%s頁-----"%(i))
    i += 1

    if driver.page_source.find("dy-Pagination-disabled dy-Pagination-next") == -1:
        time.sleep(3)
        driver.find_element_by_class_name("dy-Pagination-item-custom").click()
        print("***********************************************************")
        time.sleep(2)     
    else:
        break
print("一共爬了%s頁"%i)


























