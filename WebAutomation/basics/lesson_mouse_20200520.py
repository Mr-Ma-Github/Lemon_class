#-*-coding:utf-8-*-
#@作者：haiyu.ma
#@创建日期：2020-05-20 17:58 
# 鼠标操作
# 由selenium的ActionChains 类来完成模拟鼠标操作。
# 主要操作流程:
# 1、存储鼠标操作。
# 2、perform()来执行鼠标操作。
# 支持的操作如下:
# double_click 双击操作
# context_click 右键操作
# drag_and_drop 拖拽操作。左键按住拖动某一个元素到另外一个区域,然后释放按键
# move_to_element()---鼠标基停.以后会经常遇到
# perform()
# 引入ActionChains类:
# from selenium.webdriver.common.action_chains import ActionChains
# AC.方法名1().context_click().perform()
# 2:其体用法看代码
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import time
# 显性等待
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
# 启动谷歌浏览器，开始与浏览器之间的会话
driver = webdriver.Chrome(service_log_path=R"C:\Users\haiyu.ma\PycharmProjects\lemon_class\WebAutomation\basics\chromedrive_service.log")
driver.maximize_window()
# 全局等待--隐性等待
driver.implicitly_wait(30)
# 访问一个网页
driver.get("http://www.baidu.com")

# 1.先找到鼠标要操作的元素
# ele = driver.find_element_by_id("s-usersetting-top")
# # 2.实例化ActionChains类
# ac = ActionChains(driver)
# # 3.将鼠标操作添加到ActionChains列表中
# ac.move_to_element(ele)
# # 4.调用perform()来执行鼠标操作
# ac.perform()

# 可组合写：
ActionChains(driver).move_to_element(driver.find_element_by_id("s-usersetting-top")).perform()

WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'//a[text()="高级搜索"]'))).click()
# driver.find_element_by_xpath('//a[text()="高级搜索"]').click()

# Select类-下拉框操作
# selenium提供了Select类来处理select/option
# 引入类：
# from selenium.webdriver.support.ui import Select
# 选择下拉列表值：
# 1.通过下标选择:select_by_index(下标)从O开始:
# 2.通过value属性:select_by_value(value值)
# 3.通过文本内容:select_by_visible_text(文本内容)
# select类
from selenium.webdriver.support.ui import Select
# 1.找到select元素
WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH,'//select[@name="ft"]')))
select_ele = driver.find_element_by_xpath('//select[@name="ft"]')
# 2.实例化select类
s = Select(select_ele)
# 3.选择下拉列表值
# 方式一：下标 从0开始
s.select_by_index(4)
# 方式二：value值
s.select_by_value("all")
# 方式三:文本内容
s.select_by_visible_text("Adobe Acrobat PDF (.pdf)")