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
from class_1120.http_request import HttpRequest
from class_1120.get_data import GetData

class TestHttpRequest(unittest.TestCase):
    def setUp(self):
        print("开始进行测试了")
    # 超继承
    def __init__(self,methodNome,method,url,data,excepted):#通过初始化函数来传参数
        super(TestHttpRequest, self).__init__(methodNome)#父类的方法保留
        # super(子类名.self).__init__(父类与子类函数重名方法的参数)
        self.url=url
        self.data=data
        self.method=method
        self.excepted=excepted

    def test_api(self):
        res = HttpRequest().http_request(self.url, self.data,self.method,getattr(GetData,"cookie"))
        if res.cookies:  # 如果cookie有值的话就update
            setattr(GetData, 'cookie', res.cookies)
        try:  # 抓取错误  异常处理
            self.assertEquals(self.excepted, res.json()["code"])  # 断言
            # self.assertIn("登陆成功", res.json()["msg"])
        except AssertionError as e:
            print("test_api错误是{0}".format(e))
            raise e  # 异常处理之后需要抛出去

    def tearDown(self):
        print("结束测试")