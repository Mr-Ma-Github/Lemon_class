#-*-coding:utf-8-*-
#@作者：haiyu.ma
#@创建日期：2020-09-01 18:02
import requests
# 注册接口
url = "http://test.lemonban.com/futureloan/mvc/api/member"
data = {"mobile_phone": "18688888888", "pwd": "12345678"}
header = {"X-Lemonban-Media-Type": "lemonban.v2"}#v1无鉴权，不会返回token
# 注意：此处content-type不需要添加。
# json关键字参数就是表示等于json格式（application/json）。
# data关键字参数就是表示form表单格式(application/x-www-form-urlencoded)。
# params关键字参数就是表示querystring(?key=value)
res = requests.post(url, data=data, headers=header)#返回一个消息实体
print(res.text)

# 登录接口
# token可以放在请求体当中？根据接口文档。token只是一种协议，开发人员和你之间定义的协议
# cookie不可以放到请求体当中，HTTP协议硬性规定
# url = "http://120.78.128.25:8766/futureloan/member/login"
# data = {"mobile_phone": "18688888866", "pwd": "12345678"}
# header = {"X-Lemonban-Media-Type": "lemonban.v2"}#v2才会返回token
# res = requests.post(url, json=data, headers=header)
# print(res.json())

# 充值接口：token
# recharge_url = "http://120.78.128.25:8766/futureloan/member/recharge"
# token = res.json()["data"]["token_info"]["token"]
# # print(token)
# member_id = res.json()["data"]["id"]
# # print(member_id)
# header = {"X-Lemonban-Media-Type": "lemonban.v2", "Authorization": "Bearer {}".format(token),
#           "User-Agent": "Mozilla/5.0"}
# recharge_data = {"member_id": member_id, "amount": 100}
# recharge_res = requests.post(recharge_url, json=recharge_data, headers=header)
# # cookies=res.cookies(如果是cookie，需要把cookie放在请求方法后面，cookies关键字参数里)
# print("充值结果：", recharge_res.json())
# print("状态码：", recharge_res.status_code)
# print("代理user_agent：", recharge_res.request.headers["User-Agent"])#请求头里面的User-Agent

# 接口二：如何操作cookie
import requests
# 注册
# url = "http://test.lemonban.com/futureloan/mvc/api/member/register"
# data = {"mobilephone": "18688888866", "pwd": "12345678"}
# res = requests.post(url, data)
# print(res.json())
# 登录
url = "http://test.lemonban.com/futureloan/mvc/api/member/login"
data = {"mobilephone": "18688888888", "pwd": "12345678"}
res = requests.post(url, data)
print(res.json())

# 获取cookie:JSESSIONID=8CC86F59FE6670145E350C256BFD44F9
cookie_dict = requests.utils.dict_from_cookiejar(res.cookies)
print(cookie_dict)  # {'JSESSIONID': '81C7C6621A4466963154A4866C4A4C03'}
print(cookie_dict.items())  # [('JSESSIONID', '81C7C6621A4466963154A4866C4A4C03')]
cookies = ''
for key, value in cookie_dict.items():
    cookie_str = key + "=" + value
    cookies += cookie_str
cookie = cookies
# 充值
header = {"cookie": cookie}
print(header)
# url = "http://test.lemonban.com/futureloan/mvc/api/member/recharge"
# data = {"mobilephone": "18688888866", "amount": "100"}
# res = requests.post(url, data, cookies=cookie)  # headers=header
# # # cookies=res.cookies(如果是cookie，需要把cookie放在请求方法后面，cookies关键字参数里)
# print(res.request.headers)
# print(res.json())

# # session
# session = requests.session()
# url = "http://test.lemonban.com/futureloan/mvc/api/member/login"
# data = {"mobilephone": "18688888866", "pwd": "12345678"}
# res = session.post(url, data)
# print(res.json())
# url = "http://test.lemonban.com/futureloan/mvc/api/member/recharge"
# data = {"mobilephone": "18688888866", "amount": "100"}
# res = session.post(url, data=data)
# print(res.json())
# session.close()
#
# # 初始化另外的session:需要重新登录
# session_another = requests.session()
# res = session_another.post(url, data=data)
# print(res.text)