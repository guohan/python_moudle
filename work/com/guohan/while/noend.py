# 我们可以通过设置条件表达式永远不为 false 来实现无限循环，实例如下：


# !/usr/bin/python3

var = 1
while var == 1:  # 表达式永远为 true
    num = int(input("输入一个数字  :"))
    print("你输入的数字是: ", num)

print("Good bye!")
