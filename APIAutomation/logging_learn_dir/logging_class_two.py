#-*-coding:utf-8-*-
#@作者：haiyu.ma
#@创建日期：2020-09-16 23:42 
import logging
import os
import time


class Log(logging.Logger):

    def __init__(self, name='root', level='DEBUG', file_name=None,
                 fmt='[%(asctime)s]-[%(filename)s]-%(levelname)s:%(message)s'):

        self.logger = logging.getLogger(name)
        super().__init__(name)

        self.setLevel(level)
        formatter = logging.Formatter(fmt)

        if file_name is not None:  # 如果file是None，只输出到控制台，否则既输出控制台又输出到文件
            fh = logging.FileHandler(file_name, 'a', encoding='utf-8')
            fh.setLevel(level)
            fh.setFormatter(formatter)
            self.addHandler(fh)
        ch = logging.StreamHandler()
        ch.setLevel(level)
        ch.setFormatter(formatter)
        self.addHandler(ch)


cur_path = os.path.dirname(os.path.realpath(__file__))
log_path = os.path.join(cur_path, 'logs')  # log_path是存放日志的路径
# if not os.path.exists(log_path):  # 如果不存在这个logs文件夹，就自动创建一个
#     os.mkdir(log_path)
filename = os.path.join(log_path, '%s.log' % time.strftime('%Y_%m_%d'))

logger = Log("PYTHON", file_name=filename)  # 调用时直接调用logger即可
if __name__ == '__main__':
    # from logging_learn_dir.logging_class_two import logger
    logger.debug("第二种log类")