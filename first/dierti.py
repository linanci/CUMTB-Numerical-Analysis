M=10e15
def jisuan(M):
    print('当M的值为' + str(M) + '时：')
    print('A=1+2+3+4+M-M的值为', 1+2+3+4+M-M)
    print('B=M+1+2+3+4-M的值为',M+1+2+3+4-M)
    print('C=M+4+3+2+1-M的值为',M+4+3+2+1-M)
    return None

jisuan(M)
M*=10
jisuan(M)
