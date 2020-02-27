import requests
import json 
import csv

url = 'https://movie.douban.com/j/chart/top_list?'
headers = {"User-Agent":"Mozilla/5.0"}

tp_dict = {"劇情":"11","喜劇":"24","動作":"5"}
sin = input("請輸入電影類型:")

if sin in tp_dict:
    num = input("請輸入要爬取的數量:")
    tp = tp_dict[sin]
    params= {
        "type":tp,
         "interval_id":"100:90",
         "action":"",
         "start":"0",
         "limit":num
         }
    res = requests.get(url,params=params,headers=headers)
    res.encoding = "utf-8"
    html = res.text
    html = json.loads(html)
    for film in html:
        name = film['title']
        score = film['rating'][0]
        with open("豆瓣電影.csv","a",newline="",encoding="utf-8") as f:
            writer = csv.writer(f)
            L = [name,score]
            writer.writerow(L)
else:
    print('您輸入的類型不存在')
    







