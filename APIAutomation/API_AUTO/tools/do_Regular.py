#-*-coding:utf-8-*-
#@作者：haiyu.ma
#@创建日期：2020-01-03 17:34 
'''正则表达式
目标:正则表达式去自行匹配结果
概念:什么是正则表达式? 用一个规则匹配你想要的信息。 正则表达式: 元字符+限定符
两个重要的点:元字符  限定符
元字符           意义                        限定符                  意义
.            任意单个字符                     +                匹配至少大于1次
\d           任意单个数字                     ?                匹配0次或1次
[0-9]        等价0-9                          *                匹配0次或多次 贪婪匹配
[a-ZA-Z]     等价所有的大小写字母       {n,}、{n,m}、{n}       匹配限定次数
举例练习:元字符限定符
>匹配数字 123456     .*      \d*'     \df{6}     [0-9)(6}
>匹配useser session
>匹配token
>用在线正则表达式去验证你的结果是否正确
'''
import re
# \${.*1}
# s='www.lemfix.com'#目标字符串
# res=re.match('www',s)#全匹配  头部匹配
# res=re.match('(w)(ww)',s)#分组  根据正则表达式里面的括号去分组
# print(res)
# print(res.group())# group()==group(0),拿到匹配的全部字符  分组  根据正则表达式里面的括号去分组

# s='hellolemonfixlemon'
# res=re.findall('lemon',s)#列表  在字符串中匹配的内容 存到列表中
# # 如果有分组  就是以元祖的形式表现出来   列表嵌套元祖
# print(res)

# s='{"mobilephone": "${normal_tel}", "pwd": "123456"}'
# res=re.search('\${(.*?)}',s)
# print(res.group(0))
# print(res.group(1))

from API_AUTO.tools.get_data import GetData

class DoRegular:
    @staticmethod
    def do_regular(s):
        while re.search('\${(.*?)}', s):
            key = re.search('\${(.*?)}', s).group(0)
            value = re.search('\${(.*?)}', s).group(1)
            s = s.replace(key, str(getattr(GetData, value)))
        return s

if __name__ == '__main__':
    s = '{"mobilephone": "${normal_tel}", "pwd": "${pwd}"}'
    res=DoRegular.do_regular(s)
    print(res)
    print(type(res))

    # s = 'None'
    # res = DoRegular.do_regular(s)
    # print(res)
    # print(type(res))