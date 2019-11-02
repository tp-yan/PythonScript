from contextlib import contextmanager,closing
from urllib.request import urlopen

class Query(object):

    def __init__(self,name):
        self.name = name

    def __enter__(self):
        print('Begin')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print("Error")
        else:
            print("End")

    def query(self):
        print("Query info about %s" % self.name)

with Query("Bob") as q:
    q.query()
#输出：
# Begin
# Query info about Bob
# End

#使用Python的标准库contextlib
class Query2(object):
    def __init__(self, name):
        self.name = name

    def query(self):
        print("Query info about %s" % self.name)

@contextmanager
def create_query(name):
    print("Begin2")
    q = Query2(name)
    yield q
    print('Enb2')

with create_query("Bob2") as q:
    q.query()

#输出：
# Begin2
# Query info about Bob2
# End2

#我们希望在某段代码执行前后自动执行特定代码，也可以用@contextmanager实现
@contextmanager
def tag(name):
    print("<%s>" %name)
    yield
    print("<%s>" %name)

with tag("h1"):
    print("hello")
    print("world")
#输出
# <h1>
# hello
# world
# <h1>

#closing()来把该对象变为上下文对象
#closing也是一个经过@contextmanager装饰的generator
# @contextmanager
# def closing(thing):
#     try:
#         yield thing
#     finally:
#         thing.close()

with closing(urlopen("https://www.python.org")) as page:
    for line in page:
        print(line)

