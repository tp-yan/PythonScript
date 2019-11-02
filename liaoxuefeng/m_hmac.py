#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 09:51:43 2019

@author: tangpeng

hmac算法：
计算MD5时采用md5(message + salt)。但实际上，把salt看做一个“口令”，加salt的哈希就是：
计算一段message的哈希时，根据不通口令计算出不同的哈希。要验证哈希值，必须同时提供正确的口令。
hmac输出的长度和原始哈希算法的长度一致。需要注意传入的key和message都是bytes类型，str类型需要首先编码为bytes。

Python内置的hmac模块实现了标准的Hmac算法，它利用一个key对message计算“杂凑”后的hash，
使用hmac算法比标准hash算法更安全，因为针对相同的message，不同的key会产生不同的hash。
"""

import hmac

message = b'hello,sklois'
key = b'user-key'
# 使用hmac算法，只需传入要哈希的message和salt：key即可，由hmac去生成哈希值
h = hmac.new(key,message,digestmod='MD5') 
# 如果消息很长，可以多次调用h.update(msg)
print(h.hexdigest())

"""
练习
将上一节的salt改为标准的hmac算法，验证用户口令：
"""
import hmac, random

def hmac_md5(key, s):
    return hmac.new(key.encode('utf-8'), s.encode('utf-8'), 'MD5').hexdigest()

class User(object):
    def __init__(self, username, password):
        self.username = username
        # 每个用户的key由系统随机产生
        self.key = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.password = hmac_md5(self.key, password)

db = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}

def login(username, password):
    user = db[username]
    return user.password == hmac_md5(user.key, password)


# 测试:
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')