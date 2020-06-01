#-*-coding:utf-8-*-
#@作者：haiyu.ma
#@创建日期：2020-05-31 17:48
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from PageLocators.loginpage_locators import LoginPageLocators as loc


class BidPage:
    def __init__(self,driver):
        self.driver = driver

    #投资
    def invest(self,money):
        # 在输入框当中，输入金额
        # 点击投标按钮
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located())
        self.driver.find_element().send_keys(money)
        self.driver.find_element().click()

    # 获取用户余额
    def get_user_money(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located())
        self.driver.find_element().click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located())
        return self.driver.find_element().text

    # 投资成功的提示框--点击查看并激活
    def click_activeButton_on_success_popup(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located())
        self.driver.find_element().click()
        return self.driver.find_element().text

    # 错误提示框--页面中间
    def get_errorMsg_from_pageCenter(self):
        # 获取文本内容
        # 关闭弹出框
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located())
        self.driver.find_element().click()
        return self.driver.find_element().text

    # 获取提示信息 --投标按钮上
    def get_errorMsg_from_investButton(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located())
        self.driver.find_element().click()
        return self.driver.find_element().text


