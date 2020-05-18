#-*-coding:utf-8-*-
# 循环 for   while
# python for循环语法：
# for 变量名 in 某个数据类型：（数据类型包含：字符串  列表  元祖  字典  集合等）
    #代码块
#in？成员运算符  in
# for循环的循环次数 由数据中的元素个数决定
# a="hello"
# b=[1,2,3]
# c={"age":"18","name":"剑豪"}#字典类型的数据，返回的是key，print(c[a])
# for item in a:#for循环遍历a中每一个元素，然后赋值给变量item
#     print(item)
# L=[5,6,9,3,7]#请 利用for循环 完成列表中所有数据的相加
# sum=0
# for a in L:
#     sum=sum+a
# print(sum)

# range函数：生成整数序列
# range(m,n,k)m头默认为0 n尾 k步长默认为1，取头不取尾
# range(1,5)
# print(list(range(1,5)))
# print(list(range(8)))#头默认为0，从0开始
# for item in range(3):#0,1,2
# L=[5,6,9,3,7]# 请利用for循环 根据L的索引值，打印出每个元素的值
# for i in range(len(L)):
#     print(L[i])

# 一个班级有一个花名册，存在列表里面
# 从控制台输入一个名字，如果这个名字在名册里面
# 就打印这个用户名正确，如果不存在那就报错
# name=["小名","小红","小花","小风"]
# username=input("请输入你的名字:")
# if username in name:
#         print("用户名正确")
# else:
#         print("你的名字输入有误")

# while  控制循环
#while   条件表达式   # 逻辑  成员  比较  空数据(与if语句一致)#   布尔值
    # 代码块
# 执行规律：首先判断while后面的条件表达式是否成立
# 如果True，那么执行代码块，执行完毕后，继续判断-->如果还是True，再次执行代码块....
# 否则 不进入代码块
# 防止代码进入死循环，加一个变量来控制
# while True:#死循环
#     print("不可能结束")
# a=1#初始值
# while a<=10:
#     print("现在是第{}次循环".format(a))
#     a=a+1
# 利用while循环  实现1-100的整数相加
sum=0#求和初始值
a=1#循环的起始值
while a<=100:
    sum=sum + a
    a=a+1
print(sum)
# while 与 if语句搭配使用break continue
count=0
while 1:#非0的正数都相当于是TRUE
    print("while语句执行")
    count+=1
    if count == 10:
        break
    else:
        continue  #结束当次执行，继续下一轮执行
