#-*-coding:utf-8-*-
# python来完成http请求   get  post
# requests第三方库
import requests
# get请求
# url="http://120.78.128.25:8765/Index/login.html"
# res=requests.get(url)#返回一个消息实体
# print(res)
# # 响应头、响应报文、状态码、cookie
# print("响应头",res.headers)
# print("响应报文",res.text)#html
# print("响应状态码",res.status_code)
# post请求
url="http://clinical-portal-snapshot.gene-go.com/api/authenticate"#http://119.23.241.154:8080/futureloan/mvc/api/member/login
data={"username":"haiyu.ma","password":"password.1"}
res=requests.get(url,data)#返回一个消息实体
print(res)
# 响应头、响应报文、状态码、cookie
print("响应头",res.headers)
print("响应报文",res.text,type(res.text))#html   #:查看响应报文的类型type(res.text)
# print("响应报文",res.json())# str类型返回值用json会报错
print("响应状态码",res.status_code)
print("cookie",res.cookies)
# print("cookie_value",res.cookies['填入cookie的keys'])#字典形式，key取值
# html  xml  json-->text
# html  xml  json-->json()#会报错！只有json类型的返回值才支持json。因为json返回值是字典格式（dict）

# 充值
# recharge_url=' http://119. 23. 241. 154:8080/futureloan/mvc/api/member/recharge'
# recharge_data={"mobilephone":"18688773467","amount":"1000"}
# header={'User_Agent':'Mozilla/5.0'}#这个是伪装的
# recharge_res=requests.get(recharge_url,recharge_data,headers=header,cookies=res.cookies)
# print ("充值结果：",recharge_res.json())
# print("状态码：", recharge_res.status_code)
# print("代理user_agent",recharge.request.headers)#请求头

# 验证码处理方式：（图片、短信）
# 1：屏蔽 2：万能验证码 3：数据库查实时的 4：手动填写

# https请求:   requests.get(url,data,verify=False)

# 注意:
# 接口发送get请求还是post请求，在写代码定义功能的时候就确定好的
# 并不是所有的请求都支持get和post
# 为什么有些接口抓不到？接口地址  参数  因为数据会加密，根本就抓不到
