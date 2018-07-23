# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 14:44:48 2018

@author: tarena
"""
import requests
import time
from lxml import etree
import json
import random
import functools
from multiprocessing import Pool,Manager


def crawlPage(lock,offset):
    url = 'https://maoyan.com/board/4?offset={}'.format(offset)
    pool = [
        {"User-Agent": "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11"},
        {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"},
        {"User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)"},
        {"User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)"},
        {"User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)"},
        {"User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)"},
        {"User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)"},
        {"User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)"},
        {"User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)"},
        {"User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)"},
        ]
    headers = random.sample(pool,1)[0]
    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        html = response.content.decode('utf-8')
        for i in get_info(html):
            lock.acquire()
            save_info(i)
            lock.release()
        time.sleep(1)
    else:
        return None
    
# 获取数据      
def get_info(data):
    html = etree.HTML(data)
    data = html.xpath('//dl[@class="board-wrapper"]/dd')
    l = {}
    for i in data:
        l['name'] = i.xpath('.//p[@class="name"]/a/text()')[0]
        l['star'] = i.xpath('.//p[@class="star"]/text()')[0].strip()
        l['releasetime'] = i.xpath('.//p[@class="releasetime"]/text()')[0]
        yield l

# 保存文件
def save_info(L):
    str1 = json.dumps(L,ensure_ascii=False,indent=2)
    with open('maoyan.txt', 'a',encoding='utf-8') as f:
        f.write(str1)

if __name__ == "__main__":
    manager = Manager()
    lock = manager.Lock()
    newCrawlPage = functools.partial(crawlPage,lock)
    pool = Pool(4)
    pool.map(newCrawlPage,[i*10 for i in range(0,10)])
    pool.close()
    pool.join()
    
    
    