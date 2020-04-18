# -*- coding: utf-8 -*-
import requests
import datetime
# # 北工大疫情期间自动打卡签到用
# # Login to the website and save session
# post data & header & url
url = 'https://itsapp.bjut.edu.cn/uc/wap/login/check'
header = {
        "Content-Type": 'application/json',
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36"
    }
data = {
        'username': '学号',
        'password': '密码'
    }
# # Login in with session
s = requests.Session()
r = s.post(url, data=data,verify=False)

# # post check_in data to website
check_url = 'https://itsapp.bjut.edu.cn/ncov/wap/default/save'

# datetime
today_date = datetime.date.today().strftime('%Y%m%d')

# this data need to packet capture by yourself

data1 = {
    "ismoved": "0",
    "uid": "xxxx",
    "date": today_date,
    "tw": "2",
    "sfcxtz": "0",
    "sfyyjc": "0",
    "jcjgqr": "0",
    "sfjcbh": "0",
    "sfcxzysx": "0",
    "address": "xxxx",
    "area": "xxxxxx",
    "province": "xxxxxx",
    "city": "xxxxx",
    "geo_api_info": 'xxxxxxxxxxxxx',
    "created": "xxxxxxxxxx",
    "sfzx": "0",
    "sfjcwhry": "0",
    "sfcyglq": "0",
    "sftjwh": "0",
    "sftjhb": "0",
    "fjsj": "0",
    "sfjchbry": "0",
    "sfsfbh": "0",
    "jhfjsftjwh": "0",
    "jhfjsftjhb": "0",
    "szsqsfybl": "0",
    "sfygtjzzfj": "0",
    "dqjzzt": "1",
    "id": "xxxxxxxxx",
    }
rr = s.post(check_url, data=data1,verify=False)

# # server chan push
api = "https://sc.ftqq.com/[ your token ].send"
title = u" 签到结果！"
content = (r.text+'\n'+rr.text)
data2 = {
   "text": title,
   "desp": content
}
req = requests.post(api,data = data2)
