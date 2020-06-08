#-*-coding:utf-8-*-
#@作者：haiyu.ma
#@创建日期：2019-12-11 18:06
import logging

# logger    收集日志
# handdler  输出日志的渠道  指定的文件  或者控制台 （不指定默认输出到控制台）

# logging.debug("小明")
# logging.info("fhsdk")
# logging.warning("灰色空间开发")
# logging.error("发生地方法规")
# logging.critical("发顺丰十大歌手")

# 定义一个日志收集器 my_logger
my_logger=logging.getLogger("python")

# 设置级别e
my_logger.setLevel("DEBUG")
# 设置日志输入格式
formatter=logging.Formatter('%(asctime)s-%(levelname)s-%(filename)s-%(name)s-日志信息:%(message)s')

# 创建一个输入渠道
ch=logging.StreamHandler()
ch.setLevel('ERROR')
ch.setFormatter(formatter)

fh=logging.FileHandler("case_log.txt",encoding='utf-8')
fh.setLevel("DEBUG")
fh.setFormatter(formatter)
# 两者对接--指定输出渠道
my_logger.addHandler(ch)
my_logger.addHandler(fh)
# 收集日志
my_logger.debug("python 2019-12-11 logging学习")
# my_logger.warning("慕拉蓝钻冰白葡萄酒")
my_logger.error("好时：红珍珠-香浓牛奶巧克力")


# 1: logging是什么?作用是什么?
# logging--是Python自带的一个日志模块。
# 作用主要是有两个:
# 1)代替print,可以把大部分你想要进行调试的信息打印出来或者是输出到指定文件
# 2) 可以对一些输出的调试信息分类做输出,比如说:
# DEBUG, INFO, WARNING, ERROR, CRITICAL
# 关于日志的这个级别的定义,大家之后还是需要自己去自行进行拓展!!!一般都是
# 看你对日志的级别定义是怎样就设置为哪个级别的。

