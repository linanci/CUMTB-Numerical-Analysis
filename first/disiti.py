from math import pow
def jisuan():
    a = []
    b = []
    c=[10,50,55,60,80,100,500,1000]
    for t in c:
        x1=float( pow(2,t+1))
        x2=float( pow(2,t+1)-1000)
        x3=x4=x5=x6=float( -(pow(2,t)-1))
        a.append(x1+x2+x3+x4+x5+x6)
        b.append(x6+x5+x4+x3+x2+x1)

    print('t的取值分别为',c)
    print('a，b的值分别为',a,b)
    return None
jisuan()