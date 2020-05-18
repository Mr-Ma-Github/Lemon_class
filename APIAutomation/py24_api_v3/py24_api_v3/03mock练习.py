"""
============================
Author:柠檬班-木森
Time:2019/12/18
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

from unittest.mock import Mock
from common.handle_request import HandleRequest


url = "http://127.0.0.1:8000/login"

data = {"user":"python01","pwd":"lemona","sign_id":"123r"}
http = HandleRequest()

request = Mock(return_value='{"code":1,"msg":"登录成功"}')

response = request(url=url,method="post",data=data)
response2 = http.send(url=url,method="post",data=data)

print(response)