#-*-coding:utf-8-*-
#@作者：haiyu.ma
#@创建日期：2020-05-18 18:02 
from selenium import webdriver
import time
# 显性等待
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
# 启动谷歌浏览器，开始与浏览器之间的会话
driver = webdriver.Chrome(service_log_path=R"C:\Users\haiyu.ma\PycharmProjects\lemon_class\WebAutomation\basics\chromedrive_service.log")
# 全局等待--隐性等待（在一次会话中设置一次就行）
# driver.implicitly_wait(30)
# 访问一个网页
driver.get("http://www.baidu.com")
# 窗口最大化
driver.maximize_window()
driver.find_element_by_xpath('//div[@id="u1"]//a[@name="tj_login"]').click()
# 显性等待
id="TANGRAM__PSP_11__footerULoginBtn"
WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,id)))

# 点击用户名登录
driver.find_element_by_id('TANGRAM__PSP_11__footerULoginBtn').click()

# iframe切换方式一：（等于进入另一个HTML页面）（三种语法）
# 等待iframe存在，可见
# driver.switch_to.frame('frame_name')
# driver.switch_to.frame(1)
# driver.switch_to.frame(driver.find_elements_by_tag_name("iframe")[0])
# driver.switch_to.frame(1)
# time.sleep(0.5)
# iframe切换方式二：
# WebDriverWait(driver,10).until(EC.frame_to_be_available_and_switch_to_it(("login_frame_qq")))
# time.sleep(0.5)
# 从iframe中切换到默认页面
# driver.switch_to.default_content()
# driver.switch_to.parent_frame()#退到父级


