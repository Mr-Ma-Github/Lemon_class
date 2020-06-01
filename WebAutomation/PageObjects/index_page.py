#-*-coding:utf-8-*-
#@作者：haiyu.ma
#@创建日期：2020-05-26 22:20
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import random


class IndexPage:
    def __init__(self,driver):
        self.driver = driver

    def isExist_logout_ele(self):
        # 如果存在就返回True，如果不存在，就返回False
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//a[@herd="/Index/logout.html"]')))
            return True
        except:
            return False

    # 选标操作：默认选第一个   #元素定位的时候，过滤掉不可以投的标'//*[text()="抢投标"]'
    def click_first_big(self):
        self.driver.find_element_by_xpath('//*[text()="抢投标"]').click()

    # 随机选标
    def click_bid_by_random(self):
        # 找到所有符合的标
        eles = self.driver.find_elements_by_xpath('//*[text()="抢投标"]')
        # 随机数
        index = random.randint(0,len(eles)-1)
        eles[index].click()