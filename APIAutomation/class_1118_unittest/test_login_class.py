#-*-coding:utf-8-*-
#@作者：haiyu.ma
#@创建日期：2020-09-04 16:25 
import unittest
from class_1118_unittest.login_request import HttpHandler


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.data = {"url": "http://test.lemonban.com/futureloan/mvc/api/member/login",
                     "method": "post",
                     "data": {"mobilephone": "18688888866", "pwd": "12345678"},
                     "header": {"X-Lemonban-Media-Type": "lemonban.v2"},
                     "excepted": "登录成功"}

    def test_login_2_success(self):
        res = HttpHandler().visit(self.data["url"], self.data["method"], data=self.data["data"],
                                  headers=self.data["header"])
        try:
            self.assertEqual(self.data["excepted"], res["msg"])
            print("登录成功")
        except AssertionError as e:
            print("登录失败")
            raise e

    def test_login_1_fail(self):
        pass