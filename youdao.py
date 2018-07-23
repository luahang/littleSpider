# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 15:57:13 2018

@author: tarena
"""

import requests

url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
str1 = input('please enter your words:')
headers = {
        "User-Agent": 
            "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Requested-With": "XMLHttpRequest",
        }
data = {
        "i": str1,
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": "1531555078843",
        "sign": "1384c0cb0af734e4ddcf7dbe98be6530",
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_CLICKBUTTION",
        "typoResult": "false"
}

response = requests.post(url,data=data,headers=headers)
print(response)