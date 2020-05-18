#-*-coding:utf-8-*-
#@作者：haiyu.ma
#@创建日期：2019-12-03 23:31

# session  会话
import requests

login_url = "http://119.23.241.154:8080/futureloan/mvc/api/member/login"
login_data = {"mobilephone": "18688773467", "pwd": "123456"}
# login_res=requests.get(login_url,login_data)
# print(login_res.text)

recharge_url="http://119.23.241.154:8082/futureloan/mvc/api/member/recharge"
recharge_data={"mobilephone": "18688773467", "amount": "1000"}
# header={"User-Agent":"Mozilla/5.0 "}
# recharge_res=requests.post(register_url,register_data,cookies=login_res.cookies,headers=header)
# print("text解析的结果",recharge_res.text)
# print("json解析的结果",recharge_res.json())
# print("请求头",recharge_res.request.hearders)


s=requests.session()#创建了一个会话
login_res=s.get(login_url,params=login_data)#params  get请求必须要指明参数传给谁
# login_res=s.post(login_url,login_data)
recharge_res=s.post(recharge_url,recharge_data)#一个session中，不用cookie也可以
print("充值的结果是",recharge_res.json())

