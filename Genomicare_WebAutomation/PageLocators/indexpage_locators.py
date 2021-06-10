#-*-coding:utf-8-*-
#@作者：haiyu.ma
#@创建日期：2020-06-01 22:16 
from selenium.webdriver.common.by import By


class IndexPageLocators:
    # 元素定位
    # 判断退出按钮是否存在（是否登录成功）
    isExist_homepage_ele = (By.XPATH, '//span[contains(text(),"报表")]')
