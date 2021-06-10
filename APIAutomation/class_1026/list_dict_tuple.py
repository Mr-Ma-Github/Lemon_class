#-*-coding:utf-8-*-
# 1、当list、dic等可变类型作为函数默认参数并且调用函数时没有传参的时候，
# 要注意list、dic并不会自己清空。
# 2、默认参数只在def语句被执行的时候计算一次。
# 3、如果想要的话，把默认参数当成静态变量（也就是全局变量）
# def foo(a, b=[]):
#     b.append(a)
#     print(b)
#
# foo(1)
# foo(4)
#
# # 正确写法：
# def foo(a, b=None):
#     if b is None:
#         b = []
#     b.append(a)
#     print(b)
#
# foo(1)
# foo(2)

# 列表：list 符号[]  中括号   有序的
# 1.可以存在空列表a=[]
# 2.列表里面可以包含任何类型的数据
# 3.列表里面的元素根据逗号进行分隔
# 4.列表里面也有索引，索引值也是从零开始
# # # 5.获取列表里面的单个值，列表名[索引值]
# a=[1, 0.02, 'hello', [1, 2, 3], True]
# # print(len(a))
# print(a[1])
# print(a[::-1])
# print(a[-1])
# print(a[5])#索引如果超出界限。会报错  IndexError: list index out of range
# 6.列表的切片与字符串的操作是一样的   列表名[索引头:索引尾:步长]
# 7.列表是用来存储数据的。如果要储存的数据是同一个类型的-建议用列表
# print(a[0:5:2])
# 如何往列表里面增加数据，可以增加任何类型的数据
#函数append： 追加 追加在末尾  每次只能添加一个
# a = [1, 0.02, 'hello', [1, 2, 3], True]
# print(a)
# print(id(a))
# a.append("秦天")
# print(a)
# new_a = a.append("大黄蜂")#返回是None
# print(a)
# print(new_a)
# print(new_a)  #返回是None
# print(id(a))
# # extend([])  # 添加多个元素
# a.extend(['狂风','暴雨','西瓜','难过'])
# print(a)
# 函数insert ：插入数据   需要指定位置(索引值)，可随意放置
# a=[1, 0.02, 'hello', [1, 2, 3], True]
# a.insert(2,"老肥")
# print(a)
# 函数remove ：指定删除某个值   列表名.remove(值)
# a.remove(0.02)  # 删除指定的值
# print("a列表中的值{}".format(a))
# 函数pop ：通过索引删除列表中指定位置的元素   列表名.pop(索引值)
# a.pop()  # 默认删除最后一个元素
# print(a)
# a.pop(1)  # 删除指定位置的元素
# print(a)
# pop函数会返回被删除的那个元素。 函数returne
# res=a.pop()
# print(res)
# clear() 清空列表
# a.clear()
# print(a)
# a = [1, 0.02, 'hello', [1, 2, 3], True]
# del 从内存当中直接清除(尽量不要去用)
# del a[0]
# print(a)
# del a
# print(a)  #NameError: name 'a' is not defined
# # 修改  列表名[索引值]=新值
# print(a[2])
# a[2]='你好'  #:赋值运算
# print("a列表中的值{}".format(a))

# index   #获取指定元素的索引值
# print(a.index(1))
# # count   #获取指定元素的数量
# print(a.count(1))
# reverse  #逆序    方式一
# a.reverse()
# print(a)
# 逆序    方式二   重新创建一个新的变量
# new_a=a[::-1]
# print(new_a)
# 排序
# a = ['c', 'd', 'x', 'z']
# a.sort()
# print(a)
# # 数字排序 #默认升序
# a = [3, 5, 2, 12]
# a.sort()
# print(a)
# a.sort(reverse=True)  #倒序：增加reverse= True即可
# print(a)

# 元祖  tuple 符号 ()  圆括号
# 1.可以存在空元祖a=()
# 2.元祖里面可以包含任何类型的数据  print(type(a))
# 3.元祖里面的元素根据逗号进行分隔
# 4.元祖里面也有索引，索引值也是从零开始
# 5.获取元祖里面的单个值，元祖名[索引值]
# 6.元祖里的切片与字符串的操作是一样的   元祖名[索引头:索引尾:步长]
# 一般在操作数据库的时候使用元祖
# 元祖不支持任何修改（增删改）  也有特殊情况
# a=(1, 0.02, 'hello', [1,2,3], True, (4,5,6))
# print(type(a))
# a[2]="dfg"  #:TypeError: 'tuple' object does not support item assignment
# print(a[2])
# a[3][-1]="画画"
# print(a)
# # 如果元祖里面只有一个元素的时候，要加一个逗号。否则表示的是去掉元祖括号的原始数据类型
# a=(1,)
# print(type(a))
# print(a)
# 元祖解包 :tuple_unpack
# test1, test2 = ('hello', 'world')  #变量的数量要与value一致
# print(test1)
# print(test2)
# tuple_unpack, *test=('hello', 'world', 'python')#如果其中的某个变量前加一个*号，那多余的value都会放到这个变量里
# print(tuple_unpack)
# print(test)

# 字典 dict {} 大括号、花括号   无序    不支持索引
# python3.7之前，第一次打印和第二次打印结果可能会不一样
# python3.7及之后，是按照添加顺序去显示
# 1.可以存在空字典a={}
# 2.字典里面value可以包含任何类型的数据  print(type(a))
# 3.字典里面数据储存的方式  key:value
# 4.字典里面的元素根据逗号进行分隔
# 5.键一般是唯一的，如果重复最后的一个键值对会替换前面的，值不需要唯一。
# 6.一般存储的数据类型都不同，会用字典
# 7.值可以取任何数据类型，但键必须是不可变的，如字符串，数字或元组。
# a={"class": "python", "student": 4,"teacher": "girl", "age": 20}
# print(a[3])   #字典不支持索引
# print(len(a))
# 字典取值：字典名[key]  指明要取的值的key
# print(a["class"])
# print(a)
# #popitem() 删除 默认删除最后一个。
# python3.7之前的要注意可能是随机删除
# a.popitem()
# print(a)
# # 删除 pop(key)  指明要删除的值的key
# new=a.pop("teacher")
# print(new)
# print(a)
# 新增 a[新key]=value  字典里面不存在的key
# a["score"]=[99,88.8,100,20]
# print(a)
# 修改  a[已存在的key]=新value  字典里面已存在的key
# a["score"]=30
# print(a)
# clear() 清空字典
# a.clear()
# print(a)
# del 从内存当中直接清除(尽量不要去用)
# del a["class"]
# del a
# print(a)
# items() #获取字典里的所有值:列表里嵌套元祖
# a = {"class": "python", "student": 4, "teacher": "girl", "age": 20}
# b = a.items()
# print(b)  # dict_items([('class', 'python'), ('student', 4), ('teacher', 'girl'), ('age', 20)])
# keys  values
# print(a.keys())#获取字典里的所有key值  列表形式
# print(a.values())#或缺字典里的所有value值  列表形式

# 运算符  5大类
# 算术运算符: + - * / %
# 模运算/取余运算: % 判断某个数 是偶数 还是奇数
# 除法
# print(4/2)# 除法运算，算完以后的结果数据变成了float类型（与python版本有关系）
# 整除
# print(5//3)# 1 # 可以得到整除数
# 取余
# a=4
# print(a%2)
# 幂运算  **
# print(2**4)# 2的4次方

# 算术运算有一个坑
# 浮点数运算不能精确
# print(0.1+0.2)#0.30000000000000004
# # Decimal
# from decimal import Decimal
# print(Decimal('0.1')+Decimal('0.2'))
# print(type(Decimal('0.1')+Decimal('0.2')))
# print(Decimal('0.1')+Decimal('0.2') == Decimal('0.3'))#返回值是True/False
# Decimal 能够维持很高的精度
# Decimal 函数例接收的要是字符串形式，不要写成数字格式

# 赋值运算符： =  +=  -=
# a=5 #：赋值运算
# a+=1#d等同于a=a+1
# a-=1#等同于a=a-1
# print(a)

# 比较运算符 > >= < <= != == 6种
# 比较结果返回的值是布尔值 Ture False
# a=10
# b=5
# print(a<b)#比较运算得到的结果是布尔值
# 比较结果返回的值是布尔值 Ture False

# 逻辑运算符：  and 并且    or 或者    not 非
# 逻辑运算返回的值是布尔值 Ture False
# and 的左右两边都为真才为真，只要有一个为假就为假 #真真为真
# or 的左右两边都为假才为假，只要有一个为真就为真 #假假为假
# and
# a=5
# b=10
# print(a>11 and b>5)
# # or
# a=5
# b=10
# print(a>11 or b>5)
# # not 非，取反值
# # 加括号，提优先级，先算括号内的
# print(not(a>11 or b>5))

# 成员运算符  in         not in
# 成员运算返回的值也是布尔值 Ture False
a="hello"
b=[1, 2, 3]
c={"age": "18", "name": "剑豪"}
print("o"in a)
print(1 in b)
print("age"not in c)#字典的in：是判断key 不是value
print("18"not in c.values())# 如果要判断value，可以加.values()

# 合并字典
# 实例 1 : 使用 update() 方法，第二个参数合并第一个参数
# dict1 = {'a': 10, 'b': 8}
# dict2 = {'d': 6}
# dict2.update(dict1)
# print(dict2.update(dict1))# 返回  None
# print(dict2)
# 实例 2 : 使用 **，函数将参数以字典的形式导入
# dict1 = {'a': 10, 'b': 8}
# dict2 = {'d': 6, 'c': 4}
# dict3 = {**dict1, **dict2}
# print(dict3)

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
#             "data.txt": {"mobilephone": "18688773467", "pwd": "123456"},"title":"正常登录","method":"get"},
#             {"url": "http://119.23.241.154:8080/futureloan/mvc/api/member/login",
#              "data.txt": {"mobilephone": "18688773467", "pwd": "123456345"}, "title": "错误密码登录","method":"get"}]
# for item in test_data:
    # print(item)
    # print(item["data.txt"])
# mode={"login":123,"register":456,"recharge":'all',"business":'fs',"invest":"ty"}
# for a in mode:  # 遍历这个存在配置文件里面的字典
#     print(a)
# #     # sheet = wb[key]  # 表单名
# #     print(key)
#     print(mode["login"])

# t1 = ('aa', '11')
# t2 = ('bb', '22')
# t3 = [('cc', '33')]
# t4 = {}
# t4[t1[0]] = t1[1]
# t4[t2[0]] = t2[1]
# t4[t3[0][0]] = t3[0][1]
# print(t4)
#
# t5 = [t1, t2, t3[0]]
# print(dict(t5))
