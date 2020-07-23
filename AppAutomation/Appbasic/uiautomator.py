#-*-coding:utf-8-*-
#@作者：haiyu.ma
#@创建日期：2020-06-29 23:24 
# Appium之uiautomator定位元素
# 元素定位方式有多种，Android也有自身独有的定位方式。下面就单独介绍其基于uiautomator定位元素的方法：
# 基本语法：
# driver.find_element_by_android_uiautomator(xx)
# 1).通过text文本定位语法：new UiSelector().text("text文本")
# # text
# loc_text = 'new UiSelector().text("图书")'
# driver.find_element_by_android_uiautomator(loc_text).click()
# 2).如果文本比较长，可以用textContains模糊匹配：new UiSelector().textContains("包含text文本")
# # textContains
# loc_textContains = 'new UiSelector().textContains("图")'
# driver.find_element_by_android_uiautomator(loc_textContains).click()
# 3).同样可以用textStartsWith是以某个文本开头来匹配：new UiSelector().textStartsWith("以text文本开头")
# # textStartsWith
# loc_textStart = 'new UiSelector().textStartsWith("图")'
# driver.find_element_by_android_uiautomator(loc_textStart).click()
# 4).也可以用正则表达式textMatches匹配：new UiSelector().textMatches("正则表达式")
#
# 2.resourceId     与by_id一样
# new UiSelector().resourceId("id")
# # resourceId
# loc_id = 'new UiSelector().resourceId("com.baidu.yuedu:id/webbooktitle")'
# driver.find_element_by_android_uiautomator(loc_id).click()
#
# 3.className     页面上的class属性一般不唯一，多半用在复数定位时候。此时定位相应下标
# new UiSelector().className("className")
# # className复数定位
# loc_class = 'new UiSelector().className("android.widget.TextView")'
# driver.find_elements_by_android_uiautomator(loc_class)[2].click()
#
# 4.description     也是用contenet - des属性定位
# new UiSelector().description("contenet-des属性")
#
# 5.组合定位
# 1).id与text属性组合
# # id+text
# id_text = 'resourceId("com.baidu.yuedu:id/webbooktitle").text("小说")'
# driver.find_element_by_android_uiautomator(id_text).click()
# 2).class与text属性组合
# # class+text
# class_text = 'className("android.widget.TextView").text("图书")'
# driver.find_element_by_android_uiautomator(class_text).click()
#
# 6.关系定位
# 1).父子定位childSelector
# 有时候不能直接定位某个元素，但是它的父元素很好定位，这时候就先定位父元素，通过父元素找儿子
# 如上定位书架：
# # 父子关系childSelector
# son = 'resourceId("com.baidu.yuedu:id/rl_tabs").childSelector(text("小说"))'
# driver.find_element_by_android_uiautomator(son).click()
# 2).兄弟定位fromParent
# 有时候父元素不好定位，但是跟他相邻的兄弟元素很好定位，这时候就可以通过兄弟元素，找到同一父
# 级元素下的子元素-如上定位书架：
# # 兄弟关系fromParent
# brother = 'resourceId("com.baidu.yuedu:id/lefttitle").fromParent(text("图书"))'
# driver.find_element_by_android_uiautomator(brother).click()
# 无想法就无成就！