'''
@author guohan
@createTime 2017-12-01
@desc slice operation
'''
L=['hadoop','hbase','hive','spark','mahout']
print(L[0:3])
l1=list(range(100))
print(l1)
print(l1[:10])#get the top 10
print(l1[-10:])#get the last 10
print(l1[::5])
print(l1[:10:2])