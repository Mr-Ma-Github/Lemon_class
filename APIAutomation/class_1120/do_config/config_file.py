#-*-coding:utf-8-*-
#@作者：haiyu.ma
#@创建日期：2019-11-28 18:20
# 配置文件：
# properties config ini log4j
# configparser   可以去读取配置信息
import configparser
# 配置文件中有三个区域 section-片段  option  value相当于key:value
# [MODE]
# mode=all
cf=configparser.ConfigParser()
cf.read('case.config',encoding="utf-8")
# 读取配置文件的数据
print(cf.sections())#获取配置文件中所有的片段
print(cf.items('PYTHON11'))
# res_1=cf.get('MODE','mode')
# print(res_1)
#
# res_2=cf['MODE']['mode']
# print(res_2)

#数据类型问题--都是字符串---可以用eavl()转换一下
print(type(cf.get('PYTHON11','num')))
print(type(cf.get('PYTHON11','name')))
print(type(eval(cf.get('PYTHON11','name'))))