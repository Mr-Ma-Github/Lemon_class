#-*-coding:utf-8-*-
# decode：解码   encode：编码
# 根据指定的编码格式读取。
# 编码是根据一定的规则将计算机内部的机器字节码转化成人能看懂的字符串

# 1.file文件open之后默认是r--只读模式   如果要写入内容-报错：io.UnsupportedOperation: not writable
# 2.r+ 可读可写  先写的话从头开始覆盖写  读光标之后的内容  读写跟着光标走
# 3.utf-8 如果要写入中文  请注意编码格式
# 4.w 是只写  硬要去读 就会报错:io.UnsupportedOperation: not readable
# 5.w+ 可读可写  不管是w还是w+  如果文件存在  就直接清空  再重写
# 如果文件不存在  则新建一个文件  然后写
# file=open('recall_file.txt','w+',encoding='utf-8')
# file.write("hello world  hello lemon")
# 6.a 追加  a+   推荐
# 如果文件存在  就直接追加写  写在后面 # 如果不存在  则新建一个文件  进行结果写入
# file=open('recall_file.txt','a',encoding='utf-8')
# file.write("\n加油加油加油")

# 拓展：怎么移动光标？可以指定读取的行数么？
# 重点掌握r    a

import os
# dir_name = os.path.dirname(os.path.abspath(__file__))
# print(dir_name)
# recall_file = os.path.join(dir_name, 'recall_file.txt')
# print(recall_file)
# 如何读取文件：
# 1.打开文件，内置函数：open()     open(path/文件名称）:最好是绝对路径
# open(path/文件名称, mode='r')
# 2.读取
# 3.关闭文件
# file=open(recall_file, 'r', encoding='utf-8')
# print(file.read())#读取所有内容
# print(file.readline())#第一个只读取第一行
# print(file.readline())#第两个开始读取第二行
# print(file.readlines())#读取多行，以列表方式返回数据
# 读取机制：根据光标移动的
# file.close()
# 写入
# file_2 = open('recall_file.txt', 'a', encoding='utf-8')
# print(file_2.write("\n2019-11-04 文件操作"))

# mode   打开这个文件的模式
# r  读取
# w  写入，当已存在这个文件的时候，原来文件中的内容会被覆盖
# a  追加写入，
## t  文字模式：rt、wt、at
## b  binary，二进制   rb、wb、ab   例如：图片、视频..
# r+  w+   a+
# read   write  append
# rb   rb+       wb  wb+       ab   ab+  #做单元测试的时候学习
# file=open('recall_file.txt','r+',encoding='utf-8')
# res=file.read()#进行完一次读写操作后   光标就到文末
# file.write('中文')
# print(res)

# with
with open("error.txt","a",encoding="utf-8") as file:
    file.write("正确")
    # file.close()  # with会自动关闭文件