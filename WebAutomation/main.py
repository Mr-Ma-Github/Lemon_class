#-*-coding:utf-8-*-
#@作者：haiyu.ma
#@创建日期：2020-06-03 23:10 

import unittest
# from HTMLTestRunnerNew import HTMLTestRunner
from HTMLTestRunner import HTMLTestRunner
from Common. dir_config import *

#实例化套件对象
s = unittest.TestSuite()
# s = unittest.TestSuite().addTests(unittest.TestLoader().discover(testcases_dir))
#TestLoader的用法
#TestLoader的用法
# 1、实例化TestLoader对象
# 2、使用discover去找到一个目录下的所有测试用例
# 3、使用s
loader = unittest.TestLoader()
s.addTests(loader.discover(testcases_dir))
# #运行
# runner = unittest.TextTestRunner ()
# runner.run (s)
fp = open(htmlreport_dir +'/autoTest_report.html', 'wb')
runner = HTMLTestRunner(
                stream = fp,
                verbosity=2,
                title='单元测试报告',
                description='单元测试报告',
                # tester="小马"
                )
runner.run(s)