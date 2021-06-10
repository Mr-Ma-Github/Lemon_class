#-*-coding:utf-8-*-
# 个人作业：
# 10-30 请完成http_request类的单元测试
# 要求如下:
# 1) 针对10-27号写的http_request类做作业
# 2) 提供2个接口:登录url='http://119.23.241.154.8080/futureloan/mvc/api/member/login'
# 充值:'http://19.23 241.154.8080/futureloan/mvc/api/member/recharge'参数参照老师的python文件
# 3) 针对登录接口写4个用例:正常登录,不输入密码、不输入账号一个、输入错误的密码
# 充值接口写4个用例:正常充值、不输入账号、不输入金额一个、输入错误的金额负数
# 4)请利用任何一种方法实现用例的加载并执行
# 5) 生成html类型的测试报告
# 注意:请在测试类里面加上异常处理以及断言
import unittest


class TestHttpRequest(unittest.TestCase):
    def setUp(self):
        print("开始进行测试了")
        self.login_url = "http://119.23.241.154:8080/futureloan/mvc/api/member/login"
        self.login_data = {"mobilephone": "18688773467", "pwd": "123456"}
        self.recharge_url = ' http://119. 23. 241. 154:8080/futureloan/mvc/api/member/recharge'
        self.cookies = HttpRequest().http_request(self.login_url, self.login_data, "post").cookies
        print("登录后的cookie是：".format(self.cookies))

    def test_correct_login(self):
        data = {"mobilephone": "18688773467", "pwd": "123456"}
        res = HttpRequest().http_request(self.login_url,data,"post")
        try:#抓取错误  异常处理
            self.assertEquals('10001',res.json()["code"])#断言
            # self.assertIn("登陆成功", res.json()["msg"])
        except AssertionError as e:
            print("test_correct_login错误是{0}".format(e))
            raise e #异常处理之后需要抛出去

    def test_none_pw_login(self):
        data = {"mobilephone": "18688773467", "pwd": ""}
        res = HttpRequest().http_request(self.login_url,data,"post")
        try:
            self.assertEquals('20111',res.json()["code"])
        except AssertionError as e:
            print("test_none_pw_login错误是{0}".format(e))
            raise e

    # def test_none_un_login(self):
    #     url = "http://119.23.241.154:8080/futureloan/mvc/api/member/login"
    #     data.txt = {"": "18688773467", "pwd": "123456"}
    #     res = HttpRequest.http_request(url,data.txt,'post')
    #     print("登录结果是：", res.json())
    #
    # def test_error_pw(self):
    #     url = "http://119.23.241.154:8080/futureloan/mvc/api/member/login"
    #     data.txt = {"mobilephone": "18688773467", "pwd": "123456"}
    #     res = HttpRequest.http_request(url, data.txt, 'post')
    #     print("登录结果是：", res.json())
    def test_recharge_normal(self):
        recharge_data = {"mobilephone": "18688773467", "amount": "1000"}
        recharge_res = HttpRequest().http_request(self.recharge_url, recharge_data, 'post', self.cookies)
        try:
            self.assertEquals('10001',recharge_res.json()["code"])
        except AssertionError as e:
            print("test_recharge_normal错误是{0}".format(e))
            raise e

    def test_recharge_negative(self):
        recharge_data = {"mobilephone": "18688773467", "amount": "-1000"}
        recharge_res = HttpRequest().http_request(self.recharge_url, recharge_data, 'post', self.cookies)
        try:
            self.assertEquals('20117',recharge_res.json()["code"])
        except AssertionError as e:
            print("test_recharge_negative错误是{0}".format(e))
            raise e

    def tearDown(self):
        print("结束测试")

# -------------------------------------------------------
import unittest

COOKIE=None
class TestHttpRequest2(unittest.TestCase):
    def setUp(self):
        print("开始进行测试了")
        self.login_url = "http://119.23.241.154:8080/futureloan/mvc/api/member/login"
        self.recharge_url = ' http://119. 23. 241. 154:8080/futureloan/mvc/api/member/recharge'

    def test_correct_login(self):
        global COOKIE#声明全局变量
        data = {"mobilephone": "18688773467", "pwd": "123456"}
        res = HttpRequest().http_request(self.login_url,data,"post")
        if res.cookies:#如果cookie有值的话就update
            COOKIE=res.cookies
        try:#抓取错误  异常处理
            self.assertEquals('10001',res.json()["code"])#断言
            # self.assertIn("登陆成功", res.json()["msg"])
        except AssertionError as e:
            print("test_correct_login错误是{0}".format(e))
            raise e #异常处理之后需要抛出去

    def test_none_pw_login(self):
        data = {"mobilephone": "18688773467", "pwd": ""}
        res = HttpRequest().http_request(self.login_url,data,'post')
        try:
            self.assertEquals('20111',res.json()["code"])
        except AssertionError as e:
            print("test_none_pw_login错误是{0}".format(e))
            raise e

    def test_recharge_normal(self):
        global COOKIE
        recharge_data = {"mobilephone": "18688773467", "amount": "1000"}
        recharge_res = HttpRequest().http_request(self.recharge_url, recharge_data, 'post', COOKIE)
        try:
            self.assertEquals('10001',recharge_res.json()["code"])
        except AssertionError as e:
            print("test_recharge_normal错误是{0}".format(e))
            raise e

    def test_recharge_negative(self):
        global COOKIE
        recharge_data = {"mobilephone": "18688773467", "amount": "-1000"}
        recharge_res = HttpRequest().http_request(self.recharge_url, recharge_data, 'post', COOKIE)
        try:
            self.assertEquals('20117',recharge_res.json()["code"])
        except AssertionError as e:
            print("test_recharge_negative错误是{0}".format(e))
            raise e

    def tearDown(self):
        print("结束测试")

# ----------------------------------------------------------------------------
import unittest
from class_http_demo.http_request import HttpRequest
from class_http_demo.get_data import GetData
class TestHttpRequest3(unittest.TestCase):
    def setUp(self):
        print("开始进行测试了")
        self.login_url = "http://119.23.241.154:8080/futureloan/mvc/api/member/login"
        self.recharge_url = ' http://119. 23. 241. 154:8080/futureloan/mvc/api/member/recharge'

    def test_correct_login(self):
        data = {"mobilephone": "18688773467", "pwd": "123456"}
        res = HttpRequest().http_request(self.login_url,data,"post")
        if res.cookies:#如果cookie有值的话就update
            setattr(GetData,'cookie',res.cookies)
        try:#抓取错误  异常处理
            self.assertEquals('10001',res.json()["code"])#断言
            # self.assertIn("登陆成功", res.json()["msg"])
        except AssertionError as e:
            print("test_correct_login错误是{0}".format(e))
            raise e #异常处理之后需要抛出去

    def test_none_pw_login(self):
        data = {"mobilephone": "18688773467", "pwd": ""}
        res = HttpRequest().http_request(self.login_url,data,'post')
        try:
            self.assertEquals('20111',res.json()["code"])
        except AssertionError as e:
            print("test_none_pw_login错误是{0}".format(e))
            raise e

    def test_recharge_normal(self):
        recharge_data = {"mobilephone": "18688773467", "amount": "1000"}
        recharge_res = HttpRequest().http_request(self.recharge_url, recharge_data, 'post',getattr(GetData,'cookie'))
        try:
            self.assertEquals('10001',recharge_res.json()["code"])
        except AssertionError as e:
            print("test_recharge_normal错误是{0}".format(e))
            raise e

    def test_recharge_negative(self):
        recharge_data = {"mobilephone": "18688773467", "amount": "-1000"}
        recharge_res = HttpRequest().http_request(self.recharge_url, recharge_data, 'post',getattr(GetData,'cookie'))
        try:
            self.assertEquals('20117',recharge_res.json()["code"])
        except AssertionError as e:
            print("test_recharge_negative错误是{0}".format(e))
            raise e

    def tearDown(self):
        print("结束测试")