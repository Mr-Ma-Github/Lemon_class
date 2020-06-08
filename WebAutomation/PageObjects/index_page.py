#-*-coding:utf-8-*-
#@作者：haiyu.ma
#@创建日期：2020-05-26 22:20
import random
from PageLocators.indexpage_locators import IndexPageLocators as loc
from Common.basepage import BasePage


class IndexPage(BasePage):

    # 判断退出按钮是否存在
    def isExist_logout_ele(self):
        # 如果存在就返回True，如果不存在，就返回False
        try:
            doc = "首页_退出按钮"
            self.wait_eleVisible(loc.isExist_logout_ele,doc=doc)
            return True
        except:
            return False

    # 选标操作：默认选第一个   #元素定位的时候，过滤掉不可以投的标'//*[text()="抢投标"]'
    def click_first_bid(self):
        doc = "首页_选标操作(第一个)"
        self.click_element(loc.click_first_big,doc=doc)

    # 随机选标
    def click_bid_by_random(self):
        doc = "首页_选标操作(第一个)"
        # 找到所有符合的标
        eles = self.get_element(loc.click_bid_by_random)
        # 随机数
        index = random.randint(0,len(eles)-1)
        eles[index].click()