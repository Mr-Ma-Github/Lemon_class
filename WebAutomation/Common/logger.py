#-*-coding:utf-8-*-
#@作者：haiyu.ma
#@创建日期：2020-06-05 0:25 
import logging
from Common import dir_config

# logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(level=logging.INFO,filename=dir_config.logs_dir+'\mylog.txt',
                    format='%(asctime)s %(filename)s[line:%(lineno)s %(levelname)s %(message)s]')

logging.info("***登录用例：正常场景：使用正确的用户名和密码登录*****")