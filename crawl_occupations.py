import requests
import bs4
import pymysql as ps
import re

'''
    CREATE TABLE `professions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `p_name` varchar(30) NOT NULL,
  `c_name` varchar(30) NOT NULL,
  `c_address` varchar(50) NOT NULL,
  `salary` char(15) NOT NULL,
  `dtime` char(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
)
'''
# 获取网页信息
def get_html(url, headers):
    html = requests.get(url,headers)
    return html

# 获取公司名称　薪资　地址　和　发布日期
def get_soup(html,span,name):
    soup = bs4.BeautifulSoup(html,'html.parser')
    list = soup.find_all(span,class_=re.compile(name))
    return list

# 获取职位名称
def get_professions(html,p,name):
    soup = bs4.BeautifulSoup(html,'html.parser')
    plist = soup.find_all(p,class_=re.compile(name))
    return plist

def get_info(list,L):
    for i in list:
        L.append(i.string)
    return L

def get_profession(list,L):
    for i in list:
        L.append(i.span.a.string.strip())
    return L


def main():
    # 数据库的链接
    db = ps.connect("localhost","root","123456","occupation",charset="utf8")
    cursor = db.cursor()
    for x in range(1,35):
        url = 'https://search.51job.com/list/090200,000000,0000,00,9,99,python,2,%d.html'% x
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; \
                    WOW64)AppleWebKit/537.36 (KHTML, like Gecko)\
                    Chrome/62.0.3202.94 Safari/537.36"}
        html = get_html(url,headers).content.decode('gbk')
        # 职位名称列表
        plist = get_professions(html,'p','t1')
        L1 = get_profession(plist,L=[1])
        print(L1)
        # 公司名称列表
        clist = get_soup(html,'span','t2')
        L2 = get_info(clist,L=[])
        print(L2)
        # 地址列表
        adlist = get_soup(html,'span','t3')
        L3 = get_info(adlist,L=[])
        print(L3)
        # 薪资列表
        slist = get_soup(html,'span','t4')
        L4 = get_info(slist,L=[])
        print(L4)
        #　发布时间列表
        dlist = get_soup(html,'span','t5')
        L5 = get_info(dlist,L=[])
        print(L5)
        for j in range(1,len(L1)):
            sql = "insert into professions (p_name,c_name,c_address,salary,dtime) \
                values ('%s','%s','%s','%s','%s')"%(L1[j],L2[j],L3[j],L4[j],L5[j])
            cursor.execute(sql)
            db.commit()
    cursor.close()
    db.close()

if __name__ == '__main__':
    main()