#内置函数sorted：可以对list排序。sorted排序的关键在于实现一个映射函数
print(sorted([36,5,-12,9,-21]))
print(sorted([36,5,-12,9,-21],key=abs))	#key：指定排序的规则。即先将list的各个元素作用于key所值函数后，再进行排序
#忽略字母大小写的排序
print(sorted(['bob','about','Zoo','Credit'],key=str.lower))	#key=str.upper
print(sorted(['bob','about','Zoo','Credit'],key=str.lower,reverse=True))	#将默认排序结果反向排序