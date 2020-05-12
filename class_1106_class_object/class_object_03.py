#-*-coding:utf-8-*-
# 继承
class RobotOne:# 第一代机器人
    def __init__(self,year,name):
        self. year=year
        self. name=name
    def walking_on_ground(self):
        print (self.name+"只能在平地上行走,有障碍物就会摔倒")
    def robot_info(self):
        print("{0}年产生的机器人{1},是中国研发的".format(self.year,self.name))
    def other(self):
        print("第三代机器人"+self.name+"可以调用第一代的函数")
# 继承
# class RobotTwo(RobotOne):#第二代机器人继承于第一代机器人的类
#     def walking_on_ground(self):#之类里面的函数名与父类函数名重复的时候，就叫重写
#         print(self.name +"可以在平地上平稳的行走")
#     def walking_avoid_block(self):#拓展
#         self.robot_info()#在子类里面调用父类的函数
#         print(self.name +"可以避开障碍物")

# 继承的类  是否要用到初始化函数  请看是否从父类中继承
# 父类有的  继承后 我都可以直接拿来用
# 父类有   之类也有重名的函数   那么子类的实例就优先调用子类的函数
# r2=RobotTwo("1990","小二")
# # r2.robot_info()
# r2.walking_avoid_block()
# r2.walking_on_ground()

# r1=RobotOne("1988","小一")
# r1.robot_info()
# r1.walking_on_ground()

# 为了多继承，新创建一个第二代机器人
class RobotTwo():
    def __init__(self,name):
        self. name=name
    def walking_on_ground(self):
        print(self.name +"可以在平地上平稳的行走")
    def walking_avoid_block(self):
        print(self.name +"可以避开障碍物")
#多继承
# 第三代机器人
class RobotThree(RobotTwo,RobotOne):#第三代机器人继承于第一代和第二代机器人的类
    def jump(self):
        print(self.name +"可以单膝跳跃")
    def walking_avoid_block(self):#重写
        self.other()
        print(self.name +"完全无视障碍")

r3=RobotThree("小三")
r3.jump()
r3.walking_on_ground()
r3.walking_avoid_block()
# r3.robot_info()# 写函数时注意（或者重写）：没有传递year参数，调用robot_year的时候就会报错
# 多继承的子类具有两个父类的属性和方法  如果两个父类具有同名方法的时候
# 子类调用函数就近原则   初始化函数也包括在内