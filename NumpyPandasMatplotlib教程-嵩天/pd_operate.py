# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 13:15:01 2018

@author: tangpeng
"""

import numpy as np
import pandas as pd


#算术运算根据行列索引补齐后运算，运算默认产生浮点数
#补齐时缺项填充NaN (空值)
#二维和一维、一维和零维间为广播运算
#采用+ ‐ * /符号进行的二元运算产生新的对象

a = pd.DataFrame(np.arange(12).reshape(3,4))
b = pd.DataFrame(np.arange(20).reshape(4,5))
a+b                     #对应索引进行运算，其他的不运算用NaN填充
#等价的方法，还有.sub() .mul() .div()：可以增加可选参数
b.add(a,fill_value=100) #NaN用100填充

c = pd.Series(np.arange(4))
c-10    #广播运算：不同维度运算，低维的每个元素作用在高维元素上。一维与二维运算时，默认在1轴运算
b-c     # b的每一行减去c
b.sub(c,axis=0) #指定在0轴运算。b的每一列减去c

#比较运算只能比较相同索引的元素，不进行补齐
#二维和一维、一维和零维间为广播运算
#采用> < >= <= == !=等符号进行的二元运算产生布尔对象
a = pd.DataFrame(np.arange(12).reshape(3,4))
b = pd.DataFrame(np.arange(12,0,-1).reshape(3,4))
a>b     #同维度运算尺寸必须一致
a==b
a > c   #不同维度，广播运算，默认在1轴
c > 3
