#-*-coding:utf-8-*-
#@作者：haiyu.ma
#@创建日期：2019-12-08 14:21
import os
# 专门来获取路径的值
project_path=os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
# print(project_path)
# 测试用例的路径
test_case_path=os.path.join(project_path,"test_data","test_data.xlsx")
# print(test_case_path)
# 测试报告的路径
test_report_path=os.path.join(project_path,"test_result","html_report","test_report.html")
# print(test_case_path)
case_config_path=os.path.join(project_path,"conf","case.config")
# print(case_config_path)
case_log_path=os.path.join(project_path,"test_result","log","test_log.txt")
# print(case_log_path)