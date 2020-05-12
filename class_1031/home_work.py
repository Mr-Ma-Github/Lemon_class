#-*-coding:utf-8-*-
# 1.输入num为四位数,对其按照如下的要求进行加密
# 1)每一位分别加5,然后分别将其替换为该数除以10取余后的结果
# 2)将该数的第一位和第4为互换,第二位和第三位互换
# 3)最后合起来作为加密后的整数输出
# num=input("请输入4位数：") #input是从控制台获取数据  都是字符串形式
# new_num=""
# for item in num:
#     a=int(item)+5
#     # print(item)
#     print("每一位加5然后除以10",(int(item)+5)%10)
#     new_num+=str((int(item)+5)%10)
# last_str=new_num[::-1]
# print(last_str)

# 2.输入一个有*组成的直角三角形
# *
# **
# ***
# ****
# *****
# for i in range(1,6):#控制了行数
#     print("*"*i)

# for i in range(1,6):#控制了行数
#     for j in range(1,i+1):#range(1,2)-->1
#         print("*",end="" )#end=""   是为了不让它换行
#     print()#print语句会换行

# 3.写一段程序 分别求出1-101之间的所有偶数的和和所有奇数的和
# sum_1=0
# sum_2=0
# for i in range(1,101):
#     if i%2==0:
#         sum_2+=i
#     else:
#         sum_1+=i
# print("所有偶数的和："+str(sum_2))
# print("所有奇数的和：",sum_1)

# 4.输入一个有*组成的等边三角形，且边长都为5个*
# @@@@*
# @@@* *
# @@* * *
# @* * * *
# * * * * *
# for i in range(1,6):#控制了行数
     # 一个for控制@的输出
     #一个for控制"* "的输出
#     for j in range(1,6-i):#控制@符合4 3 2 1 0
#         print(" ",end="")
#     for k in range(1,i+1):
#         print("* ",end="")
#     print()

# 5.输出99乘法表：
# 1*1=1
# 1*2=2	2*2=4
# 1*3=3	2*3=6	3*3=9
# 1*4=4	2*4=8	3*4=12	4*4=16
# 1*5=5	2*5=10	3*5=15	4*5=20	5*5=25
# 1*6=6	2*6=12	3*6=18	4*6=24	5*6=30	6*6=36
# 1*7=7	2*7=14	3*7=21	4*7=28	5*7=35	6*7=42	7*7=49
# 1*8=8	2*8=16	3*8=24	4*8=32	5*8=40	6*8=48	7*8=56	8*8=64
# 1*9=9	2*9=18	3*9=27	4*9=36	5*9=45	6*9=54	7*9=63	8*9=72	9*9=81
# for i in range(1,10):
#     for j in  range(1,i+1):
#         print("{1}*{0}={2}\t".format(i,j,i*j),end='')#end=""   是为了不让它换行
#     print()

# 6.经典冒泡算法：利用for循环  完成a=[1,7,4,89,34,2]的冒泡排序
# 冒泡排序：小的排前面，大的排后面
# 排序 最终使得数组中的这几个数字按照从小到大的顺序排列
# 相邻的两个元素依次比较
# a=[1,7,4,89,34,2]#冒泡算法    一般最多比较n-1次就完成
# for i in range(0,len(a)-1):#0 1 2 3 4 5
#     for j in range(0,len(a)-1):
#         if a[j]>a[j+1]:
#             a[j],a[j+1]=a[j+1],a[j]
# print(a)

# # 冒泡排序
# list = [23, 342, 43, 56, 76, 14, 564]
# s = 0
# for i in range(len(list) - 1):  # 控制次数
#      #  总数的个数减去第几次排，可以得到要该次要排几下      （规律）
#     for a in range(len(list) - i - 1):  # 控制排几下
#         if list[a] >= list[a + 1]:
#             s = list[a]  # 交换位置
#             list[a] = list[a + 1]
#             list[a + 1] = s
#         else:
#             pass
# print(list)
#
# # 内层控制每次排几下，直接根据图表来算
# # 外层控制排几次，i的值等于几时就是第几次排
# # for i in range(1, len(list), 1):
# #     for a in range(0, len(list) - i, 1):

# 1.写一个函数,可以完成任意指定整数的相加,并返回结果
# def add_sum(a,b):
#     sum=a+b
#     print(sum)

# add_sum(1,2)

# 2.自动販卖机:只接受1元、5元、10元的纸币或硬币,可以1块，5元,10元。最多不超过10块钱。
# 饮料只有橙汁、椰汁、矿泉水、早餐奶,售价分别是3.5,4,2,4.5 写一个函数用来表示販卖机
# 的功能:用户投钱和选择饮料,并通过判断之后,给用户吐出饮料和找零。
# 分析：
# 选择饮料：字典
# 投钱：1  5  10  判断金额的面值
# 判断：钱不够   钱多了的情况   钱刚好的情况
# def Vending_machines(money):
drinks={"1":3.5,"2":4,"3":2,"4":4.5}
total=0#储存我们购买饮料的总金额
change=0
choose=int(input("请选择饮料：1.橙汁、2.椰汁、3.矿泉水、4.早餐奶------:"))

if choose in drinks.keys():
    total+=drinks[choose]
else:
    print("不存在该选项，请重新选择")






    # money= float(input("请投入钱币："))
    # while total<3.5:
    #     money_2=float(input("钱币不足，请继续投入:"))
    #     total=total+money
    #     total=total+money_2
    #     break
    # print("请拿走你的饮料")
    # if money==drinks["1"]:
    #     change=money-drinks["1"]
    #     print("请拿走你的饮料")
    # elif 10>=money>drinks["1"]:
    #     change=float(money-drinks["1"])
    #     print("请拿走你的饮料和剩余的%1f元零钱"%(change))
    # elif money>10:
    #     print("不接受10元以上钱币")






# 3.写函数,将 姓名、性别,城市作为参数,并且性别默认为f(女)。如果城市是在长沙并且性别为女,
# 则输出姓名、性别、城市,并返回True,否则 返回False
# def function_001(name,city,sex="f"):
#     if city =="长沙"and sex=="f":
#         print(name,city,sex)
#         print(True)
#     else:
#         print(False)
#
# function_001("小明","长沙","f")
# 4.定义一个函数,成绩作为参数传入。如果成绩小于60,则输出不及格。如果成绩在60到80 之间,
# 则输出良好 ;如果成绩高于80分,则输出优秀,如果成绩不在0-100之间,则输出成绩输入错误。
# def score(a):
#     if 0<a<60:
#         print("本次考试成绩不合格")
#     elif 60<=a<=80:
#         print("良好")
#     elif 80<a<=100:
#         print("优秀")
#     else:
#         print("成绩输入错误")
#
# score(1000)
