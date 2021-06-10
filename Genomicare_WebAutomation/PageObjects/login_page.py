#-*-coding:utf-8-*-
#@作者：haiyu.ma
#@创建日期：2020-05-26 22:23
from PageLocators.loginpage_locators import LoginPageLocators as loc
from Common.basepage import BasePage
import time

class LoginPage(BasePage):

    # 点击初始登录按钮
    def click_login(self):
        doc = "点击初始登录按钮"
        self.wait_elePresence(loc.login, doc=doc)
        self.click_element(loc.login, doc=doc)

    # 登录操作
    def login(self,username, password, remeber_user=True):
        # 输入用户名
        # 输入密码
        doc = "登录页面_登录功能"
        self.wait_eleVisible(loc.name_text, doc=doc)
        self.input_text(loc.name_text, username, doc)
        time.sleep(2)
        self.input_text(loc.pwd_text, password, doc)
        # 判断一下remeber_user的值来决定是否勾选
        if remeber_user == False:
            self.click_element(loc.remeber_user_info)
            self.click_element(loc.login_button)
            time.sleep(2)
        else:
            self.click_element(loc.login_button)
            time.sleep(2)

    # 获取错误提示信息--登录区域
    def get_errorMsg_from_loginArea(self):
        doc = "登录页面_获取登录区域错误提示"
        self.wait_elePresence(loc.errorMsg_from_loginArea, doc=doc)
        return self.get_text(loc.errorMsg_from_loginArea, doc)


    # # 注册
    # def register_enter(self):
    #     WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '')))
    #     self.driver.find_element_by_xpath('').click()

    # 忘记密码
