import itertools, time
from functools import reduce

'''
# chain()可以把一组迭代对象串联起来，形成一个更大的迭代器：
for c in itertools.chain("ABC", 'xyz', "123"):
    print(c)

# groupby()把迭代器中相邻的重复元素挑出来放在一起：
# 实际上挑选规则是通过函数(可以省略)完成的，只要作用于函数的两个元素返回的值相等，这两个元素就被认为是在一组的，而函数返回值作为组的key。
for key, group in itertools.groupby("AaaABbBbBCcCC1223", lambda c: c.upper()):
    print(key, list(group))

# repeat()负责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数：
# ns = itertools.repeat('A',5)
# for n in ns:
#     print(n)
#
#
# #cycle()会把传入的一个序列无限重复下去
# cs = itertools.cycle("ABCD")
# for c in cs:
#     print(c)
#     time.sleep(1)

# count()会创建一个无限的迭代器
natuals = itertools.count(1)
# 无限序列虽然可以无限迭代下去，但是通常我们会通过takewhile()等函数根据条件判断来截取出一个有限的序列：
ns = itertools.takewhile(lambda x: x % 2 == 1, natuals)
print(list(ns))
for n in natuals:
    print(n)
    time.sleep(1)
'''

# 练习
# 计算圆周率可以根据公式：
# 利用Python提供的itertools模块，我们来计算这个序列的前N项和：

def m_add(x,y):
    return x+y

def add_symbol(x):
    if (x // 2) % 2 == 0:
        value = 4 / x
    else:
        value = -4 / x
    return value


def pi(N):
    ' 计算pi的值 '
    # step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...
    order = itertools.count(1,2)
    # step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.
    m_list = []
    for n in order:
        if n >= 2 * N + 1:
            break
        m_list.append(n)
    print(m_list)
    #time.sleep(10)
    # step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...
    new_list =list(map(add_symbol,m_list))
    # step 4: 求和:
    #print(new_list)
    return reduce(m_add,new_list)


# 测试:
print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
print('ok')
