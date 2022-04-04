from math import sqrt,pow
def jisuan(x,n):
    for i in range(n):
        x=sqrt(x)
    for i in range(n):
        x=pow(x,2)

    return x
x=8
n=50
print('执行操作前：',x)
print('执行操作后：',jisuan(x,n))