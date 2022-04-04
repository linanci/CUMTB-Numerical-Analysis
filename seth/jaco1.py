import numpy as np
import pandas as pd
A=np.array([[15 ,4 ,7 ],[2,15,8],[3,6,10]])
b=np.array([26,25,19])
N=500
def shengchengjz(n):
    a = np.ones(n) * 6
    b = np.ones(n-1)
    c = np.ones(n-1) * 8
    A = np.diag(a) + np.diag(b, 1) + np.diag(c, -1)
    return A
def jacobi(A,b,n,E):
    x0=np.array([0]*n)
    x=[(b[i] -sum([A[i,j]*x0[j] for j in range(n) if i!=j]))/A[i,i]  for i in range(n)]
    x=np.array(x)
    k=1
    ls=[np.linalg.norm([x[i]-x0[i] for i in range(n)],ord=np.inf)]
    while np.linalg.norm([x[i]-x0[i] for i in range(n)],ord=np.inf) >E and k<N :
        k+=1
        x0=x
        x=[(b[i] -sum([A[i,j]*x0[j] for j in range(n) if i !=j]))/A[i,i]  for i in range(n)]
        ls.append(np.linalg.norm([x[i]-x0[i] for i in range(n)],ord=np.inf))
    return x,k,ls
print(jacobi(A,b,3,1e-5))
_,_,ls=jacobi(A,b,3,1e-5)
pd.DataFrame({'误差':ls}).to_excel('第一问.xls')
di={}
for i in [3,10,100,200]:
    b=[7]+[15]*(i-2)+[14]
    _,_,ls=jacobi(shengchengjz(i), b, i, 1e-5)
    di[i]=[ls[-1],ls[-10],ls[-20],ls[-30]][::-1]
    print(jacobi(shengchengjz(i),b,i,1e-5))
pd.DataFrame(di,index=[-30,-20,-10,-1]).to_excel('第二问.xls')