#-*-coding:utf-8-*-
#@作者：haiyu.ma
#@创建日期：2020-05-28 22:09

# 正常登录场景 --测试数据
success_data = {"username":"18684720553","password":"python"}

# 异常用例--手机号格式不正确(大于11位、小于11位、为空、不在号码段)
phone_data = [{"username":"186847205531","password":"python","check":"请输入正确的手机号"},
              {"username":"1868472055","password":"python","check":"请输入正确的手机号"},
              {"username":"","password":"python","check":"请输入手机号"},
              {"username":"1168472055","password":"python","check":"请输入正确的手机号"}
              ]
# 异常用例--手机号未注册、密码错误...
NoReg_ErrorPwd = [{"username":"18000000000","password":"python","check":"未注册"},
                  {"username":"18684720553","password":"python1","check":"密码错误"}]

print(phone_data[0]["username"])