#-*-coding:utf-8-*-
#@作者：haiyu.ma
#@创建日期：2020-05-12 22:24 
# 1.学习知识模块：基础知识、类与对象、单元测试、requests、openpyxl、pandas、re
# ddt、unittest、mysql、logging、
# 2.两个实战：http  考核：webservice
# 3.学习方式：多联系、多尝试
# 4.接口自动化框架梳理：
# ·写接口自动化的大前提：数据与代码分离、数据可配置
# 1.测试用例：Excel
# 2.用例可配置 数据库连接 项目路径 加标的信息-配置文件
# 3.封装功能类--把一个常用的功能写成类。方便调用(提供代码的复用性)
# public、package、Doexcel、domysql、httprequest、testhttprequests、sendemail、mylog、readconfig...
# 4.执行入口：run.py
# 加载测试用例  生成测试报告  发送邮件
# ·用到的技术/框架
# python+unittest+requests+ddt+openpyxl+logging+smtp+Jenkins+mysql


import time
print(time.time())
print(time.strftime("%Y-%m-%d %H:%M:%S"))
print(time.strftime("%Y-%m-%d-%H-%M-%S"))

receivers= ['haiyu.ma@genomicarebio.com', '846683675@qq.com']
df=";".join(receivers)
print(df,type(df))
print(df.split(';'))

a = [1,2,3,4]
print(a[1:3])
