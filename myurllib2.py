#coding:utf-8
import urllib
# 网络编程模块socket,urllib,urllib2,asyncore,cgi,Cookie服务器端,cookielib客户端，email，ftplib，httplib，imaplib，mailbox，mailcap，poplib
import urllib2
import cookielib

print('=======================urllib2.urlparse模块，网址字符串处理==========================')
#urlparse()参数:网址、网络协议、是否使用片段，返回值:网络协议、服务器所在地、文件路径、可选参数、键值对、文档锚
prot_sch,net_loc,path,params,query,frag=urllib2.urlparse.urlparse("http://www.525heart.com/index/index/index.html",None,None)
print prot_sch,net_loc,path,params,query,frag
#urlunparse()将6元组合并为网址字符串
urlpath=urllib2.urlparse.urlunparse((prot_sch,net_loc,path,params,query,frag))
print(urlpath)
#urljoin()获取根域名，连接新网址
urlpath=urllib2.urlparse.urljoin("http://www.525heart.com/index/index/index.html","../chanpin/detail.html")
print(urlpath)

 

print("=====================urllib.urlretrieve模块：下载读取远程静态文件=====================")
#远程文件
resphonse = urllib.urlopen("http://www.525heart.com/index/index/index.html")                    # urlopen(url,data,timeout)打开远程文件,返回的是类文件对象，可以使用readline等文件函数
htmlcode = resphonse.readline()  #读取一行
htmlcode = resphonse.readlines()  #读取所有行
htmlcode = resphonse.read()  #读取字节流
print(resphonse.geturl())  #文件网址
print(resphonse.info())  #数据传输的MIME头文件
resphonse.close()  #关闭
urllib.urlretrieve("http://www.525heart.com/index/index/index.html",'d:/index.html')                # 下载远程文件，参数为网址，可本地存储地址


print("=====================urllib2.Request模块：获取get方式请求响应流=====================")
request = urllib2.Request('http://www.525heart.com/web/getdiaryurl?diaryid=612')
try:
    resphonse = urllib2.urlopen(request)                    # urlopen(url,data,timeout)打开远程文件,返回的是类文件对象，可以使用readline等文件函数
except urllib2.URLError,e:   #本机没联网、连接不到服务器、服务器不存在
    print(e.reason)
except urllib2.HTTPError,e:   #响应状态，响应码
    print(e.reason,e.code)
# print(resphonse.read())  #读取响应数据



print("=====================urllib2.Request模块：获取post方式请求响应流=====================")
postobject={"diaryid":"612"}  #将字典数据序列化
postdata = urllib.urlencode(postobject)  # urlencode()字典序列化
url= "http://www.525heart.com/web/getdiaryurl"
request = urllib2.Request(url,postdata)  #创建post请求对象，get请求对象：urllib2.Request(url+"?"+data)
resphonse = urllib2.urlopen(request)   #post请求消息
# print(resphonse.read())  #读取响应数据


print("=====================urllib2.Request模块：控制HTTP头=====================")

url= "https://zhuanlan.zhihu.com/p/30488000"
postdata = urllib.urlencode({"p":"30488000"})  # urlencode()字典序列化
headers={}
headers["User-Agent"]='Mozilla/4.0 (compatible;MSIE 5.5;Windows NT)'  #标明浏览器身份，有些服务器或代理服务器会来判断。这里模仿的是IE浏览器
headers["Referer"]='http://www.zhihu.com/p'  #标明文件来源，防止盗链用的
headers["Content-Type"]='text/html'  #在谁用rest接口的服务器会检测这个值，来确定内容如何解析
request = urllib2.Request(url,headers=headers)  #headers控制请求，因为服务器会根据这个控制头决定如何响应。（resphonse.info()可以查看响应的头的信息）
resphonse = urllib2.urlopen(request)   #post请求消息
print(resphonse.read())  #读取响应数据


print("=====================urllib2.ProxyHandler函数：设置代理服务器，防止限制IP=====================")
#控制代理服务器，防止服务器限制IP。每隔一段时间换一个代理服务器
enable_proxy = True
proxy_handler=urllib2.ProxyHandler({"http":"http://some-proxy.com:8080"})
null_proxy_handler = urllib2.ProxyHandler({})
if enable_proxy:
    opener = urllib2.build_opener(proxy_handler)
else:
    opener = urllib2.build_opener(null_proxy_handler)
urllib2.install_opener(opener)



print("=====================urllib2.HTTPCookieProcessor函数：获取cookie=====================")
cookie=cookielib.CookieJar()  #声明一个CookieJar对象实例来保存cookie
handler=urllib2.HTTPCookieProcessor(cookie)  #利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
opener=urllib2.build_opener(handler)  #通过handler来构建opener
resphonse=opener.open('http://blog.csdn.net/luanpeng825485697/article/details/78264170')  #cookie是由服务器来设定的存储在客户端，客户端每次讲cookie发送给服务器来携带数据
for item in cookie:
    print('Name='+item.name)
    print('Value='+item.value)


print("=====================cookie模块：将cookie写入文件=====================")
filename='cookie.txt'
cookie=cookielib.MozillaCookieJar(filename)  #声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
handler=urllib2.HTTPCookieProcessor(cookie) #利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
opener = urllib2.build_opener(handler)  #通过handler来构建opener
resphonse=opener.open('http://blog.csdn.net/luanpeng825485697/article/details/78264170')  #创建一个请求，原理同urllib2的urlopen
cookie.save(ignore_discard=True, ignore_expires=True) #保存cookie文件


print("=====================cookie模块：从文件中读取cookie=====================")
cookie=cookielib.MozillaCookieJar()  #声明一个MozillaCookieJar对象实例
cookie.load("cookie.txt",ignore_discard=True, ignore_expires=True) #从文件中读取cookie内容到变量
req=urllib2.Request("http://blog.csdn.net/luanpeng825485697/article/details/78264170") #创建请求的request
opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))  #利用urllib2的build_opener方法创建一个opener
response=opener.open(req)  #使用包含了指定cookie的opener发起请求
print(resphonse.read())  #打印响应


print("=====================cookie模块：利用cookie模拟登陆=====================")
#创建一个带有cookie的opener，在访问登录的URL时，将登录后的cookie保存下来，然后利用这个cookie来访问其他网址
filename='cookie.txt'
cookie=cookielib.MozillaCookieJar(filename)  #声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
postdata = urllib.urlencode({
            'stuid':'201200131012',
            'pwd':'23342321'
        })
#登录教务系统的URL
loginUrl = 'http://jwxt.sdu.edu.cn:7890/pls/wwwbks/bks_login2.login'
#模拟登录，并把cookie保存到变量
result = opener.open(loginUrl,postdata)
#保存cookie到cookie.txt中
cookie.save(ignore_discard=True, ignore_expires=True)
#利用cookie请求访问另一个网址，此网址是成绩查询网址
gradeUrl = 'http://jwxt.sdu.edu.cn:7890/pls/wwwbks/bkscjcx.curscopre'
#请求访问成绩查询网址
result = opener.open(gradeUrl)
print(result.read())



# #正则匹配
# import re;
# p = re.compile('<a .*href="(.*?)".*>(.*?)</a>');   #正则表达式，捕获链接和描述
# for url,name in p.findall(htmlcode):   #正则表达式匹配字符串
#     print('%s (%s)'%(name,url));
#
# #quote网址URL编码,unquote网址URL解码
# print urllib.quote("http://www/~foo/cgi-bin/s.py?name=joe mama$num=6")
# print urllib.unquote(urllib.quote("http://www/~foo/cgi-bin/s.py?name=joe mama$num=6"))
#
# # urlencode()字典序列化
# aDict={'key':'luanpeng','value':"good"}
# print urllib.urlencode(aDict)
#
#
#
# print("=====================客户端，html智能修复=====================");
# # # tidy用来修复不规范的、有错误的、旧的html文件代码。
# # from subprocess import Popen,PIPE;
# # htmlcode = open('d:\\index.html').read();
# # tidy = Popen('tidy',stdin=PIPE,stdout=PIPE,stderr=PIPE);
# # tidy.stdin.write(htmlcode);
# # tidy.stdin.close();
# # print(tidy.sydout.read());
