# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 09:16:42 2019

pandas之数据导入：导入MySQL数据库
@author: tangpeng
"""

import pandas as pd
import pymysql # 连接MySQL的库

# 5.导入MySQL数据库
# 方法一
print('=============方法一==============')
# 连接MySQL数据库时需要的连接对象
dbconn = pymysql.connect(host="127.0.0.1",database="shopping",user="root",
                         password="2014112217",port=3306,
                         charset="utf8") # 加上字符集参数，防止中文乱码
sqlcmd = "select * from items" # 要执行的SQL查询语句
result = pd.read_sql(sqlcmd,dbconn) # 导入MySQL数据库
dbconn.close()

print(type(result))
print(result.head())
print(result.tail())

# 方法二
import pymysql.cursors
print('=============方法二==============')
# 连接配置信息
config = {
        'host':'127.0.0.1',
        'port':3306,
        'user':'root',
        'password':'2014112217',
        'db':'shopping',    # 数据库名
        'charset':'utf8',
        'cursorclass':pymysql.cursors.DictCursor
        }
# 创建连接
conn = pymysql.connect(**config)
# 执行SQL语句
try:
    with conn.cursor() as cursor:
        sql = "select * from items"
        cursor.execute(sql)
        result = cursor.fetchall()
finally:
    conn.close()
    
print(type(result))
print(result)
df = pd.DataFrame(result)
print(df.head())


print('=============方法三==============')        
from sqlalchemy import create_engine

# engine = create_engine('mysql+pymysql://user:password@host:port/databasename')
# 相当于创建数据库连接
engine = create_engine('mysql+pymysql://root:2014112217@127.0.0.1:3306/shopping')
df = pd.read_sql('items',engine)    # 第一参数是表名
print(type(df))
print(df)
