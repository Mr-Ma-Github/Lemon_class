#-*-coding:utf-8-*-
#@作者：haiyu.ma
#@创建日期：2020-05-18 22:36 
# 等待-三种等待方式
# 1、强制等待
# sleep(秒)

# 2、隐性等待
# implicitly_wait(秒)
# 设置最长等待时间,在这个时间内加载完成,则执行下一步。
# 整个drvier的会话周期内,设置一次即可,全局都可用

# 3、显性等待
# 明确等到某个条件满足之后,再去执行下一步操作。
# 程序每隔xx秒看一眼,如果条件成立了,则执行下一步,否则继续等待,直到
# 超过设置的最长时间,然后抛出TimeoutException.

# WebDriverWait类:显性等待类。
# WebDriverWait(driver,等待时长,轮循周期).until()或until_not()

# expected_conditions 模块:提供了一系列期望发生的条件。
# presence_of_element_located: 元素存在
# visibility_of_element_located: 元素可见
# element_to_be_clickable: 元素可点击
# ps:这个类有很多判断方法。具体自行了解
# 使用之前,引入相关的库:
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# 使用方法:
# 1、先确定元素的定位表达式
# web_locator(id/name/classname...) = "XXXX"
# 2、调用webdriverWait类设置等待总时长、轮询周期。并调用其until、until_not方法。
# WebDriverWait(webdriver对象名,等待总时长,轮询周期),until(判断条件)
# 3、使用expected_conditions 对应的方法来生成判断条件。
# EC.类名(定位方式、定位表达式)
# 例：(EC.presence_of_element_located((By.CSS_SELECTOR,web_locator)))
# 例:等待百度登陆的弹出框出现,再去操作弹出框。