#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 17:48:18 2019

@author: tangpeng

Base64：一种任意二进制到文本字符串的编码方法，常用于在URL、Cookie、网页中传输少量二进制数据。
Base64是一种通过查表的编码方法，不能用于加密，即使使用自定义的编码表也不行。
Base64适用于小段内容的编码，比如数字证书签名、Cookie的内容等。
Base64的原理很简单，首先，准备一个包含64个字符的数组：
['A', 'B', 'C', ... 'a', 'b', 'c', ... '0', '1', ... '+', '/']
对二进制数据进行处理，每3个字节一组，一共是3x8=24bit，划为4组，每组正好6个bit：
这样我们得到4个数字作为索引，然后查表，获得相应的4个字符，就是编码后的字符串。
所以，Base64编码会把3字节的二进制数据编码为4字节的文本数据，长度增加33%，好处是编码后的文本数据可以在邮件正文、网页等直接显示。
如果要编码的二进制数据不是3的倍数，最后会剩下1个或2个字节怎么办？Base64用\x00字节在末尾补足后，再在编码的末尾加上1个或2个=号，表示补了多少字节，解码的时候，会自动去掉。
"""

import base64
s1 = base64.b64encode(b'binary\x00string') # 将不可视的二进制数据编码为可视的二进制字符串
print(s1,type(s1)) # s1也是 <class 'bytes'>
b1 = base64.b64decode(s1)
print(b1,type(b1))

"""
由于标准的Base64编码后可能出现字符+和/，在URL中就不能直接作为参数，所以又有一种"url safe"的base64编码，\
其实就是把字符+和/分别变成-和_：
"""
s1 = base64.b64encode(b'i\xb7\x1d\xfb\xef\xff')
s2 = base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff')
print(s1)
print(s2)
print(base64.urlsafe_b64decode(s2))

"""
由于=字符也可能出现在Base64编码中，但=用在URL、Cookie里面会造成歧义，所以，很多Base64编码后会把=去掉：

# 标准Base64:
'abcd' -> 'YWJjZA=='
# 自动去掉=:
'abcd' -> 'YWJjZA'

去掉=后怎么解码呢？因为Base64是把3个字节变为4个字节，所以，Base64编码的长度永远是4的倍数，
因此，需要加上=把Base64字符串的长度变为4的倍数，就可以正常解码了。
"""
s3 = base64.urlsafe_b64encode(b'abcd')
print(s3)
s4 = s3.replace(b"==",b"")
print(s4)

length = len(s4)
if length%4 -1 == 0:
    s4 += b"="
else:
    s4 += b"=="
    
print(s4)
print(base64.urlsafe_b64decode(s4)) 

"""
练习
请写一个能处理去掉=的base64解码函数：
"""
def safe_base64_decode(s):
    s4 = s
    length = len(s4)
    if length%4 == 1:
        s4 += b"="
    elif length%4 == 2:
        s4 += b"=="
    return base64.urlsafe_b64decode(s4)

# 测试:
assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('ok')