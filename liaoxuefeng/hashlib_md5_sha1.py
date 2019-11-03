#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 23:01:43 2019

@author: tangpeng

hashlib：包含常用哈希函数，比如MD5，SHA1.
摘要算法又称哈希算法、散列算法。它通过一个函数，把任意长度的数据转换为一个长度固定的数据串（通常用16进制的字符串表示）。 
摘要算法就是通过摘要函数f()对任意长度的数据data计算出固定长度的摘要digest，目的是为了发现原始数据是否被人篡改过。 
摘要算法之所以能指出数据是否被篡改过，就是因为摘要函数是一个单向函数，计算f(data)很容易，但通过digest反推data却非常困难。

哈希算法应用：
数据库中存储用户的摘要（哈希值，比如用户口令的MD5值）
存储MD5的好处是即使运维人员能访问数据库，也无法获知用户的明文口令。
"""

"""
1.MD5
以常见的摘要算法MD5为例，计算出一个字符串的MD5值.
MD5是最常见的摘要算法，速度很快，生成结果是固定的128 bit，通常用一个32位的16进制字符串表示。 
"""
import hashlib

md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

# 如果数据量很大，可以分块多次调用update()，最后计算的结果是一样的：
md5 = hashlib.md5()
md5.update("how to use md5 in ".encode('utf-8'))
md5.update("python hashlib?".encode('utf-8'))
print(md5.hexdigest())

"""
2. SHA1
调用SHA1和调用MD5完全类似,SHA1的结果是160 bit，通常用一个40位的16进制字符串表示。 
比SHA1更安全的算法是SHA256和SHA512，不过越安全的算法不仅越慢，而且摘要长度更长。 
"""
sha1 = hashlib.sha1()
sha1.update('how to use sha1 in '.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())


"""
练习
根据用户输入的口令，计算出存储在数据库中的MD5口令：
设计一个验证用户登录的函数，根据用户输入的口令是否正确，返回True或False：
"""
db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}


def calc_md5(password):
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8')) # 必须传入二进制数据
    key = md5.hexdigest()
    print(key)
    return key



def login(user, password):
    return db[user] == calc_md5(password)

# 测试:
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')


"""
练习
根据用户输入的登录名和口令模拟用户注册，计算更安全的MD5：
然后，根据修改后的MD5算法实现用户登录的验证：
"""
import random


db = {}

# 用户注册,以用户名的MD5作为 加盐
def register(username, password):
    db[username] = get_md5(password + username + get_md5(username))
    
def get_md5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()

class User(object):
    def __init__(self, username, password):
        self.username = username
        self.salt = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.password = get_md5(password + self.salt)
        
db = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}

def login(username, password):
    user = db[username]
    return user.password == get_md5(password+user.salt)

# 测试:
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')

"""
3. Hmac算法
`Hmac`算法：Keyed-Hashing for Message Authentication。它通过一个标准算法，
在计算哈希的过程中，把key混入计算过程中。
如果salt是我们自己随机生成的，通常我们计算MD5时采用md5(message + salt)。但实际上，
把salt看做一个“口令”，加salt的哈希就是：计算一段`message`的哈希值时，
根据不通口令计算出不同的哈希。要验证哈希值，必须同时提供正确的口令
"""
import hmac
message = b'hello,swjtu!'
key = b'tp'
h = hmac.new(key,message,digestmod='MD5')
result = h.hexdigest()
print(result)
print(hashlib.md5(message).hexdigest())


