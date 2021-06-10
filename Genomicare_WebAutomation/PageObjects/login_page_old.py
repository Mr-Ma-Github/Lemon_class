#-*-coding:utf-8-*-
#@作者：haiyu.ma
#@创建日期：2020-05-26 22:23
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from PageLocators.loginpage_locators import LoginPageLocators as loc


class LoginPage:

    def __init__(self,driver):
        self.driver = driver

    # 登录
    def login(self, username, password, remeber_user=True):
        # 输入用户名
        # 输入密码
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc.name_text))
        self.driver.find_element(*loc.name_text).send_keys(username)
        self.driver.find_element(*loc.login_button).send_keys(password)
        # 判断一下remeber_user的值来决定是否勾选
        if remeber_user == False:
            self.driver.find_element(*loc.remeber_user_info).click()
            self.driver.find_element(*loc.login_button).click()
        else:
            self.driver.find_element(*loc.login_button).click()


    # 获取错误提示信息--登录区域
    def get_errorMsg_from_loginArea(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc.errorMsg_from_loginArea))
        return self.driver.find_element(*loc.errorMsg_from_loginArea).text



    # 忘记密码
