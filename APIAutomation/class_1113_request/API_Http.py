#-*-coding:utf-8-*-
# 接口的定义：1.前后端沟通的桥梁  2.数据通道
# 我们所讲的接口概念：web api
# API:应用程序可编程接口 全称：application programming interface
# 接口的分类：
# 硬件接口：USB、耳机接口、水龙头...
# 软件接口：用户界面-UI(user interface)、http://api.github.com/login、可以被外部访问的函数
# 按照不同的请求协议  http  webservice  dubbo  socket

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

'''
HTTP请求：
1.请求首行（请求的概要信息）
Request URL: http://10.10.10.181:8089/api/domain-data/upload
Request Method: POST
Status Code: 200 OK
Remote Address: 10.10.10.181:8089
Referrer Policy: no-referrer-when-downgrade  #用于过滤 Referrer 报头内容
版本：HTTP/1.0
2.请求头
3.请求体

'''


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
# 201 (Created/已创建)
# 201 (SC_CREATED)表示服务器在请求的响应中建立了新文档;应在定位头信息中给出它的URL。
# 202 (Accepted/接受)
# 301 (永久重定向)
# 302 (临时重定向):指出被请求的文档已被临时移动到别处,此文档的新的URL在Location响应头中给出
# 304 (未修改),:表示客户机缓存的版本是最新的,客户机应该继续使用它,比如说前端js  css   jpeg
# 403 (禁止):服务器理解客户端请求,但拒绝处理它,通常由于服务器上文件或目录的权限设置所致。
# 404 (找不到)服务器上不存在客户机所请求的资源。
# 500 (内部服务器错误)服务器端的CGI、ASP、JSP等程序发生错误
# 504  超时

#3: cookie    session     token
# * cookie: 在客户端 存储用户的一些数据 比如说用户名、浏览记录...

# session: 在服务器端,记录用户的信息状态,服务器验证（一般默认时间是30min.）
# 会员卡机制。
# session_id会存在cookie中,每次请求cookie中的所有信息都会传送给服务器
# 服务器通过session_id来识别是否是同一个用户的请求。不是同一个用户的话,就会要求用户重新登录
# 为什么会有这种机制?因为http请水求是无状态的。就是说这一次请求和上一次请求是没有任何关系的，
# 互不认识的，没有关联的。这种无状态的的好处是快速。坏处是假如我们想要把www.zhihu.com/
# login.html和www.zhihu.com/index.html关联起来，必须使用某些手段和工具
# 参考博文：https://www.cnblogs.com/nickjiang/p/9148136.html

# token：令牌，跨平台。只要有这个令牌，不管它是什么身份（手机、浏览器）都允许访问
# 保存再客户端本地：local_storage
# 移动端流通。手机，平板，web，第三方客户端
# 口令
# 口令是会变的

# Cookie与Session的区别
# 1.cookie数据存放在客户的浏览器上，session数据放在服务器上；
# 2.cookie不是很安全，别人可以分析存放在本地的COOKIE并进行COOKIE欺骗，考虑到安全应当使用session；
# 3.session会在一定时间内保存在服务器上。当访问增多，会比较占用你服务器的性能。考虑到减轻服务器性能方面，应当使用COOKIE；
# 4.单个cookie在客户端的限制是3K，就是说一个站点在客户端存放的COOKIE不能超过3K；

# 4:剖析访问授权
# 鉴权: 访问的接口是否正常, 是否是非法访问,绕过前端访问。token
# 授权: 是否具有访问接口的权限。key
# 一般来说:是唯一的,全局的,动态的, 具备一定特征
# 具体可以参考这个:
# https://blog.csdn.net/sjy8207380/article/details/79232644
# 如果遇到接口不会处理 怎么办?
# http://docs.python-requests.org/zh_CN/latest/

# 5.输入url的过程
# a.域名解析,DNS 解析 -》 ip 地址
# b.发起TCP连接的三次握手,建立连接。
# c.建立TCP连接后发起http请求
# d.服务端响应http请求,返回响应报文
# e.浏览器页面渲染,展示。
# f.断开TCP连接,四次挥手

# 6.三次握手四次挥手
# 三次握手
# *第一次握手:建立连接时,客户端向服务端发送请求报文(SYN),"我想建立连接"
# *第二次握手:服务器收到请求报文后,如同意连接,则向客户端发送确认报文(SYN/ACK)"同意建立"
# *第三次握手:客户端收到服务器的确认后,再次向服务器发送确认报文,完成连接(ACK)
# 三次握手主要是为了防止已经失效的请求报文字段发送给服务器,浪费资源。
# 四次挥手
# *第一次挥手:客户端想分手,发送消息(FIN)给服务器
# *第二次挥手:服务器通知客户端已经接受的挥手请求,返回确认消息(ACK),但还没做好分手准备;
# *第三次挥手:服务器已经做好分手准备,通知客户端(FIN)
# *第四次挥手:客户端发送消息给服务器(ACK),确认分手,服务器关闭连接。
