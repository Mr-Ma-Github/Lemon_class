#-*-coding:utf-8-*-
# #结合Excel的方法二：
import unittest
import HTMLTestRunner
from class_1120.test_http import TestHttpRequest
from class_1120.do_excel2 import DoExcel

t=DoExcel("Excel_study.xlsx","python")
suite=unittest.TestSuite()  # 存储用例
for i in range(1,t.max_row+1):
    suite.addTest(TestHttpRequest("test_api",t.get_data(i,1),t.get_data(i,2),
                                  eval(t.get_data(i,3)),str(t.get_data(i,4))))
# 以实例的方法加载储存用例url  data  method  excepted

with open("test_report.html", "wb")as file:
    runner = HTMLTestRunner.HTMLTestRunner(stream=file,verbosity=2,title="python单元测试报告",description="这是一份测试报告")
    runner.run(suite)


