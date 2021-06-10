#-*-coding:utf-8-*-
#@作者：haiyu.ma
#@创建日期：2020-09-16 15:13
# encoding=utf-8
import logging


class Log:  # 缺点：如果打印行号，那么打印的是被调用方法定义时的行号，而不是调用时的行号
    def __init__(self,name='root',level='DEBUG',file_name=None,
                 fmt='[%(asctime)s]-[%(filename)s]-%(levelname)s:%(message)s'):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        formatter = logging.Formatter(fmt)

        if file_name is not None:  # 如果file是None，只输出到控制台，否则既输出控制台又输出到文件
            fh = logging.FileHandler(file_name, 'a', encoding='utf-8')
            fh.setLevel(level)
            fh.setFormatter(formatter)
            self.logger.addHandler(fh)
        ch = logging.StreamHandler()
        ch.setLevel(level)
        ch.setFormatter(formatter)
        self.logger.addHandler(ch)

    def debug(self, message):
        return self.logger.debug(message)

    def info(self, message):
        return self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        return self.logger.error(message)


if __name__ == '__main__':
    Log().debug("愤怒的小狗")

    # import os , time
    # cur_path = os.path.dirname(os.path.realpath(__file__))
    # log_path = os.path.join(cur_path, 'logs')  # log_path是存放日志的路径
    # # if not os.path.exists(log_path):  # 如果不存在这个logs文件夹，就自动创建一个
    # #     os.mkdir(log_path)
    # file_name = os.path.join(log_path, '%s.log' % time.strftime('%Y_%m_%d'))
    # Log(file_name=file_name).debug("愤怒的小猥琐")
