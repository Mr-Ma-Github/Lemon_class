#-*-coding:utf-8-*-
#@作者：haiyu.ma
#@创建日期：2019-12-07 12:36
# import unittest
# from API_AUTO.tools.http_request import HttpRequest
# from API_AUTO.tools.get_cookie import GetCookie
# class TestHttpRequest(unittest.TestCase):
#     def __init__(self,methodName,url,data.txt,method,excepted):
#         super(TestHttpRequest,self).__init__(methodName)
#         self.url=url
#         self.data.txt=data.txt
#         self.method=method
#         self.excepted = excepted
#
#     def setUp(self):
#         print("测试开始了")
#
#     def test_http(self):
#         res=HttpRequest().http_request(self.url,self.data.txt,self.method,getattr(GetCookie,"Cookie"))
#         if res.cookies:
#             setattr(GetCookie,"Cookie",res.cookies)
#         try:  # 抓取错误  异常处理
#             self.assertEquals(self.excepted, res.json()["code"])  # 断言
#             # self.assertIn("登陆成功", res.json()["msg"])
#         except AssertionError as e:
#             print("test_api错误是{0}".format(e))
#             raise e  # 异常处理之后需要抛出去
#
#     def tearDown(self):
#         print("用例执行结束了")

# ------------------------------------------------------------------
import unittest
from API_AUTO.tools.http_request import HttpRequest
from API_AUTO.tools.get_data import GetData
from ddt import ddt,data
from API_AUTO.tools.do_excel import DoExcel
from API_AUTO.tools.project_path import *
from API_AUTO.tools.my_log import MyLog
from API_AUTO.tools.do_mysql import DoMysql
my_logger=MyLog()
test_data=DoExcel.do_excel(test_case_path)

@ddt
class TestHttpRequest(unittest.TestCase):
    def setUp(self):
        print("测试开始了")

    @data(*test_data)
    def test_http(self,item):
        my_logger.info("开始执行用例：{0}--{1}".format(item['case_id'], item['title']))
        if item['data.txt'].find('${loan_id}')!= -1 :# 请求之前完成loan_id的替换
            if getattr(GetData,'loan_id')==None:
                query_sql='select max(Id) from loan where MemberID={0}'.format(getattr(GetData,'loan_member_id'))
                loan_id=DoMysql().do_mysql(query_sql)[0][0]
                item['data.txt']=item['data.txt'].replace(('${loan_id}'),str(loan_id))
                setattr(GetData,'loan_id',loan_id)
                my_logger.info(loan_id)
            else:
                my_logger.info(getattr(GetData,'loan_id'))
                item['data.txt']=item['data.txt'].replace(('${loan_id}'),str(getattr(GetData,'loan_id')))
        my_logger.info("获取到的请求数据是:{0}".format(item['data.txt']))

        if item['check_sql']!=None:#当文件中check_sql不为空的时候，需要进行数据库校验
            my_logger.info("此条数据需要做数据库校验:{0}".format(item["title"]))
            query_sql=eval(item['check_sql'])['sql']#拿到了sql语句，注意是存在字典里面的（Excel）
            # print(query_sql)
            # 开始查询
            Before_Amount=DoMysql().do_mysql(query_sql,1)[0]#请求之前的账户余额
            my_logger.info("用例：{0}请求之前的余额是：{1}".format((item["title"]),Before_Amount))
            my_logger.info('----------开始http接口请求---------')
            res = HttpRequest().http_request(item["url"], eval(item["data.txt"]), item["http_method"],getattr(GetData, "Cookie"))
            my_logger.info('----------完成http接口请求---------')
            After_Amount = DoMysql().do_mysql(query_sql, 1)[0]#请求之后的账户余额
            my_logger.info("用例：{0}请求之后的余额是：{1}".format((item["title"]), After_Amount))
            print(abs(After_Amount))
            # 检查结果
            if float(eval(item["data.txt"])['amount'])== float(abs(Before_Amount-After_Amount)):#abs绝对值
                my_logger.info('数据库余额校验通过')
                check_sql_result = '数据库检查通过'
            else:
                my_logger.info('数据库余额校验未通过')
                check_sql_result = '数据库检查未通过'
            # 写回结果
            DoExcel.write_back(test_case_path, item["sheet_name"], item["case_id"]+1,10,check_sql_result)
        else:
            my_logger.info("此条数据不需要做数据库校验:{0}".format(item["title"]))
            my_logger.info('----------开始http接口请求---------')
            res = HttpRequest().http_request(item["url"], eval(item["data.txt"]), item["http_method"],getattr(GetData, "Cookie"))
            my_logger.info('----------完成http接口请求---------')
        if res.cookies:
            setattr(GetData,"Cookie",res.cookies)
        try:  # 抓取错误  异常处理
            self.assertEqual(str(item["expected"]), res.json()["code"])  # 断言
            # self.assertIn("登陆成功", res.json()["msg"])
            TestResult="PASS"
        except AssertionError as e:
            TestResult="failed"
            my_logger.info("test_api错误是{0}".format(e))
            raise e  # 异常处理之后需要抛出去
        finally:
            DoExcel.write_back(test_case_path, item["sheet_name"], item["case_id"]+1,8,str(res.json()))
            DoExcel.write_back(test_case_path, item["sheet_name"], item["case_id"]+1,9,TestResult)
            my_logger.info("获取到的结果是：{0}".format(res.json()))
    def tearDown(self):
        print("用例执行结束了")
