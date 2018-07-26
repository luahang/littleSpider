# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class PicturePipeline(object):
    def process_item(self, item, spider):
        src = dict(item)
        with open(src['picName']+'.jpg', 'ab') as f:
            f.write(src['picSrc'])
        return item
