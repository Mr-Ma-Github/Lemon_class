#-*-coding:utf-8-*-
#@作者：haiyu.ma
#@创建日期：2020-07-05 23:34 
from appium.webdriver.common.mobileby import MobileBy as Mb

class BidPageLocator:
    # 标名
    project_name = (Mb.ID,"com.xxzb.fenwoo:id/tv_title")
    # 用户余额,同时也是投资金额输入处
    invest_input = (Mb.ID,"com.xxzb.fenwoo:id/et_investamount")
    # 投资按钮
    invest_button = (Mb.ID,"com.xxzb.fenwoo:id/btn_investnow")
    # 投资成功 - 弹出框 - 弹出框消息
    popUp_message = (Mb.ID,"com. xxzb.fenwoo:id/tv_message")
    # 投资成功 - 弹出框 - 确定按钮
    popup_confirm_button = (Mb.ID,"com.xxzb.fenwoo:id/btn_confirm")
    # 返回按钮
    back_button = (Mb.ID,"com.xxzb.fenwoo:id/btn_back")