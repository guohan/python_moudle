#元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号(())里，元素之间用逗号隔开。
#元组中的元素类型也可以不相同：

tinytuple = (123, 'runoob');
list = [ 'abcd', 786 , 2.23, 'runoob', 70.2 ];
tuple = ('abcd', 786, 2.23, 'runoob', 70.2,list);
print(list)
print(tuple)  # 输出完整元组
print(tuple[0])  # 输出元组的第一个元素
print(tuple[1:3])  # 输出从第二个元素开始到第三个元素
print(tuple[2:])  # 输出从第三个元素开始的所有元素
print(tinytuple * 2)  # 输出两次元组
print(tuple + tinytuple)  # 连接元组

hello=(5,6,7,"hello",True);
print(hello)
list[0]='abc';
print(list)
print(tuple)