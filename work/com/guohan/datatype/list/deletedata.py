# !/usr/bin/python3
'''
@author guohan
@createTime 2017-11-28
@desc show list data
'''
list = ['Google', 'Runoob', 1997, 2000]

print(list)
del list[2]
print("删除第三个元素 : ", list)
list.append("hahhah");


print(list.count(2000))
print(list)

for x in [1, 2, 3]: print(x, end=" ")