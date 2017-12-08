#@author guohan
# @createtime 2017-12-04

# f.readline()
#
# f.readline() 会从文件中读取单独的一行。换行符为 '\n'。f.readline() 如果返回一个空字符串, 说明已经已经读取到最后一行。
# readlines read more lines
#!/usr/bin/python3

file=open("foo.txt","r");#open the file
str=file.readlines() #read more line
print(str)#print the content
file.close()#close the file