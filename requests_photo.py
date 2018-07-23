import requests
import re
import os

# 获取网页信息
def get_html(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36'}
    html = requests.get(url,headers).content.decode()
    return html

# 使用正则表达式 进行数据查找
def get_img(html):
    str1 = r'<img class="BDE_Image" src="(.*?)".*?>'
    imglist = re.findall(str1,html)
    # # 用来存放图片的资源
    # img_sourse = []
    # for i in imglist:
    #     source = i.split('/')[-1]
    #     img_sourse.append(source)
    return imglist

# 将获取的图片保存到指定的路径
def save_img(img_sourse):
    os.mkdir('img')
    os.chdir('img')
    count = 0
    for i in img_sourse:
        print(i)
        filename = 'photo' + str(count)
        with open(filename,'wb') as f:
            img = requests.get(i)
            f.write(img.content)
        f.close()
        count += 1

def main():
    url = 'https://tieba.baidu.com/p/3823765471'
    html = get_html(url)
    imglist =  get_img(html)
    save_img(imglist)

if __name__ == '__main__':
    main()