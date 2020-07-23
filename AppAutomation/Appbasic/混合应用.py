#-*-coding:utf-8-*-
#@作者：haiyu.ma
#@创建日期：2020-06-29 22:55

# hybird混合应用自动化方案
# 基于UIAutomator+Chromedriver
# native部分则uiautomator,webview部分走chromedriver,二者结合
# 要求:1.android 4.4+   2.webview必须为debug版本
# 获取webview页面的三种方式:
# 1、chrome://inspect,需要FQ
# 2、使用driver.page_source获取html页面
# 3、找开发人员要源文件
# 4、uc-devtools 不需要FQ
# 常见问题
# contexts只能获取NATIVE_APP,无法获取WEBVIEW
# 使用uiautomatorviewer定位元素, 显示class值为：android.webkit.WebView
# 但是driver.contexts只打印出了：'NATIVE_APP'
# 解决方法:
# 1、app打包的时候需要开启webview的debug属性setWebContentDebuggingEnabled(true)
# 这个直接让开发加上就好;
# 2、模拟器的contexts中有webview,但有些手机没有。
# 官方给出的答案是:需要将手机root,然后再去获取。
# 开启webview可见:
# https://developers.google.com/web/tools/chrome-devtools/remote-debugging/webviews

## appium - native/webview
## native:安卓原生控件
## webview: 网页视图。H5等,就是web页面。

# contexts:上下文切换
# 可用的上下文(Contexts)
# 列出所有可用的上下文(contexts)
# driver.contexts
# driver.window_handles
# 当前上下文(context):列出当前的上下文 (context)
# driver.current context
# 切换至默认的上下文(context)
# 切换回默认的上下文(context). (注:一般就是原生上下文"NATIVE_APP")
# driver.switch to.context(None)
# 当前 Activity:获取当前的 Acticity.仅支持 Android,
# driver.current activity
# 当前包名(package):获取当前包各名(package).仅支持 Android。
# driver.current package

from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as  EC
from appium.webdriver.common.mobileby import MobileBy
from time import sleep

desired_caps = {}
# 平台类型
desired_caps["platformName"] = 'Android'
# 平台版本号
desired_caps["platformVersion"] = '7.1.2'
# 设备名称
desired_caps["deviceName"] = '127.0.0.1:62026'
# app包名
desired_caps["appPackage"] = 'com.cn.xizeng'
# app入口activity
desired_caps["appActivity"] = 'com.cn.xizeng.view.FaceActivity'
# app绝对路径
# desired_caps['app'] = R'C:\Users\haiyu.ma\Downloads\积木分支\duoduohuipin.apk'
desired_caps['app'] = R'C:\Users\haiyu.ma\Downloads\xizeng.apk'
desired_caps['newCommandTimeout'] = 180


# 连接appium server   前提：appium desktop要启动，有监听端口
# 将desired_caps发送给appium server ，打开app
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

loc = 'new UiSelector().text("全程班")'
WebDriverWait(driver,20).until(EC.visibility_of_element_located((MobileBy.ANDROID_UIAUTOMATOR, loc)))
driver.find_element_by_android_uiautomator("loc").click()

# 等待WebView元素出现
WebDriverWait(driver,20).until(EC.visibility_of_element_located((MobileBy.CLASS_NAME, 'Android,webkit,WebView')))
sleep(1)

# 前提：代码可以识别到webview （需要开启app的webview debug属性）
# context    #原生控件   #webview
# 1.先列出所有的context
cons = driver.contexts   #列表
print(cons)
# 2.切换至webview，要确保Chromedriver要与webview的版本匹配。也要放置在对应的位置
driver.switch_to.context(cons[-1])
# 3.切换之后：当前的操作对象-HTML页面。。。uc-devtools工具识别HTML页面，定位元素
# 等待元素可见
WebDriverWait(driver,20).until(EC.visibility_of_element_located((MobileBy.XPATH,'//button[@class="button-btn buy"]')))
driver.find_element_by_xpath('//button[@class="button-btn buy"]').click()

##注意：Chromedrive要支持webview版本(即支持与webview一致的chrome版本)
# 路径C:\Users\haiyu.ma\AppData\Local\Programs\Appium\resources\app\node_modules\appium\node_modules\appium-chromedriver\chromedriver\win