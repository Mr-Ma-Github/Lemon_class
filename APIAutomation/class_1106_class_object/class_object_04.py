#-*-coding:utf-8-*-
# debug-->哪行代码出错  就debug哪一行

# 超继承  super() 函数是用于调用父类(超类)的一个方法
class MathMethod:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        print(self.a+self.b+1)
    def sub(self):
        return self.a-self.b
class MathMethod_1(MathMethod):
    def divide(self):#拓展
        return self.a/self.b
    def add(self):#重写
        super(MathMethod_1, self).add()## 超继承：想用父类的方法，又不想重写
        print(self.a+self.b+10)

MathMethod_1(3,4).add()