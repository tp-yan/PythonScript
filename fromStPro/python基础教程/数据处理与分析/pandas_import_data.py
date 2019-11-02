# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 23:04:20 2019

pandas之数据导入
@author: tangpeng
"""

from pandas import read_table,read_csv,read_excel


# 1.导入txt文件
# 路径不能包含中文名
txt_path = r'C:\Users\tangpeng\Documents\my_data_source\big_data_source\rz.txt'
# read_table(file,names=[列1，列2,...],sep=' ',...):读取txt文件(须是utf-8编码格式)
df_txt = read_table(txt_path,sep=" ")   # 默认txt的第一行为列名
print(df_txt.head())    # 默认返回前5条
print(df_txt.tail(10))  # 返回后10条
print(type(df_txt))     # DataFrame

# 2.导入csv文件
# csv:纯文本文件(数字和文本)存储表格数据，每条记录由多个字段构成，字段间由分隔符（逗号，制表符）等分隔
csv_path = r"C:\Users\tangpeng\Documents\my_data_source\big_data_source\rz.csv"
# read_csv(file,names=[列1，列2,...],sep=' ',...)
df_csv = read_csv(csv_path,sep=',') # sep默认为空格
print(df_csv)
print(df_csv.head())
print(df_csv.tail())
print(type(df_csv))     # DataFrame

# 3.导入Excel数据: .xls与.xlsx一样的，都兼容
excel_path = r"C:\Users\tangpeng\Documents\my_data_source\big_data_source\i_nuc.xls"
excel_path2 = r"C:\Users\tangpeng\Documents\my_data_source\big_data_source\rz.xlsx"
# read_excel(file,sheet_name,header=0):sheet_name:sheet的名称；header：列名，只能为0或1，一般以第一行作为列名
# header=0:以文件第一行作为表头显示
# header=1:文件第一行丢弃，不作为表头显示。则后面的第一行数据作为表头
df_excel = read_excel(excel_path,sheet_name='Sheet3')
df_excel2 = read_excel(excel_path,sheet_name='Sheet3',header=1)
df_excel3 = read_excel(excel_path2,sheet_name='Sheet2',header=0)
print(df_excel)
print('===================')
print(df_excel2)
print(df_excel2[0:1])   # 第一行数据
print('===================')
print(df_excel3)
print('===================')

# 跳过指定行或读取多个表
# sheet_name=[0,2]:读取第一和第三页
# skiprows=[0,3]：所有表都跳过第一和第四行
df_excel4 = read_excel(excel_path,sheet_name=[0,2],skiprows=[0,3])
print(type(df_excel4))  # OrderedDict
print(df_excel4)
