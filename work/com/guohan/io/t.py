'''
@author guohan
@createTime 2017-12-04
@desc get the suffix file name
'''
def getfile_fix(filename):
    return filename[filename.rfind('.') + 1:]


print(getfile_fix('runoob.xml'))

import math
print('常量 PI 的值近似为： {}。'.format(math.pi))
print('常量 PI 的值近似为：%5.3f。' % math.pi)