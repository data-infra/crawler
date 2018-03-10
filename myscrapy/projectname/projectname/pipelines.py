# -*- coding: utf-8 -*-
#pipelines.py主要根据item保存的信息，进行进一步多线程操作

from projectname import settings
from scrapy import Request
import requests
import os


class MyPipeline(object):
    allpaper=[]
    def process_item(self, item, spider):
        paper={}
        paper['name']=item['name']
        paper['link'] = item['link']
        paper['read'] = item['readnum']
        self.allpaper.append(paper)

        file_object = open('data.txt', 'a')
        file_object.write(str(paper)+"\r\n")
        file_object.close()
        return item