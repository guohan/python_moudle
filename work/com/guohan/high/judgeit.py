'''
@author guohan
@createTiime 2017-12-01
@desc judge the iterable

'''
from collections import  Iterable

print(isinstance('abc',Iterable))
print(isinstance([1,2,3],Iterable))
print(isinstance({'a':1,'b':2},Iterable))
print(isinstance(123,Iterable))
#遍历下标与value
for i,value in enumerate(['a','b','c']):
    print(i,value)
