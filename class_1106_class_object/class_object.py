#-*-coding:utf-8-*-
# python类  抽象的概念，类的划分标准，写代码的人来定
# 类的语法   关键字class
# class  类名: #类名的规范是数字、字母、下划线组成 (不能以数字开头  首字母大写  驼峰命名)
    #类属性  #写在类里面的变量值-例如：a=1                          (不是必须)
    #类方法  #写在类里面的函数                                      (不是必须)
class BoyFriend:
    #类属性
    height=180
    weight=130
    money="500万"
    #类函数
    def cooking(self):#self  代表实例本身(可以当成固定的占坑符)
        print(self)
        print("男人要会做饭")
    def earn(self):# 类里面的方法  都必须带self这个参数
        print("月薪过万")

# 实例/对象  具体的一个例子      ##格式：类名()
# 实例/对象具有类里面的所有的属性和方法的使用权限
bf=BoyFriend()#创建一个对象   调用类    #这就是一个实例
# print(bf)
# 调用属性：  实例名.属性名
print(bf.money)
# 调用方法：  实例名.方法/函数名()      def 开头的才是函数
bf.cooking()

# BoyFriend.cooking()#应该先对类进行实例化，然后在应用类
BoyFriend().cooking()















