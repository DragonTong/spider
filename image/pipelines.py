# -*- coding: utf-8 -*-
import re
import urllib

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ImagePipeline(object):
    def process_item(self, item, spider):
        for i in range(0, len(item["url"])):
            image_url = item["url"][i]
            pattern = "http://img85.nipic.com/file/(.*?)_1.jpg"
            image_id = re.compile(pattern).findall(image_url)[0]
            image = "http://pic136.nipic.com/file/" + image_id + "_2.jpg"
            print image
            store_path = "/sre/python-project/gunlei_spider/result/" + image_id[-12:] + ".jpg"
            urllib.urlretrieve(image, filename=store_path)
        return item
