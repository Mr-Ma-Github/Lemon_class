#-*-coding:utf-8-*-
#@作者：haiyu.ma
#@创建日期：2020-05-14 23:00 
# Web页面
# 博客地址：https://www.cnblogs.com/Simple-Small/
# web学习目录：
# 1. selenium webdriver环境安装、原理
# web自动化环境安装
# 1)安装selenium
# 命令行使用以下命令安装selenium:
# pip install -U selenium
# 2)安装chrome浏览器chrome和chromedriver下载
# 链接: https://pan.baidu.com/s/1eSct8LO 密码: xeca
# 3)chromedriver放在python的安装根目录下面即可
# 下载链接中,只提供了windows版本的chrome和chromedriver.
# 其它操作系统需要另外下载。
# chromedriver下载地址:http://npm.taobao.org/mirrors/chromedriver/

# 2. 前端页面:html、DOM对象(前端页面是由HTML、Css、Javascript构成)
# HTML
# 1)什么是HTML?
# HTML 是用来描述网页的一种语言。
# HTML 指的是超文本标记语言 (Hyper Text Markup Language)
# HTML 不是一种编程语言,而是一种标记语言 (markup language)
# 标记语言是一套标记标签 (markup tag)
# HTML 使用标记标签来描述网页
# 2)HTML标签对
# HTML 标记标签通常被称为HTML 标签 (HTML tag)。
# HTML 标签是由尖括号包围的关键词,比如 <html>;
# HTML 标签通常是成对出现的,比如 <b>和</b>;
# 标签对中的第一个标签是开始标签,第二个标签是结束标签
# 开始和结束标签也被称为开放标签和闭合标签
# 3)HTML标签 - 属性
# placeholder: text 规定帮助用户填写输入字段的提示
# readonly: readonly 规定输入字段为只读。
# type : button/checkbox/file/password/radio/submit/text 规定input元素的类型
# checked: checked 规定此 input 元素首次加载时应当被选中
# disabled: disabled 当input元素加载时禁用此元素
# 4)DOM对象
# DOM (Document Object Mode)是一套web标准:
# 定义了访问HTML文档的一套属性、方法和事件。
# 本质:
# 网页 与 脚本语言 沟通的桥梁。
# 脚本语言通过DOM对象来访问html页面,从而改变文档的结构,样式和内容。
# 当浏览器载入HTML 文档,它就会成为 document 对像。
# HTML DOM 独立于平台和编程语言。
# 它可被任何编程语言诸如 Java、JavaScript和VBScript 使用
# 5)Javascript - 简单语法
# <script></script>
# 变量表达:
# var 变量名 =值
# 列表: var he = [a,b,c,d] alert(he[1])
# 字典: var hei = {"name":"value","sex":"unknown"}      hei.name
# 函数:
# function 函数名称(参数){
# return 值;
# 调用:函数名称(参数)

# 3. 8大元素定位、xpath详解
# 查找元素：
# document.getElementById("kw")
# document.getElementsByName("wd")
# document.getElementsByName("wd")
# document.getElementsByTagName("input")
# css、xpath

# 4. web常用元素操作
# 1)元素的属性：
# 改变属性:
# document.getElementByXXX("").属性名=属性值
# 获取属性2：
# document.getElementByXXX("").getAttribute(属性名)
# 改变元素的内容：
# 包含html元素标签--有后代：
# document.getElementByXXX("").innerHTML=newHTML
# 包含html元素标签,纯文字：
# document.getElementByXXX("").innerText=newtext
# 2)样式
# 改变样式
# document.getElementByXXX("").style.样式名=样式值
# 例:
# 元素的可见性
# document.getElementByXXX("").style.visibility='hidden'
# 元素的颜色
# document.getElementByXXX("").style.color='red'
# 3)事件
# 浏览器和用户事件-触发-执行js代码带来不同的页面响应。
# 例如:点击事件、输入事件、鼠标事件等。
# #页面加载完成事件
# window.onload = function(){
# alert( "everything is ready!!");
# };
# #点击事件
# document.findElementByld(XXX).onclick = function(){
# alert("哈哈,点我了呀!");
# };

# 5. PageObject横式应用、自动化用例设计

# 6. 深入分层设计

# 7. basepage页面提取
# 8. pytest框架应用
# 9. jenkins集成
# 10.allure报告集成
