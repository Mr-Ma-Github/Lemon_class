#-*-coding:utf-8-*-
# def print_msg(*args):
#     print(args)
#
# t=[1,2]
# print(*t)#加*号--》脱外套

# ddt  ddt+unittest 来进行数据的处理  第三方库
#装饰器   可以自行去了解   会在你的函数运行之前运行
import unittest
from ddt import ddt,data,unpack

test_data=[[1,3],[4,5,7]]#-->[1,3],[4,5,7]-->1  3要用两个参数来接收，4 5 7要用三个来接收

@ddt#装饰测试类
class TestMath(unittest.TestCase):

    @data(*test_data)#装饰测试方法   拿到几个数据就执行几次用例
    @unpack#如果unpack后的参数 少于5个 推荐使用。要注意参数不多等的情况，提供对应个数的参数来接收变量
    def test_print_data(self,a,b,c=None):#测试用例
        print("a:",a)
        print("b:",b)
        print("c:",c)

# # -------------------------------------------------------
# test_data=[{"url":1,"name":"稳当"},{"url":2,"name":"小黄"}]#列表里面嵌套字典
# @ddt#装饰测试类
# class TestMath(unittest.TestCase):
#
#     @data(*test_data)#装饰测试方法   拿到几个数据就执行几次用例
#     # @unpack#如果unpack后的参数 少于5个 推荐使用。要注意参数不多等的情况，提供对应个数的参数来接收变量
#     # 如果要对字典进行unpack，参数名要与字典key对应
#     def test_print_data(self,a):#测试用例
#         # print("a:", a)
#         print(a["url"],  a["name"])
#         # print("url:", a["url"],"name:", a["name"])
#     # def test_print_data_3(self,url,name):#测试用例
#     #     print("url:", url)
#     #     print("name:", name)

# # 异常用例--手机号格式不正确(大于11位、小于11位、为空)
# phone_data = [{"username":"186847205531","password":"python","check":"请输入正确的手机号"},
#               {"username":"1868472055","password":"python","check":"请输入正确的手机号"},
#               {"username":"","password":"python","check":"请输入手机号"}]
# # print(*phone_data)
# @ddt
# class TestLogin(unittest.TestCase):
#
#     @data(*phone_data)
#     def test_login_user_wrongFormat(self,data):
#         print(data)
#
# if __name__ == '__main__':
#     tl = TestLogin().test_login_user_wrongFormat(data)









    # def test_add(self):
    #     a=10
    #     b=20
    #     print(a+b)

