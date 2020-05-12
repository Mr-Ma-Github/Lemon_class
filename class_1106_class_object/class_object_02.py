#-*-coding:utf-8-*-
# 类与对象
# class 命名规范:  首字母大写   驼峰命名   见名知意
# 类的概念   具有某一类共同属性和特性的事物
# 类一般包含  属性以及方法
class  Teacher:
    def __init__(self,name,age=23):#初始化函数。实例方法,一般不传动态参数和关键字参数
        self.name=name
        self.age=age
        self.height='170'
    #初始化函数没有return返回值
    def play_game(self,play_game):
        return (self.name+"会玩{0}".format(play_game))

    def coding(self,lines,language='python'):#实例方法
        print(self.name+"会写{0}代码.写了{1}行代码".format(language,lines))

    def cooking(self,*args):#实例方法
        for item in args:
            print(self.name+"会制作{}".format(item))

    def teacher_info(self):
        self.cooking("海鲜大餐","疙瘩汤")#参数是写死的
        print("{0}老师今年{1}岁,身高{2},可以嫁人了".format(self.name,self.age,self.height))
    def teacher_info_2(self,*args):
        self.cooking(*args)#参数不是写死的
        print("{0}老师今年{1}岁,身高{2},可以嫁人了".format(self.name,self.age,self.height))

    @classmethod
    def swimming(cls):
        print("还非常会唱歌")

    @staticmethod
    def sing(a):
        print("{0}会唱歌".format(a))
# 类方法分为三种：
# 实例方法意味着这个方法   只能实例来调用
# t=Teacher()#实例   隐式的传递
# t.cooking()
# Teacher.coding(t)#显示的传递    不建议使用
# # Teacher().coding()#类自己实例化

# Teacher.coding()   #要先实例化才能调用Teacher().coding()
# #TypeError: coding() missing 1 required positional argument: 'self'

# 类方法   @classmethod
# Teacher.swimming()
# t.swimming()
# 类方法和静态方法可以直接  类名.方法调用,也可以通过实例调用
# 静态方法：@staticmethod
# Teacher.sing()
# t.sing()

# 1.实例方法self 类方法cls  静态方法（普通方法） 实例和类名都可以直接调用
# 2.不同点：静态方法和类方法 不可以调用类里面的属性值  如果需要参数  只能自己传递
# 3.当某个函数与其他的类函数、类属性没有任何关系  才会定义为静态方法和类方法
# 4.如果类中有__init__这个方法，在创建类的实例的时候，就必须要有和方法__init__匹配的参数

# t1=Teacher("花花")#
# print(t1.play_game('LOL'))
# t1.coding(1000)
# t1.cooking('蛋炒饭','回锅肉','西红柿炒鸡蛋')
# t1.teacher_info()
# t1.swimming()
# t1.sing('赤道的边境，万里无云，天很晴')

# t2=Teacher("朵朵")
# t2.teacher_info()

t3=Teacher("多多").teacher_info_2("糖醋排骨","红烧鱼")













# for i in range(100):
#     Teacher(Teacher.name)
#     print(Teacher.name)








