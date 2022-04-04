import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams
from scipy import interpolate
from math import isnan
rcParams['font.sans-serif']='Fangsong'
def read_grades(path) :
    global grades
    grades=pd.read_excel(path)
    return 0
def data_processing(grades):
    ls=list(grades.columns)
    '''ls[0]='姓名'''''
    grades.columns=ls
    print(grades)
    grades.drop(grades.columns[0],axis=1,inplace=True)
    grades.set_index('姓名',drop=True ,inplace=True)

    '''grades.fillna(value=0,inplace=True)'''
    '''grades.fillna(value=np.NaN,inplace=True)'''
    return 0
def data_extraction(name,grades):
    global average,personal,yanew,panew,ypnew,ppnew,pp,p1,ability_label
    print(grades)
    personal=grades.loc[name]
    '''for i in personal.index:
        if isnan(personal.loc[i]):
            personal=personal.drop(i)'''

    j=0
    for i in personal.values:
        j+=1

    pp=np.linspace(0,2*np.pi,j,endpoint=False)
    pp=np.arange(1,j+1)
    ppnew=np.arange(1,j,0.1)
    func = interpolate.interp1d(pp,personal.values,kind='cubic')
    ypnew = func(ppnew)
    p1=np.linspace(0,2*np.pi,j,endpoint=False)
    ability_label = ['概念训练','简单计算','综合计算','图像训练','概念训练']
    '''ability_label =['原子结构','物质的量','摩尔质量','气体摩尔体积','物质的量浓度','原子结构']'''
    '''ability_label =['集合关系','集合运算','不等式','分段函数','定义域','值域1','值域2','单调性与奇偶性1','单调性与奇偶性2','集合关系']'''
    '''for i in range(j):
        ability_label.append('第'+str(i+1)+'次小测')
    ability_label.append('第'+'1'+'次小测')'''
    personal.loc[j]=personal.iloc[0]
    p1=np.append(p1,0)
    print(p1)
    return 0
def drawAndSave(name,obj,dir1,personal):

    plt.style.use("ggplot")
    ax1 = plt.subplot(111, projection = "polar")
    ax1.plot(p1,personal.values, "r")
    ax1.fill(p1, personal.values, "r",alpha=0.3)
    print(p1)
    ax1.set_xticks(p1)
    ax1.set_xticklabels(ability_label,y=0.1)
    picture_name=name+'的模块能力雷达图'+'('+obj+')'
    plt.title(picture_name,fontsize=20)
    save_name=dir1+'\\'+ picture_name+'.jpg'
    plt.savefig(save_name)
    return 0
def tiqumingdan():
    global mingdan
    mingdan=grades.index
    mingdan=list(mingdan)
    return 0
path=input('请输入路径或直接输入文件名\n')
read_grades(path)
data_processing(grades)
tiqumingdan()
obj=input('请输入科目\n')
dir1=input('请输入需要保存的文件夹名\n')
for i in mingdan:
    data_extraction(i,grades)
    try:
        drawAndSave(i,obj,dir1,personal)
    except TypeError:
        print('请检查是否有不是数字的单元格')
    plt.close('all')



