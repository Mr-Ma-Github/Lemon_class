#-*-coding:utf-8-*-
#@作者：haiyu.ma
#@创建日期：2020-05-16 11:53 
# 元素定位
# id、name、classname、tagname
from selenium import webdriver
# 启动谷歌浏览器，开始与浏览器之间的会话
driver = webdriver.Chrome(service_log_path=R"C:\Users\haiyu.ma\PycharmProjects\WebAutomation\chromedrive_service.log")
# 访问一个网页
driver.get("http://www.baidu.com")
# 窗口最大化
driver.maximize_window()  # driver.set_window_size()
# 方式一：id
ele=driver.find_element_by_id("kw")
print(ele)
print(ele.get_attribute("class"))
# 方式二：class
eles1=driver.find_element_by_class_name("s_ipt")
# element：即使找到多个元素也只去第一个（从上而下）
eles=driver.find_elements_by_class_name("s_ipt")
# elements：列表，可能找到多个元素
# 方式三：name
driver.find_element_by_name("wd")
driver.find_elements_by_name("wd")
# 方式四：tagname
driver.find_element_by_tag_name("input")
driver.find_elements_by_tag_name("input")
# 方式五、六
driver.find_element_by_link_text("更多")# 精确匹配
driver.find_element_by_partial_link_text("更")# 模糊匹配
# xpath
driver.find_element_by_xpath()
# 绝对定位：以/开头  非常依赖于页面的顺序和位置 例：/html/body/div[1]/div[1]/div[5]/div/div/form/span[1]/input
# 相对定位：以//开头 不依赖于页面的顺序和位置  只看整个页面中有没有符合表达式的元素 例：//*[@id="kw"]
# 1) //标签名[@属性名="属性值"]
# 2）逻辑运算：and  or   //标签名[@属性名="属性值"and@属性名="属性值"]
# 3) 层级定位：//父标签名[@父属性名="父属性值"]/子标签名[@子属性名="子属性值"]
# 4) 函数使用:
# text():文本定位 --元素的text内容
# 例: //*[@id="XXX"]//[text()="文本内容"]
# contains(@属性名称/text(),value): 包含函数
# 例: //*[contains(@class,"XXXX")]  或   contains(text(),"XXXX")
# 例: //div[@class="XXX"and contains(@style,"display:visibility")]
# 应用场景:一个页面的几个操作,都会有弹出框出现。定位到弹出框会有几个。
# 但通过display的值来定位到当前显示的那一个。
# 5)轴定位语法
# 轴运算:
# ancestor:祖先结点 包括父
# parent:父结点
# preceding:当前元素节点标签之前的所有结点(html页面先后顺序)
# preceding-sibling: 当前元素节点标签之前的所有兄弟结点
# following:当前元素节点标签之后的所有结点(html页面先后顺序)
# following-sibling ,当前元素节点标标签之后的所有兒弟结点
# 使用语法：
# /轴名称::节点名称[@属性=值]
# 例：//div//table/td//preceding::td
# 较多的应用场景:
# 页面显示为一个表格样式的数据列。需要通过组合来定位元素

# css
driver.find_elements_by_css_selector()