#-*-coding:utf-8-*-
#@作者：haiyu.ma
#@创建日期：2019-12-07 13:02
import unittest
import HTMLTestRunner
import sys
sys.path.append('C:\\Users\haiyu.ma\PycharmProjects\lemon_class\APIAutomation')
from API_AUTO.tools.project_path import test_report_path
from API_AUTO.tools.test_http_request import TestHttpRequest

suite=unittest.TestSuite()
loader=unittest.TestLoader()
# # 并行用例方法一
# suite.addTest(loader.loadTestsFromModule(test_http_request))
suite.addTest(loader.loadTestsFromTestCase(TestHttpRequest))

with open(test_report_path, "wb")as file:
    runner = HTMLTestRunner.HTMLTestRunner(stream=file,verbosity=2,title="python单元测试报告",description="这是一份测试报告")
    runner.run(suite)

'''多个用例同时执行
1.写多个模块 不同的模块 就用不同test_http_request   run里面去做加载
2.通过配置文件去决定执行哪个模块的用例'''