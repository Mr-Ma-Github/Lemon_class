#-*-coding:utf-8-*-
# #没有结合Excel的用例传参方法
# import unittest
# import HTMLTestRunner
# from class_1120.test_http import TestHttpRequest
# test_data=[{"url":"http://119.23.241.154:8080/futureloan/mvc/api/member/login",
#             "data":{"mobilephone": "18688773467", "pwd": "123456"}, "excepted": "10001", "method": "get"},
#            {"url": "http://119.23.241.154:8080/futureloan/mvc/api/member/login",
#             "data":{"mobilephone": "18688773467", "pwd": "325"}, "excepted": "20111", "method": "post"},
#            {"url": "http://119.23.241.154:8080/futureloan/mvc/api/member/recharge",
#             "data":{"mobilephone": "18688773467", "amount": "1000"}, "excepted": "10001", "method": "get"},
#            {"url": "http://119.23.241.154:8080/futureloan/mvc/api/member/recharge",
#             "data":{"mobilephone": "18688773467", "amount": "-100"}, "excepted": "20117", "method": "get"}]
# 收集存储用例
# suite=unittest.TestSuite()

# 加载用例
# suite.addTest(TestHttpRequest("test_api",test_data[0]["url"],test_data[0]["data"],test_data[0]["method"],test_data[0]["excepted"]))
# # for item in test_data:#创建实例
# #     suite.addTest(TestHttpRequest("test_api",item["url"], item["data"], item["method"], item["excepted"]))
# # 以实例的方法加载储存用例url  data  method  excepted

#执行用例
# with open("test_report.html", "wb")as file:
#     runner = HTMLTestRunner.HTMLTestRunner(stream=file,verbosity=2,title="python单元测试报告",description="这是一份测试报告")
#     runner.run(suite)

# ---------------------------------------------------------------------------------------------------------
# #结合Excel的方法一：
import unittest
import HTMLTestRunner
from class_1120.test_http import TestHttpRequest
from class_1120.do_excel import DoExcel

test_data=DoExcel("Excel_study.xlsx","python").get_data()

# 存收集储用例
suite=unittest.TestSuite()
# 加载用例
for item in test_data:
    suite.addTest(TestHttpRequest("test_api",item["method"],item["url"],
                  eval(item["data"]),str(item["excepted"])))#要按照传参顺序
# 以实例的方法加载储存用例url  data  method  excepted

# 执行用例
with open("test_report.html", "wb")as file:
    runner = HTMLTestRunner.HTMLTestRunner(stream=file,verbosity=2,title="python单元测试报告",description="这是一份测试报告")
    runner.run(suite)