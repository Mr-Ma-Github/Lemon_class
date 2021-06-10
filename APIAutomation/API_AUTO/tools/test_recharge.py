#-*-coding:utf-8-*-
#@作者：haiyu.ma
#@创建日期：2019-12-07 12:36
import unittest
from API_AUTO.tools.http_request import HttpRequest
from API_AUTO.tools.get_data import GetData
from ddt import ddt,data
from API_AUTO.tools.do_excel_old import DoExcel
from API_AUTO.tools.project_path import *

test_data=DoExcel.do_excel(test_case_path,'recharge')
@ddt
class TestHttpRequest(unittest.TestCase):
    def setUp(self):
        print("测试开始了")

    @data(*test_data)
    def test_http(self,item):
        res=HttpRequest().http_request(item["url"],item["data.txt"],item["method"],getattr(GetData,"Cookie"))
        if res.cookies:
            setattr(GetData,"Cookie",res.cookies)
        try:  # 抓取错误  异常处理
            self.assertEquals(item["excepted"], res.json()["code"])  # 断言
            # self.assertIn("登陆成功", res.json()["msg"])
            TestResult="PASS"
        except AssertionError as e:
            TestResult="failed"
            print("test_api错误是{0}".format(e))
            raise e  # 异常处理之后需要抛出去
        finally:
            DoExcel.write_back(test_case_path,"recharge",item["case_id"]+1,str(res.json()),TestResult)
            print("获取到的结果是：".format(res.json()))
    def tearDown(self):
        print("用例执行结束了")