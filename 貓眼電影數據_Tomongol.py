import re 
import pymongo
import requests

class CatMovie():
    def __init__(self):
        self.headers = {"User-Agent":"Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_8;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50"}
        self.baseurl = "http://maoyan.com/board/4?offset="
        self.page = 1
        self.offset = 0
        self.conn = pymongo.MongoClient("localhost",27017)
        self.db = self.conn.CatMovie
        self.myset = self.db.top100

    def loadPage(self,url):
        res = requests.get(url,headers=self.headers,timeout=5)
        res.encoding = "utf-8"
        html = res.text
        print("讀取頁面成功，正在解析...")
        self.parePage(html)
    
    def parePage(self,html):
        pattern = '<div class="movie-item-info">.*?title="(.*?)".*?<p class="star">.*?主演.(.*?)</p>.*?releasetime">上映时间.(.*?)</p>'
        p = re.compile(pattern,re.S)
        r_list = p.findall(html)
        print("解析成功，正在寫入數據庫...")
        print(r_list)
        self.writePage(r_list) 
        
    def writePage(self,r_list):
        for r_tuple in r_list:
            name = r_tuple[0].strip()
            actor = r_tuple[1].strip()
            m_time = r_tuple[2].strip()
            D = {"name":name,"actor":actor,"time":m_time}
            self.myset.insert(D)
        print("寫入成功")
    
    def workOn(self):
        while True:
            c = input("是否爬取(y/n)?")
            if c.strip().lower() == "y":
                self.offset = (self.page-1) *10
                url = self.baseurl + str(self.offset)
                self.loadPage(url)
                self.page += 1
            else:
                print("爬取結束，謝謝使用")
                break
    
if __name__ == "__main__":
    spider = CatMovie()
    spider.workOn()