#-*-coding:utf-8-*-
#@作者：haiyu.ma
#@创建日期：2019-12-11 23:38
import logging
from API_AUTO.tools.project_path import case_log_path
class MyLog:
    def my_log(self,msg,level):
        my_logger = logging.getLogger("python")# 定义一个日志收集器 my_logger
        my_logger.setLevel("DEBUG")# 设置级别
        # 设置日志输入格式
        formatter = logging.Formatter('%(asctime)s-%(levelname)s-%(filename)s-%(name)s-日志信息:%(message)s')
        # 创建一个输入渠道
        ch = logging.StreamHandler()
        ch.setLevel('ERROR')
        ch.setFormatter(formatter)
        fh = logging.FileHandler(case_log_path, 'a',encoding='utf-8')
        fh.setLevel("DEBUG")
        fh.setFormatter(formatter)
        # 两者对接--指定输出渠道
        my_logger.addHandler(ch)
        my_logger.addHandler(fh)
        # 收集日志
        if level=="DEBUG":
            my_logger.debug(msg)
        elif level=="INFO":
            my_logger.info(msg)
        elif level=="WARNING":
            my_logger.error(msg)
        elif level=="ERROR":
            my_logger.error(msg)
        elif level=="CRITICAL":
            my_logger.critical(msg)
        my_logger.removeHandler(ch)#关闭渠道
        my_logger.removeHandler(fh)
        ch.close()
        fh.close()

    def debug(self,msg):
        self.my_log(msg,'DEBUG')
    def info(self,msg):
        self.my_log(msg,'INFO')
    def error(self,msg):
        self.my_log(msg,'ERROR')
if __name__ == '__main__':
    # MyLog().my_log("stone 今天心情不咋地","ERROR")
    # MyLog().my_log("miracle 明天心情会好的", "ERROR")
    # MyLog().my_log("jkjlsd 明天心情会好的", "ERROR")
    MyLog().debug("发生的开了房间")
    MyLog().info("就水力发电")
    MyLog().error("的分类感觉到了")