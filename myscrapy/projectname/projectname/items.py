# -*- coding: utf-8 -*-

# 定义我们要爬取信息的标准格式，这个类被爬虫引用，爬虫解析数据后赋值给该类实例，并将类实例提交给pipelines，再进行进一步处理。

import scrapy

class myentity(scrapy.Item):
    name = scrapy.Field()
    link = scrapy.Field()
    readnum = scrapy.Field()

