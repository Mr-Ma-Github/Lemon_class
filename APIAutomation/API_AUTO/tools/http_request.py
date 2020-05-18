#-*-coding:utf-8-*-
#@作者：haiyu.ma
#@创建日期：2019-12-03 23:31
import requests
from API_AUTO.tools.my_log import MyLog
my_logger=MyLog()
class HttpRequest:
    def http_request(self,url,data,method,cookie=None):
        try:
            if method.upper()=="GET":
                res=requests.get(url,data,cookies=cookie)
            elif method.upper()=="POST":
                res=requests.post(url,data,cookies=cookie)
            else:
                print("不支持你输入的请求方法")
        except Exception as e:
            # print("请求报错了".format(e))
            my_logger.error("请求报错了".format(e))
            raise e
        return res  # 返回消息实体

if __name__ == '__main__':
    login_url = "http://test.lemonban.com/futureloan/mvc/api/member/login"
    login_data = {"mobilephone": "18688773467", "pwd": "123456"}
    login_res = HttpRequest().http_request(login_url, login_data, "get")
    res = HttpRequest().http_request('http://test.lemonban.com/futureloan/mvc/api/loan/add',
                                     {"memberID": 272144, "title": "同学借钱买房", "amount": 2000, "loanRate": 12.0,
                                      "loanTerm": 6, "loanDateType": 0, "repaymemtWay": 11, "biddingDays": 5}, 'get',login_res.cookies)
    print(res.json())
    # 注册：
    register_url = "http://test.lemonban.com/futureloan/mvc/api/member/register"
    # register_data = {"mobilephone": "18688773467", "pwd": ""}
    register_data ={"mobilephone": "15096090608", "pwd": "123456"}
    # 登录：
    login_url = "http://test.lemonban.com/futureloan/mvc/api/member/login"
    login_data = {"mobilephone": "18688773467", "pwd": "123456"}
    # 充值
    recharge_url="http://test.lemonban.com/futureloan/mvc/api/member/recharge"
    recharge_data={"mobilephone": "18688773467", "amount": "1000"}

    # register_res = HttpRequest().http_request(register_url, register_data, "get")
    # print(register_res.text)
    # login_res=HttpRequest().http_request(login_url,login_data,"get")
    # print(login_res.text)
    # recharge_res=HttpRequest().http_request(recharge_url,recharge_data,"post",login_res.cookies)
    # print(recharge_res.json())



