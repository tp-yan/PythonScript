#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 08:41:03 2019

@author: 10841

"""

"""
ThreadLocal
在多线程环境下，每个线程都有自己的数据。一个线程使用自己的局部变量比使用全局变量好，
因为局部变量只有线程自己能看见，不会影响其他线程，而全局变量的修改必须加锁。
"""
import threading

class Student:
    pass

# 1.线程中的函数采用函数参数的方式传递局部变量
def process_student(name):
    # std是线程的局部变量，线程中的每个函数都要用它，因此必须传进去
    std = Student(name) 
    do_task_1(std)
    do_task_2(std)

def do_task_1(std):
    # 又需要调用其他函数，也得将局部变量传进去
    do_subtask_1(std)
    do_subtask_2(std)

def do_task_2(std):
    do_subtask_2(std)
    do_subtask_2(std)

# 2.用一个全局dict存放所有的Student对象，然后以thread自身作为key获得线程对应的Student对象
global_dict = {}

def std_thread(name):
    std = Student(name)
    global_dict[threading.current_thread()] = std
    do_task_1()
    do_task_2()
    
def do_task_1():
    # 不传入std，而是根据当前线程查找：
    std =  global_dict[threading.current_thread()]
    
def do_task_2():
    # 任何函数都可以查找出当前线程的std变量：
    std = global_dict[threading.current_thread()]
    
# 3.更简单的方式：使用ThreadLocal
"""
创建全局ThreadLocal对象:
全局变量local_school就是一个ThreadLocal对象，每个Thread对它都可以读写student属性，
但互不影响。你可以把local_school看成全局变量，但每个属性如local_school.student都是
线程的局部变量，可以任意读写而互不干扰，也不用管理锁的问题，ThreadLocal内部会处理。 

一个ThreadLocal变量虽然是全局变量，但每个线程都只能读写自己线程的独立副本，互不干扰。
ThreadLocal解决了参数在一个线程中各个函数之间互相传递的问题。 

ThreadLocal最常用的地方就是为每个线程绑定一个数据库连接，HTTP请求，用户身份信息等，
这样一个线程的所有调用到的处理函数都可以非常方便地访问这些资源。
"""
local_school = threading.local()
    
def process_student():
    # 获取当前线程关联的student:
    std = local_school.student
    print('Hello, %s (in %s)' % (std,threading.current_thread().name))
    
def process_thread(name):
    # 给ThreadLocal绑定只属于单个线程的属性
    local_school.student = name
    process_student()

    
t1 = threading.Thread(target=process_thread,args=("Alic",),name="Thread-A")
t2 = threading.Thread(target=process_thread,args=("Bob",),name="Thread-B")
t1.start()
t2.start()
t1.join()
t2.join()
