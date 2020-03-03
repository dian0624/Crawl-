from selenium import webdriver
import time 
import csv

pro = input("請輸入要爬取的商品:")
dreiver = webdriver.Chrome()
dreiver.get('https://www.jd.com/')

text = dreiver.find_element_by_class_name('text')
text.send_keys(pro)
button = dreiver.find_element_by_class_name('button')
button.click()
time.sleep(2)
page = 1

while True:
    print("正在爬取第%s頁"%page)
    dreiver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(2)
    r_list = dreiver.find_elements_by_xpath("//div[@id='J_goodsList']//li")
    
    for r in r_list:
        m = r.text.split("\n")
        price = m[0]
        name = m[1]
        commit = m[2]
        market = m[3]

        with open("商品.csv","a",newline="",encoding="utf-8") as f:
            writer = csv.writer(f)
            L = [name.strip(),price.strip(),
                 commit.strip(),market.strip()]
            writer.writerow(L)

    if dreiver.page_source.find('pn-next disabled') == -1:
        time.sleep(2)
        dreiver.find_element_by_class_name('pn-next').click()
        time.sleep(2)
        page += 1
    else:
        break

