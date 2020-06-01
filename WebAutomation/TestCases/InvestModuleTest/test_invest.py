#-*-coding:utf-8-*-
#@作者：haiyu.ma
#@创建日期：2020-05-31 0:05

#正常用例
#前提条件:
######尽量不要依赖测 试坏境数据,如果没有,就自己造 环境#####
# 1、用户已登陆
# 2、有能够投资的标   #如果没有标,则先加标。 #接口的方式加标。
# 3、用户有余额可以投资
    #1、1个亿
    #2、接口方式:查询当前用户还有多少钱。&gt;6000 不用充值。如果小于用例中投资的金额,那就充值
#步骤
#1、在首页选标 -- 不根据标名,根据抢投标。 默认第一个标。
### 标页面-- 获取一下投资前的用户余额
#2、标页面 -- 输入投资金额、点击投资按钮
#3、标页面--点击投资成功的弹出框 查看并激活,进入个人页面
#断言
#钱    投资后的金额,是不是少了投资的量。
# 个人页面 获取 投资后的金额
# 投资前的金额额减去投资后的金额 = 投资金额
# 投资记录对不对

# 异常用例：非常好创造环境，非常好写的

# 不考虑自动化实现的--不好实现，建议手工
# 异常用例：全投操作 ？   标的可投金额 > 个人余额
         # 投资金额 > 标的可投金额  #满足这种条件标 、用户
import unittest
from selenium import webdriver
from TestDatas import Common_Datas as CD
from PageObjects.login_page import LoginPage
from TestDatas.LoginModuleDatas import login_datas as LD
from PageObjects.index_page import IndexPage
from PageObjects.bid_page import BidPage
from PageObjects.user_page import UserPage



class TestInvest(unittest.TestCase):

    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get(CD.web_login_url)
        cls.BP = BidPage(cls.driver)

    def setUp(self):
        LoginPage(self.driver).login(LD.success_data["username"], LD.success_data["password"])
        self.assertTrue(IndexPage(self.driver).isExist_logout_ele())
        IndexPage(self.driver).click_first_big()
        UserPage(self.driver).get_money()
        UserPage(self.driver).user_page_close()

    def tearDown(self):
        # 后置  刷新页面
        self.driver.refresh()

    def test_invest_success(self):
        # 步骤
        # 1、在首页选标 -- 不根据标名,根据抢投标。 默认第一个标。
        ### 标页面-- 获取一下投资前的用户余额
        # 2、标页面 -- 输入投资金额、点击投资按钮
        # 3、标页面--点击投资成功的弹出框 查看并激活,进入个人页面
        # 断言
        # 钱    投资后的金额,是不是少了投资的量。
        # 个人页面 获取 投资后的金额
        # 投资前的金额额减去投资后的金额 = 投资金额
        # 投资记录对不对
        self.BP.invest("100")
        self.a

        pass
    def test_invest_failed_no100(self):
        pass
    def test_invest_failed_no10(self):
        pass


