'''
@author guohan
@createTime 2017-12-1
@desc 过滤空格
'''
def not_empty(s):
    return s and s.strip()
L=list(filter(not_empty,['a','c','',' ',None]))
print(L)