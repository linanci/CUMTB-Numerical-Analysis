x=1,2,3,4
y=0,-5,-6,3
def prod(ls):
    pro=1
    for i in ls:
        pro*=i
    return pro
x0=1.5
n=3
def Lchazhi(x0,n):
    return sum([y[i]*prod([x0-x[j] for j in range(n) if i !=j])/prod(x[i]-x[j] for j in range(n) if i !=j) for i in range(n)])
f05=[Lchazhi(0.5,i) for i in range(2,5)]
f15=[Lchazhi(1.5,i) for i in range(2,5)]
f25=[Lchazhi(2.5,i) for i in range(2,5)]
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']
(pd.DataFrame({'f(0.5)':f05,'f(1.5)':f15,'f(2.5)':f25})).to_excel('第一题数据.xls')
x=np.linspace(0.3,0.9,num=7)
y=np.log(x)
f054=[Lchazhi(0.54,i) for i in range(6)]
E=[abs(f054[i]-math.log(0.54)) for i in range(6)]
(pd.DataFrame({'f(0.54)':f054,'误差':E})).to_excel('第二题数据.xls')
plt.figure(figsize=(16,9))
plt.plot(E)
plt.xticks(range(6), labels=[str(i) +'次Lagrange插值' for i in range(1,7)],fontsize=16)
plt.title('n次插值误差曲线图',fontsize=30)
plt.savefig('误差曲线.jpg')