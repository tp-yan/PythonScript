
#使用协程实现生产消费者问题
#协程使用generator实现
def consumer():
    print("====")
    r = ''
    while True:
        print("loop1...")
        print("r1:", r)
        n = yield r     #yield不但可以返回一个值，它还可以接收调用者发出的参数。返回上轮r的值
        print("loop2...")
        print("r2:",r)
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = "200 OK"    #consumer通过yield拿到消息，处理，又通过yield把结果传回；

def producer(c):
    print("p1")
    c.send(None) #启动生成器转到consumer,第一次执行到‘n = yield r’停止后转到producer
    print("p2")
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n) #c.send(1),consumer接着上一次中止的地方即‘ n = yield r’执行，n被赋值为1，而r并没有被赋值依旧r=''
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

c = consumer()
producer(c)