from PIL import Image
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
def mergeReport(files,name,ax,leixing):
    baseimg=Image.open(files[0])
    sz = baseimg.size
    basemat=np.atleast_2d(baseimg)
    for file in files[1:]:
        im=Image.open(file)
    #resize to same width
        sz2 = im.size
        if sz2!=sz:
            im=im.resize((sz[0],round(sz2[0] / sz[0] * sz2[1])),Image.ANTIALIAS)
        mat=np.atleast_2d(im)
        basemat=np.append(basemat,mat,axis=ax)
    report_img=Image.fromarray(basemat)
    report_img.save('.\\A班'+leixing+'\\'+name+leixing+'.png')
def tiqumingdan(mingdan):

    mingdan=pd.read_excel(mingdan)
    mingdan.set_index('姓名',inplace=True)
    mingdan=mingdan.index
    return mingdan
mingdan=input('请输入名单文件名')
mingdan=tiqumingdan(mingdan)
sub=['数学','物理','化学']
dils=['新高一A班数学','新高一A班物理','新高一A班化学']
for name in mingdan:
    files1=[]
    files2=[]
    files3=[]
    i=0
    while i < 3:
        files1.append('.\\'+dils[i]+'\\'+name+'的成绩曲线图('+sub[i]+').jpg')
        files2.append('.\\'+dils[i]+'极坐标'+'\\'+name+'的模块能力雷达图('+sub[i]+').jpg')
        i+=1
    mergeReport(files1,name,0,'曲线')
    mergeReport(files2,name,0,'极坐标')
    files3.append('.\\'+'A班曲线'+'\\'+name+'曲线'+'.png')
    files3.append('.\\'+'A班极坐标'+'\\'+name+'极坐标'+'.png')
    mergeReport(files3,name,1,'总')
