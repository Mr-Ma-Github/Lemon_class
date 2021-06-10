# -*-coding:utf-8-*-
# @作者：haiyu.ma
# @创建日期：2019-12-03 23:31
import requests
from GC_API.tools.my_log import MyLog

my_logger = MyLog()


class HttpRequest:
    def http_request(self, url, method, data=None, json=None, params=None, **kwargs):
        global res
        try:
            if method.upper() == "GET":
                res = requests.get(url, **kwargs)
            elif method.upper() == "POST":
                res = requests.post(url, data=data, json=json, params=params, **kwargs)
            else:
                print("不支持你输入的请求方法")
        except Exception as e:
            my_logger.error("请求报错了".format(e))
            raise e
        return res  # 返回消息实体


if __name__ == '__main__':
    login_url = "http://clinical-portal-snapshot.gene-go.com/api/authenticate"
    login_data = {"username": "m", "password": "password.1"}
    res = HttpRequest().http_request(login_url, "post", json=login_data)
    print(res.json()["id_token"])
