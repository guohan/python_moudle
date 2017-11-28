#check the data typ      type()不会认为子类是一种父类类型。 isinstance()会认为子类是一种父类类型。
a, b, c, d = 20, 5.5, True, 4+3j
print(type(a), type(b), type(c), type(d))