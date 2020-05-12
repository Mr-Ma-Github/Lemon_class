#-*-coding:utf-8-*-
# 标识符：我们在写代码的时候，取的名字。命名的符号。
# 项目名：project name
#包名: package name
# 模块名:   .py   python文件名
# 标识符规范:1.由字母数字下划线组成,但是不能以数字开头2.见名知意
# 3.不同的字母、数字隔开（提升可读性）4.不能用关键字（例如：int、if、while）
# print 输出函数，输出内容到控制台
# print(a)
# 当你要是用某个变量的时候 确定它已经被定义和赋值
# 数据类型：
# 1.数字：整型（关键字 int）、浮点型（关键字 float）
# 2.布尔值(Ture、False)，首字母要大写
# 3.字符串：string（成对的单引号、双引号、三引号中的内容都是字符串）
# 字符串中：单个字母、数字、汉字、单个符合都称之为一个元素
# a='hello!'#:赋值运算
# print(type(a))   #：函数type：判断数据类型 int 、float 、str
# print(len(a))   #：函数len：统计数据的长度
# 字符串取值：字符串名[索引值]
# 索引：从0开始标记
# print(a[3])
# 字符串切片（取多个值）：字符串名[索引头：索引尾：步长]  步长默认为1   # 取头不取尾
# print(a[1:5:1]) # 1 2 3 4 # 取头不取尾
# print(a[2:4:2]) # l
# print(a[-1]) #  ！
# print(a[::-1]) # !olleh  ==  print(a[-1:-7:-1])
# 字符串的切割:函数split：对字符串进行分割
# a='hello!'
# print(a.split("l"))  #:此函数只能对字符串使用,可以指定切割符号、切割次数
# print(a.split("l",1))#指定的切割符会被切走。逗号后面的数字是指定分割次数
# 字符串的替换：字符串.函数replace（指定替换值、新值。替换次数）
# a='hello!'
# print(a.replace('l','@',1))
# new=a.replace('l','@')#:new=a.replace('l','@',1)   次数
# print(new)
# 字符串的去除:函数strip：去除字符串中的指定字符  字符串.strip（指定字符）
# a='hello!'
# print(a.strip('!'))
# print(len(a))
# new=a.strip("h")#1：默认去掉首尾空格 #2：只能去掉头和尾的指定的字符
# print(len(new))
# print(new)
# 字符串的拼接：+ 保证+左右两边的变量值类型要一致
# s_1='python11'
# s_2='中秋节快乐'
# s_3=666  #整数 str（数字）---可以强制转换为str类型
## print(s_1,s_2,s_3)#：这不是拼接，这是依次进行输出
# print(s_1+s_2+str(s_3))#：只有+才是拼接
# 字符串的格式化输出 % format
age=20
name='python'
score=99.89
# print("2019-10-24"+name+"今年"+str(age)+"岁了")
# # 格式化输出1：format 特点{}  用这个{}来占坑
# print("2019-10-24{}今年{}岁了".format(name,age))#format后面默认从左往右从索引0开始
# # print("2019-10-24{0}今年{1}岁了".format(name,age))
# # 格式化输出2：%    %s字符串    %d数字   %f浮点数
# print("2019-10-24%s今年%d岁了"%(name,age))
#: %s可以是任何数据
#：%d必须是数字（整型、浮点数(但是会舍弃小数点后数据)）
#：%f必须是数字（整型、浮点数）--默认保留6位小数点
print("2019-10-24%s今年%f岁了，考试考了%f分"%(name,age,score))#：整数、浮点数用%f都会默认保留6位小数点
print("2019-10-24%s今年%d岁了，考试考了%d分"%(name,age,score))#：浮点数用%d会舍弃小数点后数据
print("2019-10-24%s今年%d岁了，考试考了%.2f分"%(name,age,score))#%.数字f--保留小数点位数
print("2019-10-24%s今年%s岁了，考试考了%s分"%(name,age,score))
# find 函数
s='hello'
print(s.find('m'))#寻找字符串里面的子字符   子字符串
# 找到的话  返回的是字符串所在索引
# 找不到的  返回的是-1

if s.find('9')!=-1:#if 后面 非空、非零、成立表达式都为TRUE  只有是TRUE   子句都会执行
    new_s=s.replace('o','kevin')

    print(new_s)