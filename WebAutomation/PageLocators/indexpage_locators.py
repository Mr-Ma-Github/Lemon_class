#-*-coding:utf-8-*-
#@作者：haiyu.ma
#@创建日期：2020-06-01 22:16 
from selenium.webdriver.common.by import By


class IndexPageLocators:
    # 元素定位
    # 判断退出按钮是否存在（是否登录成功）
    isExist_logout_ele = (By.XPATH,'//a[@herd="/Index/logout.html"]')
    # 选择第一个标
    click_first_big = (By.XPATH,'//*[text()="抢投标"]')
    # 随机选标
    click_bid_by_random = (By.XPATH,'//*[text()="抢投标"]')