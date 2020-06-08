#-*-coding:utf-8-*-
#@作者：haiyu.ma
#@创建日期：2020-06-04 0:31 
# 正常登录场景 --测试数据
# t=[1,2]
# print(*t)#加*号--》脱外套

# 正常投资场景 --测试数据
success = {"money":"1000"}
# print(success['money'])

# 投资异常用例--异常场景:投资金额为非100的整数倍、错误的格式等
wrong_format_money = [{"money":"1010"},{"money":"100?"},{"money": "1001"}]