#-*-coding:utf-8-*-
# python来完成http请求   get  post
# requests第三方库
import requests
# get请求
# url="http://120.78.128.25:8765/Index/login.html"
# data = {"username":"haiyu.ma", "password":"password.1"}
# get请求只能通过querystring形式传递参数
# res=requests.get(url, params=data)#返回一个消息实体
# print(res)
# # 响应头、响应报文、状态码、cookie
# print("响应状态码",res.status_code)
# print("响应头",res.headers)
# 获取响应文本，得到的数据类型是string
# print("响应报文",res.text) # 返回值是字符串
# 获取二进制形式
# print("响应报文",res.content)
# 获取json形式：如果响应数据不是json就会报错。 处理方式try  except
# json返回值是字典格式
# print("响应报文",res.json)

# post请求
# url = "http://52.83.166.21:8091/api/authenticate"
# data = {"username":"haiyu.ma", "password":"password.1"}
# res = requests.post(url, json=data)# 返回一个消息实体
# print(res)
# 响应头、响应报文、状态码、cookie
# print("响应头", res.headers)
# print("响应报文", res.text, type(res.text))  # html   #:查看响应报文的类型type(res.text)
# # print("响应报文json", res.json())# str类型返回值如果不是json，用json会报错
# print("响应报文json", res.text, type(res.json()))
# print("响应状态码", res.status_code)
# print("cookie", res.cookies)
# cookie = res.json()
# print("cookie_value", cookie['id_token'])  # 字典形式，key取值
# html  xml  json-->text
# html  xml-->json()#会报错！只有json类型的返回值才支持json。因为json返回值是字典格式（dict）

# # 如何修改请求头
# header = {"token":"123", "User-Agent":"Mozilla/5.0 (Windows NT 6.1"}
# 注意：传参时一定要添加headers关键字参数，不能以位置参数传递
url = "http://120.78.128.25:8765/Index/login.html"
# res1 = requests.get(url, headers=header)
# # 如何传递参数-位置参数或者关键字参数：params   以querystring形式传递（拼在URL里）
# url="http://clinical-portal-snapshot.gene-go.com/api/authenticate"
header = {"token":"123", "User-Agent":"Mozilla/5.0 (Windows NT 6.1"}
data ={"username":"haiyu.ma","password":"password.1"}
# res2 = requests.get(url, data, headers=header)#返回一个消息实体
# # 注意：post传递参数有多种方式 ：def post(url, data=None, json=None, **kwargs):
# # 方式一：querystring形式。使用params传递时，默认是querystring格式
post1 = requests.post(url, headers=header, params=data)#返回一个消息实体
print(1111,post1.text)
# # 方式二：表单形式。使用data传递时，默认content-tpye是data格式
# form_data = {"new_admin":"benben"}
# post2 = requests.post(url, data=form_data, headers=header)#
# # 方式三：json形式。使用json传递时，默认content-tpye是json格式
# json_data = {"new_admin":"benben"}
# post3 = requests.post(url, json=form_data, headers=header)#


# 验证码处理方式：（图片、短信）
# 1：屏蔽 2：万能验证码 3：数据库查实时的 4：手动填写

# https请求:   requests.get(url,data.txt,verify=False)

# 注意:
# 接口发送get请求还是post请求，在写代码定义功能的时候就确定好的
# 并不是所有的请求都支持get和post
# 为什么有些接口抓不到？接口地址  参数  因为数据会加密，根本就抓不到

