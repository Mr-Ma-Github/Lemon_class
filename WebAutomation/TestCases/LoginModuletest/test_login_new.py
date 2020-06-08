#-*-coding:utf-8-*-
#@作者：haiyu.ma
#@创建日期：2020-05-26 23:36
import unittest
from selenium import webdriver
from PageObjects.login_page import LoginPage
from PageObjects.index_page import IndexPage
from TestDatas import Common_Datas as CD
from TestDatas.LoginModuleDatas import login_datas as LD
from ddt import ddt,data
import pytest
import logging

@pytest.mark.usefixtures("func_demo")
@pytest.mark.usefixtures("class_demo")
@pytest.mark.demo
def test_demo():
    print("test")
    assert False

def demo():
    print("test")

@pytest.mark.usefixtures("access_web")
@pytest.mark.usefixtures("refresh_page") #在运行的时候，会去运行access_web函数
class TestLogin:

    # @classmethod
    # def setUpClass(cls):#所有用例执行前,整个测试类只执行一次
    #     #通过Excel读取本功能当中需要的所有测试数据
    #     cls.driver = webdriver.Chrome()
    #     cls.driver.get(CD.web_login_url)
    #     cls.lg = LoginPage(cls.driver)
    #     # setUpClass、tearDownClass
    #     # 需要考虑：1.每一个测试用例失败后，会不会影响到其他的用例
    #     #           2.稳定性
    #     # 用法：1.所有用例执行前,打开浏览器，访问登录页面
    #     #       2.每一个用例执行完成后刷新当前页面
    #     #       3.最后一个用例是登录成功的用例
    #
    # # def setUp(self):#每个用例执行前
    # #     #前置  打开浏览器--访问登录页面
    # #     self.driver = webdriver.Chrome()
    # #     self.driver.get(CD.web_login_url)
    # #     self.lg = LoginPage(self.driver)
    #
    # @classmethod
    # def tearDownClass(cls):#所有用例执行后,整个测试类只执行一次
    #     cls.driver.quit()
    #
    # def tearDown(self):#每个用例执行后
    #     # 后置  刷新页面
    #     self.driver.refresh()

    # 正常用例--登录成功
    @pytest.mark.smoke
    def test_login_2_success(self, access_web):#fixture的函数名称作为用例参数，用来接收fixture返回值
        logging.info("***登录用例：正常场景：使用正确的用户名和密码登录*****")
        #步骤  输入用户名：XXX、密码XXX、点击登录
        access_web[1].login(LD.success_data["username"], LD.success_data["password"])
        #断言  首页当中--能否找到  退出  元素
        assert IndexPage(access_web[0]).isExist_logout_ele()

    @pytest.mark.parametrize("data",LD.phone_data)
    def test_login_0_user_wrongFormat(self, data, access_web):
        # 步骤  输入用户名：XXX、密码XXX、点击登录
        access_web[1].login(data["username"], data["password"])
        # 断言  登录页面  提示：请输入正确的手机号
        # 登录页面中--获取提示框的文本
        # 比对文本内容与 期望的值  是否相等
        assert access_web[1].get_errorMsg_from_loginArea() == data["check"]

    @pytest.mark.parametrize("data",LD.NoReg_ErrorPwd)
    def test_login_1_wrongPwd_noReg(self,data, access_web):
        # 步骤  输入用户名：XXX、密码XXX、点击登录
        access_web[1].login(data["username"], data["password"])
        # 断言  登录页面  页面正中间提示：请输入正确的手机号
        # 登录页面中--获取提示框的文本
        # 比对文本内容与 期望的值  是否相等
        assert access_web[1].get_errorMsg_from_PageCenter() == data["check"]



    # 异常用例--未注册手机号
    # 异常用例--密码为空
    # 异常用例--密码不正确
    # def test_login_NoUser(self):
    #     # 前置  访问登录页面
    #     # 步骤  输入用户名：XXX、密码XXX、点击登录
    #     # 断言  首页当中--能否找到  退出  元素
    #     pass
        # 等待10秒  元素有没有出现
        # 找元素   //a[@herd="/Index/logout.html"]
        # self.driver.find_element_by_xpath('')