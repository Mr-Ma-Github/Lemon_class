#-*-coding:utf-8-*-
# 列表：list 符号[]  中括号
# 1.可以存在空列表a=[]
# 2.列表里面可以包含任何类型的数据
# 3.列表里面的元素根据逗号进行分隔
# 4.列表里面也有索引，索引值也是从零开始
# # 5.获取列表里面的单个值，列表名[索引值]
# a=[1,0.02,'hello',[1,2,3],True]
# print(len(a))
# print(a[::-1])
# print(a[-1])
# 6.列表的切片与字符串的操作是一样的   列表名[索引头:索引尾:步长]
# 7.列表是用来存储数据的。如果要储存的数据是同一个类型的-建议用列表
# print(a[0:5:2])
# 如何往列表里面增加数据，可以增加任何类型的数据
#函数append： 追加 追加在末尾  每次只能添加一个
# a.append("秦天")
# print("a列表中的值{}".format(a))
# 函数insert ：插入数据   需要指定位置(索引值)，可随意放置
# a.insert(2,"老肥")
# 函数pop ：删除列表中的最后一个元素   列表名.pop(索引值)
# 函数remove ：指定删除某个值   列表名.remove(值)
# a.pop()  # 默认删除最后一个元素
# a.pop(1)  # 删除指定位置的元素
# a.remove(0.02)  # 删除指定的值
# print("a列表中的值{}".format(a))
# pop函数会返回被删除的那个元素。 函数returne
# res=a.pop()
# print(res)
# a=[1,0.02,'hello',[1,2,3],True]
# # 修改  列表名[索引值]=新值
# print(a[2])
# a[2]='你好'  #:赋值运算
# print("a列表中的值{}".format(a))

# 爱的飞行日记

# 元祖  tuple 符号 ()  圆括号
# 1.可以存在空元祖a=()
# 2.元祖里面可以包含任何类型的数据  print(type(a))
# 3.元祖里面的元素根据逗号进行分隔
# 4.元祖里面也有索引，索引值也是从零开始
# 5.获取元祖里面的单个值，元祖名[索引值]
# 6.元祖里的切片与字符串的操作是一样的   元祖名[索引头:索引尾:步长]
# 一般在操作数据库的时候使用元祖
# 元祖不支持任何修改（增删改）  也有特殊情况
# a=(1,0.02,'hello',[1,2,3],True,(4,5,6))
# print(type(a))
# # a[2]="dfg"  #:TypeError: 'tuple' object does not support item assignment
# a[3][-1]="画画"
# print(a)
# # 如果元祖里面只有一个元素的时候，要加一个逗号
# a=(1,)
# print(type(a))


# 字典 dict {} 大括号、花括号   无序
# 1.可以存在空字典a={}
# 2.字典里面value可以包含任何类型的数据  print(type(a))
# 3.字典里面数据储存的方式  key:value
# 4.字典里面的元素根据逗号进行分隔
# 5.字典里面的key必须是唯一的
# 6.一般存储的数据类型都不同，会用字典
# a={"class":"python","student":4,"teacher":"girl","age":20}
# 字典取值：字典名[key]  指明要取的值的key
# print(a["class"])
# # 删除 pop(key)  指明要删除的值的key
# new=a.pop("teacher")
# print(new)
# 新增 a[新key]=value  字典里面不存在的key
# a["score"]=[99,88.8,100,20]
# print(a)
# 修改  a[已存在的key]=新value  字典里面已存在的key
# a["score"]=30
# print(a)
# key  value
# print(a.keys)#获取字典里的所有key值
# print(a.values)#或缺字典里的所有value值

# 运算符  5大类
# 算术运算符: + - * / %
# 模运算/取余运算:  判断某个数 是偶数 还是奇数
# a=4
# print(a%2)
# 赋值运算符： =  +=  -=
# a=5 #：赋值运算
# a+=1#d等同于a=a+1
# a-=1#等同于a=a-1
# print(a)
# 比较运算符 > >= < <= != == 6种
# 比较结果返回的值是布尔值 Ture False
# a=10
# b=5
# print(a<b)
# a="We"
# print(a.lower())#小写
# print(a.upper())#大写
# 逻辑运算符  and  or  拓展not
# 比较结果返回的值是布尔值 Ture False
# and 的左右两边都为真才为真，只要有一个为假就为假 #真真为真
# or 的左右两边都为假才为假，只要有一个为真就为真 #假假为假
# a=5
# b=10
# print(a>11 or b>5)
# 成员运算符  in         not in
# 比较结果返回的值是布尔值 Ture False
# a="hello"
# b=[1,2,3]
# c={"age":"18","name":"剑豪"}
# print("o"in a)
# print("age"not in c)#字典：需要用key判断
# user = {1: '曹操', 2: '张飞', 3: '刘备'}
# user_01=user[1]
# print(user_01)

# user = {1: '曹操', 2: '张飞', 3: '刘备'}
# num = 0
# while num == 0:
#     choose_role=int(input("请选择一个角色(1曹操2张飞3刘备)："))
#     if choose_role in user:
#         while num==0:
#             guessing=int(input("请输入出拳(1=剪刀2=石头3=布):"))
#             if guessing in range(1,4):
#                 num = 1
#             else:
#                 print("出拳错误，请重新出拳")
#     else:
#         print("角色选择有误,请重新输入")

# test_data=[{"url": "http://119.23.241.154:8080/futureloan/mvc/api/member/login",
#             "data": {"mobilephone": "18688773467", "pwd": "123456"},"title":"正常登录","method":"get"},
#             {"url": "http://119.23.241.154:8080/futureloan/mvc/api/member/login",
#              "data": {"mobilephone": "18688773467", "pwd": "123456345"}, "title": "错误密码登录","method":"get"}]
# for item in test_data:
    # print(item)
    # print(item["data"])
mode={"login":123,"register":456,"recharge":'all',"business":'fs',"invest":"ty"}
for a in mode:  # 遍历这个存在配置文件里面的字典
    print(a)
#     # sheet = wb[key]  # 表单名
#     print(key)
    print(mode["login"])

