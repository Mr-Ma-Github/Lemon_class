#-*-coding:utf-8-*-
#@作者：haiyu.ma
#@创建日期：2019-12-11 18:06
import logging
# 步骤
# 1.logger    日志收集器logger。收集日志：my_logger = logging.getLogger("python")
# 2.level     日志收集器级别：my_logger.setLevel("DEBUG")
# 3.handdler  日志处理器准备，输出日志的渠道  指定的文件或者控制台 （不指定默认输出到控制台）
# console_handler = logging.StreamHandler()
# 4.日志处理器级别设置：console_handler.setLevel("ERROR")
# 5.添加handler：logger.addHandler(console_handler)
# 6.format设置日志格式:formatter = logging.Formatter()
# 7.添加日志处理器: console_handler.setFormatter(formatter)

# 日志级别：
# 1.NOSET    0    等于没写，废话
# 2.debug    1    调试  一些额外信息，备注，往往和主体功能无关。相当于日报里面的备注
# 3.info     2    主体功能的信息。相当于日报（今天做了什么事情）
# 4.warning  3    警告，下次可能要出错了。
# 5.error    4    出错。违法
# 6.critical 5    极其严重。

# 如何定义级别
# 1.级别是自己定义的

# 设置级别
# 当设置成debug的时候，只有高于debug的级别才会打印
# 当设置成warning的时候，只有高于warning的级别才会打印

# logging.debug("小明")
# logging.info("fhsdk")
# logging.warning("灰色空间开发")
# logging.error("发生地方法规")
# logging.critical("发顺丰十大歌手")  # 崩溃

# 定义一个日志收集器
my_logger = logging.getLogger("python")

# 设置级别
my_logger.setLevel("DEBUG")

# 创建一个输出渠道。默认是使用控制台输出
console_handler = logging.StreamHandler()
console_handler.setLevel("ERROR")
# 指定输出渠道，放到一个文件当中
file_handler = logging.FileHandler("case_log.txt", encoding='utf-8')
file_handler.setLevel('WARNING')
# 添加handler 两者对接--指定输出渠道
my_logger.addHandler(console_handler)
my_logger.addHandler(file_handler)

# 设置日志输出格式
formatter = logging.Formatter('%(asctime)s-%(levelname)s-%(filename)s-%(name)s'
                              '-行号:%(lineno)d-日志信息:%(message)s')
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# 收集日志
my_logger.info("python 2019-12-11 logging学习")
my_logger.debug("python 2019-12-11 logging学习")
my_logger.warning("慕拉蓝钻冰白葡萄酒")
my_logger.error("好时：红珍珠-香浓牛奶巧克力")


# 1: logging是什么?作用是什么?
# logging--是Python自带的一个日志模块。
# 作用主要是有两个:
# 1)代替print,可以把大部分你想要进行调试的信息打印出来或者是输出到指定文件
# 2) 可以对一些输出的调试信息分类做输出,比如说:
# DEBUG, INFO, WARNING, ERROR, CRITICAL
# 关于日志的这个级别的定义,大家之后还是需要自己去自行进行拓展!!!一般都是
# 看你对日志的级别定义是怎样就设置为哪个级别的。

