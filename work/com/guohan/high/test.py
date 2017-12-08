
'''
@author guohan
@createTime 2017-12-01
@desc 过滤数据打印值
'''
L1=['Hello','World',18,'Apple',None]
print(L1)

from collections import  Iterable
print([s.lower() for s in L1 if isinstance(s,Iterable)==True])
