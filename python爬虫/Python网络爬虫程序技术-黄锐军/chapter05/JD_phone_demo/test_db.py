# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 14:46:12 2019

@author: 10841
"""
import os
import sqlite3

conn = sqlite3.connect("mobiles.db")
cursor = conn.cursor()
cursor.execute("select * from mobiles")
rows = cursor.fetchall()
print(rows[:10])

cur_dir = os.path.abspath(os.path.dirname(__file__))
print(cur_dir)

os.chdir(r"C:\Users\10841\Desktop")
print(os.getcwd())
