#-*-coding:utf-8-*-
#@作者：haiyu.ma
#@创建日期：2020-06-01 23:04 

# 封装基本函数 -- 执行日志、异常处理、失败截图
# 所有的页面的公共部分
import logging
from Common import logger
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from Common import dir_config


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    # 等待元素可见
    def wait_eleVisible(self, locator, timeout=30, poll_frequency=0.5, doc=""):
        '''
        :param locator:元素定位。元祖类型（元素定位类型，元素定位方式）
        :param times:等待元素的最大时长
        :param poll_frequency:通话之间的睡眠间隔
        :param doc:save_screenshot函数需要的参数-模块名称_页面名称_操作名称
        :return:None
        '''
        timeout = int(timeout)
        logging.info("等待元素{0}可见".format(locator))
        try:
            # 开始等待的时间
            start_time = datetime.now()
            WebDriverWait(self.driver, timeout, poll_frequency).until(EC.visibility_of_element_located(locator))
            # 结束等待的时间
            end_time = datetime.now()
            # 求一个差值、写在日志中、等待了多久
            wait_times = (end_time-start_time).seconds
            logging.info("{0}:元素{1}已可见,等待起始时间:{2},等待结束时间:{3},等待时长为：{4}".
                         format(doc,locator, start_time, end_time, wait_times))
        except:
            logging.exception("等待元素可见失败！！！")
            # 截图
            self.save_screenshots(doc)
            raise

    # 等待元素存在
    def wait_elePresence(self, locator, times=30, poll_frequency=0.5, doc=''):
        '''
        :param locator:元素定位。元祖类型（元素定位类型，元素定位方式）
        :param times:等待元素的最大时长
        :param poll_frequency:通话之间的睡眠间隔
        :param doc:save_screenshot函数需要的参数-模块名称_页面名称_操作名称
        :return:None
        '''
        logging.info("等待元素{0}存在".format(locator))
        try:
            # 开始等待的时间
            start_time = datetime.now()
            WebDriverWait(self.driver, times, poll_frequency).until(EC.presence_of_element_located(locator))
            # 结束等待的时间
            end_time = datetime.now()
            # 求一个差值、写在日志中、等待了多久
            # datetime.strptime(str(starttime), "%Y-%m-%d %H:%M:%S.%f")
            # datetime.strptime(str(endtime), "%Y-%m-%d %H:%M:%S.%f")
            wait_times = (end_time - start_time).seconds
            logging.info("等待结束、等待时长为：{0}".format(wait_times))
        except:
            logging.exception("等待元素存在失败！！！")
            # 截图
            self.save_screenshots(doc)
            raise

    # 查找元素
    def get_element(self, locator, doc=''):
        logging.info("查找元素：{0}".format(locator))
        try:
            return self.driver.find_element(*locator)
        except:
            logging.exception("查找元素失败！！！")
            # 截图
            self.save_screenshots(doc)
            raise

    # 点击操作
    def click_element(self, locator, doc=''):
        # 找元素
        ele = self.driver.find_element(*locator)
        logging.info("点击元素：{0}".format(locator))
        # 点击操作
        try:
            ele.click()
        except:
            logging.exception("元素点击操作失败！！！")
            # 截图
            self.save_screenshots(doc)
            raise

    # 输入操作
    def input_text(self, locator, text, doc=''):
        # 找元素
        ele = self.driver.find_element(*locator)
        logging.info("元素输入：{0}".format(locator))
        # 输入操作
        try:
            ele.send_keys(text)
        except:
            logging.exception("元素输入操作失败！！！")
            # 截图
            self.save_screenshots(doc)
            raise

    # 获取元素的文本内容
    def get_text(self, locator, doc=''):
        # 找元素
        ele = self.driver.find_element(*locator)
        logging.info("获取元素文本：{0}".format(locator))
        try:
            return ele.text
        except:
            logging.exception("获取元素文本失败！！！")
            # 截图
            self.save_screenshots(doc)
            raise

    # 获取元素的属性
    def get_element_attribute(self, locator, attr, doc=''):
        # 找元素
        ele = self.driver.find_element(*locator)
        logging.info("获取元素属性：{0}".format(locator))
        try:
            ele.get_arrtibute(attr)
        except:
            logging.exception("获取元素属性失败！！！")
            # 截图
            self.save_screenshots(doc)
            raise

    # alert处理
    def alert_action(self):
        pass

    # iframe切换
    def switch_iframe(self):
        pass

    # 上传操作
    def upload_file(self):
        pass

    # 滚动条处理

    # 窗口切换

    # 截图操作
    def save_screenshots(self, doc):
        # 图片名称：模块名称_页面名称_操作名称_时间(年月日时分秒).png
        # file_path = 指图片保存目录/model(页面功能名称)_当前时间到秒.png
        file_path = dir_config.screenshot_path + "/{0}_{1}.png".format(doc, (time.strftime("%Y-%m-%d %H:%M:%S.%f", time.localtime())))
        # print(file_path)
        # 截图文件存放在screenshots目录下
        # driver方法：self.driver.save_screenshot()
        try:
            self.driver.save_screenshot(file_path)
            logging.info("截取网页成功，文件路径为：{0}".format(file_path))
        except:
            logging.exception("截图失败")
