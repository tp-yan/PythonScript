#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 16:02:08 2019

@author: tangpeng

多进程
"""

"""
1. multiprocessing模块
os模块中的 fork()系统调用：复制父进程来创建子进程，只能在Mac或Unix系统上调用。若要在Windows上
实现多线程，则需要multiprocessing模块（可以再任何OS上使用）
multiprocessing模块提供了一个Process类来代表一个进程对象：
"""
import os

def only_mac_unix():
    print("Process (%s) start..." % os.getpid()) # 获取当前进程ID
    pid = os.fork() # 子进程永远返回0，而父进程返回子进程的ID。
    if pid == 0:
        print('I am child process (%s) and my parent is %s.' % (os.getpid(),os.getppid()))
    else:
        print('I (%s) just created a child process (%s).' % (os.getpid(),pid))
              
              
from multiprocessing import Process

# 子进程需要执行的代码
def run_proc(name):
    print("Run child process %s(%s)..." % (name,os.getpid()))
# 在控制台执行此脚本，才会显示子进程输出内容
def create_subprocess():
    print("Parent process %s." % os.getpid())
    p = Process(target=run_proc,args=('test',)) # 创建子进程实例，指定要执行的函数并传入所需参数
    print(" Child process will start")
    p.start() # 启动子进程
    p.join() # 父进程等待子进程执行完后再继续执行，通常用于进程间的同步。
    print(" Child process end")

"""
2. Pool类：创建线程池
用进程池的方式批量创建子进程
"""
from multiprocessing import Pool
import time,random

def long_time_task(name):
    print("Run task %s(%s)..." %(name,os.getpid()))
    start = time.time()
    time.sleep(random.random()*3)
    end = time.time()
    print('Task %s runs %0.2f seconds. ppid:%s' % (name, (end - start),os.getppid()))
    
def create_thread_pool():
    print('Parent process %s.' % os.getpid())
    p = Pool(4) # Pool的默认大小是CPU的核数。这里设为4个，则最多同时执行4个进程。多余的进程只能等待前面的执行完
    for i in range(5): # 按添加顺序启动各子进程
        p.apply_async(long_time_task,args=(i,)) # 同 Process 的构造函数
    print("Waiting for all subprocesses done...")
    p.close() # 调用close()之后就不能继续添加新的Process了。相当于Process.start()
    p.join() # 调用join()之前必须先调用close()
    print("All subprocesses done.")

"""
3. subprocess模块：启动外部子进程
subprocess模块可以让我们非常方便地启动一个子进程，然后控制其输入和输出。
"""
import subprocess

def external_subprocess():
    print('$ nslookup www.python.org')
    r = subprocess.call(['nslookup','www.python.org']) # 调用OS系统命名即进程，传入参数
    print('Exit code:', r)
    
# 如果子进程还需要手动输入的参数，则可以通过communicate()方法输入
r''' 注意：这里面包含 转义字符 \ 故需要使用 r指示不转义
此函数实现的功能，等价于此过程：
C:\Users\cv>nslookup
默认服务器:  ns2.cstnet.cn
Address:  159.226.8.7

> set q=mx # >指示输入数据
> python.org
服务器:  ns2.cstnet.cn
Address:  159.226.8.7

非权威应答:
python.org      MX preference = 50, mail exchanger = mail.python.org
> exit
'''

def external_subprocess_PIPE():
    print('$ nslookup')
    p = subprocess.Popen(['nslookup'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    output, err = p.communicate(b'set q=mx\npython.org\nexit\n') # 给子进程传入更多参数
    print("p type:",type(p)) # SubprocessPopen
    print("output type:",type(output))
    print("err type:",type(err))
    print(output.decode('GB18030')) # GB18030:中国最新国标编码。返回内容中有某些utf-8无法解码的字节会报错
    print("Exit code:",p.returncode) 


"""
4. 进程间通信
Process之间肯定是需要通信的，操作系统提供了很多机制来实现进程间的通信。
Python的multiprocessing模块包装了底层的机制，提供了Queue、Pipes等多种方式来交换数据。
"""
from multiprocessing import Queue

"""
模拟生产消费者过程：一个进程负责put，另一个负责get（不断循环取）
"""
# 向Queue中put数据
def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A','B','C']:
        print("Put %s to queue..." % value)
        q.put(value)
        time.sleep(random.random()) # 进程休眠
# 从queue中get数据
def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)

# 子进程拥有父进程创建的Queue
def process_communicate():
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=write,args=(q,)) # 生产者
    pr = Process(target=read,args=(q,))  # 消费者
    pw.start()
    pr.start()
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()
    
"""
注意：
在Unix/Linux下，multiprocessing模块封装了fork()调用，使我们不需要关注fork()的细节。由于Windows没有fork调用，因此，multiprocessing需要“模拟”出fork的效果，父进程所有Python对象都必须通过pickle序列化再传到子进程去，所以，如果multiprocessing在Windows下调用失败了，要先考虑是不是pickle失败了。

"""

if __name__ == "__main__":
#    create_subprocess()
#    create_thread_pool()
#    external_subprocess()
#    external_subprocess_PIPE()
     process_communicate()