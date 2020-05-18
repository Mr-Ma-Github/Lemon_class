#-*-coding:utf-8-*-
# 类与对象--调试
# 异常处理--抓了之后  要raise出来-----单元测试

# 异常处理&调试（类与对象再去讲调试）
# 异常：你在运行代码过程中遇到的任何错误  带有error字样的  都是异常
    # 异常即是一个事件，该事件会在程序执行过程中发生，影响了程序的正常执行。
# 异常处理：我们对代码中所有可能会出现的异常 进行的处理
# 疑问：为什么要处理 异常？
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
#     print("抓捕归案等待进一步处理")
# else:    #只有当try中没有报错才会执行
# print("处理后可以执行")
# finally:  #不管上面是否报错，都会执行
# print("处理后可以执行")

# 既要抓  还要有处罚措施
try:#警察
    os.mkdir("test_file")#OSError（由于此块代码出错，会导致本文件中其余代码也不执行）
except Exception as e: #把错误抓出来，存储到e里面  error
    print("捕获错误，等待进一步处理")
    print("错误：{0}".format(e))
    file=open("error.txt","a",encoding="utf-8")
    file.write("\n错误："+str(e))
    file.close()  #关闭文件
else:
    print("Try不报错才会执行")
finally:
    print("不管try是否报错，都要执行")