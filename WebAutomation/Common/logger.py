# -*-coding:utf-8-*-
# @作者：haiyu.ma
# @创建日期：2020-06-05 0:25
# 使用默认的日志收集器RootLogger，输出日志（默认输出WARN级别以上的日志）
import logging
from logging.handlers import RotatingFileHandler
import time
from Common import dir_config

fmt = "%(asctime)s %(levelname)s %(filename)s " \
      "%(funcName)s [line:%(lineno)s %(levelname)s 日志信息:%(message)s]"

datefmt = "%a, %d %b %Y %H:%M:%S"

handler_1 = logging.StreamHandler()

curTime = time.strftime("%Y-%m&ndash;%d %H%M", time.localtime())

handler_2 = RotatingFileHandler(dir_config.logs_dir+"/Web_Autotest_{0}.log".format(curTime), backupCount=10,encoding='utf-8')
#设置rootlogger 的输出内容形式,输出渠道
logging.basicConfig(format=fmt,datefmt=datefmt, level=logging.INFO, handlers=[handler_1,handler_2])

logging.info("hehehe")

