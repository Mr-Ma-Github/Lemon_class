#-*-coding:utf-8-*-
#@作者：haiyu.ma
#@创建日期：2020-05-31 17:48
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from PageLocators.bidpage_locators import BidPageLocators as loc
from Common.basepage import BasePage


class BidPage(BasePage):

    #投资
    def invest(self,money):
        # 在输入框当中，输入金额
        doc = "标详情页面_投资按钮"
        self.wait_eleVisible(loc.money_input,doc=doc)
        self.input_text(loc.money_input, money, doc)
        # 点击投标按钮
        self.click_element(loc.invest_button, doc)

    # 获取用户余额
    def get_user_money(self):
        doc = "投资页面_获取用户余额"
        self.wait_eleVisible(loc.money_input, doc=doc)
        return self.get_element_attribute(loc.money_input, "data_mount", doc=doc)


    # 投资成功的提示框--点击查看并激活
    def click_activeButton_on_success_popup(self):
        doc = "投资页面_投资成功的提示框-点击查看并激活"
        self.wait_eleVisible(loc.active_button_on_successPop, doc=doc)
        self.click_element(loc.active_button_on_successPop, doc)

    # 错误提示框--页面中间
    def get_errorMsg_from_pageCenter(self):
        # 获取文本内容
        doc = "投资页面_页面中间错误提示框"
        self.wait_eleVisible(loc.invest_failed_popup, doc=doc)
        msg = self.get_text(loc.invest_failed_popup, doc)
        # 关闭弹出框
        return msg

        # 获取提示信息 --投标按钮上
    def get_errorMsg_from_investButton(self):
        # 获取文本内容
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located())
        msg = self.driver.find_element().text
        # 关闭弹出框
        self.driver.find_element().click()
        return msg

