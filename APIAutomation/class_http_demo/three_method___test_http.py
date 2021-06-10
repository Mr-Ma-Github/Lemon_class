#-*-coding:utf-8-*-
# 处理用例中的依赖关系（第二条用例需要调用第一个用例返回的参数，比如cookie）
# 1.setUp
# 缺点：关联性比较强，一步错步步错
# 2.全局变量  局部变量   如果要修改全局变量，需要先global声明一下
# 缺点：关联性比较强，一步错步步错
# 3.反射                属性：attribute
# 缺点：关联性比较强，一步错步步错
class GetData:
    cookie="小明"

print(GetData.cookie)
setattr(GetData,'cookie',"小红")#可以直接把类里面的属性值修改
print(GetData.cookie)
print(hasattr(GetData,'cookie'))#判断是否有这个属性值
print(getattr(GetData,'cookie'))#获取这个属性
delattr(GetData,'cookie')       #删除这个属性
print(hasattr(GetData,'cookie'))#判断是否有这个属性值


