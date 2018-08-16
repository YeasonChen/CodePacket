import xlrd

data = xlrd.open_workbook('./CosBeauty App5.1.2三语版埋点及页面转化路径.xls')
table = data.sheets()[2] # 打开第一张表
nrows = table.nrows # 获取表的行数

for i in range(nrows): # 循环逐行打印
    row_list = table.row_values(i)
    if i == 0:
        continue
    else: # 开始整合数据
        str = row_list[4] + ',' + '日语-' + row_list[3] + ',' + '0'
        print(str)
