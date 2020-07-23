#-*-coding:utf-8-*-
#@作者：haiyu.ma
#@创建日期：2020-07-05 21:11
from Common.basepage import BasePage
from PageLocators.login_locators import LoginLocator as loc


class LoginPage(BasePage):

    # 登录
    def input_usernaem(self, username):
        # 输入用户名
        doc = "登录页面_输入用户名页面"
        self.wait_eleVisible(loc.user_input,doc=doc)
        self.input_text(loc.user_input, username,doc)
        self.click_element(loc.next_step, doc)#点击下一步

    def input_password(self, passwd):
        # 输入密码
        doc = "登录页面_输入密码页面"
        self.wait_eleVisible(loc.passwd_input, doc=doc)
        self.input_text(loc.passwd_input, passwd, doc)
        self.click_element(loc.next_step, doc)

    def get_wrongMsg_from_userPage(self):
        pass

    def get_wrongMsg_from_passwdPage(self):
        pass