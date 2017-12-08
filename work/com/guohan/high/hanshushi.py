from functools import  reduce
def add(x,y):
    return x*10+y
value=reduce(add,[1,3,5,7,9])
print(value)