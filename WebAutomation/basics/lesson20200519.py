#-*-coding:utf-8-*-
#@作者：haiyu.ma
#@创建日期：2020-05-19 17:30 
from selenium import webdriver
import time
# 显性等待
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
# 启动谷歌浏览器，开始与浏览器之间的会话
driver = webdriver.Chrome(service_log_path=R"C:\Users\haiyu.ma\PycharmProjects\lemon_class\WebAutomation\basics\chromedrive_service.log")
# 全局等待--隐性等待
driver.implicitly_wait(30)
# 访问一个网页
driver.get("http://www.baidu.com")
# 窗口最大化
driver.maximize_window()

driver.find_element_by_id("kw").send_keys("柠檬班")
driver.find_element_by_id("su").click()
WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'//*[@tpl="tieba_general"]/h3/a')))
# # 方法一：
# # 此操作，引起了窗口数量的变化
# driver.find_element_by_xpath('//*[@tpl="tieba_general"]/h3/a').click()
# time.sleep(0.5)
# # 窗口切换
# # step1：获取窗口的总数以及句柄  一般新打开的窗口，位于最后一个
# handles = driver.window_handles
# print(handles)
# # 当前窗口的句柄
# print(driver.current_window_handle)
# # step2: 切换句柄
# driver.switch_to.window(handles[1])

# 方法二：
# step1：获取窗口的总数以及句柄  一般新打开的窗口，位于最后一个
handles = driver.window_handles   #窗口总数为1
# 此操作，引起了窗口数量的变化，窗口数量变为2
driver.find_element_by_xpath('//*[@tpl="tieba_general"]/h3/a').click()
# 等待新的窗口出现
WebDriverWait(driver,10).until(EC.new_window_is_opened((handles)))
# 重新获取一次窗口
handles = driver.window_handles
# 切开为最新打开的窗口
driver.switch_to.window(handles[1])

# 新的窗口页面操作
WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,'j_head_focus_btn')))
driver.find_element_by_id('j_head_focus_btn').click()


