#-*-coding:utf-8-*-
#@作者：haiyu.ma
#@创建日期：2020-05-30 23:22
from selenium.webdriver.common.by import By


class LoginPageLocators:
    # 元素定位
    # 用户名输入框
    name_text = (By.XPATH, '//input[@name="phone"]')
    # 密码输入框
    pwd_text = (By.XPATH, '//input[@name="password"]')
    # 记住密码
    remeber_user_info = (By.XPATH, '')
    # 登录按钮
    login_button = (By.XPATH, '//button[@text()="登录"]')
    # 获取错误提示信息--登录区域
    errorMsg_from_loginArea = (By.XPATH, '//div[@class="from-error-info"]')
    # 获取错误提示信息--页面正中间 区域
    errorMsg_from_PageCenter = (By.XPATH, '//div[@class="layul-layer-content"]')
    # print(errorMsg_from_PageCenter)
