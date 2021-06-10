# -*-coding:utf-8-*-
# @作者：haiyu.ma
# @创建日期：2019-12-07 13:02
import unittest
import HTMLTestRunner
import time
import os
from GC_API.tools.project_path import test_report_path
from GC_API.tools import test_login
from GC_API.tools.test_login import TestHttpRequest
from GC_API.tools.send_email6 import SendEmail
import sys

# # 获取执行文件的绝对路径
dir_run_test_case = os.path.dirname(os.path.abspath(__file__))
# 获取 "test_case" 的绝对路径
dir_test_case = os.path.join(dir_run_test_case, r'tools')
# 把 "test_case" 的绝对路径 加入 sys.path
sys.path.insert(0, dir_test_case)  # 序号从0开始，表示最大优先级
for i in sys.path:
    print(i)

loader = unittest.TestLoader()
# # 收集用例方法：
# case_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tools')
# suite = loader.discover(case_path)  # 收集传入路径下所有以test_开头文件下的所有用例
suite = loader.loadTestsFromName('test_login.TestHttpRequest.test_http_1')  # 收集单条用例:如果执行文件与用例文件不在同一目录，需要把测试用例路径加入sys.path
# suite = loader.loadTestsFromModule(test_login)  # 收集文件/模块中的所有用例
# suite = loader.loadTestsFromTestCase(TestHttpRequest)  # 收集类中的所有用例
print(suite)

now = time.strftime("%Y%m%d-%H%M")
report_path = os.path.join(test_report_path, 'report'+str(now)+'.html')
with open(report_path, "wb")as file:
    runner = HTMLTestRunner.HTMLTestRunner(stream=file, verbosity=2, title="python单元测试报告", description="这是一份测试报告")
    runner.run(suite)

# SendEmail().send_email(report_path)
# '''
# 多个用例同时执行
# 1.写多个模块 不同的模块 就用不同test_http_request   run里面去做加载
# 2.通过配置文件去决定执行哪个模块的用例
# '''
