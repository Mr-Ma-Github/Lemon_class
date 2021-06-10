# -*-coding:utf-8-*-
# @作者：haiyu.ma
# @创建日期：2019-12-08 22:26
import configparser


class ReadConfig:
    @staticmethod
    def get_config(file_path, section, option):
        cf = configparser.ConfigParser()
        cf.read(file_path)
        return cf[section][option]


if __name__ == '__main__':
    from GC_API.tools.project_path import case_config_path
    print(ReadConfig.get_config(case_config_path, 'MODE', 'mode'))
