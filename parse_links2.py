#coding:utf-8
#爬虫
from HTMLParser import HTMLParser
from cStringIO import StringIO
from urllib2 import urlopen
from urlparse import urljoin

from bs4 import BeautifulSoup, SoupStrainer
from html5lib import parse, treebuilders

URLS = (
    'http://www.525heart.com/index/index/index.html',
#     'http://blog.csdn.net/luanpeng825485697',
)

def output(x):
    print('\n'.join(sorted(set(x))))

def simpleBS(url, f):  #使用BeautifulSoup解析所有的标签并获取链接
    output(urljoin(url,x['href']) for x in BeautifulSoup(f).findAll('a'))  #urljoin根据主机地址，获取网址（相对网址）的绝对网址

def fasterBS(url, f):  #使用BeautifulSoup解析链接标签
    output(urljoin(url, x['href']) for x in BeautifulSoup(f, parse_only=SoupStrainer('a')))

def htmlparser(url, f):   #使用HTMLParser解析链接标签
    class AnchorParser(HTMLParser):
        def handle_starttag(self, tag, attrs):
            if tag != 'a':
                return
            if not hasattr(self, 'data'):
                self.data = []
            for attr in attrs:
                if attr[0] == 'href':
                    self.data.append(attr[1])
    parser = AnchorParser()
    parser.feed(f.read())
    output(urljoin(url, x) for x in parser.data)

def html5libparse(url, f):  #使用html5lib解析链接标签
    output(urljoin(url, x.attributes['href']) \
        for x in parse(f) if isinstance(x,
        treebuilders.simpletree.Element) and \
        x.name == 'a')

def process(url, data):
    print('\n简单的网络爬虫')
    simpleBS(url, data)
    data.seek(0)
    # print('\n更直接的网络爬虫')
    # fasterBS(url, data)
    # data.seek(0)
    print('\nHTMLParser网络爬虫')
    htmlparser(url, data)
    data.seek(0)
    print('\nHTML5lib网络爬虫')
    html5libparse(url, data)

def main():
    for url in URLS:
        f = urlopen(url)
        data = StringIO(f.read())
        f.close()
        process(url, data)

if __name__ == '__main__':
    main()
