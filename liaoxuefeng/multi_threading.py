#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 18:00:01 2019

@author: tangpeng

多线程
"""

"""
1. 创建线程
`_thread`是低级模块，`threading`是高级模块，对`_thread`进行了封装.
只用threading就可以了
"""


import threading,time

def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0 
    while n < 5:
        print("thread %s >>> %s" %(threading.current_thread().name,n))
        time.sleep(1)
        n = n + 1
        
    print('thread %s is ended.' % threading.current_thread().name)

print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop,name='LoopThread')
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)


"""
2. Lock
由于线程的调度是由操作系统决定的，因为高级语言的一条语句在CPU执行时是若干条语句，修改balance的
语句若不是原子操作，执行这几条语句时，线程可能中断，从而导致多个线程把同一个对象的内容改乱了。
锁的好处就是确保了某段关键代码只能由一个线程从头到尾完整地执行。

GIL锁
Python解释器执行代码时，有一个GIL锁：Global Interpreter Lock，任何Python线程执行前，必须先获得GIL锁，
然后，每执行100条字节码，解释器就自动释放GIL锁，让别的线程有机会执行。
这个GIL全局锁实际上把所有线程的执行代码都给上了锁，所以，多线程在Python中只能交替执行，
即使100个线程跑在100核CPU上，也只能用到1个核。

Python解释器由于设计时有GIL全局锁，导致了多线程无法利用多核。始终只能在一个核上切换线程，但是
可以使用多进程来使用多核。
"""
# 假定这是你的银行存款:
balance = 0
lock = threading.Lock()

def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n # ==> x = balance + n; balance = x
    balance = balance - n

def run_thread(n):
    for i in range(100000):
        # 获取锁
        # 当多个线程同时执行lock.acquire()时，只有一个线程能成功地获取锁，然后继续执行代码，
        # 其他线程就继续等待直到获得锁为止
        lock.acquire() # 由于锁只有一个，无论多少线程，同一时刻最多只有一个线程持有该锁
        try:
            change_it(n)
        finally:
            # 一定要释放锁
            lock.release()

