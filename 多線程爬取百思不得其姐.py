import requests
from lxml import etree
from queue import Queue
import threading
import time

class Bsspider:
    def __init__(self):
        self.baseurl = "http://www.budejie.com/"
        self.headers = {"User-Agent":"Mozilla/5.0"}
        self.urlQueue = Queue()
        self.resQueue = Queue()
        
    def geturl(self):
        for pNum in range(1,51):
            url = self.baseurl + str(pNum)
            self.urlQueue.put(url)
    
    def getHtml(self):
        while True:
            url = self.urlQueue.get()
            res = requests.get(url,headers=self.headers)
            res.encoding = "utf-8"
            html = res.text
            self.resQueue.put(html)
            self.urlQueue.task_done()      
    
    def getContent(self):
        while True:
            html = self.resQueue.get()
            parseHtml = etree.HTML(html)
            r_list = parseHtml.xpath('//div[@class="j-r-list-c-desc"]/a/text()')
            for r in r_list:
                print(r+"\n")
            self.resQueue.task_done()
            
    def run(self):
        thread_list = []
        self.geturl()
        for i in range(3):
            threadRes = threading.Thread(target=self.getHtml)
            thread_list.append(threadRes)
        
        for i in range(2):
            threadPare =threading.Thread(target=self.getContent) 
            thread_list.append(threadPare)
            
        for th in thread_list:
            th.setDaemon(True)
            th.start()
            
        self.urlQueue.join()
        self.resQueue.join()
        
        print("運行結束")
        
   
if __name__ == "__main__":
    begin = time.time()
    spider = Bsspider()
    spider.run()
    end = time.time()
    print(end-begin)

