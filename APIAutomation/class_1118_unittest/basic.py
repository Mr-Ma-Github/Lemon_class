# -*-coding:utf-8-*-
# @作者：haiyu.ma
# @创建日期：2021-04-07 22:48 
# @Software：PyCharm
# ----------------------------------------------------------------------------
# 接口测试的本质  就是测试类里面的函数
# 单元测试的本质  测试函数  代码级别
# 单元测试的框架  unittest+接口   pytest+web--》接口
# python+Jenkins+allure

# 功能测试
# 1.写用例     TestCase
# 2.执行用例1.TestSuite 储存用例2.TestLoader 找用例，加载用例，存到1的TestSuite
# 3.对比测试结果，判定是否通过  #断言：Assert
# 4.出具测试报告  TextTestRunner

# 注意书写规范：
# 1.模块名称以test开头
# 2.类以Test开头
# 3.测试用例以test开头

# unittest运行方式：
# 1.鼠标右击：出现unittest
# 如果没有出现，那么要配置：run->Edit Configurations...
# 2.使用python去运行，前提是文件中要写入下方代码
# if __name__ == '__main__':
    # unittest.main()  # 加载所有用例
# 3.python -m unittest 文件名

# 用例执行顺序
# 根据ASCII编码排序
# 123456789....
# abcdefghighlmn....这种方法用例会根据函数名的开头字母顺序执行

# pycharm注意事项：
# 1. 在空行上右击运行，执行整个模块
# 2. 在类名上右击运行，执行当个测试类
# 3. 在方法名上右击运行，执行单个测试用例
# tips：注意要在空行的地方去运行

# 解决在cmd中运行报找不到模块的方法
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
print(curPath,rootPath)
