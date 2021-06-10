#-*-coding:utf-8-*-
#@作者：haiyu.ma
#@创建日期：2020-05-19 22:37

# Alert弹出框操作
# 浏览器弹出框:
# 1、使用 switch_to 方法先切換到浏览器弹出框。
# driver.switch_to.alert
# 2、Alert 类提供了一系列的操作方法。
# dismiss(): 否
# accept(): 是
# text(): 获取弹出框里的内容。
# Send_keys();往弹出框里输入文本。

from selenium import webdriver
import time
# 显性等待
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
# 启动谷歌浏览器，开始与浏览器之间的会话
driver = webdriver.Chrome(service_log_path=R"C:\Users\haiyu.ma\PycharmProjects\lemon_class\WebAutomation\basics\chromedrive_service.log")
driver.maximize_window()
# 全局等待--隐性等待
driver.implicitly_wait(30)
# driver.get(R'C:\Users\haiyu.ma\PycharmProjects\lemon_class\WebAutomation\basics\class_0512.html')
driver.get('http://localhost:63342/WebAutomation/basics/class_0512.html?_ijt=8rua653igd0gm67oi61shsmrnm')
# 等待alert出现
WebDriverWait(driver,10).until(EC.alert_is_present())
# alert切换    不是html的元素
alert=driver.switch_to.alert
# 打印弹窗的内容
print(alert.text)
# 关闭弹窗
alert.accept()#接受
# alert.dismiss()#拒绝

