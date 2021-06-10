# -*-coding:utf-8-*-
# @作者：haiyu.ma
# @创建日期：2021-04-09 10:02 
# @Software：PyCharm
# ----------------------------------------------------------------------------
'''
python：unittest之discover()
方法批量执行用例
自动化测试过程中，自动化覆盖的功能点和对应测试用例之间的关系基本都是1 VS N，如果每次将测试用例一个个单独执行，不仅效率很低，
无法快速反馈测试结果，而且维护起来很麻烦。在python的单元测试框架unittest中，提供了批量执行的测试用例的方法。
这篇博客，介绍下unittest框架的常用类和方法，以及利用discover()方法批量执行测试用例的方法。。。

官方文档：unittest单元测试框架
一、unittest框架
首先介绍一下unittest框架和执行测试用例相关的几个模块：
1、TestCase()类
TestCase类的实例表示unittest中的逻辑测试单元，此类旨在用作基类，具体测试由具体的子类实现。该类实现了测试运行器所需的接口，
以允许它驱动测试，以及测试代码可用于检查和报告各种故障的方法。每个实例都将运行unittest的一个名为methodName的基本方法。
2、setUp()方法
该方法的主要作用是用来初始化测试环境，它在测试用例执行之前立即调用，除了AssertionError或SkipTest，通过该方法产生的任何异
常都将被认为是错误的。只有测试成功执行，才会被调用，默认什么都不做。
3、tearDown()方法
该方法的主要作用是在测试用例执行完毕后记录测试结果并恢复测试环境，即使出现异常，也会调用此方法。
4、run()方法
该方法的作用是运行测试用例，将测试结果收集到TestResult中作为传递的对象。
如果省略结果或者用None创建临时结果对象（通过调用defaultTestResult()方法），结果对象会返回给run()的调用者。
5、defaultTestResult()方法
该方法返回应该用于此测试用例类的测试结果作为实例（如果没有其他结果，实例应返回给run()方法）。
6、TestSuite()类
该类代表单个测试用例和测试套件的集合。它提供了运行测试所需的接口以使其可以像其他测试一样运行。TestSuite实例和遍历套件相同，单独运行每个测试用例。
TestSuite的行为和TestCase非常相似，但它并未实际执行测试，而是用于将测试用例聚合到一起，下面的2个方法用于向TestSuite实例中添加测试用例：
addTest()：添加测试用例到TestCase或TestSuite套件中；
addTests()：将迭代TestCase和TestSuite实例中的所有测试用例添加到此测试组件，相当于调用addTest()
的每个元素。
7、TestLoader()类
所述TestLoader类被用来创建类和模块的测试套件。通常不需要创建该类的实例。unittest框架提供了一个可以共享的实例unittest.defaultTestLoader。
8、discover()方法
discover（start_dir, pattern = 'test *.py', top_level_dir = None ）
start_dir：要测试的模块名或测试用例目录；
pattern = 'test*.py'：表示用例文件名的匹配原则，下面的例子中匹配文件名为以“test”开头的“.py”文件，
星号“ * ”表示任意多个字符；
top_level_dir = None：测试模块的顶层目录，如果没有顶层目录，默认为None；
该方法通过从指定的开始目录递归到子目录中查找所有测试模块，并返回包含它们的TestSuite对象，只有与模式匹配测试文件和
可导入的模块名称才会被加载。
所有测试模块必须可以从项目的顶层导入，如果起始目录不是顶层目录，则顶层目录必须单独指定。
如果一个测试文件的名称符合pattern，将检查该文件是否包含load_tests()函数，如果load_tests()函数存在，
则由该函数负责加载本文件中的测试用例。
如果不存在，就会执行loadTestsFromModule()，查找该文件中派生自TestCase的类包含的test开头的方法。
9、TestResult()类
该类用于记录哪些测试成功或失败的信息。一个TestResult对象存储一组测试的结果, 在TestCase和TestSuite中保证结果正确记录。
测试框架unittest需要访问TestResult作为报告目的运行一组测试所生成的对象，为此目的TestResult和TestRunner.run()
方法返回一个实例 。

二、addTest()实例
举个例子来说，如果测试用例有下面这些：
使用addTest()方法执行测试用例，示例代码如下：
# coding=utf-8
import unittest

# 加载测试用例
import test_user
import test_mobile
import test_mobcode
import test_txtcode
import test_pwd
import test_signup
import test_login
import test_vipcenter
import test_search

# 将测试用例添加到测试集合
suite = unittest.TestSuite()
suite.addTest(test_user.UserTest("test_user"))  # 用户名
suite.addTest(test_mobile.MobileTest("test_mobile"))  # 手机号码
suite.addTest(test_mobcode.MobCodeTest("test_mobcode"))  # 手机验证码
suite.addTest(test_txtcode.TxtCodeTest("test_txtcode"))  # 图形验证码
suite.addTest(test_pwd.PasswordTest("test_pwd"))  # 密码
suite.addTest(test_signup.SignUpTest("test_signup"))  # 注册功能
suite.addTest(test_login.LoginTest("test_loggin"))  # 登录功能
suite.addTest(test_vipcenter.VipTest("test_vip"))  # 会员中心
suite.addTest(test_search.SearchTest("test_search"))  # 搜索功能

# 运行测试用例
runner = unittest.TextTestRunner()
runner.run(suite)
Ps:可以看出需要进行很多的用例导入和添加操作，如果用例成百上千条，那么这将是一场灾难！！！

三、discover()使用实例
还是上面的那些测试用例，这次使用discover()方法批量执行用例，示例代码如下：
# coding=utf-8
import unittest
from unittest import defaultTestLoader

# 测试用例存放路径
case_path = './Testcase/case'

# 获取所有测试用例
def get_allcase():
    discover = unittest.defaultTestLoader.discover(case_path, pattern="test*.py")
    suite = unittest.TestSuite()
    suite.addTest(discover)
    return suite


if __name__ == '__main__':
    # 运行测试用例
    runner = unittest.TextTestRunner()
    runner.run(get_allcase())

相比于addTest()方法，discover()方法更方便高效，也可以提高测试反馈速率。
PS：使用discover()方法，切记测试用例中需要执行的测试方法必须以test开头，否则无法加载！！！
'''


