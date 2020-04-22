#the code is to get the figure of the ratio of targeted IDs to the number of 
#valid user IDs in each interval of UNI,adpUNI and MHRW for Twitter 
import matplotlib.pyplot as plt
from pylab import mpl
import pandas as pd
import numpy as np
import math
from matplotlib.ticker import LogLocator,MultipleLocator
import seaborn as sns
import pandas as pd
mpl.rcParams['font.serif'] = ['Times']
mpl.rcParams['font.size'] = 12.0
sns.set_style('white')

mhrwFile = r'H:\testData\MHRW_4\MHRW_2700698\500000\repeat_IDStatistic.txt'

dataFile1 = r'H:\testData\weiboID_uniStatistic.txt'
dataFile2 = r'H:\testData\weiboID_uninStatistic.txt'
index = []
orig = []
uni = []
adpuni = []
mhrw = []
adpunin = []
with open(dataFile1,'r') as f:
    i = 0
    next(f)
    for row in f.readlines():
        row = row.strip('\n').split('\t')
        index.append(int(row[0]))
        orig.append(float(row[7]))
        uni.append(float(row[12]))
        sum = 0
        sum += float(row[8])+float(row[9])+float(row[10])+float(row[11])
        adpuni.append(round(sum/4,4))
        if i == 26:
            break
        i += 1
with open(dataFile2,'r') as f:
    i = 0
    next(f)
    for row in f.readlines():
        row = row.strip('\n').split('\t')
        sum = 0
        sum += float(row[8])+float(row[9])+float(row[10])+float(row[11])
        adpunin.append(round(sum/4,4))
        if i == 26:
            break
        i += 1
with open(mhrwFile,'r') as f:
    i = 0
    next(f)
    for row in f.readlines():
        row = row.strip('\n').split('\t')
        mhrw.append(float(row[3]))
        if i == 26:
            break
        i += 1
index = np.array(index)
uni = np.array(uni)
adpuni = np.array(adpuni)
orig = np.array(orig)
mhrw = np.array(mhrw)
adpunin = np.array(adpunin)

fig = plt.figure(figsize=(12,7))
ax1 = fig.add_subplot(111)
ax1.set_xlabel('user space %s' %(r'$(10^8)$'))
ax1.set_ylabel('ratio')
sns.lineplot(index[uni>0],uni[uni>0],label='UNI')
sns.scatterplot(index[uni>0],uni[uni>0])
sns.lineplot(index[adpuni>0],adpuni[adpuni>0],label='adpUNI')
sns.scatterplot(index[adpuni>0],adpuni[adpuni>0])
sns.lineplot(index[adpunin>0],adpunin[adpunin>0],label='adpUNI+N')
sns.scatterplot(index[adpunin>0],adpunin[adpunin>0])
sns.lineplot(index[mhrw>0],mhrw[mhrw>0],label='MHRW')
sns.scatterplot(index[mhrw>0],mhrw[mhrw>0])
ax1.legend(loc="upper left")

ax2 = ax1.twinx()
plt.plot(index[orig>0],orig[orig>0],color='black',linestyle='--',marker='o',label='original')
ax2.legend(loc="upper right")
plt.text(0.2,0.93,'(b)',transform=ax2.transAxes)
plt.savefig(r'H:\testData\UNI32_2\result3\wei_unifrom2.pdf',dpi = 300)
plt.show()
