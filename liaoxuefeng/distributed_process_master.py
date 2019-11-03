#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 22:32:26 2019

@author: tangpeng

分布式进程之服务进程即master负责发送任务给worker进程
Python的multiprocessing模块不但支持多进程，其中managers子模块还支持把多进程分布到多台机器上。
一个服务进程可以作为调度者，将任务分布到其他多个进程中，依靠网络通信。
managers模块把Queue通过网络暴露出去，就可以让其他机器的进程访问Queue了.
服务进程负责启动Queue，把Queue注册到网络上，然后往Queue里面写入任务：
"""
import random, time, queue
from multiprocessing import freeze_support
from multiprocessing.managers import BaseManager



"""
注：
Queue的作用是用来传递任务和接收结果，每个任务的描述数据量要尽量小。比如发送一个处理日志文件的任务，
就不要发送几百兆的日志文件本身，而是发送日志文件存放的完整路径，由Worker进程再去共享的磁盘上读取文件。
Queue对象由master进程创建保存
"""
# 在服务进程中创建发送任务和接收返回值的Queue。Queue是master和worker进程之间通信的通道
task_queue = queue.Queue() # 发送任务的队列
result_queue = queue.Queue()  # 接受返回值的队列

# 从BaseManager继承的QueueManager:
class QueueManager(BaseManager):
    pass

def task_q():
    return task_queue
def result_q():
    return result_queue

def test():
    # 把两个Queue都注册到网络上, callable参数关联了Queue对象:
    # BaseManager可能会管理很多个Queue，所以必须为每个Queue定义一个名字
    QueueManager.register('get_task_queue',callable=task_q)
    QueueManager.register('get_result_queue',callable=result_q)
    # 绑定端口 12345, 设置验证码'abc':
    manager = QueueManager(address=('127.0.0.1',12345),authkey=b'abc')
    # 启动Queue:
    manager.start()
    # 获得通过网络访问的Queue对象:
    task = manager.get_task_queue() #在分布式环境下必须通过QueueManager来获得Queue。不能直接使用
    result = manager.get_result_queue()
    # 放几个任务进去:
    for i in range(10):
        n = random.randint(0,1000)
        print('put task %d...' % n)
        task.put(n)
        
    # 从result队列读取结果:
    print('Try get results...')
    for i in range(10):
        r = result.get(timeout=10) # 会阻塞进程
        print("result:%s"%r)、
    
    # 关闭
    manager.shutdown()
    print("master exit")


if __name__ == "__main__":
    freeze_support()# add this if your system is windows
    test()


