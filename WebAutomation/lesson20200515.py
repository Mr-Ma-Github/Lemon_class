#-*-coding:utf-8-*-
#@作者：haiyu.ma
#@创建日期：2020-05-15 23:18 
from selenium import webdriver
# 启动谷歌浏览器，开始与浏览器之间的会话
driver = webdriver.Chrome(service_log_path=R"C:\Users\haiyu.ma\PycharmProjects\WebAutomation\chromedrive_service.log")
# 访问一个网页
driver.get("http://www.baidu.com")
# 窗口最大化
driver.maximize_window()  # driver.set_window_size()
# 访问淘宝
driver.get("http://www.taobao.com")
# 回退上一页
driver.back()
# 回退到下一页
driver.forward()
# 刷新
driver.refresh()
# 获取标题
print(driver.title)
# 获取网址
print(driver.current_url)
# 窗口的句柄
print(driver.current_window_handle)

# # 结束会话
# driver.quit()