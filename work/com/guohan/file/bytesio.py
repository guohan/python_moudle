from io import  BytesIO
import  os
f=BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())


# print(os.environ)
str=x
x for x in os.listdir(".") if os.path.isdir(x)
print()