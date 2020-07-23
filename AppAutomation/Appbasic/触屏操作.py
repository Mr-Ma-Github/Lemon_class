#-*-coding:utf-8-*-
#@作者：haiyu.ma
#@创建日期：2020-06-27 22:13 
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as  EC
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from time import sleep

desired_caps = {}
# 平台类型
desired_caps["platformName"] = 'Android'
# 平台版本号
desired_caps["platformVersion"] = '7.1.2'
# 设备名称
desired_caps["deviceName"] = '127.0.0.1:62026'
# app包名
desired_caps["appPackage"] = 'com.cn.xizeng'
# app入口activity
desired_caps["appActivity"] = 'com.cn.xizeng.view.FaceActivity'
# app绝对路径
desired_caps['app'] = R'C:\Users\haiyu.ma\Downloads\xizeng.apk'
# 等待最大时长
desired_caps['newCommandTimeout']= 180
# 重置与否
desired_caps['noReset'] = True

# 连接appium server   前提：appium desktop要启动，有监听端口
# 将desired_caps发送给appium server ，打开app
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
# 等待元素出现
loc = 'new UiSelector().text("")'
WebDriverWait(driver,30).until(EC.visibility_of_element_located((MobileBy.ANDROID_UIAUTOMATOR,loc)))

# appium-模拟触屏
# TouchAction类
# 将一系列的动作放在一个链条中,然后将该链条传递给服务器。服务器接受到该链条后,解析链条中的每个
# 动作,逐个执行。
# 短按(press)
# 长按(longPress)
# 点击(tap)
# 移动到(move_to) x,y为相对上一个坐标的移动距离
# 等待(wait)
# 释放(release)
# 执行(perform)
# 取消(cancel)
# ####正方形视图处理
ele = driver. find_element_by_id("")
#元素的大小
size = ele.size
#均分的步长 高和宽一样。
step = size["width"]/6
#元素的起点坐标 - 左上角
ori = ele.location
point1 = (ori["x"]+step, ori["y"]+step)
point2 = (point1[0] + step*2, point1[1]) ##相对于pointl, X轴增加了2*step
point3 = (point2[0] + step*2, point2[1]) ##相对于point2, X轴增加了2*step
point4 = (point3[0] - step*2, point3[1]+step*2) #相对于point3, X轴减少了2*step,Y轴增加了2*step
point5 = (point4[0], point4[1] + step*2) #相对于point4, X轴不变, Y轴增加了2*step

TouchAction(driver).\
    press(x=point1[0], y=point1[1]).wait(200).\
    move_to(x=point2[0], y=point2[1]). wait(200).\
    move_to(x=point3[0], y=point3[1]). wait(200).\
    move_to(x=point4[0], y=point4[1]). wait(200).\
    move_to(x=point5[0], y=point5[1]). wait (200).\
    release().\
    perform()