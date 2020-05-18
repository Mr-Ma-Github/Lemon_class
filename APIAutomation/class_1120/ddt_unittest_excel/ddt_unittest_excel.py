#-*-coding:utf-8-*-
import unittest
from class_1120.http_request import HttpRequest
from class_1120.get_data import GetData
from ddt import ddt,data,unpack
from class_1120.do_excel import DoExcel

test_data = DoExcel("Excel_study.xlsx", "python").get_data()#这里传参可控制想要执行的用例all/列表
@ddt
class TestHttpRequest(unittest.TestCase):
    def setUp(self):
        print("开始进行测试了")

    @data(*test_data)
    def test_api(self,item):
        res = HttpRequest().http_request(item['url'],eval(item['data']),item['method'],getattr(GetData,'cookie'))
        if res.cookies:  # 如果cookie有值的话就update
            setattr(GetData, 'cookie', res.cookies)
        try:  # 抓取错误  异常处理
            self.assertEquals(str(item["excepted"]), res.json()["code"])  # 断言
            # self.assertIn("登陆成功", res.json()["msg"])
        except AssertionError as e:
            print("test_api错误是{0}".format(e))
            raise e  # 异常处理之后需要抛出去

    def tearDown(self):
        print("结束测试")


##注意：如果需要用TestSuite来调用的时候，可以用loader 类加载器
# suite = unittest.TestSuite()  # 存储用例
# loader = unittest.TestLoader()  # 创建一个加载器
# suite.addTest(loader.loadTestsFromTestCase(TestHttpRequest))


# 总结：
# 两种unittest+Excel  1）超继承  2）ddt
# 类
# unittest  单元测试  可通过单元测试 实现对自己写的类的测试
# TestCase   self.assert   try  except

# 参数化  80%   Excel   openpyxl
# 写成类  方法1 方法2 方法3

# 超继承      ddt