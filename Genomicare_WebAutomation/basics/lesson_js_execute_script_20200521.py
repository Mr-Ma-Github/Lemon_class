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
driver.get("https://www.12306.cn/index/")
WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,'fromStationText')))
# 输入出发地：
# 方法一：
# driver.find_element_by_id('fromStationText').click()
# driver.find_element_by_xpath('//li[@data="BJP"]').click()
# 方法二：
# driver.find_element_by_id('fromStationText').clear()
# driver.find_element_by_id('fromStationText').send_keys("北京")
# driver.find_element_by_id("citem_2").click()
# time.sleep(2)
# 方法三：
# come='var a = document.getElementById("fromStation");a.value="BJP";b=document.getElementById("fromStationText");b.value="北京";b.className=("input inp-txt_select");'
come_a='var a = document.getElementById("fromStation");a.value="BJP";'
driver.execute_script(come_a)
WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,'fromStationText')))
come_b='var b=document.getElementById("fromStationText");b.value="北京";b.className=("input inp-txt_select");'
driver.execute_script(come_b)
time.sleep(2)
driver.find_element_by_id('toStationText').click()
driver.find_element_by_xpath('//li[@data="SHH"]').click()
time.sleep(2)
# 12306日期框操作js
# JS语句
js = 'var ele = document.getElementById("train_date");ele.readOnly=false;ele.value="2020-06-01";'
# js2= 'var ele = document.getElementById("train_date");ele.removeAttribute("readOnly");'
driver.execute_script(js)

chaxun='var cx =document.getElementById("search_one");cx.click();'
driver.execute_script(chaxun)
