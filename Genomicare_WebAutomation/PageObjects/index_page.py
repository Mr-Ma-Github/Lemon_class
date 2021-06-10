#-*-coding:utf-8-*-
#@作者：haiyu.ma
#@创建日期：2020-05-26 22:20
import random
from PageLocators.indexpage_locators import IndexPageLocators as loc
from Common.basepage import BasePage


class IndexPage(BasePage):

    # 判断是否在首页
    def isExist_homepage_ele(self):
        # 如果存在就返回True，如果不存在，就返回False
        try:
            doc = "报表button"
            self.wait_eleVisible(loc.isExist_homepage_ele, doc=doc)
            return True
        except:
            return False

    # # 判断是否在首页
    # def isExist_homepage_ele(self):
    #     # 如果存在就返回True，如果不存在，就返回False
    #     doc = "欢迎title"
    #     try:
    #         self.wait_eleVisible(loc.isExist_homepage_ele, doc=doc)
    #         return True
    #     except Exception:
    #         return False
