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
    grades.set_index('姓名',inplace=True)
    '''grades.iloc[:,0]=grades.iloc[:,0]*4
    grades.iloc[:,1]=grades.iloc[:,1]*2
    grades.iloc[:,2]=grades.iloc[:,2]*2'''
    '''grades.fillna(value=grades.mean(1),inplace=True)
    print(grades.mean(axis=1))'''
    print(grades)
    '''grades.fillna(value=np.NaN,inplace=True)'''
    return 0
def data_extraction(name,grades):
    global average,personal,yanew,panew,ypnew,ppnew
    average=grades.loc['平均分']
    personal=grades.loc[name]
    for i in personal.index:
        if isnan(personal.loc[i]):
            personal=personal.drop(i)
            average=average.drop(i)

    j=0
    for i in personal.values:
        j+=1
    pp=np.arange(1,j+1)
    ppnew=np.arange(1,j,0.1)
    func = interpolate.interp1d(pp,personal.values,kind='cubic')
    ypnew = func(ppnew)
    j=0
    for i in average.values:
        j+=1
    pa=np.arange(1,j+1)
    panew=np.arange(1,j,0.1)
    func = interpolate.interp1d(pa,average.values,kind='cubic',bounds_error=False)
    yanew = func(panew)
    return 0
def drawAndSave(name,obj,dir1,average,personal):
    plt.style.use("ggplot")
    plt.plot(panew,yanew)
    plt.plot(ppnew,ypnew)
    picture_name=name+'的成绩曲线图'+'('+obj+')'
    plt.title(picture_name,fontsize=20)
    plt.legend(['平均分',name])
    plt.ylim(0,110)
    plt.xticks(np.arange(1,5,1))
    save_name=dir1+'\\'+ picture_name+'.jpg'
    plt.savefig(save_name)
    return 0
def tiqumingdan():
    global mingdan
    mingdan=grades.index
    mingdan=list(mingdan)[:-1]
    return 0
path=input('请输入路径或直接输入文件名\n')
read_grades(path)
data_processing(grades)
print(grades)
tiqumingdan()
obj=input('请输入科目\n')
dir1=input('请输入需要保存的文件夹名\n')
for i in mingdan:
    data_extraction(i,grades)
    try:
        drawAndSave(i,obj,dir1,average,personal)
    except TypeError:
        print('请检查是否有不是数字的单元格')
    plt.close('all')



