import requests
import json

key = input("請輸入要翻譯的內容:")
data = {"i":key,
        "from":"AUTO",
        "to":"AUTO",
        "smartresult":"dict",
        "client":"fanyideskweb",
        "salt":"15776891664336",
        "sign":"49f47437a2fe8b491ea85e8968229a85",
        "ts":"1577689166433",
        "bv":"42160534cfa82a6884077598362bbc9d",
        "doctype":"json",
        "version":"2.1",
        "keyfrom":"fanyi.web",
        "action":"FY_BY_REALTlME"}


url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
headers = {"User-Agent":"Mozilla/5.0"}
res = requests.post(url,data=data,headers=headers)
res.encodin = "utf-8"
html = res.text
r_dict = json.loads(html)
result = r_dict["translateResult"][0][0]["tgt"]
print("翻譯為:",result)


