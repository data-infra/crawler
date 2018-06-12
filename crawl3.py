#coding:utf-8
#一个简单的web爬虫
import io  #解析html
import formatter  #解析html
from html.parser import HTMLParser  #解析html
import http.client  #其中定义的一个异常
import os  #文件系统方面的函数
import sys  #使用其中提供的argv来处理命令行参数
import myurllib2  #其中的urlretrive下载web页面
from myurllib2 import request
import myurllib2.parse #处理url,urllib2、urlparse、和robotparser并入了urllib中:urllib.error、urllib.parse、urllib.request、urllib.response、urllib.robotparser
import codecs  #编码库

class Retriever(object):  #下载web页面。解析文档中的链接，加入到链接列表
    __slots__ = ('url', 'file')   #网址和本地存储路径
    def __init__(self, url):
        self.url, self.file = self.get_file(url)

    def get_file(self, url, default='index.html'):  #根据url地址转换为本地地址，用于存储
        parsed = myurllib2.parse.urlparse(url)   #返回6元组
        host = parsed.netloc.split('@')[-1].split(':')[0]  #主机地址，丢掉附加的用户名、密码、端口号
        filepath = '%s%s' % (host, parsed.path)  #设置本地存储路径
        if not os.path.splitext(parsed.path)[1]:
            filepath = os.path.join(filepath, default)
        linkdir = os.path.dirname(filepath)  #获取目录路径
        if not os.path.isdir(linkdir): #如果不是目录
            if os.path.exists(linkdir): #如果是普通文件（无格式文件）
                os.unlink(linkdir)  #删除文件
            os.makedirs(linkdir)  #创建目录
        print("网址："+url+"   本地路径："+filepath)
        return url, filepath

    def download(self):  #根据url下载文件
        try:
            retval = myurllib2.request.urlretrieve(self.url, self.file)  #下载url文件到指定本地文件
        except (IOError, http.client.InvalidURL) as e:
            retval = (('*** url： "%s"出错： %s' % (self.url, e)),)
        return retval #返回文件名

    def parse_links(self):   #解析刚下载下来的页面链接
        f = codecs.open(self.file, 'rb', 'utf-8')  #读取下载的页面
        data = f.read()  #.decode("utf-8")
        f.close()
        parser = HTMLParser(formatter.AbstractFormatter(   #AbstractFormatter用来解析数据
            formatter.DumbWriter(io.StringIO())))  #DumbWriter用来输出内容，cStringIO保障不输出到标准输出（最好输出到文件）
        parser.feed(data)
        parser.close()
        return parser.anchorlist  #返回解析后的列表

class Crawler(object):
    count = 0

    def __init__(self, url):
        self.queue = [url]   #queue存储带下载的链接队列
        self.seen = set()  #seen已下载链接的集合
        parsed = myurllib2.parse.urlparse(url) #返回6元组
        host = parsed.netloc.split('@')[-1].split(':')[0]  #获取主机名，去除附加的用户名，密码，端口号。如果是想获取同一个目录下，需要自己调整
        print('主机地址：'+host)
        self.dom = host #'.'.join(host.split('.')[-2:])  #dom主链接的域名，只在同域名下进行爬虫


    def get_page(self, url, media=False):  #下载页面，解析页面，调整链接列表
        r = Retriever(url)
        fname = r.download()[0]  #下载页面
        if fname[0] == '*':                 #如果连接是当前页面就跳过连接
            print(fname+'... 跳过解析')
            return
        Crawler.count += 1
        print('处理页面数量：%d' % Crawler.count)
        print('当前网址:'+url)
        print('当前文件地址:'+fname)
        self.seen.add(url)  #添加已下载链接列表
        ftype = os.path.splitext(fname)[1]      #获取下载文件类型
        if ftype not in ('.htm', '.html'):   #这里只解析html和htm文件
            return

        for link in r.parse_links():  #解析文件，获取文件中的连接列表
            if link.startswith('mailto:'):
                print('... 忽略邮件链接')  #忽略邮件连接处理
                continue
            if not media:
                ftype = os.path.splitext(link)[1]  #连接文件的类型
                if ftype in ('.mp3', '.mp4', '.m4v', '.wav'):  #忽略媒体文件，不处理
                    print('... 忽略媒体文件链接')
                    continue
            if not link.startswith('http://'):    #如果连接是相对路径
                link = myurllib2.parse.urljoin(url, link)  #相对url路径，转变为绝对url路径
            print('发现网页：'+link)
            if link not in self.seen:  #如果是已下载文件，则放弃
                if self.dom not in link:  #如果是站外连接，则放弃
                    print('... 忽略站外链接')
                else:
                    if link not in self.queue:  #如果还没有访问过，则添加到需要爬虫的链接列表
                        self.queue.append(link)
                        print('... 添加新的链接到队列')
                    else:
                        print('... 已经在链接列表中')
            else:
                    print('... 已经处理过')

    def go(self, media=False):  #启动爬虫
        while self.queue:
            url = self.queue.pop()
            self.get_page(url, media)


#只能识别h5代码中的跳转，不能识别js中的跳转
def main():
    url = 'http://www.525heart.com/index/index/index.html'
    if not url:
        return
    if not url.startswith('http://') and not url.startswith('ftp://'):
            url = 'http://%s' % url  #自动添加http头
    robot = Crawler(url)
    robot.go()

    for x in robot.seen:
        print(x)


if __name__ == '__main__':
    main()
