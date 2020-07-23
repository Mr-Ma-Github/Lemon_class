#-*-coding:utf-8-*-
#@作者：haiyu.ma
#@创建日期：2020-07-05 22:34
from Common.basepage import BasePage

def get_loginStatus(driver):
    # 获取当前app的登录状态，已登录为True，未登录为False
    try:
        # 等待5秒   #找登录/注册按钮
        return False
    except:
        return True
    pass