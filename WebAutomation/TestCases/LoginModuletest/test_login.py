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


@ddt
class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):#所有用例执行前,整个测试类只执行一次
        #通过Excel读取本功能当中需要的所有测试数据
        cls.driver = webdriver.Chrome()
        cls.driver.get(CD.web_login_url)
        cls.lg = LoginPage(cls.driver)
        # setUpClass、tearDownClass
        # 需要考虑：1.每一个测试用例失败后，会不会影响到其他的用例
        #           2.稳定性
        # 用法：1.所有用例执行前,打开浏览器，访问登录页面
        #       2.每一个用例执行完成后刷新当前页面
        #       3.最后一个用例是登录成功的用例

    # def setUp(self):#每个用例执行前
    #     #前置  打开浏览器--访问登录页面
    #     self.driver = webdriver.Chrome()
    #     self.driver.get(CD.web_login_url)
    #     self.lg = LoginPage(self.driver)

    @classmethod
    def tearDownClass(cls):#所有用例执行后,整个测试类只执行一次
        cls.driver.quit()

    def tearDown(self):#每个用例执行后
        # 后置  刷新页面
        self.driver.refresh()

    # 正常用例--登录成功
    def test_login_2_success(self):
        #步骤  输入用户名：XXX、密码XXX、点击登录
        self.lg.login(LD.success_data["username"], LD.success_data["password"])
        #断言  首页当中--能否找到  退出  元素
        self.assertTrue(IndexPage(self.driver).isExist_logout_ele())

    # 异常用例--手机号格式不正确(大于11位、小于11位、为空、不在号码段)
    # //ddt(前置、步骤、断言方式都是一样的，可用ddt)
    # def test_login_user_wrongFormat(self):
    #     # 步骤  输入用户名：XXX、密码XXX、点击登录
    #     self.lg.login("186847205534", "python")
    #     # 断言  登录页面  提示：请输入正确的手机号
    #     # 登录页面中--获取提示框的文本
    #     # 比对文本内容与 期望的值  是否相等
    #     self.assertEqual(self.lg.get_errorMsg_from_loginArea(),'请输入正确的手机号')
    # def test_login_user_wrongFormat_2(self):
    #     # 步骤  输入用户名：XXX、密码XXX、点击登录
    #     self.lg.login("18684720", "python")
    #     # 断言  登录页面  提示：请输入正确的手机号
    #     # 登录页面中--获取提示框的文本
    #     # 比对文本内容与 期望的值  是否相等
    #     self.assertEqual(self.lg.get_errorMsg_from_loginArea(),'请输入正确的手机号')
    # def test_login_user_wrongFormat_3(self):
    #     # 步骤  输入用户名：XXX、密码XXX、点击登录
    #     self.lg.login("", "python")
    #     # 断言  登录页面  提示：请输入正确的手机号
    #     # 登录页面中--获取提示框的文本
    #     # 比对文本内容与 期望的值  是否相等
    #     self.assertEqual(self.lg.get_errorMsg_from_loginArea(),'请输入手机号')
    @data(*LD.phone_data)
    def test_login_0_user_wrongFormat(self, data):
        # 步骤  输入用户名：XXX、密码XXX、点击登录
        self.lg.login(data["username"], data["password"])
        # 断言  登录页面  提示：请输入正确的手机号
        # 登录页面中--获取提示框的文本
        # 比对文本内容与 期望的值  是否相等
        self.assertEqual(self.lg.get_errorMsg_from_loginArea(), data["check"])

    @data(*LD.NoReg_ErrorPwd)
    def test_login_1_wrongPwd_noReg(self,data):
        # 步骤  输入用户名：XXX、密码XXX、点击登录
        self.lg.login(data["username"], data["password"])
        # 断言  登录页面  页面正中间提示：请输入正确的手机号
        # 登录页面中--获取提示框的文本
        # 比对文本内容与 期望的值  是否相等
        self.assertEqual(self.lg.get_errorMsg_from_PageCenter(), data["check"])

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