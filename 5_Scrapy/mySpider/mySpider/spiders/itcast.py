# -*- coding: utf-8 -*-
import scrapy
from mySpider.items import ItcastItem


class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml',]

    def parse(self, response):
        #filename = "teacher.html"
        #with open(filename, 'wb+') as f:
        #    f.write(response.body)
        # 存放老师信息的list
        items = []

        for i in response.xpath("//div[@class='li_txt']"):
            # 生成一个ItcastItem对象
            item = ItcastItem()
            # 抓取数据
            name = i.xpath('h3/text()').extract()
            title = i.xpath('h4/text()').extract()
            info = i.xpath('p/text()').extract()
            # 写入ItcastItem对象
            item['name'] = name
            item['title'] = title
            item['info'] = info
            # 存放到items
            items.append(item)
        
        #返回列表
        return items
