#-*-coding:utf-8-*-
# debug-->哪行代码出错  就debug哪一行

# 超继承  super() 函数是用于调用父类(超类)的一个方法
# 语法：
# super().父类方法名
# super(子类名, self).父类方法名
class MathMethod:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        print(self.a+self.b+1)

    def sub(self):
        return self.a-self.b


class MathMethod_1(MathMethod):
    def divide(self):#拓展
        return self.a/self.b

    def add(self):#重写
        # super(MathMethod_1, self).add()## 超继承：想用父类的方法，又不想重写  # python3
        super().add()   # python3
        print(self.a+self.b+10)

# print(MathMethod_1(3, 3).divide())
MathMethod_1(3, 4).add()


# debug：调试
# 1.最简单的方式：print()     缺陷：1.要写入print  2.调试完成后还要删除print
# 2.出现问题后，print出来然后百度
# 3.打断点(优先使用)
'''
如果使用debug模式：
1.鼠标右击，Debug按钮。配合断点使用
2.断点：程序运行到红点的地方会暂停
Step Over(F8):下一步，单步调试
Resume Program(F9):进入到下一个断点
Run To Cursor:运行到光标所在位置
Step Into(F7)：进入对应的代码
Step Into My Code(Ait+Shift+F7)：进入自己写的代码（内置库进不去）
Step Out(Shift+F8)：退出

'''