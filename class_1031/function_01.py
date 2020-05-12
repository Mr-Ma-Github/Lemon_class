#-*-coding:utf-8-*-
# return  当你调用函数的时候  就会返回一个值，return后面的表达式
# 在函数里面相当于一个结束符合  表示函数到此为止
# def add_num(m,n,k=1):#形参  位置参数
#     sum=0
#     for i in range(m,n,k):
#         sum=sum+i
#     return sum
#
# add_num(1,5)
# print(add_num(1,5))

# def add_two(a,b):
#     return (a+b)
#     print("不能打印出来")
# 1、写函数 检查传入列表的长度，如果大于2，那么仅仅保留的两个长度的内容，并将新内容返回
# def check_list(L):
#     if len(L)>2:
#         new_list=L[0:2]
#     return new_list
# L=[1,2,3,4]
# new_list=check_list(L)
# print(new_list)

# 动态参数/不定长参数   *args   arguments   格式：* 变量名   (必须*)
# 在
# def make_sandwich(*args):
#     # print(args)
#     b=""
#     for a in args:
#         b=b+a
#         b+="、"
#     print("你的三明治包含了"+b)
#
# make_sandwich("生菜","鸡蛋","培根","牛肉")
# make_sandwich()

# 关键字参数  key value  **kwargs  格式：** 变量名   (必须**)
# 在函数里面体现为  字典
# 第一种：
# def kw_function(**kwargs):
#     print(kwargs)
# kw_function(x=1,y=2)
# 第二种：
# def kw_function(**kwargs):
#     print(kwargs)
# kwa={'x':1,'y':2}
# kw_function(**kwa)

# def sum_1(a,*k,**l):
#     print(k)
#     sum=0
#     for i in k:
#         sum+=i
#     print("总和为",sum)
#     print("a的值",a)
#     print("l的值", l)
# #
# sum_1(1,2,3,4,5,x=1,y=2)





def add_num(m,n,k=1):#形参  位置参数
    sum=0
    for i in range(m,n,k):
        sum=sum+i
    print("最后的结果值",sum)

if __name__ == '__main__':#主程序的执行入口  只有当你在当前模块执行时，才会执行
    add_num(1,101)