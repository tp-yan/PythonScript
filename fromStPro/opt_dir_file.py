#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#利用os模块编写一个能实现dir -l输出的程序
#编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径。
import os 

fpath = r"."
dirs = [ x for x in os.listdir(fpath)]

for filename in dirs:
	statinfo = os.stat(filename)
	#print(statinfo)
	
#print(dirs)



def find_file(fpath,sub_str):
	dirs = [ x for x in os.listdir(fpath)]
	print(dirs)
	new_dirs = []
	if dirs:
		print('+++++++++++++')
		for m_dir in dirs:
			print(m_dir)
			if os.path.isfile(m_dir):
				print('======')
				if m_dir.find(sub_str) != -1:
					print("file: ",m_dir)
			elif os.path.isdir(m_dir):
				print("dir: ",m_dir)
				new_dirs.append("./"+m_dir)
	print("new_dirs: ",new_dirs)
	for m_dir in new_dirs:
		find_file(m_dir,sub_str)

find_file('./test_dir','class')
