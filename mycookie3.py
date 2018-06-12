# -*- coding: UTF-8 -*-
from urllib import request
from urllib import error
from urllib import parse
import http.cookiejar
from bs4 import BeautifulSoup
import requests
import time

login_url='http://www.zhihu.com/login/phone_num'
#post登陆，生成cookie文件
session = requests.Session()
agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER'
headers = {   #这个http头，根据审查元素，监听发包，可以查看
    "Host": "www.zhihu.com",
    "Origin":"https://www.zhihu.com",
    "Referer":"http://www.zhihu.com/",
    'User-Agent':agent
}

postdata = {
    'phone_num': '18158208197',  #填写手机号  如果有email登陆是email
    'password': '19910101a', #填写密码
    'captcha_type':'cn',  #验证码类型
}

response = session.get("https://www.zhihu.com", headers=headers)
soup = BeautifulSoup(response.content, "html.parser")
xsrf = soup.find('input', attrs={"name": "_xsrf"}).get("value")  #解析_xsrf字段
postdata['_xsrf'] =xsrf  #因为知乎登陆需要这个字段的消息
result = session.post(login_url, data=postdata, headers=headers)  #发送数据  如果使用email登陆，这里是http://www.zhihu.com/login/email
print(result.text)


#cookie可以通过模拟登陆获取，也可以直接通过浏览器登陆后，在检查属性中复制过来
# headers['Cookie'] = 'aliyungf_tc=AQAAACum4wgXEAwAfYinr2dyx7O8DkQP; q_c1=03d6e41e93f34eeca73f2e7ea55038c0|1510136265000|1510136265000; _xsrf=cb9dd07e7669df946c0260bb522fc95a; d_c0="ACBC3lrcpgyPTl43F7t7FXiob49qgQMjLSM=|1510136266"; _zap=00565658-21f7-4989-8831-642011c54493; r_cap_id="MmUxMjYyNjhjNmM2NDY1ZmE1ZjgwMjg3ZTVmYjI4Yjg=|1510142790|101827cd78722f116af24645eba8664d2f232554"; cap_id="OGE3NTViYjk5OTNiNDI2YmExYmEyMjc1ODJkOTg4ZTU=|1510142790|d4707ced06a7dacac87c270cb3746737e52712ed"; __utma=51854390.1743963056.1510142597.1510142597.1510142597.1; __utmb=51854390.0.10.1510142597; __utmc=51854390; __utmz=51854390.1510142597.1.1.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/question/67306523/answer/256577474; __utmv=51854390.000--|3=entry_date=20171108=1; z_c0=Mi4xeTY3YkF3QUFBQUFBSUVMZVd0eW1EQmNBQUFCaEFsVk5ZRUh3V2dDcGlaYnRjX2NVN2NydHlOejJrU3dNQXBiVEZn|1510142816|39272ec5cf263296db314c0f64c7c24efa43d79c; _xsrf=cb9dd07e7669df946c0260bb522fc95a'

# url = "https://www.zhihu.com/"
# r = session.get(url, headers=headers, allow_redirects=False)
# print(r.text)
# login_code = r.status_code


