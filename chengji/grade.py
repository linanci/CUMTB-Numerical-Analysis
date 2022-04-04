import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams
rcParams['font.sans-serif']='Fangsong'
def read_grades(path) :
    global grades
    grades=pd.read_excel(path)
    return 0
def data_processing(grades):
    grades.set_index('姓名',inplace=True)
    '''grades.fillna(value=0,inplace=True)'''
    return 0
def data_extraction(name,grades):
    global average,personal
    average=grades.loc['平均分']
    personal=grades.loc[name]
    return 0
def drawAndSave(name,obj,dir1,average,personal):
    average.plot()
    personal.plot()
    x_major_locator=plt.MultipleLocator(1)
    ax=plt.gca()
    ax.xaxis.set_major_locator(x_major_locator)
    picture_name=name+'的成绩曲线图'+'('+obj+')'
    plt.title(picture_name,fontsize=20)
    plt.legend(['平均分',name])
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
tiqumingdan()
obj=input('请输入科目\n')
dir1=input('请输入需要保存的文件夹名\n')
for i in mingdan:
    data_extraction(i,grades)
    drawAndSave(i,obj,dir1,average,personal)
    plt.close('all')



