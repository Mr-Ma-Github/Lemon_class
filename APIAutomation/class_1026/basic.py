#-*-coding:utf-8-*-

# 变量：存储数据
# 当你要是用某个变量的时候 确定它已经被定义和赋值

# 标识符（变量名）：我们在写代码的时候，取的名字。命名的符号。
# 项目名：project name
# 包名: package name
# 模块名:   .py   python文件名

# 标识符（变量名）规则:
# 1.由字母数字下划线组成,但是不能以数字开头
# 2.不能用关键字（例如：int、if、while）#import keyword #/n keyword.kwlist
# 标识符（变量名）规范:
# 3.见名知意
# 4.不同的字母、数字隔开（下划线命名、驼峰命名-提升可读性）

# print 输出函数，输出内容到控制台
# print("hello")

# input 输入函数，让用户输入信息
# a = input("请输入你的姓名：")
# if a == "盲僧":#用户输入的是字符串，要注意数据类型
#     print("天神下凡")
# else:
#     print("一锤三")

# 数据类型：
# 1.数字：整型（关键字 int）、浮点型（关键字 float）
# 2.布尔值(Ture、False)，首字母要大写
# 3.字符串：string（成对的单引号、双引号、三引号中的内容都是字符串）
# 字符串中：单个字母、数字、汉字、单个符合都称之为一个元素

# a='hello!'#:赋值运算
# 字符串取值：字符串名[索引值]
# 索引：从0开始标记
# print(a[3])
# 字符串切片（取多个值）：字符串名[索引头：索引尾：步长]  步长默认为1   # 取头不取尾
# print(a[1:5:1]) # 1 2 3 4 # 取头不取尾
# print(a[0:-1]) # 取头不取尾
# print(a[-2:])
# print(a[2:4:2]) # l
# print(a[-1:]) # 从右边开始第一个
# print(a[-1:-3:-1])#从右到左必须加负数步长
# print(a[::-1]) # !olleh  ==  print(a[-1:-7:-1])#步长如果为负数就是从右往左
# print(a[1:1000])#如果切片超出，获取所有元素
# print(a[1000])#如果使用索引，超出范围会报错   IndexError

## 字符串的格式化输出 % format
# age=20
# name='python'
# score=99.89
# print("2019-10-24"+name+"今年"+str(age)+"岁了")
# # 格式化输出1：format 特点{}  用这个{}来占坑
# print("2019-10-24{}今年{}岁了".format(name,age))#format后面默认从左往右从索引0开始
# # print("2019-10-24{0}今年{1}岁了".format(name,age))
# # 格式化输出2：%    %s字符串    %d数字   %f浮点数
# print("2019-10-24%s今年%d岁了"%(name,age))
#: %s可以是任何数据
#：%d必须是数字（整型、浮点数(但是会舍弃小数点后数据)）
#：%f必须是数字（整型、浮点数）--默认保留6位小数点
# print("2019-10-24%s今年%f岁了，考试考了%f分"%(name,age,score))#：整数、浮点数用%f都会默认保留6位小数点
# print("2019-10-24%s今年%d岁了，考试考了%d分"%(name,age,score))#：浮点数用%d会舍弃小数点后数据
# print("2019-10-24%s今年%d岁了，考试考了%.2f分"%(name,age,score))#%.数字f--保留小数点位数
# print("2019-10-24%s今年%s岁了，考试考了%s分"%(name,age,score))

# 字符串内置函数：
# a='hello!'
## 类型 type()
# print(type(a))   #：函数type：判断数据类型 int 、float 、str
# #长度 len()
# print(len(a))   #：函数len：统计数据的长度
## 大小写转化 lower() upper()
# my_string="Hello hY World!"
# print(my_string.upper())
# print(my_string.lower())
## 大小写互换 swapcase()
# print(my_string.swapcase())
## 首字母大写 title(), capitalize()
# print(my_string.title())     #每个单词的首字母都大写  Hello My World!
# print(my_string.capitalize())#只把第一个单词的首字母大写  Hello my world!
## 统计数量 count() # 区分大小写
# print(my_string.count('H'))
# print((my_string.lower()).count('h'))

## 字符重复多次
# print(a * 5)
# isdigit()  判断是否是一个正整数
# a = '2345'
# print(a.isdigit()) # 返回值是True   False
# islower()  判断是否是小写     isupper()   判断是否是大写
# b = 'Hello'
# print((b[1]).islower())
# print((b[0]).isupper())

# 字符串的拼接：join     +       保证+左右两边的变量值类型要一致
# join() 正规方式的字符串拼接   代替+
s_1 = 'python11'
s_2 = '中秋节快乐'
s_3 = 666  # 整数 str（数字）---可以强制转换为str类型
# print(s_1,s_2,s_3)#：这不是拼接，这是依次进行输出
# print(s_1+s_2+str(s_3))#：只有+才是拼接
# print("".join([s_1, s_2, str(s_3)])) # join也是拼接
print("/".join([s_1, s_2, str(s_3)]))

a = ['1', '2', '3', '4']#列表转换成字符串
b = "".join(a)
print(b)

## split()
# 字符串的切割:函数split：对字符串进行分割,返回值是list
# a = "hello"
# print(a.split("e"))  #:此函数只能对字符串使用,可以指定切割符号、切割次数
# print(a.split("1",1))#指定的切割符会被切走。逗号后面的数字是指定分割次数

## 替换 replace(old, new)
# 字符串的替换：字符串.函数replace（指定替换值,新值,替换次数）
# a='hello!'
# print(a.replace('l','@',1))#最后的值代表次数
# print(a.replace('l','@'))
# print(a)    #字符串一旦定义，除非重新赋值，不然不会变化
## strip()
# 字符串的去除:函数strip：去除字符串中的指定字符  字符串.strip（指定字符）
# a=' helloh '
# print(a.strip())#1：默认去掉首尾空格
# b='hello '
# new = b.strip("h") #2：只能去掉头和尾的指定的字符
# print(new)
# # print(len(new))
# print(b.lstrip('he').rstrip('o')) # 首尾字符不一致时，可分别指定去除
# print(b.strip('l'))##注意：中间的字符无法去除

# find 函数 # 查找元素 find()没有找到就返回-1。  index()找不到时,会报错
# s = 'hello'
# print(s.find('m'))#寻找字符串里面的子字符   子字符串（必须是连续的）
# 找到时    返回的是字符串开始字母所在的索引
# 找不到时  返回的是-1
# if s.find('o') != -1:  # if 后面 非空、非零、成立表达式都为TRUE  只有是TRUE   子句都会执行
#     new_s = s.replace('o','kevin')
#     print(new_s)
#     print(id(new_s))
# print(id(s))


# index 函数和find的作用类似
# 不同之处在于：如果index没有找到元素就会报错 ：ValueError: substring not found
# s = 'hello'
# print(s.index('m'))



def pow(x, n=2):
    r = 1
    while n > 0:
        r *= x
        n -= 1
    return r

print(pow(5)) # output: 25

# eval(str)  # 将字符串str当成有效的表达式来求值并返回计算结果。 eval里必须是str，
a = "1"
print(a, type(a))
print(eval(a), type(eval(a)))