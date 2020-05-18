#-*-coding:utf-8-*-
# python的内置函数：
# 试错
# print input len type str int float list range
# pop append insert keys split replace srtip remove cleak click

# 总结一下函数的特点:
# 可以重复使用

# 函数的语法:def 关键字    define
# 函数命名的规范：小写字母  不能以数字开头 不同的字母之间用下划线隔开
# def 函数名(参数):
    #函数体：你希望这个函数去给你实现什么功能？

# 调用: 函数名()

# def da_lao(a):#形参  位置参数  2）def da_lao(name="花花")#默认参数
#     print("{0}是大佬".format(a))
# # 调用函数
# da_lao("小名")#实参
# da_lao("小风")

# 利用range函数请求1-100的连续整数相加功能，写成一个函数
# def add_numbers(m,n,k=1):#形参  位置参数    #:变量名 要在 变量名=值 前面
#     sum=0
#     for i in range(m,n,k):
#         sum=sum+i
#     print("求和值是:{0}".format(sum))

# add_numbers(1,5)#实际参数  1+2+3+4
# 默认情况下，按顺序赋值
# 默认参数  默认参数必须放在位置参数后面
# 第一步先用代码实现功能  还可以选取一组数据来证明自己的diamante是否正确
# 第二步变成函数   加def
# 第三步想办法提高代码的复用性

# 镜像文字
# 字符串的translate
# swapcase