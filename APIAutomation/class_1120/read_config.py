#-*-coding:utf-8-*-
#@作者：haiyu.ma
#@创建日期：2019-11-29 14:37
import configparser
class ReadConfig:
    def read_config(self,file_name,section,option):
        cf=configparser.ConfigParser()
        cf.read(file_name,encoding="utf-8")
        return cf.get(section,option)

if __name__ == '__main__':
    res=ReadConfig().read_config('case.config','MODE','mode')
    print(res)