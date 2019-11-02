#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 09:45:34 2019

@author: tangpeng

行末尾添加不可见字符
"""
from os import path
import pandas as pd
from pandas import DataFrame

root_path = r'C:\Users\cv\Desktop'

def save_csv(filepath):
    col_names = ["id","name","score","age"]
    data = [["2019001","zhangsan",22.90,25],
            ["2019002","lisi",66.23,33],
            ["2019003","zhaowu",81.10,72],
            ["2019004","wanger",55.00,18]]
    
    df = DataFrame(data,index=None,columns=col_names)
    print(df)
    df.to_csv(filepath)


def add_invisible_char(filepath):
    with open(filepath) as f:
        lines = f.readlines()
    
    with open(filepath,"w") as f:
        counter = 0
        for line in lines:
            counter += 1
            suffix = " " if counter % 2 == 0 else chr(0x01)
            line = line.strip() + suffix # line读进来时带有 \n
            print(line,'-->',line.encode('ascii'))
            f.write(line)
            f.write("\n")

    
def read_csv(filepath):
    df = pd.read_csv(filepath)
    print(df)
    data = df.values
    print(type(data))
    for row in data:
        for e in row:
            print(e,":",type(e),"-->",str(e).encode('utf-8'))
            if isinstance(e,str):
                print(e.strip(),":",type(e),"-->",e.strip().encode('utf-8'))
    print('=====================================')
#    for index, row in df.iterrows():
#        print(row["id"],":",type(row["id"]))
#        print(row["name"],":",type(row["name"]))
#        print(row["score"],":",type(row["score"]))
#        print(row["age"],":",type(row["age"]))
        
        
def read_txt_file(filepath):
    with open(filepath) as f:
        for line in f.readlines():
            print(line,'-->',line.encode('ascii'))
    print('++++++++++++++++++++++++++++++++++++++')


def main():
    filename = "test.csv"
    filepath = path.join(root_path,filename)
    read_csv(filepath)
#    read_txt_file(filepath)
#    add_invisible_char(filepath)
#    read_txt_file(filepath)

main()
