#-*-coding:utf-8-*-
# 控制语句 分支分流  循环语句  for   while
# 一、判断语句 关键字 if  elif   else
# 1.if条件语句（比较、逻辑、成员运算均可）   if语句是对不同情况的处理
# age =18
# if age>15:#当if后面的语句 满足条件 运算结果为Ture 就会执行它的子语句
#     print("恭喜你,成年了")
# 2.(字符串、列表、元祖、字典)空数据等于false，非空数据等于true
# a=""    # 为空数据等于false，非空数据等于true
# if a:
#     print("恭喜你,成年了")#空数据==False  非空数据==True
# 3.直接用布尔值去控制   ---鸡肋
# if False:#布尔值False也代表否定，True代表确定
#     print('打印成功')   #不打印

#二、一个条件语句里面只能有一个if 和一个else，else后面不能添加条件语句
# if 条件语句:
#    子语句
# else: 此处不能添加条件语句
#     子语句
# age =14
# if age>15:
#     print("恭喜你,成年了")
# else:
#     print("未成年")
# 三、
# if  条件语句:
#    子语句
# elif条件语句:
#     子语句
# else:
#    子语句
# 函数input() 从控制台获取一个数据，获取的数据都是字符串类型
# isdigit
# age=int(input("请输入你的年龄："))
# # age=print(type(input("请输入你的年龄：")))
# # age =-2
# if age>=18:
#     print("恭喜你,成年了")
# elif 18>age>=0:
#     print("未成年")
# else:
#     print("你的输入有误，请重新输入")
# 习题:
# 1.一家商场在降价促销,如果购买金额在50-100元之间(包含50和100元),会给10%的优惠,
# 如果购买金额大于100元,会给20%的折扣
# 编写一程序,询问购买价格,再显示出折扣(10%或20%)和最终价格
# total=int(input("请输入购买价格:"))
# if 50<total<0:
#         print("不好意思，你没法享受折扣")
#         print("你需要支付{0}元".format(total))
# elif 50<=int(total)<=100:
#         print("你将享受10%折扣")
#         print("你需要支付{0}元".format(total*(1-0.1)))
# elif total>100:#else：
#         print("你将享受20%折扣")
#         print("你需要支付{0}元".format(total*(1-0.2)))
# elif total<=0:
#         print("请输入大于0的价格")
#     print("fkjds")
# total=input("请输入购买价格:")
# if total.isdigit():
#     if 0<int(total)<50:
#         print("不好意思，你没法享受折扣")
#         print("你需要支付{0}元".format(int(total)))
#     elif 50<=int(total)<=100:
#         print("你将享受10%折扣")
#         print("你需要支付{0}元".format(int(total)*(1-0.1)))
#     elif 100<int(total):
#         print("你将享受20%折扣")
#         print("你需要支付{0}元".format(int(total)*(1-0.2)))
# else:
#     print('请输入正确的金额！')
