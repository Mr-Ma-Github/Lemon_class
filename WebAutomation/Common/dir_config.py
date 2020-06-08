#-*-coding:utf-8-*-
#@作者：haiyu.ma
#@创建日期：2019-12-08 14:21
import os

# 框架项目顶层目录
base_dir = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
# print(project_path)

testdatas_dir = os.path.join(base_dir, "TestDatas")

testcases_dir = os.path.join(base_dir, "TestCases")

htmlreport_dir = os.path.join(base_dir, "Outputs", "reports")

logs_dir = os.path.join(base_dir, "Outputs", "logs")
# print(logs_dir+'\mylog.txt')

# 截屏文件的路径
screenshot_path=os.path.join(base_dir,"Outputs","screenshots")
# print(screenshot_path+"\{0}_{1}.png".format("登录页面_登录功能","2020-06-02"))
