import requests
import json


class GetDoubanTv(object):
    def __init__(self):
        self.str_url = 'https://movie.douban.com/j/search_subjects?type=tv&tag=%E7%BE%8E%E5%89%A7&sort=recommend&page_limit=20&page_start={}'
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36',
                        'Referer': 'https://movie.douban.com/tv/'}


    def get_data(self,str_html):
        data_list = json.loads(str_html)['subjects']
        return data_list

    def save_file(self,data_list):
        with open("douban",'a',encoding="utf-8") as f:
            str_list = json.dumps(data_list,ensure_ascii=False)
            f.write(str_list)
            f.write('/n')

    # 主流程控制
    def run(self):
        num = 0
        total = 480
        while num < total + 20:
            # 1.url地址
            url = self.str_url.format(num)
            print(url)
            # 2.发送请求　获取响应
            html = requests.get(url,self.headers).content.decode()
            # 3.提取数据
            data_list = self.get_data(html)
            # 4.保存
            self.save_file(data_list)
            # 5.构造下一个url地址
            num += 20

if __name__ == '__main__':
    dbtv = GetDoubanTv()
    dbtv.run()