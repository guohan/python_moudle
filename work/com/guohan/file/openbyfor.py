#!/usr/bin/python3

# 打开一个文件
f = open("foo.txt", "r")

for line in f:
    print(line, end='')

# 关闭打开的文件
f.close()