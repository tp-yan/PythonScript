import base64

#请写一个能处理去掉=的base64解码函数：
def safe_base64_decode(s):
   # print(s)
    t = len(s) % 4
    #ss = str(s)
   # print(len(s))
    if t != 0:
        while t > 0:
            s = s+b"="
            t -= 1
    return base64.b64decode(s)


# 测试:
assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('ok')
