#-*-coding:utf-8-*-
#@作者：haiyu.ma
#@创建日期：2020-05-21 21:19 
#-*-coding:utf-8-*-
#@作者：haiyu.ma
#@创建日期：2020-05-20 23:20
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service_log_path=R"C:\Users\haiyu.ma\PycharmProjects\lemon_class\WebAutomation\basics\chromedrive_service.log")
driver.maximize_window()
# 全局等待--隐性等待
driver.implicitly_wait(30)
# 访问一个网页
driver.get("http://www.baidu.com")
WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'//span[@id="s-usersetting-top"]')))
# 输入内容且自动回车(可以省略一步点击操作)
driver.find_element_by_xpath('//input[@id="kw"]').send_keys("柠檬班",Keys.ENTER)
# # 滚动条操作-滚动条不是HTML页面元素
# 1、移动到元素element对象的"底端"与当前窗口的"底部"对齐:
# driver.execute_script("arguments[0].scrollIntoView(false);",element)
# 2、移动到元素element对象的"顶端"与当前窗口的"顶部"对齐:
# driver.execute_script("arguments[0].scrollIntoView();",element)
# 3、移动到页面底部:
# driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
# 4、移动到页面顶部:
# driver.execute_script("window.scrollTo(document.body.scrollHeight,0)")
# 滚动条处理
# 1.找到要滚动到可视区域的元素
WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'//a[contains(text(),"知乎")]')))
ele = driver.find_element_by_xpath('//a[contains(text(),"知乎")]')
# 2.使用JS进行滚动操作
driver.execute_script("arguments[0].scrollIntoView(false);",ele)

# 12306日期框操作js
# JS语句
js = 'var ele = ele=document.getElementById("train_date");ele.readOnly=false;ele.value="2020-06-01";'
# js2= 'var ele = ele=document.getElementById("train_date");ele.removeAttribute("readOnly");'
driver.execute_script(js)


