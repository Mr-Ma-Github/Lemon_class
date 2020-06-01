#-*-coding:utf-8-*-
#@作者：haiyu.ma
#@创建日期：2020-05-31 17:49 
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from PageLocators.loginpage_locators import LoginPageLocators as loc


class UserPage:
    def __init__(self,driver):
        self.driver = driver

    #获取金额
    def get_money(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located())
        return self.driver.find_element().text

    def user_page_close(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located())
        self.driver.find_element().click()