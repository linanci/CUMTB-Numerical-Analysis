import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams
from scipy import interpolate
from math import isnan
rcParams['font.sans-serif']='Fangsong'
def read_mingdan(nianduan,geshi):
    global dwuli,dshuxue,dhuaxue,mingdanwuli,mingdanshuxue,mingdanhuaxue,dic1,mingdantotal
    path=nianduan+'物理'+'成绩排名表'+geshi
    dwuli=pd.read_excel(path)
    ls=list(dwuli.columns)
    ls[0]='姓名'
    dwuli.columns=ls
    dwuli.set_index('姓名',inplace=True)
    path=nianduan+'数学'+'成绩排名表'+geshi
    dshuxue=pd.read_excel(path)
    ls=list(dshuxue.columns)
    ls[0]='姓名'
    dshuxue.columns=ls
    dshuxue.set_index('姓名',inplace=True)
    path=nianduan+'化学'+'成绩排名表'+geshi
    dhuaxue=pd.read_excel(path)
    ls=list(dhuaxue.columns)
    ls[0]='姓名'
    dhuaxue.columns=ls
    dhuaxue.set_index('姓名',inplace=True)
    mingdanwuli=dwuli.index
    mingdanshuxue=dshuxue.index
    mingdanhuaxue=dhuaxue.index
    mingdanwuli=list(mingdanwuli)
    mingdanshuxue=list(mingdanshuxue)
    mingdanhuaxue=list(mingdanhuaxue)
    mingdantotal=[]
    for i in mingdanwuli:
        mingdantotal.append(i)
    for i  in mingdanshuxue:
        mingdantotal.append(i)
    for i in mingdanhuaxue:
        mingdantotal.append(i)
    mingdantotal=tuple(mingdantotal)
    dic1={}
    for i in mingdantotal:
        k=0
        if i in mingdanwuli:
            k+=1
        if i in mingdanshuxue:
            k+=2
        if i in mingdanhuaxue:
            k+=4
        dic1[i]=k
    return 0
def data_extraction(name):
    global wuli,shuxue,huaxue,ywulinew,pwulinew,yshuxuenew,pshuxuenew,yhuaxuenew,phuaxuenew
    if dic1[name] == 1 or 3 or 5 or 7:
        wuli=dwuli.loc[name]
        wuli=wuli.dropna()
        wuli.index=wuli.index.astype(str)
        j=0
        for i in wuli.values:
            j+=1
        pwuli=np.arange(1,j+1)
        pwulinew=np.arange(1,j,0.1)
        func = interpolate.interp1d(pwuli,wuli.values,kind='cubic')
        ywulinew = func(pwulinew)
    if dic1[name] == 2 or 3 or 6 or 7:
        shuxue=dshuxue.loc[name]
        shuxue=shuxue.dropna()
        shuxue.index=shuxue.index.astype(str)
        j=0
        for i in shuxue.values:
            j+=1
        pshuxue=np.arange(1,j+1)
        pshuxuenew=np.arange(1,j,0.1)
        func = interpolate.interp1d(pshuxue,shuxue.values,kind='cubic')
        yshuxuenew = func(pshuxuenew)
    if dic1[name] == 4 or 5 or 6 or 7:
        huaxue=dhuaxue.loc[name]
        huaxue=huaxue.dropna()
        huaxue.index=huaxue.index.astype(str)
        j=0
        for i in huaxue.values:
            j+=1
        phuaxue=np.arange(1,j+1)
        phuaxuenew=np.arange(1,j,0.1)
        func = interpolate.interp1d(phuaxue,huaxue.values,kind='cubic')
        yhuaxuenew = func(phuaxuenew)
def drawAndSave(name,dir1):
    plt.style.use("ggplot")
    if dic1[name] == 1:
        wuli.plot()
        plt.legend(['物理'])
    if dic1[name] == 2:
        shuxue.plot()
        plt.legend(['数学'])
    if dic1[name] == 4:
        huaxue.plot()
        plt.legend(['化学'])
    if dic1[name] == 3:
        plt.plot(pwulinew,ywulinew)
        plt.plot(pshuxuenew,yshuxuenew)
        plt.legend(['物理','数学'])
    if dic1[name] == 5:
        plt.plot(pwulinew,ywulinew)
        plt.plot(phuaxuenew,yhuaxuenew)
        plt.legend(['物理','化学'])
    if dic1[name] == 6:
        plt.plot(pshuxuenew,yshuxuenew)
        plt.plot(phuaxuenew,yhuaxuenew)
        plt.legend(['数学','化学'])
    if dic1[name] == 7:
        plt.plot(pwulinew,ywulinew)
        plt.plot(pshuxuenew,yshuxuenew)
        plt.plot(phuaxuenew,yhuaxuenew)
        plt.legend(['物理','数学','化学'])
    picture_name=name+'的成绩曲线图'
    plt.title(picture_name,fontsize=20)
    plt.ylim(0,100)
    save_name=dir1+'\\'+ picture_name+'.jpg'
    plt.savefig(save_name)
    return 0
nianduan=input('请输入年段')
geshi=input('请输入格式')
read_mingdan(nianduan,geshi)
dir1=input('请输入存储的文件夹')
for i in mingdantotal:
    data_extraction(i)
    drawAndSave(i,dir1)
    plt.close('all')








