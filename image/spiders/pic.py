# -*- coding: utf-8 -*-
import scrapy
from image.items import ImageItem


class PicSpider(scrapy.Spider):
    name = 'pic'
    allowed_domains = ['58pic.com']
    start_urls = ['http://58pic.com/']

    def parse(self, response):
        item = ImageItem()
        item["url"] = response.xpath("//div[@class='list-box-l']//a/@href").extract()
        yield item
