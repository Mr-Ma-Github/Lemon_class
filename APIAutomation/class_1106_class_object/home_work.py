#-*-coding:utf-8-*-
# 1.编写一个软件测试工程师类,属性与函数自己定。
# 创建一个名为 User 的类,其中包含属性 first_name（名字）和 last_name（姓氏）,
# 还有用户简介通常会存储的其他几个属性。在类 User 中定义一个名为
# describe_user() 的方法,它打印用户信息摘要:再定义一个名为
# greet_user() 的方法,它向用户发出个性化的问候。创建多个表示不同用户
# 的实例,并对每个实例都调用上述两个方法。
# class User:
#     def __init__(self,first_name,last_name):
#         self.first_name=first_name
#         self.last_name=last_name
#
#     def describe_user(self):
#         print("{1}{0}的姓氏是{1}，名字是{0}".format(self.first_name,self.last_name))
#     def greet_user(self,content):
#         print(self.last_name+self.first_name+content)

# 方法一：
# User("alisa","赵").describe_user()
# 方法二：
# m=User("先生","马")
# m.describe_user()
# m.greet_user("，你今天怎么了")

# 2:定义一个学生类。
# 1）有下面的类属性：1.姓名 2.年龄 3.成绩（语文、数学、英语）
# [每课成绩的类型为整数],均放在初始化函数里面。
# 2) 实例方法：
# a)获取学生的姓名:get_name ()返回类型:str
# b)获取学生的年龄:get_age ()返回类型: int
# c)返回三门科目中最高的分数 get_course ()返回类型::int
# 写好类以后,可以定义2个同学测试下:zm = Student('zhangming',20, [69, 88, 100])
# 返回结果: zhangming  20  100
# class Student () :
#     def __init__(self, name, age, grade):
#         self.name=name
#         self.age=age
#         self.grade=grade
#
#     def get_name(self):
#         return
#     def get_age(self):
#         return
#     def get_scose(self):
#         return max(self.grade)

# s=Student("小明",20,[69,78,198])
# print(s.name)
# print(s.age)
# print(s.get_scose())

# class Student () :
#     def __init__(self, name, age, grade):
#         self.name=name
#         self.age=age
#         self.grade=grade
#
#     def get_name(self):
#         return self.name
#     def get_age(self):
#         return self.age
#     def get_scose(self):
#         return max(self.grade)
#
# s=Student("小明",20,[69,78,198])
# print(s.get_name())
# print(s.get_age())
# print(s.get_scose())

# 拓展：如果我的成绩放在字典里面
# grade={"语文":60,"数学":80,"英语":100}
# 高阶函数  sorted

# 3.按照以下要求定义一个游乐园门票类，并创建实例调用函数
# 完成儿童和大人的总门票价统计（人数不定，由你输入的人数个数来决定）
# 1）平日票价100元
# 2）周末票价为平日票价120%
# 3.儿童半价
# class CostTicket:
#     def __init__(self,price=100):
#         self.price=price
#         total=0
#
#     def cost_ticket(self):#统计票价
#         # total=0
#         day=int(input("你需要购买哪天的票，1-5分别代表周一到周五，6-7代表周末两天"))
#         man=input("请输入你需要购买的成人票数量")
#         child=input("请输入你需要购买的儿童票数量")
#         if day in range(1,6):
#             total=int(man)*self.price+int(child)*self.price*0.5
#         elif day in range(6,8):
#             total=int(man)*self.price+int(child)*self.price*1.2*0.5
#         else:
#             print("你的输入有误")
#         return total
#
# total=CostTicket().cost_ticket()
# print("你总共需要支付{0}元".format(total))

# 3、人和机器猜拳游戏写成一个类,有如下几个的数:
# 1)函数1:选择角色1曹操2张飞3刘备
# 2)函数2:角色猜拳1剪刀2石头3布 玩家输入一个1-3的数字
# 3)函数3:电脑出拳随机产生1个1-3的数字,提示电脑出拳结果
# 4)函数4:角色和机器出拳对战,对战结束后,最后出示本局对战结果..赢 输
# 然后提示用户是否继续?按y继续,按n退出。
# 5)最后结束的时候输出结果 角色赢几局 电脑赢几局,平局几次 游戏结束
import random#随机
class GuessingGame:
    def get_user(self):#获取角色
        self.user={1:"曹操",2:"张飞",3:"刘备"}
        self.fist = {1: "剪刀", 2: "石头", 3: "布"}
        num=0
        while num == 0:
            self.choose_role = int(input("请选择一个角色(1曹操2张飞3刘备)："))
            if self.choose_role in self.user:
                print("{0}请出拳".format(self.user[self.choose_role]))#字典[key]等于字典的value
                break
            else:
                print("角色选择有误,请重新输入")
    def people_fist(self):#人类出拳
        num=0
        while num == 0:
            guessing = int(input("请选择招式(1=剪刀2=石头3=布):"))
            if guessing in self.fist:
                num = 1
                print("{0}出的是{1}".format(self.user[self.choose_role],self.fist[guessing]))
                return guessing
            else:
                print("出拳错误，请重新出拳")
    def get_computer_fist(self):#同时出拳
        fist_num=random.randint(1,3)#从一到三里随机选择一个数字
        print("电脑出的是{0}".format(self.fist[fist_num]))
        return fist_num

    def play_game(self):
        people_win=0
        pc_win=0
        draw=0
        while True:
            self.get_user()
            guessing=self.people_fist()
            computer=self.get_computer_fist()
            if guessing-computer==1 or guessing-computer==-2:
                print("角色赢")
                people_win+=1
            elif guessing-computer==-1 or guessing-computer==2:
                print("电脑赢")
                pc_win+=1
            elif guessing-computer==0:
                print("平局")
                draw+=1
            hint=input("您是否要继续？按y继续，按n退出")
            if hint=="n":
                break
        print("角色赢了{0}局，电脑赢了{1}局,平{2}局".format(people_win,pc_win,draw))

game=GuessingGame().play_game()
