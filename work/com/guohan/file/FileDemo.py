# -*- coding: UTF-8 -*-
import os;

# document = open("testfile.txt", "w+");
# print ("文件名: ", document.name);
# document.write("这是我创建的第一个测试文件！\nwelcome!");
# print (document.tell());
# #输出当前指针位置
# document.seek(os.SEEK_SET);
# #设置指针回到文件最初
# context = document.read();
# print (context);
# document.close();
doc=open("2017.txt","w+");
print("filename",doc.name)
doc.write("this is my first file\nwelcome!");
print(doc.tell());
doc.seek(os.SEEK_SET);
context=doc.read();
print(context);
doc.close();