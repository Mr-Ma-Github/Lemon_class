#-*-coding:utf-8-*-
#@作者：haiyu.ma
#@创建日期：2020-05-31 17:49 

from PageLocators.userpage_locators import UserPageLocators as loc
from Common.basepage import BasePage

class UserPage(BasePage):

    #获取用户余额
    def get_user_leftMoney(self):
        doc = "个人页面_获取用户余额"
        # 等待元素
        self.wait_eleVisible(loc.user_leftMoney, doc=doc)
        # 获取个人可用余额的文本内容
        text = self.get_text(loc.user_leftMoney, doc)
        # 截取数字部分 --分隔符为：元
        return text.strip("元")

    # 获取第一条投资记录的时间、投资金额、收益金额--拓展
    # def  get_first_investRecord_info(self):
    # pass