# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 14:40:07 2019

@author: tangpeng

Python程序接收控制台参数
"""

import os
import argparse

#设置参数
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,help="path to the input image")
ap.add_argument("-o", "--output", required=True,help="path to output directory to store augmentation examples")
ap.add_argument("-p", "--prefix", type=str, default="image",help="output filename prefix")
args = vars(ap.parse_args())
#获取参数并且打印出来
print(args['image'])
print(args['output'])

# eg :  python argparse_ArgumentParser.py --image my.png --output out.png



parser = argparse.ArgumentParser(description = 'G729A编码文件参数提取工具')
parser.add_argument("input", help = "输入文件/文件夹", type = str)
parser.add_argument("output", help = "输出文件夹", type = str)
		
args = parser.parse_args()
		
if not os.path.isdir(args.output):
	print("output not exists!")
	exit(1)

# eg. python argparse_ArgumentParser.py path_input path_output