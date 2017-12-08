'''
@author guohan
@createTime 2017-12-01
@description 列出当前目录的所有文件
'''
import  os
print([d for d in os.listdir('.')])