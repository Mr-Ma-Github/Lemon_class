#-*-coding:utf-8-*-
#@作者：haiyu.ma
#@创建日期：2020-07-05 23:27 
# Yaml
# YAML 是一种简洁的非标记语言。
# YAML以数据为中心,使用空白,缩进,分行组织数据,从而使得表示更加简洁易懂
# 基本规则:
# 1、大小写敏感
# 2、使用缩进表示层级关系
# 3、禁止使用tab缩进,只能使用空格
# 4、缩进长度没有限制,只要元素对齐就表示这些元素属于一个层级。
# 5、使用#表示注释
# 6、字符串可以不用引号标注

# 三种数据结构:
# 1、字典
# 使用冒号(: )表示键值对,同一缩进的所有键值对属于一个map
# #Yaml 方式一(注意冒号后的空格)
# platformName: Android
# platformVersion: 5.1
# #Yaml 方式二
# {platformName:Android,platformVersion:5.1}
# 2、列表
# 使用连字符(-)表示,注意-后的空格
# - hello
# - world
# #方式二
# [hello,world,12,13]
# 3、scalar,纯量

# python库:
# 1.PyYAML
# 2.ruamel.yaml
# PyYAML安装:
# pip命令: pip install PyYaml
# 引入: import yaml
# 读取yaml文件的数据,并转换成python对象
# 1、打开yaml文件
# 2、使用yaml的load()函数
# 示例代码:
# fs = open(os.path.join(caps_dir,"caps.yaml"))
# datas = yaml.load(fs)

