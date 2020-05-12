#-*-coding:utf-8-*-
# 用例中URL  测试数据  断言期望结果 除了这几个不同，其他的都是高度相似的
# 参数化  url  data  excepted

# 存到Excel里  python操作Excel
# 1.xlsx--->openpyxl  只支持这种格式
# 2.
from openpyxl import load_workbook
# 1.打开Excel文件
wb=load_workbook("Excel_study.xlsx")#Open the given filename and return the workbook
# 2.定位表单
sheet=wb['python']#传表单名    返回一个表单对象
# 3.定位单元格   根据行列值
res=sheet.cell(1,1).value    #(行，列)
print("行数:{}".format(sheet.max_row))
print("列数:{}".format(sheet.max_column))
# print(res)

# 数据从Excel中拿出来是什么类型？
# 数字依然是int、folat，其他都是字符串
print("url:{},类型是{}".format(sheet.cell(1,1).value,type(sheet.cell(1,1).value)))
print("data:{},类型是{}".format(sheet.cell(1,2).value,type(sheet.cell(1,2).value)))
print("excepted:{},类型是{}".format(sheet.cell(1,3).value,type(sheet.cell(1,3).value)))
print("method:{},类型是{}".format(sheet.cell(1,4).value,type(sheet.cell(1,4).value)))

# homework:
# 请完成数据参数化+结合Excel

# eval() 把数据类型转换成 原本数据类型
s="True"
print(eval(s),type(eval(s)))
b='{"name": "推荐食谱", "1": "症状", "name1": "浑身忽冷忽热"}'
print(b,type(b))
print(eval(b),type(eval(b)))


# 读取数据  方式一 方式二  以后肯定是方法一
# 方法一：一次性读取所有的数据，对内存的要求比较高
# 方法二：需要用的时候读取所有的数据，对磁盘读写要求比较高
# 方法三：比较复杂一点

