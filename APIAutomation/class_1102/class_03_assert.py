#-*-coding:utf-8-*-
# 类与对象--调试
# 异常处理--抓了之后  要raise出来-----单元测试

# 异常处理&调试（类与对象再去讲调试）
# 异常：你在运行代码过程中遇到的任何错误  带有error字样的  都是异常
    # 异常即是一个事件，该事件会在程序执行过程中发生，影响了程序的正常执行。
# 异常处理：我们对代码中所有可能会出现的异常 进行的处理。

# 为什么不直接使用默认的捕获？
# 1.不方便定位问题
# 2.不确定是什么原因造成的异常
# 2.一般不使用，而是会加入异常类型

'''
try:
    需要执行的可能错误的代码。当没有出现错误，那么try就会执行完。
    一旦出现错位，立即跳到except里面去继续运行
except:   # except 异常类型    不加异常类型表示所有的类型(语法错误除外)
    出现异常以后要运行的代码
'''

# 断言结果:
# 1. . 表示通过
# 2. F 表示False,断言没有通过
# 3. E 表示Error,程序内部发生了错误

import os

# 初级的异常处理
# try    except    finally
# try：语句用来检测try语句块中的错误，从而让except语句捕获异常信息并处理
# except：捕获异常 并处理异常（如果你不想在异常发生时结束你的程序，只需在except里捕获它）
# finally:无论是否有异常产生，均执行
# else:当try语句块正常执行时，无异常产生，执行else语句块

# try:#警察
#     os.mkdir("Alisa")#FileExistsError（由于此块代码出错，导致其余代码也不执行）
# except FileExistsError:#捕获异常（如果结果在判断范围内，继续执行）
# # except OSError:      #只有发生OS类型的异常，执行这块代码
# # except Exception:    #常规错误的基类    基类：包含所有实体共性的类型
# # except:              #只要发生异常，执行这块代码
# # 1.处理某个错误   2.处理某种类型的错误   3.处理任何错误（有错就抓）
# except后面加Exception和不加是一样的，但是加上可以as 别名，把错误信息打印出来
#     print("抓捕归案等待进一步处理")
# else:    #只有当try中没有报错才会执行
# print("处理后可以执行")
# finally:  #不管上面是否报错，都会执行
# print("处理后可以执行")

# 既要抓  还要有处罚措施
try:#警察
    os.mkdir("test_file")  # OSError（由于此块代码出错，会导致本文件中其余代码也不执行）
except Exception as e:  # 把错误抓出来，存储到e里面  error
    print("捕获错误，等待进一步处理")
    print("错误：{0}".format(e))
    file=open("error.txt","a", encoding="utf-8")
    file.write("\n错误："+str(e))
    file.close()  # 一定要关闭文件
else:
    print("Try不报错才会执行")
finally:
    print("不管try是否报错，都要执行")

'''
错误类型
常见的异常:
ImportError: 无法引入模块或包。
IndexError: 下标索引超出序列边界;
NameError: 使用一个还未赋予对象的变量;
SyntaxError: 代码逻辑语法出错,不能执行;不能去捕获
TypeError: 传入的对象类型与要求不符;
ValueError: 传入一个不被期望的值,即使类型正确。
KeyError: 试图访问你字典里不存在的健。
1OError: 输入输出异常:文件操作
'''

# with
with open("error.txt","a",encoding="utf-8") as file:
    file.write("正确")
    # file.close()  # with会自动关闭文件

# 断言方式：
# self.assertEqual(excepted, actual)  # 提示能够提示出预期结果和实际结果
# self.assertTrue(表达式) # 预期结果和实际结果没有具体的提示