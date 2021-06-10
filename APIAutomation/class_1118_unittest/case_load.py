#-*-coding:utf-8-*-

"""
收集存储用例: TestLoader
放到测试集合(测试套件): TestSuite

1.初始化加载器：testloader
loader = unittest.TestLoader()
2.查找测试用例：使用testloader.discover(文件夹路径, "demo_*.py")
"demo_*.py"：表示收集以demo_开头的文件。不传表示默认：test_
suite = loader.discover(case_path)
3.TestRunner:
    1.运行用例
    2.生成测试报告
"""

# import unittest
# import os
# import HTMLTestRunner
# # 1.初始化加载器：testloader
# loader = unittest.TestLoader()
# # 2.查找测试用例，加载
# case_path = os.path.dirname(os.path.abspath(__file__))
# suite = loader.discover(case_path)  # 以文件执行
# print(suite)
# # 3.1 执行收集的测试用例
# # runner=unittest.TextTestRunner()
# # runner.run(suite)
# # 3.2 执行收集的测试用例并生成文本测试报告
# # with open("test_report_2.txt", "w+", encoding="utf-8")as file:
# #     # 初始化运行器，是以普通文本生成测试报告TextTestRunner
# #     runner = unittest.TextTestRunner(file, verbosity=2)#0 1 2 #2执行的结果是最详细的
# #     # 运行测试用例
# #     runner.run(suite)
# # 3.3 执行收集的测试用例并生成html报告
# with open("test_report_2.html", "wb")as file:
#     runner = HTMLTestRunner.HTMLTestRunner(stream=file,
#                                            verbosity=2,
#                                            title="python单元测试报告",
#                                            description="这是一份测试报告")
#     runner.run(suite)

# --------------------------------------------------------------------------------------
import unittest
from HTMLTestRunner import HTMLTestRunner  # 导入HTMLTestRunner模块中的HTMLTestRunner类
from class_1118_unittest.test_class_mathod import TestMathMethod  # 具体到类名
from class_1118_unittest import test_class_mathod, test_login_class  # 具体到模块
import os
import time
from datetime import datetime


# # 方法一：加载单条用例，不用创建类加载器
# 收集存储用例
# suite = unittest.TestSuite()
# # suite.addTest(测试用例的类名("用例名"))
# suite.addTest(TestMathMethod('test_add_two_zero'))# 只执行一条 两个零相加
# suite.addTest(TestMathMethod('test_add_two_positive'))# 只执行一条 两个正数相加
# 或者：
# loader = unittest.TestLoader()  # 创建一个加载器
# suite = loader.loadTestsFromName('test_add_two_zero')
# suite = loader.loadTestsFromName('test_class_mathod.TestMathMethod.test_add_two_zero')
# print(suite)

# # 方法二：# 加载类里面的所有用例（添加指定的测试类）
# loader = unittest.TestLoader()  # 创建一个加载器
# suite = loader.loadTestsFromTestCase(TestMathMethod)  # 加载类里面的所有用例

# # 方法三：加载模块（文件）里面的所有用例
loader = unittest.TestLoader()  # 创建一个加载器
suite = loader.loadTestsFromModule(test_class_mathod)  # 加载模块（文件）里面的所有用例
suite2 = loader.loadTestsFromModule(test_login_class)
# 注意加载两个模块当中的测试用例，保存到测试套件中(可以用for循环，但是不建议)
# 正确：将这两个测试套件合并并添加到一个总的测试套件中
suite_total = unittest.TestSuite()
suite_total.addTests(suite)
suite_total.addTests(suite2)

# # 方法一：执行用例
# runner = unittest.TextTestRunner()
# runner.run(suite)

# # 方法二：执行用例并把结果写入到文本文件中（由于这种方式打开文件后还要关闭，所以采用with open）
# file = open("test.txt","w+",encoding="utf-8")
# runner = unittest.TextTestRunner(stream=file,verbosity=2)#0 1 2 #2执行的结果是最详细的
# runner.run(suite)
# file.close()
# print(file.closed)#判断文件的状态
# # 上下文管理器（当运行完子代码后会自动关闭文件，减少资源占用）
# with open("test.txt", "w+",encoding="utf-8")as file:
#     runner = unittest.TextTestRunner(stream=file, verbosity=2)#0 1 2 #2执行的结果是最详细的
#     runner.run(suite)
# # print(file.closed)#判断文件的状态

# 文件路径处理+文件名称处理（+时间戳）
file_path = os.path.dirname(os.path.abspath(__file__))
if not os.path.exists(file_path):  # 创建目录
    os.mkdir(file_path)
# 格式：先转换成整数（舍弃小数），再转换成字符串（用来拼接）
# 方式一：
ts = str(int(time.time()))
# 方式二：
# ts = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
file_name = "test_report_{}.html".format(ts)
report_path = os.path.join(file_path, file_name)
# print(report_path)

# 生成html报告
# 因为html采用二进制进行数据传送，所以要使用二进制的方式打开：wb
with open(report_path, "wb")as file:
    # 使用HTMLTestRunner
    runner = HTMLTestRunner(stream=file,
                            verbosity=2,
                            title="python单元测试报告",
                            description="这是一份测试报告")
    runner.run(suite_total)

# HTMLTestRunner，不是unittest自带的，需要自己去安装
# 1. 安装方式不是pip
# 2. 是别人写好的一个模块，你可以直接下载下来  .py
# 3.1 复制到项目目录下，然后直接导入即可
# 3.2 放到python的公共库当中：site-packages下即可

# 执行结果中 . 表示正确，F 表示失败，E 表示代码有问题

# 几种加载用例的方式：
# 1.用的最多，整个项目一起加载，使用：discover
# 2.你想只测试某一个具体的模块、功能，使用loadTestsFromModule、loadTestsFromTestCase
# 3.pytest