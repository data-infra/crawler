# -*- coding:utf-8 -*-
#python+selenium+PhantomJS 无视图的浏览器处理。高效处理模拟js功能
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.PhantomJS(executable_path='./phantomjs.exe')  #使用当前目录下的PhantomJS这个浏览器来作为js处理器

driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html")  #请求指定网址。所以的js反应会自动修改driver，所以不同时间访问driver会有不同的效果

#隐式等待（等待特定的时间）
time.sleep(3)  #等待页面中的初始化js函数和初始化ajax函数完成。如果这里时间短，则下面的driver内容会不一样。
# driver.implicitly_wait(3) # seconds


#显示等待，等待指定条件结束
driver.get("http://somedomain/url_that_delays_loading")
try:
    element = WebDriverWait(driver, 10).until(  #10为超时时间
        EC.presence_of_element_located((By.ID, "myDynamicElement"))  #程序默认会 500ms 调用一次来查看元素是否已经生成，如果本来元素就是存在的，那么会立即返回。
        #以下是内置的等待条件
        # title_is
        # title_contains
        # presence_of_element_located
        # visibility_of_element_located
        # visibility_of
        # presence_of_all_elements_located
        # text_to_be_present_in_element
        # text_to_be_present_in_element_value
        # frame_to_be_available_and_switch_to_it
        # invisibility_of_element_located
        # element_to_be_clickable – it is Displayed and Enabled.
        #     staleness_of
        # element_to_be_selected
        # element_located_to_be_selected
        # element_selection_state_to_be
        # element_located_selection_state_to_be
        # alert_is_present
    )
finally:
    driver.quit()

html = driver.page_source  #获取页面执行后的网页源代码（初始化js和初始化ajax执行结束后的源代码，即谷歌中审查元素的网页源代码）
print(html)


#获取元素、元素列表
element = driver.find_element_by_css_selector('#content')  #根据css选择器获取元素
element = driver.find_element_by_tag_name("div")  #根据标签名称获取元素
element = driver.find_element_by_name("passwd")  #根据名称选择
element = driver.find_element_by_xpath("//input[@id='passwd-id']")  #根据路径表达式选择
element = driver.find_element_by_class_name('class1')  #根据样式类选择元素
element = driver.find_element_by_id('content')  #根据id获取元素
elements = driver.find_elements_by_css_selector("div")  #find_elements获取元素列表

#通过by类来实现选择
driver.find_element(By.XPATH, '//button[text()="Some text"]')
driver.find_elements(By.XPATH, '//button')
# ID = "id"
# XPATH = "xpath"
# LINK_TEXT = "link text"
# PARTIAL_LINK_TEXT = "partial link text"
# NAME = "name"
# TAG_NAME = "tag name"
# CLASS_NAME = "class name"
# CSS_SELECTOR = "css selector"

#selsect选择元素
select = Select(driver.find_element_by_name('name'))  #根据查找到的select元素，构建Select对象
select.select_by_index(1)   #根据索引来选择
select.select_by_visible_text("text")  #根据值来选择
select.select_by_value("value1")  #根据文字来选择
select.deselect_all()  #全部取消选择
all_selected_options = select.all_selected_options  #获取所有的已选选项
options = select.options  #获取所有可选选项

#元素属性
element.get_attribute("value")  #元素属性
element.text  #元素文本

#模拟操作
element.send_keys("some text")  #追加填入文本
element.send_keys("and some", Keys.ARROW_DOWN)  #点击按键
element.clear()  #清除文本
element.click()  #模拟点击
element.submit()  #提交元素提交
#元素拖拽
element = driver.find_element_by_name("source")
target = driver.find_element_by_name("target")

from selenium.webdriver import ActionChains
action_chains = ActionChains(driver)
action_chains.drag_and_drop(element, target).perform()


# 页面切换
driver.switch_to.window("windowName")  #切换到指定名称的窗口
for handle in driver.window_handles:  #遍历窗口对象
    driver.switch_to.window(handle)  #切换到窗口对象
driver.switch_to.frame("frameName.0.child")  #切换到指定名称的fragme，焦点会切换到一个 name 为 child 的 frame 上

# 弹窗处理
alert = driver.switch_to.alert()  #获取弹窗对象

# 历史记录
driver.forward()  #页面前进
driver.back()  #页面后退

# Cookies处理
cookie = {'name' : 'foo', 'value' : 'bar'}  #使用字典定义cookie的值
driver.add_cookie(cookie)  #设置cookie
cookie = driver.get_cookies()  #读取cookie


driver.close()
