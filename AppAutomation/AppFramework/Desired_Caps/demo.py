#-*-coding:utf-8-*-
#@作者：haiyu.ma
#@创建日期：2020-07-05 23:26 
import yaml

# 1.打开yaml文件
fs = open("demo.yaml")
# 2.转换成python对象
# yaml.load(fs)
res = yaml.load(fs, Loader=yaml.FullLoader)
print(res)