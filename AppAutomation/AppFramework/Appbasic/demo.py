#-*-coding:utf-8-*-
#@作者：haiyu.ma
#@创建日期：2020-06-15 23:05
# Android 自动化环境搭建
# 需要安装的软件如下:
# 1. Node.js
# Appium server 的运行环境
# 2. Appium server
# 两种安装方式:
# 1)通过 Nmp 命令来安装。
# 命令: npm install -g appium
# 等待命令执行完成即可。
# 2)安装 appium desktop 版本。
# 在官方网站中下载最新的 appium desktop 版本。
# 对应安装包下载地址:
# https://github.com/appium/appium-desktop/releases
# 3、Jdk1.8 64位及以上版本
# 4. Android sdk
# 下载 Android ADT 工具。并解压即可。
# 配置环境变量:
# 1)添加ANDROID_HOME 环境变量,配置 sdk 根目录。
# ANDROID_HOME=android-sdk的安装路径
# 2)在PATH 变量中添加 adb 所有的目录:
# ;%ANDROID_HOME%\platform-tools;%ANDROID_HOME%\tools
# 检测:进入 cmd 命令行,输入 adb version
# 能够正常显示 adb 的版本就 okay.
# 5、模拟器、真机
# 安卓模拟器是能在 PC 平台模拟安卓手机系统的模拟器软件
# 比较常用的安卓模拟器有:夜神、海马、逍遥、genymotic
# 1)夜神模拟器:
# 去官方网站下载夜神模拟器,windows 平台双击安装。
# 地址：https://www.yeshen.com
# 2更换 adb.exe:
# 拷贝 ADT 目录下的 adb,重命名为 nox_adb.exe
# 使用命令 adb devices 找不到夜神模拟器
# 一、先检测夜神模拟器是否已经打开，不打开显然是无法测试到的。
# 二、如果夜神模拟器已经打开，但是使用adb devices依旧找不到设备，这就有好戏上演了
# 三、将SDK\platform-tools下的adb.exe文件，替换成夜神模拟器bin目录下的adb.exe。
# 四、将SDK\platform-tools下的adb.exe，copy出来重命名为nox_adb.exe，替换成夜神模拟器bin目录下的 nox_adb.exe
# 6.安装Appium Python Client 包
# 安装Appium Python Client 包的命令：
# pip install Appium-Python-Client
# 7.开启虚拟机USB调试：关于--版本点5下--打开USB调试
# 8.获取apk包appPackage、appActivity的命令：aapt dump badging + 路径+apk包名
# 获取应用包名和入口activity: aapt命令
# aapt目录:安卓sdk的build-tools目录下
# 示例:adt-bundle-windows-x86_64-20140702\sdk\build-tools\android-4.4W
# 命令语法:
# aapt dump badging apk 应用名
# 示例:aapt dump badging D:\BaiduNetdiskDownload\Future-release-2018.apk

from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as  EC
from appium.webdriver.common.mobileby import MobileBy

desired_caps = {}
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

# print(desired_caps)

#运行代码之前：
# 1.appium server启动成功，处于监听状态
# 2.模拟器/真机必须能够被电脑识别，即adb devices能够识别到要操作的设备

# appium - app页面元素定位
# 1. 通过id定位元素: resrouce-id
# 2. 通过ClassName定位: classname
# 3. 通过Accessibilityld定位: content-desc
# 4. 通过AndroidUiAutomator定位
# 5. 通过xpath定位
# xpath,id,class,accessibility id, -android uiautomator
# id
# driver.find_element_by_id('')
# # class
# driver.find_elements_by_class_name('')
# # content-desc
# driver.find_elements_by_accessibility_id('')

# # uiautomator
# AndroidUiAutomator定位
# 使用UiAutomator中的UiSelector类来处理元素定位。
# 在python客户端appium库中通过,uiautomator来获取元素的方法为:
# driver.find_elements_by_android_uiautomator()
# 该方法的参数为UiSelector类定位元素的表达式:
# new UiSelector().函数名称("定位表达式")
# 实例化一个UiSelector对象,然后通过实例调用接口。
# 示例:
# driver.find_elements_by_android_uiautomator(
# 'new UiSelector().resourceld("com.xxzb.fenwoo:id/btn_login")')

# driver.find_element_by_android_uiautomator('')
# WebDriverWait(driver,20).until(EC.visibility_of_element_located((MobileBy.ID,'')))
# driver.find_element_by_id('').click()