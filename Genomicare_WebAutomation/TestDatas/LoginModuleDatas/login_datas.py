#-*-coding:utf-8-*-
#@作者：haiyu.ma
#@创建日期：2020-05-28 22:09

# 正常登录场景 --测试数据
success_data = {"username": "haiyu.ma", "password": "password.1"}

# 异常用例--账号不正确、密码不正确、账号为空、密码为空
phone_data = [{"username": "haiyu.ma1", "password": "password.1", "check": "登录失败! 请检查您的登录信息, 并重试一次."},
              {"username": "haiyu.ma", "password": "password.2", "check": "登录失败! 请检查您的登录信息, 并重试一次."},
              {"username": "", "password":"password.1", "check": "登录失败! 请检查您的登录信息, 并重试一次."},
              {"username": "haiyu.ma", "password": "", "check": "登录失败! 请检查您的登录信息, 并重试一次."}
              ]
# # 异常用例--手机号未注册、密码错误...
# NoReg_ErrorPwd = [{"username":"18000000000","password":"python","check":"未注册"},
#                   {"username":"18684720553","password":"python1","check":"密码错误"}]

# print(phone_data[0]["username"])