# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 09:48:31 2019

pandas之数据导出
@author: tangpeng
"""

from pandas import Series,DataFrame
from sqlalchemy import create_engine # alchemy:魔力
from pandas import read_csv, read_excel, read_sql
import pymysql

# 字符串最后一个是'\'会出错，要么改为'\\'，要么最后不要用'\'
data_source_path = r'C:\Users\tangpeng\Documents\my_data_source\big_data_source'

# 1.导出为csv文件
df = DataFrame({
        'age':Series([26,27,31]),
        'name':Series(['Tom','Jone','Curry'])})
print(df)
filename1 = "\export_csv_01.csv"
filename2 = "\export_csv_02.csv"
df.to_csv(data_source_path+filename1) # 默认分隔符为逗号
# index=False:不导出行号，header=False：不导出列名
df.to_csv(data_source_path+filename2,index=False,header=False)

print(read_csv(data_source_path+filename1),'\n')
print(read_csv(data_source_path+filename2),"\n")

# 2.导出为Excel
filename3 = "\export_excel_01.xls"
filename4 = "\export_excel_02.xlsx"
df.to_excel(data_source_path+filename3)
df.to_excel(data_source_path+filename4,index=False) # header与to_csv一样

print(read_excel(data_source_path+filename3,sheet_name="Sheet1"),"\n")
print(read_excel(data_source_path+filename4,sheet_name="Sheet1"))

# 3.导出到MySQL数据库
# 启动引擎==创建数据库连接
user = 'root'
password = '2014112217'
host = '127.0.0.1'
port = 3306
database_name = 'shopping'
charset = 'charset=utf8'    # 作为参数传递

engine = create_engine("mysql+pymysql://"+user+":"+password+"@"+host+":"+
                       str(port)+"/"+database_name+"?"+charset)
df_mysql = DataFrame({
        # id列由数据库自动生成
        'name':Series(['火箭','火锅']),
        'city':Series(['北京','成都']),
        'price':Series([10000,100]),
        'number':Series([1,1010]),
        'picture':Series(['020.jpg','021.jpg'])
        })
df_mysql.to_sql(        
        name="items",   # 表名
        con = engine,
        if_exists = 'append',
        index = False,
        index_label = False
        )

dbconn = pymysql.connect(host=host,
                         database = database_name,
                         user = user,
                         password = password,
                         port = port,
                         charset='utf8')
sqlcmd = "select * from items"
df_result  = read_sql(sqlcmd,dbconn)
dbconn.close()
print(df_result)
