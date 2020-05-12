#-*-coding:utf-8-*-
import unittest
import HTMLTestRunner
from class_http_demo.test_http import TestHttpRequest

suite = unittest.TestSuite()  # 存储用例
loader = unittest.TestLoader()  # 创建一个加载器
suite.addTest(loader.loadTestsFromTestCase(TestHttpRequest))  # 执行类里面的所有用例
with open("test_report.html", "wb")as file:
    runner = HTMLTestRunner.HTMLTestRunner(stream=file,verbosity=2,title="python单元测试报告",description="这是一份测试报告")
    runner.run(suite)