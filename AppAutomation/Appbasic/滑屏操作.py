#-*-coding:utf-8-*-
#@作者：haiyu.ma
#@创建日期：2020-06-24 0:13 
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as  EC
from appium.webdriver.common.mobileby import MobileBy
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
# appium - 滑动屏幕
# 滑动接口:
# swipe(起始X,起始Y,结束X,结束Y)
# 结束X- 起始X:X轴滑动的距离
# 结束Y - 起始Y:Y轴滑动的距离
# Q:手机的屏幕尺寸有很多,如何兼容?     进入app时的导航页面
# appium - 左右上下滑动屏幕
# 原理:
# 1、先获取设备的屏幕大小(长、宽)
# 2、再设置滑动的距离与屏幕大小的百分比。
# 3、调用滑动接口执行滑动操作。
# 获取当前窗口大小的接口:
# get_window_size: 返回窗口的宽和高。
# 滑动接口:
# swipe(起始X,起始Y,结束X,结束Y)
#height, width
size = driver.get_window_size()
start_x = size["width"] * 0.9
start_y = size["height"] * 0.5
end_x = size["width"] * 0.1
end_y = size["height"] * 0.5
#从右向左滑
driver.swipe(start_x, start_y, end_x, end_y, 200)
sleep(2)
driver.swipe(start_x, start_y, end_x, end_y, 200)
# #从左向右滑
# driver.swipe(end_x, end_y, start_x, start_y, 200)
#
# #上下滑动
# #向上滑动:X轴不变,Y轴从大到小。
# driver.swipe(size["width"] * 0.5, size["height"] * 0.9, size["width"] * 0.5, size["height"] * 0.1)
# #向上滑动:X轴不变,Y轴从小到大。
# driver.swipe(size["width"] * 0.5, size["height"] * 0.1, size["width"] * 0.5, size["height"] * 0.9)
