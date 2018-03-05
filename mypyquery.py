#coding:utf-8
#网络爬虫库pyquery的应用，以下代码同时支持python2和python3
from pyquery import PyQuery as pq


print(u'=====================初始化====================')
doc = pq("<html></html>")  #传入html代码
#from lxml import etree
#doc = pq(etree.fromstring("<html></html>"))  #可以首先用lxml 的 etree 处理一下代码
doc = pq('http://www.baidu.com')  #传入网址
text = '''
<html><body><div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </li></ul>
 </div>
</body></html>
'''
#将字符串写入文件
fh = open('test.html', 'w')
fh.write(text)
fh.close()
doc = pq(filename='test.html')  #传入本地文件


print(doc.html())   #获取元素的内部html代码
print(type(doc))   #返回类型是PyQuery
li = doc('li')  #获取所有的li元素
print(type(li))  #返回类型依然是PyQuery，可以进行二次筛选
print(li.text())  #获取li的内部文本

print(u'=====================属性====================')
p = pq('<p id="hello" class="hello"></p>')('p')  #创建dom树后获取标签
print(p.attr("id"))   #读取属性值
print(p.attr("id", "plop"))   #设置属性值
print(p.attr("id", "hello"))  #设置属性值

print(p.addClass('beauty'))  #添加class
print(p.removeClass('hello'))  #去除class
print(p.css('font-size', '16px'))  #设置css值
print(p.css({'background-color': 'yellow'}))  #通过列表设置css


print(u'=====================DOM====================')
print(p.append(' check out <a href="http://reddit.com/r/python"><span>reddit</span></a>'))  #在内部原有html代码后添加代码
print(p.prepend('Oh yes!'))  #在内部原有html代码前添加代码
d = pq('<div class="wrap"><div id="test"><a href="http://cuiqingcai.com">Germy</a></div></div>')  #创建一个dom树
td = d('#test')  #获取id为test的元素
p.prependTo(td)  #将p元素添加到td元素内，在td内部html代码的前面，源节点不变
print(d)
d.empty()  #清空元素内部html代码
print(d)


print(u'=====================遍历====================')
doc = pq(filename='test.html')
lis = doc('li')
for li in lis.items():
    print(li.html())  #打印li元素的内部html代码

print(lis.each(lambda e: e))  #each遍历函数，lambda表达式，不常用


print(u'=====================网页请求====================')
print(pq('http://www.525heart.com/index/index/index.html', headers={'user-agent': 'pyquery'}))  #get请求方式，可设置headers
print(pq('http://httpbin.org/post', {'foo': 'bar'}, method='post', verify=True))  #post请求方式，可设置data和headers，已经控制是否检验
