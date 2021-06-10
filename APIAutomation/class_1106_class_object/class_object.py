#-*-coding:utf-8-*-
# 1.类：具有相同特征的某一些事务的种类，集合

# python类  抽象的概念，类的划分标准，写代码的人来定
# 类名也是标识符
# 类名的规范是数字、字母、下划线组成且不能以数字开头
# 能是关键字
# 驼峰命名-最好是大驼峰

# 类的语法   关键字class
# class  类名:
    #类属性  #写在类里面的变量值-例如：a=1                          (不是必须)
    #类方法  #写在类里面的函数                                      (不是必须)

class BoyFriend:
    #类属性
    height=180
    weight=130
    money="500万"

    def __init__(self, name, age):
        '''定义具体的对象，初始化函数、初始化方法。'''
        self.name = name
        self.age = age
        pass

    #类函数
    def cooking(self):#self  代表实例本身(可以当成固定的占坑符)
        print(self)
        print(self.__dir__())
        print("男人要会做饭", self.height)

    def earn(self):# 类里面的方法  都必须带self这个参数
        print("月薪过万")


bf = BoyFriend(1,2)
bf.cooking()

# 类的使用、类的实例化、对象化
# 使用整个类
# print(BoyFriend)
# 使用类当中的一个对象
# print(BoyFriend())
# 实例/对象  具体的一个例子      ##格式：类名()
# 实例/对象具有类里面的所有的属性和方法的使用权限
# bf = BoyFriend.money#创建一个对象   调用类    #这就是一个实例
# print(bf)

# 类的属性：包含类属性和实例化属性
# 类属性：类集体的属性
# 1）类属性：所有成员都具备的属性
# 类里面表示的变量，就是属性。类属性又称为类变量

# 调用属性：  类名.属性名
# print(bf.money)
# 类属性的修改：类名.属性名 = 新值
# bf.money = 500
# print(bf.money)

# 2）实例属性：实例变量
# 类成员自己独有的特征，并不是每个类成员都有
# 如何表示实例属性：__init__里面：self.属性名 = 属性值
# 实例属性的使用：实例名称（不是类名）.属性名
# bf = BoyFriend("小名", 1).name
# print(bf)

# print(BoyFriend("小名", 1).age)

# 如何去定义一个具体的对象？
# 具体的对象的定义：在类的下面定义具体的函数名称：__init__(self,参数1,参数2,参数3)

# 如何去使用对象？初始化一个对象
# 初始化对象：类名(参数1,参数2,参数3)

# 3）类方法
# 调用方法：  实例名（不是类名）.方法/函数名()      def 开头的才是函数
# bf = BoyFriend("小名", 1)
# bf.cooking()

# BoyFriend.cooking()#应该先对类进行实例化，然后在应用类
# BoyFriend().cooking()


"""
getattr：获取属性（动态获取某个属性的函数）
getattr（对象或类名，属性名称，当没有此属性的时候，需要提供默认值）
"""
# print(getattr(BoyFriend, 'height'))
# print(getattr(BoyFriend, 'height', 169))
# print(getattr(BoyFriend, 'name'))  # AttributeError: type object 'BoyFriend' has no attribute 'none'
# print(getattr(BoyFriend, 'name', '124'))
# bf = BoyFriend("小名", 1)
# print(getattr(bf, 'height'))
# print(getattr(bf, 'height', 169))
# print(getattr(bf, 'name'))
# print(getattr(bf, 'name1', '124'))

"""
setattr：设置属性（动态获取某个属性的函数）
setattr（对象或类名，属性名称，赋值的新值）
不管属性存不存在，都会赋值给新的值
"""
# setattr(BoyFriend, 'he', 'mei')
# print(BoyFriend.he)
# setattr(BoyFriend, 'height', 'mei')
# print(BoyFriend.height)
# setattr(BoyFriend, 'name', 'jdk')
# print(BoyFriend.name)
# bf = BoyFriend("小名", 1)
# setattr(bf, 'he', 'mei')
# print(bf.he)
# setattr(bf, 'name', 'xiaomei')
# print(bf.name)
# setattr(bf, 'height', '1456')
# print(bf.height)










