# -*- coding: utf-8 -*-

import scrapy
from image.items import ImageItem
from scrapy.http import Request


class NipicSpider(scrapy.Spider):
    name = 'nipic'
    allowed_domains = ['nipic.com']
    start_urls = ['http://nipic.com']

    def parse(self, response): # 爬取首页导航地址
        urldata = response.xpath("//div[@class='newIndex-nav-condition fl']//a/@href").extract()
        for i in range(0, len(urldata)):
            url = urldata[i]
            thisurl = self.start_urls[0] + url
            yield Request(url=thisurl, callback=self.next)

    def next(self, response): # 爬取第二层专题页地址
        nexturl = response.xpath("//div[@class='menu-box-bd']//a/@href").extract()
        if len(nexturl) > 2:
            child_url = nexturl
            for i in child_url:
                true_url = self.start_urls[0] + i
                print true_url
                yield Request(url=true_url, callback=self.page)

    def page(self, response): # 爬取专题页所有页面
        all_page = response.xpath("//div[@class='common-page-box mt10 align-center']//a/@href").extract()
        page = all_page[-1].split("=")[-1]
        print page
        for i in range(1, int(page)):
            page_url = "http://www.nipic.com/design/yidong/youxi/index.html?page=" + str(i)
            yield Request(url=page_url, callback=self.image)

    def image(self, response): # 爬取图片链接地址
        item = ImageItem()
        item["url"] = response.xpath("//li[@class='works-box mb17 fl']//img/@src").extract()
        yield item
