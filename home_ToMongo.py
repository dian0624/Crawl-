import requests
import pymongo
import re

class HomeSpyder:
    def __init__(self):
        self.headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"}
        self.baseurl = "https://bj.lianjia.com/ershoufang/pg"
        self.proxies = {"http":"http://216.198.188.26:51068"}
        self.page = 1
        self.conn = pymongo.MongoClient("localhost",27017)
        self.db = self.conn.Lianjia
        self.myset  = self.db.Price
    
    def readPage(self,url):
        res = requests.get(url,proxies=self.proxies,headers=self.headers,timeout=5)
        res.encoding = "utf-8"
        html = res.text
        print("頁面讀取成功，正在解析...")
        self.parePage(html)

    def parePage(self,html):
        pattern = '<div class="positionInfo".*?"region">(.*?)</a>.*?"_blank">(.*?)</a>.*?totalPrice.*?<span>(.*?)</span>'
        p = re.compile(pattern,re.S)
        r_list = p.findall(html)
        print("頁面解析完成，正在存入數據庫...")
        self.writePage(r_list)
        
    def writePage(self,r_list):
        for r_tuple in r_list:
            houseName = r_tuple[0].strip()+"-"+r_tuple[1].strip()
            totalPrice = float(r_tuple[2].strip())*10000
            D = {"houseName":houseName,
                  "totalPrice":totalPrice}
            self.myset.insert(D)  
        print("寫入成功")

    def workOn(self):
        while True:
            c = input("是否爬取(y/n):")
            if c.strip().lower() == "y":
                url = self.baseurl + str(self.page) +"/"
                self.readPage(url)
                self.page += 1
            else:
                print("爬取結束")
                break
    
if __name__ == "__main__":
    spyder = HomeSpyder()
    spyder.workOn()





