#-*-coding:utf-8-*-
# 变量的作用域
# a=1#全局变量:在模块里面的都能调用
# def add(b):
#     # a=5#局部变量:函数的局部变量只能作用于函数
#     global a #声明这是一个全局变量
#     a=10 #赋值运算
#     print(a+b)
#
# add(10)
# print(a)
#全局变量和局部变量
# 1.作用范围不一样  #全局变量:在模块里面的都能调用  #局部变量:函数的局部变量只能作用于函数
# 2.当全局变量和局部变量同名且同时存在的时候  函数优先调用局部变量
# 3.当局部变量没有  就用全局
# 4.global

# import class_1031.function_01
# class_1031.function_01.add_num(1,100)


# def get_num(*args):
#     sum = 1
#     for i in args:
#         sum *= float(i)  # sum = 1 * float(i)
#     return sum / 2
#
# nums = input("请输入数字，如果是多个请用逗号隔开：")
# nums_list = nums.split(",")# split返回值是列表
# # print(nums_list)
# print(get_num(*nums_list))

# zip()
a = [1, 2, 3]
b = ['a', 'b', 'c']
new = zip(a, b)
print(dict(new)) # {1: 'a', 2: 'b', 3: 'c'}
# print(list(new))

# enumerate函数
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
list(enumerate(seasons))
#[(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
list(enumerate(seasons, start=1))       # 下标从 1 开始
#[(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]

cases = [['case_id', 'title', 'en'], ['1', '用例1', 'a'], ['2', '用例2', 'b'], ['3', '用例3', 'c'], ['4', '用例4', 'd']]
title = cases[0]
new_case = []
for case in cases[1:]:
    new_dict = {}
    for j, k in enumerate(case):
        new_dict[title[j]] = k
    new_case.append(new_dict)
print(new_case)


