#coding:utf-8
# BeautifulSoup抓取
import urllib  #python3中urllib整合了五大模块urllib.error、urllib.parse、urllib.request、urllib.response、urllib.robotparser
import re
from bs4 import BeautifulSoup

print("============获取网页源代码============")
host = 'http://www.525heart.com/index/index/index.html'
text = urllib.request.urlopen(host).read()  #获取网页源代码

print("============解析网页源代码============")
soup = BeautifulSoup(text, 'html.parser')  #前一个参数为要解析的文本，后一个参数为解析模型
# bs4的HTML解析器：BeautifulSoup(mk,'html.parser')——条件：安装bs4库
# lxml的HTML解析器：BeautifulSoup(mk,'lxml')——pip install lxml
# lxml的XML解析器：BeautifulSoup(mk,'xml')——pip install lxml
# html5lib的解析器：BeautifulSoup(mk,'html5lib')——pip install html5lib
# print(soup.prettify())  #打印解析的内容

print("============对象划分============")
#解析以后全部html代码转变为4种类型：
#基本对象类型
# 1、Tag——标签，最基本的信息组织单元，分别用<>和</>表明开头和结尾
# 1.1、标签Name属性——标签的名字，<p>...</p>的名字是'p',格式：<tag>.name
# 1.2、标签Attributes属性——标签的属性，字典形式组织，格式：<tag>.attrs
# 2、NavigableString——标签内非属性字符串，<>...</>中的字符串，格式：<tag>.string
# 3、Comment——标签内字符串的注释部分，一种特殊的Comment类型（尖括号叹号表示注释开始：<!--This is a commet-->）
# 4、BeautifulSoup对象(整个html对象soup)

print(soup.a)   #第一个a标签
print(soup.a.string)  #第一个a标签的文本显示
print(type(soup.a.string))   #第一个a标签的对象类型，类型可以能是bs4.element.xxx

print(soup.title)  #第一个title标签
print(soup.head)   #第一个head标签

print("============标签获取============")

#标签获取
for tag in soup('a'):   #根据标签名获取标签
#     print tag.name          #标签的名字
#     print tag.parent.name     #标签的父标签的名字
#     print tag.parent.parent.name       #标签的父标签的父标签名字
#     print tag.string      #获得标签内非属性字符串（NavigableString ）innerText
    link = tag.attrs['href']         #标签的属性
    link = tag['href']         #标签的属性
    link = tag.get('href')         #标签的属性
    print(urllib.parse.urljoin(host,link)),        #在指定网址中的连接的绝对连接
    print(tag.name),   #标签的名称
    print(tag.attrs),  #属性
    print(tag.string)  #标签内的文本显示

print("============搜索============")
# find_all( name , attrs , recursive , text , **kwargs )  #返回结果只包含一个元素的列表
# find( name , attrs , recursive , text , **kwargs )  #直接返回结果
print("============搜索-按标签搜索============")
print(soup.find_all('a')[0])  #按字符串查询
print(soup.find_all(re.compile("^a"))[0])  #按正则表达式查询
print(soup.find_all(["a", "b"])[0])  #按列表查询
print(soup.find_all(True)[1])  #查询所有元素，第一个元素就是html元素，就是整个全文

def has_class_but_no_id(tag):
  return tag.has_attr('href') and not tag.has_attr('target')  #返回 True才查询
print(soup.find_all(has_class_but_no_id))  #按方法查询


print("============搜索-按属性搜索============")
print(soup.find_all(id='headerImg'))  #按属性值查询,data-*不能查询
print(soup.find_all(href=re.compile("#")))  #按属性值的正则表达式查询
print(soup.find_all(href=re.compile(".*index\.html"), target='_blank'))  #按属性值列表查询
print(soup.find_all("a", class_="current"))  #标签属性联合搜索，class 是 python 的关键词，所以加了_
print(soup.find_all(attrs={"class": "current"}))  #搜索包含指定属性值的元素



print("============搜索-按文本搜索============")

print(soup.find_all(text="首页"))  #按文本搜素，接受的参数与按标签搜索一样
print(soup.find_all("a", limit=2,recursive=False))  #以上所有搜索都可以用limit限定最大搜索到的数目，用recursive限定只搜索直接子节点



print("============搜索-按css选择器名称搜索============")
print(soup.select('title'))   #按名称
print(soup.select('.current'))  #按类名
print(soup.select('#headerImg')) #按id
print(soup.select('li .current'))  #后代查询
print(soup.select("head > title")) #子标签查询
print(soup.select('a[class="current"]'))  #属性查询


print("============节点遍历-向下遍历============")

#find_parents() find_parent() #搜索当前节点的父辈节点
#find_next_siblings() find_next_sibling() #搜索符合条件的后面的兄弟节点
#find_previous_siblings() find_previous_sibling() #搜索符合条件的前面的兄弟节点
#find_all_next() find_next() #对当前 tag 的之后的 tag 和字符串进行迭代
#find_all_previous() 和 find_previous()  #对当前节点前面的 tag 和字符串进行迭代

#遍历（向下）
# contents属性：直接子节点的列表，将<tag>所有儿子节点存入列表
print(soup.head.contents[0])
# children属性：子节点的迭代类型，与.contents类似，用于循环遍历儿子节点
# descendants属性：后代节点的迭代类型，包含所有子孙节点，用于循环遍历
for child in soup.body.children:        #直接子节点列表,迭代类型，需要用循环方式，空格、换行也是子节点
    print("body's child："+str(child.name))

#for string in soup.strings:  #遍历获取所有显示文本内容，soup.stripped_strings可以去除空格或换行
#  print(repr(string))


#遍历（向上）
# parent属性：节点的父标签
# parents属性：节点先辈标签的迭代类型，用于循环遍历先辈节点

print("============节点遍历-同胞遍历============")

#遍历（平级）
firstli=soup('li')[0]  #等价于soup.li
print(firstli.next_sibling)   #注意空格换行也是节点
print(firstli.previous_sibling)  #注意空格换行也是节点
for sibling in firstli.next_siblings:  #注意空格换行也是节点
    print('next_siblings:',sibling)
for sibling in firstli.previous_siblings:  #注意空格换行也是节点
     print('previous_siblings:'+str(sibling))

#遍历（代码前后）
#next_elements当前节点之后的所有节点
#previous_elements当前节点之前的所有节点
#next_element当前节点的下一个节点
#previous_element当前节点的前一个节点