# -*-coding:utf-8-*-
# @作者：haiyu.ma
# @创建日期：2020-09-03 17:31
import requests


class HttpHandler:
    def __init__(self):
        self.session = requests.session()

    def visit(self, url, method, params=None, data=None, json=None, **kwargs):
        """访问接口
        :param url:请求网址
        :param method:请求方法
        :param params:请求参数以querystring形式传递
        :param data:请求参数以表单形式传递
        :param json:请求参数以json形式传递
        :param kwargs:未定义参数
        :return:返回结果
        """
        # if method.lower() == 'get':
        #     res = self.session.get(url, params=params, **kwargs)
        # elif method.lower() == 'post':
        #     res = self.session.post(url, params=params, data=data, json=json, **kwargs)
        # else:  # session.request可以处理多种请求方法
        #     res = self.session.request(method, url, params=params, data=data, json=json, **kwargs)

        res = self.session.request(method, url, params=params, data=data, json=json, **kwargs)
        try:
            return res.json()
        except ValueError:
            print("not json")


if __name__ == '__main__':
    # data = {"url": "http://test.lemonban.com/futureloan/mvc/api/member/login",
    #         "method": "post", "data": {"mobilephone": "18688888866", "pwd": "12345678"},
    #         "header": {"X-Lemonban-Media-Type": "lemonban.v2"},
    #         "excepted": "hello world"}
    # res = HttpHandler().visit(data["url"], data["method"], data=data["data"], headers=data["header"])
    # print(res)
    login_url = "http://clinical-portal-snapshot.gene-go.com/api/authenticate"
    login_data = {"username": "m", "password": "password.1"}
    res = HttpHandler().visit(login_url, "post", json=login_data)
    print(res)
