# open(filename, mode)
#
#     filename：filename 变量是一个包含了你要访问的文件名称的字符串值。
#     mode：mode决定了打开文件的模式：只读，写入，追加等。所有可取值见如下的完全列表。这个参数是非强制的，默认文件访问模式为只读(r)。

#!/usr/bin/python3
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')
# -*-coding:utf-8-*-

# 打开一个文件
f = open("foo.txt", "w")

f.write( "Python 是一个非常好的语言。\n是的，的确非常好!!\n" )

# 关闭打开的文件
f.close()