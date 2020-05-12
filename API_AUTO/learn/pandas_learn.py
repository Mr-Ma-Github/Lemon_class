#-*-coding:utf-8-*-
#@作者：haiyu.ma
#@创建日期：2019-12-06 18:18
# pandas   pip install xlrd          pip install pandas
import pandas as pd
df=pd.read_excel('test_data.xlsx',sheet_name='login')
test_data=[]
for i in df.index.values:
    row_data=df.ix[i,["url","data","title","method"]].to_dict()
    test_data.append(row_data)
print(test_data)
# print(df.values)
# print(df.ix[0].values)
# print(df.ix[1,1])
# print(df.ix[:].values)
# print(df.ix[:,["url"]].values)
# print(df.ix[1,["url","data","title","method"]].to_dict())

