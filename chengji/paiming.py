import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams
rcParams['font.sans-serif']='Fangsong'
list1=['物理','数学','化学']
def read_grades(nianduan,geshi) :
    global gradeswuli,gradesshuxue,gradeshuaxue
    gradeswuli=pd.DataFrame()
    gradeshuaxue=pd.DataFrame()
    gradesshuxue=pd.DataFrame()
    global list2
    list2=[gradeswuli,gradesshuxue,gradeshuaxue]
    j=0
    for i in list1:
        path='2020'+nianduan+'A班'+i+'成绩表'+geshi
        list2[j]=pd.read_excel(path)
        j+=1
    return 0
def data_processing(grades):
    grades.set_index('姓名',inplace=True)
    '''grades.fillna(value=0,inplace=True)'''
    '''grades.fillna(value=np.NaN,inplace=True)'''
    return 0
def creat_mingdan():
    global mingdanwuli,mingdanshuxue,mingdanhuaxue
    mingdanwuli=list()
    mingdanshuxue=list()
    mingdanhuaxue=list()
    global list3
    list3=[mingdanwuli,mingdanshuxue,mingdanhuaxue]
    j=0
    i=0
    while i<3:
        list3[i]=list(list2[j].index.dropna())
        list3[i].remove('平均分')
        j+=1
        i+=1
    return 0
def data_extraction():
    global list4
    p=0
    q=0
    global dwuli,dshuxue,dhuaxue
    dwuli=pd.DataFrame(None,index=list3[0])
    dshuxue=pd.DataFrame(None,index=list3[1])
    dhuaxue=pd.DataFrame(None,index=list3[2])
    list4=[dwuli,dshuxue,dhuaxue]
    while p<3:
        list4[p]['姓名']=list4[p].index
        list4[p].set_index('姓名')
        j=0
        for i in list2[q].columns:
            paiming=list2[q].iloc[:,j]
            paiming=paiming.drop('平均分')
            total=paiming.count()
            rank_paiming=paiming.rank(ascending=False)
            dic1={}
            for k in list3[q][:]:
                result=(1-rank_paiming[k]/total)*100
                dic1[k]=result
            s1=pd.Series(dic1)
            d1=pd.DataFrame(s1)
            d1.columns=[i]
            d1['姓名']=d1.index
            d1.set_index('姓名')
            list4[p]=pd.merge(list4[p],d1,how='left',left_index=True,right_index=True,sort=True)

            j+=1
        list4[p].drop('姓名_x',axis=1,inplace=True)
        list4[p].drop('姓名_y',axis=1,inplace=True)
        p+=1
        q+=1
def data_out():
    global nianduan,geshi
    nianduan=input('请输入年段')
    geshi=input('请输入格式')
    read_grades(nianduan,geshi)
    for i in list2:
        data_processing(i)
    creat_mingdan()
    data_extraction()


data_out()
i=0
print(list4)
while i <3:
    file=nianduan+list1[i]+'成绩排名表'+geshi
    list4[i].to_excel(file)
    i+=1
