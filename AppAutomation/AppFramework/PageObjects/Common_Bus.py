#-*-coding:utf-8-*-
#@作者：haiyu.ma
#@创建日期：2020-07-05 22:23 
from Common.basepage import BasePage
import time
from PageLocators.login_locators import LoginLocator as loc


# 欢迎页面
class ComonBus(BasePage):
    # 处理欢迎页面
    def do_welcome(self):
        time.sleep(7 )
        # 如果没有找到首页的元素或者不包含main_activity，那么就是在欢迎页面
        curAcr = self.driver.current_activity
        if curAcr.find("MainActivity") == -1:
            # 滑动欢迎页面至首页
            # 左滑三次，点击立即体检
            for i in range(3):
                self.swipe_left(self.get_size())
                time.sleep(1)
            # 点击立即体检
            BasePage(self.driver).click_element(loc.experience)

# 导航栏

# 是否设置手势密码(弹窗)
    def is_setGesture(self, action=False):
        #首先判断有没有设置手势密码的弹窗   --5秒
        # 如果有，是设置还是不设置
        if action == False:
            pass#点击不设置
        else:
            pass#点击立即设置
