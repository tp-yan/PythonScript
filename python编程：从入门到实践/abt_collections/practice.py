from collections import namedtuple, deque, defaultdict, OrderedDict, Counter

# namedtuple('名称', [属性list]):
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x, p.y)

print(isinstance(p, Point), isinstance(p, tuple))

Circle = namedtuple('Circle', ['x', 'y', 'r'])

q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)
q.popleft()
print(q)
q.pop()
print(q)

dd = defaultdict(lambda: 'N/A')
dd['k1'] = 'abc'
print(dd['k1'])
print(dd['k2'])

d = dict([('a', 1), ('b', 2), ('c', 3)])
print(d)
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od)
od['x'] = 1
od['y'] = 2
od['z'] = 3
print(list(od.keys()))

# OrderedDict可以实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key：
class LastUpdatedOrderedDict(OrderedDict):

    def __int__(self,capacity):
        super(LastUpdatedOrderedDict,self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) -  containsKey >= self._capacity:
            last = self.popitem(last=False)
            print('remove:',last)
        if containsKey:
            del self[key]
            print('set:',(key,value))
        else:
            print('add:',(key,value))
        OrderedDict.__setitem__(self,key,value)

c = Counter()
for ch in "programming":
    c[ch] = c[ch] + 1
print(c)