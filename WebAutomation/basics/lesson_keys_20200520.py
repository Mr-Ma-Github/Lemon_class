#-*-coding:utf-8-*-
#@作者：haiyu.ma
#@创建日期：2020-05-20 23:20 
# 键盘操作
# selenium 提供了比较完整的键盘操作,在使用的模拟键盘操作之前需要我们导入
# from selenium.webdriver.common.keys import Keys 即可,然后就可以来模拟键盘操作
# 导入Keys 模块,然后我们看看Keys模块定义了哪些按键
from selenium.webdriver.common.keys import Keys
# 在Keys类中,定义了非常多的按键操作,我们实际上使用的按键并不多,介绍一些常用的按键。
# 组合健:
# 我们经常使用的Ctrl+A,ctrl+C都是组合键。
# 在使用按键操作的时候我们需要借助send_keys来模拟操作。
# Keys.CONTROL 也就是我们键盘上的Ctrl 键,下面是几个常用的组合键。
# 1.send_keys(Keys.CONTROL.'a') #全选(Ctrl+A)
# 2.send_keys(Keys.CONTROL.'c') #复制(Ctl+C)
# 3.send_keys(Keys.CONTROL.'x') #剪切(Cul+X)
# 4.send_keys(Keys.CONTROL,'v') #粘贴(Ctl+V)
# 注意:send_keys 两个参数。
# 常用的非组合键:
# 回车键 Keys.ENTER
# 删除键 Keys.BACK_SPACE
# 空格键 Keys.SPACE
# 制表键 Keys.TAB
# 回退键 Keys.ESCAPE
# 刷新键 Keys.FS
# 比如百度搜索中,可以利用Keys.Enter 代替点击搜索按组

from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service_log_path=R"C:\Users\haiyu.ma\PycharmProjects\lemon_class\WebAutomation\basics\chromedrive_service.log")
driver.maximize_window()
# 全局等待--隐性等待
driver.implicitly_wait(30)
# 访问一个网页
driver.get("http://www.baidu.com")
WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'//span[@id="s-usersetting-top"]')))
# 获取元素的文本内容
print(driver.find_element_by_xpath('//span[@id="s-usersetting-top"]').text)
# 获取元素的属性
print(driver.find_element_by_xpath('//input[@id="kw"]').get_attribute('name'))
# 输入内容且自动回车(可以省略一步点击操作)
driver.find_element_by_xpath('//input[@id="kw"]').send_keys("柠檬班",Keys.ENTER)
# # 滚动条操作-滚动条不是HTML页面元素
# 1、移动到元素element对象的"底端"与当前窗口的"底部"对齐:
# driver.execute_script("arguments[0].scrollIntoView(false);",element)
# 2、移动到元素element对象的"顶端"与当前窗口的"顶部"对齐:
# driver.execute_script("arguments[0].scrollIntoView();",element)
# 3、移动到页面底部:
# driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
# 4、移动到页面顶部:
# driver.execute_script("window.scrollTo(document.body.scrollHeight,0)")




