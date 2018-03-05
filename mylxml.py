# coding:utf-8
# 网络爬虫库lxml的应用
from lxml import etree

print(u'解析html（具有自动修复功能）')
text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </ul>
 </div>
'''
html = etree.HTML(text)
result = etree.tostring(html)
print(result)

# 将字符串写入文件
fh = open('test.html', 'w')
fh.write(result.decode("utf8"))    #fh.write(result)
fh.close()

print(u'读取文件（要求html代码完整）')
html = etree.parse('test.html')
result = etree.tostring(html, pretty_print=True)
print(result)

print(u'获取所有的 <li> 标签')
html = etree.parse('test.html')  # 创建dom树
print(type(html))
result = html.xpath('//li')  # 获取元素列表
print(result)
print(len(result))  # 获取列表长度
print(type(result))
print(type(result[0]))  # 获取元素

result = html.xpath('//li/@class')  # 获取 <li> 标签的所有 class属性的值
print(result)

result = html.xpath('//li/a[@href="link1.html"]')  # 获取 <li> 标签下 href 为 link1.html 的 <a> 标签
print(result)

result = html.xpath('//li//span')  # 获取 <li> 标签下的所有后代元素 <span> 标签
print(result)

result = html.xpath('//li/span')  # 获取 <li> 标签下的所有子元素 <a> 标签
print(result)

result = html.xpath('//li/a//@class')  # 获取 <li> 标签下的所有a元素的后代 class
print(result)

result = html.xpath('//li[last()]/a/@href')  # 获取最后一个 <li> 下的 <a> 的 href属性
print(result)

result = html.xpath('//li[last()-1]/a')  # 获取倒数第二个li元素下的a元素列表
print(result[0].text)  # 打印输出元素文本

result = html.xpath('//*[@class="bold"]')  # 获取 class 为 bold 的标签名
print(result[0].tag)