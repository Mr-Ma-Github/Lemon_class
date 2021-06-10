#-*-coding:utf-8-*-
#@作者：haiyu.ma
#@创建日期：2019-12-13 18:29
# import mysql.connector   #mysql数据库需要安装mysql/pymysql/mysql.connector包
# # import psycopg2           #postgresql数据库需要安装psycopg2包
# db_config={'host': '47.107.168.87','user': 'python',
#            'password': 'python666','port':3306,'database': 'future'}
# # 创建一个数据库连接
# cnn=mysql.connector.connect(**db_config)
# # 游标cursor()
# cursor=cnn.corsor()
# # 写sql语句--字符串
# query_sql='select max(MobilePhone)from member'
# # query_sql='select MobilePhone from member where Id<23504'
# # 执行语句
# cursor.execute(query_sql)
# # 获取结果  打印结果
# res=cursor.fetchone()#元祖   针对一条数据
# # res=cursor.fetchall()#列表(列表嵌套元祖)   针对多条数据
# print(res)
# print(int(res[0])+1)
# 提交保存（查询不需要提交）
# cnn.commit()
# # 关闭游标
# cursor.close()
# # 关闭连接
# cnn.colse()
# -----------------------------------------------------
# lims数据库:
import pymysql
from API_AUTO.tools.case_config import ReadConfig
from API_AUTO.tools import project_path
from pymysql.cursors import DictCursor
class DoMysql:
    def do_mysql(self,query_sql,state='all'):
        db_config=eval(ReadConfig.get_config(project_path.case_config_path,'DB','db_config'))
        cnn=pymysql.connect(**db_config)
        cur=cnn.cursor()
        cur.execute(query_sql)
        if state==1:
            res = cur.fetchone()#元祖   针对一条数据
        else:
            res = cur.fetchall()#元祖(元祖嵌套元祖)   针对多条数据
        cur.close()
        cnn.close()

        return res
if __name__ == '__main__':
    res=DoMysql().do_mysql("select max(CLIENT_PHONE)from CQ_CLIENT where CLIENT_PHONE like'156%'")
    print(res)
    # print(int(res[0]['max(CLIENT_PHONE)'])+1)
    # print(int(res[0][0])+1)


# ------------------------------------------
# import psycopg2           #postgresql数据库需要安装psycopg2包
# conn = psycopg2.connect(host="10.10.10.113",user="postgres",password="postgres",port=5432,dbname="clinical_repository_test")
# # print("Opened database successfully")
# cur=conn.cursor()
# cur.execute("select max(cellphone)from cr_patient where cellphone like '178%'")
# res=cur.fetchall()
# print(res)
# # print(int(res[0])+1)#fetchone
# # print(int(res[0][0])+1)#fetchall
# cur.close()
# conn.commit()
# conn.close()

##--拓展--o
# import pymysql
#
# # 链接数据库
# conn = pymysql.connect(host='192.168.1.115',  # ID地址
#                        port=3308,  # 端口号
#                        user='root',  # 用户名
#                        passwd='123456',  # 密码
#                        db='任务协作',  # 库名
#                        charset='utf8')  # 链接字符集
# '''
# connect常用方法：
# begin()：            开启事务
# commit()：           提交事务
# cursor()：           创建游标
# ping()：             检查链接是否存活，会重新发起链接
# rollback()：         回滚事务
# close()：            关闭链接
# select_db()：        选择数据库
# show_warnings()：    查看warnings信息
# '''
#
# # 游标就相当于是一辆货车，把程序中的sql语句运送到数据库中执行，所以要先叫一辆货车，即创建游标cursor
# cur = conn.cursor()  # 创建游标
# cur.execute('select * from 员工资料')  # 然后往货车上搬货物，让游标带上sql 执行语句
#
# '''
# cursor(游标)核心方法
# execute()：          执行单条语句
# executemany()：      执行多条语句
# fetchone()：         获取第一行
# fetchmany(size)：    获取下几(size)行
# fetchall()：         获取剩下所有的行
# scroll(num,mode)：   移动游标
# rowcount：           计算corsor的行数
# description：        返回字段信息
# close()：            关闭游标
# '''
#
# data1 = cur.fetchone()  # 从货车（游标cursor）上取一件货物看看 获取第一行数据
# print(data1)
#
# data2 = cur.fetchmany(3)  # 此时货车中的第一行已经取走了，那么这里在取2行，则是从剩下的货物中取
# print(data2)
#
# data3 = cur.fetchall()  # 获取货车中剩下的所有数据
# print(data3)
#
# cur.scroll(0, mode='absolute')  # 移动游标(绝对位置移动，以整个cursor作为起点)
# data4 = cur.fetchall()  # 获取所有数据
# print(data4)
#
# cur.scroll(-1, mode='relative')  # 移动游标位置(相对位置移动，以当前位置作为起点)
# data5 = cur.fetchall()  # 获取最后一行数据
# print(data5)
#
# cur.close()  # 关闭游标
# conn.close()  # 关闭数据库