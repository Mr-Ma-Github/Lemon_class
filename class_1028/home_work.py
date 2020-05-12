#-*-coding:utf-8-*-
# 习题1：
# 一个足球队在寻找10岁到12岁的小女孩（包括10和12岁），
# 编写一个程序，询问用户的性别（m表示男性，f表示女性）和年龄，
# 然后编写显示一条信息指出这个人是否可以加入球队，询问10次后，
# 输入满足条件的总人数
# 方法一：
# a=1
# count=0
# while a<=3:
#     age=int(input("请问你的年龄是:"))
#     if 10<=age<=12:
#         sex=input("请问你的性别是:")
#         if sex =="f":
#             print("恭喜你，可以加入我们的球队")
#             count=count+1
#         else:
#             print("很遗憾你的性别不符合要求")
#     else:
#         print("很遗憾你的年龄不符合要求")
#     a=a+1
# print("一共有{0}个人符合要求".format(count))
# 方法二：
# i=10
# count=0
# while True:
#     sex=input("请输入你的性别:" )
#     if sex=='f':
#         age=int(input("请输入你的年龄:"))
#         if 10<=age<=12:
#             print("恭喜你可以加入足球队!")
#             count+=1
#             i-=1
#         else:
#             print("很遗憾不满足加入条件")
#             i-=1
#     else:
#         print("很遗憾不满足加入条件")
#         i-=1
#     if i==0:
#         break#结束本轮循环，跳出循环
#     else:
#         continue#结束本轮循环，继续下一轮
# print("一共有{0}个人符合要求".format(count))
# 方法三：
# i=10
# count=0
# while i>0:
#     age = int(input("请问你的年龄是:"))
#     i=i-1
#     if 10<=age<=12:
#         sex=input("请问你的性别是:")
#         if sex =="f":
#             print("恭喜你，可以加入我们的球队")
#             count=count+1
#         else:
#             print("很遗憾你的性别不符合要求")
#     else:
#         print("很遗憾你的年龄不符合要求")
# print("一共有{0}个人符合要求".format(count))

# 2.输入num为4位数，对其按照如下的规则进行加密
# 1）每一位分别加5，然后分别将其替换为该数除以10取余后的结果
# 2）将该数的第1位和第4位互换，第二位和第三位互换
# 3)最后合起来作为加密后的整数输出
# num=int(input("请输入一个4位数："))


# 3、例如：password = {"admin":"123321","user1":"123456"}
# 1、设计一个登陆程序,不同的用户名和对应密码存在一个字典里面,输入正确的用户和密码去登陆
# 2、首先输入用户名,如果用户名不存在或者为空,则一直提示输入正确的用户名
# 3、当用户名正确的时候,提示去输入密码,如果密码跟用户名不对应,则提示密码错误请重新输入
# 4、如果密码输入错误超过三次,中断程序运行。
# 5、当输入密码错误时,提示还有几次机会
# 6、用户名和密码都输入成功的时候,提示登陆成功!!
# passwd = {"admin":"123","user1":"456"}
# count=3
# while True:
#     username = input("请输入用户名：")
#     if username in passwd.keys():
#         while count>0:
#             password=input("请输入密码：")
#             if password == passwd[username]:
#                 print("登录成功")
#                 break
#             else:
#                 print("密码不正确，请重新输入")
#                 count-=1
#                 print("你还有{0}次机会".format(count))
#         break
#     elif username not in passwd.keys()or username=='':
#         print("用户名不正确，请重新输入")
