# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 09:45:24 2019

@author: cv
"""

# -*- coding: utf-8 -*-

import pandas as pd
from os import path
from pandas import DataFrame


file_path = r'C:\Users\cv\Desktop\1'

for k  in range(1):
    myear = str(2011)
    file_name = path.join(file_path,myear + ".csv")
    df = pd.read_csv(file_name,iterator=True)
    
    header = df.get_chunk(1)
    print(header.values)
    
    num = 189 # 国家个数
    
    results = []
    
    for i in range(num):
        data = df.get_chunk(26)
        two_cols = data.iloc[:,0:2] # 前2列非数值数据
        data = data.iloc[:,2:]
        all_sum = []
        for j in range(num):
            if i == j:
                all_sum.append(0)
                continue
            col_offset = j*26
            rectangle = data.iloc[12:24,col_offset+12:col_offset+24]
            all_sum.append(rectangle.sum().sum())
        results.append(all_sum)
    
    cols_name = data.columns.values.tolist()
    countries_name = []
    for i in range(num):
        countries_name.append(cols_name[i*26])
    
    print(results)
    final_results = DataFrame(results,index=countries_name,columns=countries_name)
    final_results.to_csv(r'C:\Users\cv\Desktop\result_'+myear+'.csv')
