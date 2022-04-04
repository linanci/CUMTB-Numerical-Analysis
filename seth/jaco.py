import  numpy as np
def shengchengjz(n):
    a = np.ones(n) * 6
    b = np.ones(n-1)
    c = np.ones(n-1) * 8
    A = np.diag(a) + np.diag(b, 1) + np.diag(c, -1)
    return A
