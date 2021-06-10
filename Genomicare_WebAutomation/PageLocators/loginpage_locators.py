#-*-coding:utf-8-*-
#@作者：haiyu.ma
#@创建日期：2020-05-30 23:22
from selenium.webdriver.common.by import By


class LoginPageLocators:
    # 初始登录按钮
    start_login = (By.XPATH, '//a[@id="login"]/span/span')
    # 元素定位
    login = (By.XPATH, '//a[@class="alert-link"]')
    # 用户名输入框
    name_text = (By.XPATH, '//input[@id="username"]')
    # 密码输入框
    pwd_text = (By.XPATH, '//input[@id="password"]')
    # 记住密码
    remeber_user_info = (By.XPATH, '//input[@id="rememberMe"]')
    # 登录按钮
    login_button = (By.XPATH, '//button[@class="btn btn-primary mt-1"]/span')
    # 获取错误提示信息--登录区域
    errorMsg_from_loginArea = (By.XPATH, '//div[@class="alert alert-danger"]/span')
