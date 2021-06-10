#-*-coding:utf-8-*-
#@作者：haiyu.ma
#@创建日期：2020-08-20 23:34
# 多重继承
# 菱形问题/砖石问题

'''
广度优先：
深度优先：

c3算法：

'''
# 深度优先：
# class A:
#     def play(self):
#         print("a is a playing")
#
# class B(A):
#     # def play(self):
#     #     print("b is a playing")
#     pass
#
# class C():
#     def play(self):
#         print("c is a playing")
#
# class D(B, C):
#     # def play(self):
#     #     print("d is a playing")
#     pass
#
# d = D()
# d.play()
# # 查找顺序
# print(D.__mro__)
#
# # 广度优先：
# class A:
#     def play(self):
#         print("a is a playing")
#
# class B(A):
#     # def play(self):
#     #     print("b is a playing")
#     pass
#
# class C(A):
#     def play(self):
#         print("c is a playing")
#
# class D(B, C):
#     # def play(self):
#     #     print("d is a playing")
#     pass
#
# d = D()
# d.play()
# # 查找顺序
# print(D.__mro__)


# attribute：属性
class GetData:
    cookie = "小明"

# print(GetData.cookie)
# getattr：获取属性（动态获取某个属性的函数）
# getattr(对象或者类名，属性名称，当没有此属性的时候需要提供的默认值)
# print(getattr(GetData, 'cookie'))#获取这个属性
# print(getattr(GetData, 'other', 'test'))#没有other这个属性，所以test就是other的值

# setattr：设置属性（动态获取某个属性的函数）
# setattr(对象或者类名，属性名称，赋值的新值)
# 不管属性存不存在，都会赋值新值
# setattr(GetData,'cookie',"小红")#可以直接把类里面的属性值修改
# print(GetData.cookie)
# setattr(GetData, 'other', 'test')
# print(GetData.other)

# hasattr：判断属性是否存
# hasattr(对象或者类名，属性名称)  #返回值是True、False
# print(hasattr(GetData,'cookie'))#判断是否有这个属性值
# print(hasattr(GetData,'c'))

# delattr(GetData,'cookie')       #删除这个属性

# ---------------------------------
a = ' '
# 当值为False，'', [], {}, 0, None, ()   为false
# 注意：' '空格为true
if a:
    print("hello world!")# 为true则打印，为false则不打印