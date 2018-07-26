# -*- coding: utf-8 -*-
import scrapy
from picture.items import PictureItem
import requests

class PicturnSpider(scrapy.Spider):
    name = 'picturn'
    allowed_domains = ['desk.zol.com.cn']
    start_urls = ['http://desk.zol.com.cn/fengjing/']
    
    def get_data(self,src):
        r = src.split('/')
        r[3] = 't_s1920x1080c5'
        src1 = '/'.join(r)
        data = requests.get(src1).content
        return data
    
    def parse(self, response):
        item = PictureItem()
        s = response.xpath('//li[@class="photo-list-padding"]')
        for i in s:
            item['picSrc'] = self.get_data(i.xpath('./a/img/@src').extract()[0])
            item['picName'] = i.xpath('./a/span/@title').extract()[0]
            yield item

        # 获取下一页链接
        if response.xpath('//*[@id="pageNext"]/@href').extract()[0]:
            nextUrl = 'http://desk.zol.com.cn' + response.xpath('//*[@id="pageNext"]/@href').extract()[0]
            yield scrapy.Request(nextUrl,callback=self.parse)