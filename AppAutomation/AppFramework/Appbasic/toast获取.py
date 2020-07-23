#-*-coding:utf-8-*-
#@作者：haiyu.ma
#@创建日期：2020-06-28 22:30 
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as  EC
from appium.webdriver.common.mobileby import MobileBy

desired_caps = {}
# 自动化测试引擎
# desired_caps["automationName"] = 'UiAutomator2'
# 平台类型
desired_caps["platformName"] = 'Android'
# 平台版本号
desired_caps["platformVersion"] = '7.1.2'
# 设备名称
desired_caps["deviceName"] = '127.0.0.1:62026'
# app包名
# desired_caps["appPackage"] = 'com.oyf.rryp'
desired_caps["appPackage"] = 'com.cn.xizeng'
# app入口activity
# desired_caps["appActivity"] = 'com.oyf.rryp.SplashActivity'
desired_caps["appActivity"] = 'com.cn.xizeng.view.FaceActivity'
# app绝对路径
# desired_caps['app'] = R'C:\Users\haiyu.ma\Downloads\积木分支\duoduohuipin.apk'
desired_caps['app'] = R'C:\Users\haiyu.ma\Downloads\xizeng.apk'
desired_caps['newCommandTimeout']= 180


# 连接appium server   前提：appium desktop要启动，有监听端口
# 将desired_caps发送给appium server ，打开app
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
# 什么都不输，点击登录（显示的提示信息）
# WebDriverWait(driver,20).until(EC.visibility_of_element_located((MobileBy.ID,'')))
# driver.find_element_by_id('').click()

# Toast提示信息获取
# 要获取toast信息要满足以下两个要求:
# 1.appium server版本1.6.3+才支持toast获取
# (而appium server 1.6.3没有可视化界面,解决方案:下载appium-desktop-Setup-1.4.1-ia32.exe)
# 2.代码中必须指定automationName为: UIAutomator2
# 3.UIAutomator2只支持安卓版本5.0+
# 因此夜神模拟器,海马王都用不了,因为他们的最高支持安卓版本为4.4.2,可以使用genymotion
# 4、要求安装jdk1.8 64位及以上。配置其环境变量JAVA_HOME和path
# toast注意事项
# 配置toast请注意:
# 1, desired_caps[("automationName"] = "UiAutomator2"
# 2、要求安装jdk1.8 64位及以上。配置其环境变量JAVA_HOME和path
# 3、Android系统5.0以上
# 4、appium server版本 1.6.3以上
# xpath表达式:
# xpath = '//*[contains(@text,"部分文本内容")]'
# 注意:
# driverWait方法中，请用presence_of_element_located
# 不要用visibility_of_element_located,对toast的可见处理并不支持,会直接报错命令无法执行

# 1.xpath表达式  --文本匹配
loc = '//*[contains(@text,"{}")]'.format("手机号码或密码")
# 等待的时候，要用元素存在的条件。不能用元素可见的条件
try:
    WebDriverWait(driver,10,0.01).until(EC.presence_of_element_located((MobileBy.XPATH,loc)))
    print(driver.find_element_by_xpath(loc).text)
except:
    print("没有找到匹配的toast！")