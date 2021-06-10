# -*-coding:utf-8-*-
# @作者：haiyu.ma
# @创建日期：2019-12-07 12:36
import unittest
from GC_API.tools.http_request import HttpRequest
from GC_API.tools.get_data import GetData
from ddt import ddt, data
from GC_API.tools.do_excel import DoExcel
from GC_API.tools.project_path import *
from GC_API.tools.my_log import MyLog

my_logger=MyLog()
test_data = DoExcel.do_excel(test_data_path)

@ddt
class TestHttpRequest(unittest.TestCase):
    def setUp(self):
        print("测试用例开始执行!")

    @data(*test_data)
    def test_http_1(self, item):
        global TestResult
        my_logger.info("开始执行用例：{0}--{1}".format(item['case_id'], item['title']))
        my_logger.info("获取到的请求数据是:{0}".format(item['data']))
        res = HttpRequest().http_request(item["url"], item["method"], json=eval(item["data"]))
        if "id_token" in res.json():
            setattr(GetData, "Authorization", res.json()["id_token"])
            try:  # 抓取错误  异常处理
                self.assertEqual(item["expected"], res.status_code)  # 断言
                TestResult = "PASS"
            except Exception as e:
                TestResult = "failed"
                my_logger.info("捕捉错误是{0}".format(e))
                raise e  # 异常处理之后需要抛出去
            finally:
                DoExcel.write_back(test_data_path, "login", item["case_id"] + 1, 8, TestResult)
                my_logger.info("获取到的结果是：{}".format(res.json()))
                my_logger.info(TestResult)
        else:
            try:  # 抓取错误  异常处理
                self.assertEqual(item["expected"], res.status_code)  # 断言
                TestResult = "PASS"
            except Exception as e:
                TestResult = "failed"
                my_logger.info("捕捉错误是{0}".format(e))
                raise e  # 异常处理之后需要抛出去
            finally:
                DoExcel.write_back(test_data_path, "login", item["case_id"] + 1, 8, TestResult)
                my_logger.info("获取到的结果是：{}".format(res.json()))
                my_logger.info(TestResult)

    def test_demo(self):
        pass

    def tearDown(self):
        print("测试用例执行结束！")
