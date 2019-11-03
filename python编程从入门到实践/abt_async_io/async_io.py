import asyncio

#@asyncio.coroutine把一个generator标记为coroutine类型，然后这个coroutine就可扔到EventLoop中执行。
@asyncio.coroutine
def hello():
    print("Hello World!")
    #异步调用asyncio.sleep(3) yield from语法可以让我们方便地调用另一个generator
    r = yield from asyncio.sleep(3) #由于asyncio.sleep()也是一个coroutine，所以线程不会等待asyncio.sleep()，而是直接中断并执行下一个消息循环。
    print("Hello again!")

#获取EventLoop
loop = asyncio.get_event_loop()
#执行coroutine
loop.run_until_complete(hello())
# loop.close()

@asyncio.coroutine
def wget(host):
    print("wget %s..." % host)
    connect = asyncio.open_connection(host,80)
    reader,writer = yield from connect
    header = "GET / HTTP/1.0\r\nHost: %s\r\n\r\n" % host
    writer.write(header.encode("utf-8"))
    yield from writer.drain()
    while True:
        line = yield from reader.readline()
        if line == b"\r\n":
            break
        print("%s header > %s" % (host,line.decode("utf-8".rstrip())))
    writer.close()

loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()