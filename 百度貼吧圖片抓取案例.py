import requests
from lxml import etree
import random


class ImageSpider:
    def __init__(self):
        self.baseurl = "http://tieba.baidu.com/f?"
        self.baseimurl = "http://tieba.baidu.com"
        self.header_list = [{"User-Agent":"Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0;"}]
        self.headers = random.choice(self.header_list)

    def getPageUrl(self,params):
        res = requests.get(self.baseurl,params=params,headers=self.headers)
        res.encoding = "utf-8"
        html = res.text
        parsehtml = etree.HTML(html)
        t_list = parsehtml.xpath('//div[@class="t_con cleafix"]/div/div/div/a/@href')
        
        for t in t_list:
            turl = self.baseimurl + t            
            self.getImageUrl(turl)
    
    def getImageUrl(self,turl):  
        tres = requests.get(turl,headers=self.headers)
        tres.encoding = "utf-8"
        thtml = tres.text
        pih = etree.HTML(thtml)
        im_list = pih.xpath('//img[@class="BDE_Image"]/@src')
        self.writeImage(im_list)

    def writeImage(self,im_list):
        for im in im_list:
            ires = requests.get(im,headers=self.headers)
            ires.encoding = "utf-8"
            ihtml = ires.content
            
            im_name = '%s'%im[-12:]
        
            with open(im_name, 'wb') as f:
                f.write(ihtml)
                print("%s下載成功"%im_name)
  
    def workOn(self):
        key = input("請輸入要爬取的關鍵字:")
        big = int(input("請輸入爬取起始頁:"))
        end = int(input("請輸入爬取中止頁:"))
        for i in range(big,end+1):
            pn = (i-1)*50
            params = {"kw":key,"pn":pn}
            print("*****開始爬取第 %s 頁*****"%i)
            self.getPageUrl(params)
        print("爬取完畢")
        
if __name__ == "__main__":
    spider = ImageSpider()
    spider.workOn()
    
