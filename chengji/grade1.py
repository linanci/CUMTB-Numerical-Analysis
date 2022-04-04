import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
grades=pd.read_excel('grade.xlsx')
grades.set_index('姓名',inplace=True)
grades.fillna(value=0,inplace=True)
average=grades.loc['平均分']
personal=grades.loc['赖贵和']
from matplotlib import rcParams
rcParams['font.sans-serif']='Fangsong'
average.plot()
personal.plot()
x_major_locator=plt.MultipleLocator(1)
ax=plt.gca()
ax.xaxis.set_major_locator(x_major_locator)
plt.title('赖贵和的成绩曲线图',fontsize=20)
plt.legend(['平均分','赖贵和'])
plt.savefig('赖贵和的成绩曲线图.jpg')