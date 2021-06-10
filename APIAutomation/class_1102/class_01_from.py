#-*-coding:utf-8-*-
# 怎么看函数：选中函数-->Ctrl+鼠标左键
# a=[1,2,3,4]
# print(a.pop())

# python优点：非常丰富的库
# 第三方模块需要安装：
# a.在线安装：
# 1.打开cmd   输入pip install 模块名
# 2.使用国内源去进行安装 pip install 国内源地址  模块名
# 3.file-setting-project interpreter-+......
# b.离线安装：
# 自己去python的官网或者是网上找到python安装路径
# 1.解压# 2.拷贝解压后额文件  到python安装路径
# 3.windows  在cmd里利用cd 进入到安装包路径  安装文件  setup.py
# python setup.py install

# 文件安装位置：lib      lib-->site-packages

# 模块: py 文件
# 包:带有 _init__.py 文件的文件夹
# 1.模块名称:模块名称是一个标识符。
# 标识符命名规则:
# 1)数字,下划线,字母,不能以数字开头,不能关键字
# 2)模块名称命名一般是使用下划线的形式命名, 驼峰
# 3)模块名称不能和 python 内置的模块名称重合。
# random,内置模块, 那么我们命名自己的模块的时候,就不要使用 random
# time
#
# 包:python3 新版本,不带 __init_.py 同样可以作为包使用。

# 2,模块导入
# from 模块名称 import 类名,函数名,变量名    #适用于项目根目录/内置模块
# from (项目根目录开始)包名.包名.包名.模块名 import 类名,函数名,变量名
# from (项目根目录开始)包名.包名 import 模块名
# 使用的时候：模块名.函数名

# 1.如果出现了重名的函数，那么要使用别名
# 2.函数名称很长要使用别名
# 公式： from 模块名称 import 类名,函数名,变量名 as alias

# from time import time
# from random import randint
# print(time())
# print(randint(1, 10))# 打印随机数

# 1)import
# import 只能是模块名(as 别名) #内置函数
# 调用：模块名.函数名()
# import 包名.包名.模块名
# import class_1031.function_01
# class_1031.function_01.add_num(1,101)
# 2)from...import....#至少具体到模块名
# from class_1031.function_01 import add_num#引用文件function_01中的add_num方法
# add_num(1,10)
#from class_1031.function_01 import *   #引用文件function_01中的所有方法
# 2.python自带的或者后面安装的第三方库 怎么引用
# 1）import
# import email.mime.python_math#import+导入库的路径
# email.mime.python_math.add(1,3)
# 2)from...import....#至少具体到模块名
# from email.mime import python_math #/from email.mime.python_math import add
# python_math.add(1,4) #/add(1,4)q

# 如果不是python内置的：
# 1.放到项目下面，作为一个包或者模块
# 2.放到lib/site-packages下

import os
print(os.path.dirname(__file__))
print(os.path.abspath(__file__))
# 若print os.path.dirname(file)所在脚本是以绝对路径运行的，则会输出该脚本所在的绝对路径，
# 若以相对路径运行，输出空目录
# 所以最好用os.path.dirname(os.path.abspath(__file__))
# 只会打印运行所在文件夹下面的路径
'''
__file__:当前文件路径
如果执行命令时使用绝对路径，__file__就是脚本的绝对路径。
python C:\\Users\haiyu.ma\PycharmProjects\lemon_class\APIAutomation\class_1102\do_file.py"
如果使用的是相对路径，__file__输出空目录/相对路径。python do_file.py
__name__:是否为主文件
如果当前模块是用来作为 程序运行的脚本文件（入口文件）：模块名称永远是__main__
如果当前模块不是用来作为 程序运行的脚本文件：包名.模块名
__main__：表示运行python文件的模块名

if __name__ == '__main__':
    pass
# 当py文件被作为脚本（入口）执行的时候，if下面的代码会执行
# 如果py文件是被导入其他的模块，if下面的代码不会执行 
'''


# print(__file__)
# print(__name__)

