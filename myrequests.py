#coding:utf-8
#python网络爬虫库requests库应用全解
import requests
import json

print(u'================入门================')

r = requests.get(url='http://blog.csdn.net/luanpeng825485697/')  #返回Response对象
# print(r.status_code)  # 获取整型返回状态
# print(r.headers)  # 获取头部信息，#以字典对象存储服务器响应头，但是这个字典比较特殊，字典键不区分大小写，若键不存在则返回None
# print(r.encoding)  #获取编码类型
# print(r.url)  #获取响应网址
# print(r.history)  #获取访问历史
# print(r.reason)  #获取文本描述，"Not Found" or "OK".
# print(r.cookies)  #获取cookie
# print(r.raw) #返回原始响应体，也就是 urllib 的 response 对象，使用 r.raw.read() 读取
# print(r.content) #字节方式的响应体，会自动为你解码 gzip 和 deflate 压缩
# print(r.text) #字符串方式的响应体，会自动根据响应头部的字符编码进行解码
# print(r.links)   #解析响应的头部连接
# print(r.is_redirect)  #是否是重定向响应
#*特殊方法*#
# r.json() #如果返回的是json字符串将翻译为python对象
# r.raise_for_status() #功能：如果失败请求(非200响应)抛出异常
# r.close()   #关闭连接



print(u'================基本请求================')
r = requests.post("http://httpbin.org/post")
r = requests.put("http://httpbin.org/put")
r = requests.delete("http://httpbin.org/delete")
r = requests.head("http://httpbin.org/get")
r = requests.options("http://httpbin.org/get")



print(u'================基本GET请求================')
payload = {'key1': 'value1', 'key2': 'value2'}  #字典数据
headers = {'content-type': 'application/json'}  #header数据
r = requests.get("http://httpbin.org/get", params=payload, headers=headers) #payload可以省略，会在网址中添加
print(r.url)


print(u'================基本POST请求================')

url = 'http://httpbin.org/post'
payload = {'some': 'data'}
r = requests.post(url, data=payload)  #上传字典数据
r = requests.post(url, json=json.dumps(payload))  #上传json数据
print(r.text)

url = 'http://httpbin.org/post'
myfiles = {'file': open('test.txt', 'rb')}  #获取文件对象
r = requests.post(url, files=myfiles)  #上传文件
print(r.text)

#with open('test.txt') as f:  #流式上传
#    requests.post('http://some.url/streamed', data=f)


print(u'================Cookies================')

url = 'http://httpbin.org/cookies'
r = requests.get(url)  #响应中会包含cookie
print(r.cookies)

url = 'http://httpbin.org/cookies'
cookies = dict(cookies_are='working')  #自定义cookie变量
r = requests.get(url, cookies=cookies)  #请求时附带cookie
print(r.text)

print(u'================超时配置================')

requests.get('http://github.com', timeout=1)  #1秒没有响应就报错

print(u'================会话对象（持久连接）================')

s = requests.Session()
s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')  #get方式设置cookie
r = s.get("http://httpbin.org/cookies")  #获取cookie
print(r.text)


headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Encoding': 'gzip, deflate, compress',
           'Accept-Language': 'en-us;q=0.5,en;q=0.3',
           'Cache-Control': 'max-age=0',
           'Connection': 'keep-alive',
           'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}

s = requests.Session()
s.headers.update(headers)  #更新header
r = s.get('http://httpbin.org/headers', headers={'x-test': 'true'})  #get函数中添加的headers会覆盖原有同名，添加不同名的，去除值为None的
print(r.text)

print(u'================SSL证书验证================')

r = requests.get('https://github.com', verify=True)
print(r.text)

r = requests.get('https://kyfw.12306.cn/otn/', verify=False)  #把 verify 设置为 False即可跳过证书验证
print(r.text)


print(u'================设置代理服务器================')
#第一种方法
proxies = {
  "https": "http://121.193.143.249:80"
}
r = requests.post("http://httpbin.org/post", proxies=proxies)
print(r.text)
#第2中方法
s = requests.session()
s.proxies = {'http': '121.193.143.249:80'}
s.get('http://httpbin.org/ip')