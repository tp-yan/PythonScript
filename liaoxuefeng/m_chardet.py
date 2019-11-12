import chardet
#当我们拿到一个bytes时，就可以对其检测编码。用chardet检测编码，只需要一行代码：
print(chardet.detect(b'Hello,World!'))

#注意到输出还有个confidence字段，表示检测的概率是1.0（即100%）。

#试试检测GBK编码的中文：
data = '离离原上草，一岁一枯荣'.encode('gbk')
print(chardet.detect(data))
#检测的编码是GB2312，注意到GBK是GB2312的超集，两者是同一种编码

#对UTF-8编码进行检测：
data = '离离原上草，一岁一枯荣'.encode('utf-8')
chardet.detect(data)

#对日文进行检测：
data = '最新の主要ニュース'.encode('euc-jp')
print(chardet.detect(data))

#用chardet检测编码，使用简单。获取到编码后，再转换为str