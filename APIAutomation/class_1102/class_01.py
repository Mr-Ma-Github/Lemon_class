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

# 怎么引入不同的模块-->
# 1.自己写的  怎么导入
# 1)import
# import class_1031.function_01
# class_1031.function_01.add_num(1,101)
# 2)from...import....#至少具体到模块名
from class_1031.function_01 import add_num#引用文件function_01中的add_num方法
add_num(1,10)
#from class_1031.function_01 import *   #引用文件function_01中的所有方法
# 2.python自带的或者后面安装的第三方库 怎么引用
# 1）import
# import email.mime.python_math#import+导入库的路径
# email.mime.python_math.add(1,3)
# 2)from...import....#至少具体到模块名
# from email.mime import python_math #/from email.mime.python_math import add
# python_math.add(1,4) #/add(1,4)q