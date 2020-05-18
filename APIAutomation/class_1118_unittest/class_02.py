#-*-coding:utf-8-*-
import unittest
import HTMLTestRunner#写好的模块，可直接调用
from class_1118_unittest.class_01 import TestMathMethod#具体到类名
#收集存储用例
suite=unittest.TestSuite()
# 加载用例
# # 方法一：suite.addTest(测试用例的类名("用例名"))
# suite.addTest(TestMathMethod('test_add_two_zero'))# 只执行一条 两个零相加
# suite.addTest(TestMathMethod('test_add_two_positive'))# 只执行一条 两个正数相加

# 方法二：TestLoader
loader=unittest.TestLoader()#创建一个加载器
suite.addTest(loader.loadTestsFromTestCase(TestMathMethod))#加载类里面的所有用例
# 或者
# loader=unittest.TestLoader()#创建一个加载器
# from class_1118_unittest import class_01#具体到模块
# suite.addTest(loader.loadTestsFromModule(class_01))#加载模块（文件）里面的所有用例

# # 执行用例
# runner=unittest.TextTestRunner()
# runner.run(suite)

# file=open("test.txt","w+",encoding="utf-8")
# runner=unittest.TextTestRunner(stream=file,verbosity=2)#0 1 2 #2执行的结果是最详细的
# runner.run(suite)
# # file.close()
# print(file.closed)#判断文件的状态
# 上下文管理器（当运行完子代码后会自动关闭文件，减少资源占用）
# with open("test.txt","w+",encoding="utf-8")as file:
#     runner=unittest.TextTestRunner(stream=file,verbosity=2)#0 1 2 #2执行的结果是最详细的
#     runner.run(suite)
# print(file.closed)#判断文件的状态

# 执行结果中 . 表示正确，F 表示失败，E 表示代码有问题

# 生成html报告
with open("test_report.html","wb")as file:
    runner=HTMLTestRunner.HTMLTestRunner(stream=file,
                                         verbosity=2,
                                         title="python单元测试报告",
                                         description="这是一份测试报告")
    runner.run(suite)
