#-*-coding:utf-8-*-
#@作者：haiyu.ma
#@创建日期：2019-12-02 18:04 
data=[]
info={}
info["name"]="小名"
data.append(info)
print(data)

info={}
info["name"]="小红"
data.append(info)
print(data)

# 知识补充
# 1.用例之间关联性不要太强
# 2.所有的功能模块都要写么？
# 用户端   用户操作相关的接口
# 后台端   管理平台相关的数据
# 3.数据的关联性
# 4.数据库的校验
# business  加标--审核
{"memberID":"${loan_member_id}","title":"lina同学借钱买房","amount":"2000","loanRate":"12.0","loanTerm":3,"loanDateType":0,"repaymemtWay":11,"biddingDays":5}