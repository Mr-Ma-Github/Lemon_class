#-*-coding:utf-8-*-
#@作者：haiyu.ma
#@创建日期：2020-07-02 23:12 
import pytest
from Common.basepage import BasePage
import time
from PageLocators.login_locators import LoginLocator as loc
import yaml
from Common.dir_config import caps_dir
from appium import webdriver
from PageObjects.Common_Bus import ComonBus

# 登录用例使用的前置
@pytest.fixture
def startApp():
    # 准备服务器参数，与appium server进行连接。noReset=True
    driver = baseDriver()
    # 1、判断欢迎页面是否存在
    ComonBus(driver).do_welcome()
    # 2、判断当前用户是否已登录  --如果有接口可以用接口
    # 3、如果已登录，那么先退出        --如果有接口可以用接口

# 除登录以外，通用的前置
@pytest.fixture
def LoginApp():
    # 准备服务器参数，与appium server进行连接。noReset=True
    driver = baseDriver()
    # 1、判断欢迎页面是否存在
    ComonBus(driver).do_welcome()
    # 2、判断当前用户是否已登录，如果没有登录，则进行登录操作
    # 3、是否有设置手势密码的弹窗。不设置
    # 3、如果已登录，那么先退出

# 服务器参数
def baseDriver(server_port=4723, noReset=None, automationName=None, **kwargs):
    #将默认的配置数据读取出来
    fs = open(caps_dir+"/caps.yaml")
    desired_caps = yaml.load(fs, Loader=yaml.FullLoader)
    #调整参数
    if noReset is not None:
        desired_caps["noReset"] = noReset
    if automationName is not None:
        desired_caps["automationName"] = noReset
    #kwargs
    #返回一个启动对象 --driver
    return webdriver.Remote('http://127.0.0.1:{}/wd/hub'.format(server_port), desired_caps)