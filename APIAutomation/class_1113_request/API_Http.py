#-*-coding:utf-8-*-
# 接口的分类：
# 外部 内部 广泛的分类
# 按照不同的请求协议  http  webservice  dubbo  socket
# 学习的思路-方法很重要：
# 接口的本质:登录接口 注册的接口 获取某个省份天气预报的接口
# #类:函数/方法-->就是测试类里面的方法
# #Apache tomcat 中间件容器服务-->URL地址
# #参数(数据) 逻辑
# http协议的接口
# http请求分为哪几种：get  post  delete  put  head  option
# 查看工具  fiddler  f12   charles

# 本节课 目标
# 1:剖析http request
# 2: http response
# 3: cookie session
# 4:接口的 本质
# 3:如何利用soapui做接口测试
# 1: http request
# -个http request (http请求) 指从客户端到服务端的请求消息,包括了以下信息:
# 请求地址url
# 请求方法：HEAD、GET、POST、PUT、OPTIONS、DELETE、PATCH
# HTTP协议/版本:大家 可以自己打开浏览器按F12去仔细查看
# 请求网址:stps://csdnimg.cn/search/baidu_search-1.1.2.js?v«2018020710568autorun«true&is
# 请求方法:GET
# 远程地址：124.232.170.85:443
# 状态码：200
# 版本:HTTP/2.0
# 请求头：https://jingyan.baidu.com/article/375c8e19770f0e25f2a22900.html
# 请求正文:也就是我们说的请求参数

# 2: http response
# * 状态码:标记响应状态的一个标识,200-成功,404-资源找不到,500服务器异
# 常,302-重定向等,自行去拓展。-->;常见的HTTP状态码有哪些?
# * 响应头:
# * 响应正文:针对请求从服务响应回来的数据,比如html、xml、json 等
# 常见http返回状态码:
# 200 (正常):表示一切正常,请求到了服务器,并且服务器正常的响应了你的请求。
# 302(临时重定向):指出被请求的文档已被临时移动到别处,此文档的新的URL在Location响应头中给出
# 304 (未修改),:表示客户机缓存的版本是最新的,客户机应该继续使用它,比如说前端js  css   jpeg
# 403 (禁止):服务器理解客户端请求,但拒绝处理它,通常由于服务器上文件或目录的权限设置所致。
# 404(找不到)服务器上不存在客户机所请求的资源。
# 500 (内部服务器错误)服务器端的CGI、ASP、JSP等程序发生错误
# 504:超时

#3: icookie session token
# * cookie: 在客户端 存储用户的一些数据 比如说用户名啥的浏览记录啥的
# session: 在服务器端,记录用户的请求状态,一般默认时间是30min.
# 会员卡机制。
# session_id会存在cookie中,每次请求cookie中的所有信息都会传送给服务器,服务器通过
# session_id来识别是否是同一个用户的请求。不是同一个用户的 话,就会要求用户重新登录
# 为什么会有这种机制?因为http请水求是无状态的。就是说这一次请求和上一次请求是没有任何关系的，
# 互不认识的，没有关联的。这种无状态的的好处是快速。坏处是假如我们想要把www.zhihu.com/
# login.html和www.zhihu.com/index.html关联起来，必须使用某些手段和工具
# 参考博文：https://www.cnblogs.com/nickjiang/p/9148136.html

# 4:剖析访问授权
# 鉴权: 访问的接口是否正常, 是否是非法访问,绕过前端访问。token
# 授权: 是否具有访问接口的权限。key
# 一般来说:是唯一的,全局的,动态的, 具备一定特征
# 具体可以参考这个:
# https://blog.csdn.net/sjy8207380/article/details/79232644
# 如果遇到接口不会处理 怎么办?
# http://docs.python-requests.org/zh_CN/latest/
import requests
