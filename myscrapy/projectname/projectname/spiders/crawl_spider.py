# -*- coding: utf-8 -*-
# 在这里实现请求、响应、解析的过程

import re
import scrapy
import urllib
from scrapy import Selector
from projectname.items import myentity

class MySpider(scrapy.Spider):
    name = 'myspider'       #爬虫名称，需要这个名称才能启动爬虫
    def __init__(self):
        self.allowed_domains = ['blog.csdn.net']
        self.start_urls = ['http://blog.csdn.net/luanpeng825485697/article/list/']

    #从start_requests发送请求
    def start_requests(self):
        yield scrapy.Request(url = self.start_urls[0]+"1", meta = {'data':1},callback = self.parse1)  #请求网址，设置响应函数，同时向响应函数传递参数

    #解析response,获得文章名称、连接、阅读数目，还可以进行二次请求。
    def parse1(self, response):
        index = response.meta['data']  #接收请求函数发来的参数
        if index>100:  #这里只爬取前100页
            return
        hxs = Selector(response)
        #文章链接地址
        links = hxs.xpath("//span[@class='link_title']/a[1]/@href").extract()  #xpath路径表达式获取文章连接地址
        #文章名
        names = hxs.xpath("//span[@class='link_title']/a[1]/text()").extract()  #xpath路径表达式获取文章名
        #文章阅读数量
        reads = hxs.xpath("//span[@class='link_view']/text()").extract()  #xpath路径表达式获取文章阅读数量

        #将爬取的数据赋值给items
        for i in range(1,len(links)):
            item = myentity()
            item['link'] = urllib.parse.urljoin('http://blog.csdn.net/',links[i])  #获取绝对域名
            item['name'] = names[i]
            item['readnum'] = reads[i]
            # 返回item，交给item pipeline处理
            yield item

        #迭代下一页
        yield scrapy.Request(url=self.start_urls[0]+str(index+1), meta={'data': index+1}, callback=self.parse1)

