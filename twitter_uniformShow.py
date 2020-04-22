#the code is to get the figure of the ration of targeted IDs to the number of 
#valid user IDs in each interval of UNI,adpUNI and MHRW for Twitter 
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math
from pylab import mpl
from matplotlib.ticker import LogLocator,MultipleLocator
import seaborn as sns
sns.set_style('white')
mpl.rcParams['font.serif'] = ['Times']
mpl.rcParams['font.size'] = 12.0

adpunifile1 = r'H:\testData\twitter\adp\noNeighbours\IDstatistic_100w.txt'
adpuninfile1 = r'H:\testData\twitter\adp\addNeighbours\IDstatistic_100w.txt'
mhrwFile = r'H:\testData\twitter\mhrw\mhrwIDsta_100w.txt'

index = []
ori = []
uni = []
adpuni1 = []
with open(adpunifile1,'r') as f:
    i = 0
    next(f)
    for row in f.readlines():
        row = row.strip('\n').split('\t')
        index.append(int(row[0]))
        ori.append(float(row[7]))
        uni.append(float(row[8]))
        adpuni1.append(float(row[9]))
        if i == 61:
            break
        i += 1
        
adpunin1 = []
mhrw = []
with open(adpuninfile1,'r') as f:
    i = 0
    next(f)
    for row in f.readlines():
        row = row.strip('\n').split('\t')
        adpunin1.append(float(row[9]))
        if i == 61:
            break
        i += 1
with open(mhrwFile,'r') as f:
    i = 0
    next(f)
    for row in f.readlines():
        row = row.strip('\n').split('\t')
        mhrw.append(float(row[5]))
        if i == 61:
            break
        i += 1
        
adpunifile2 = r'H:\testData\twitter\adp\noNeighbours\IDstatistic_500w.txt'
adpuninfile2 = r'H:\testData\twitter\adp\addNeighbours\IDstatistic_500w.txt'
adpuni2 = []
adpunin2 = []
with open(adpunifile2,'r') as f:
    i = 0
    next(f)
    for row in f.readlines():
        row = row.strip('\n').split('\t')
        adpuni2.append(float(row[7]))
        if i == 61:
            break
        i += 1
with open(adpuninfile2,'r') as f:
    i = 0
    next(f)
    for row in f.readlines():
        row = row.strip('\n').split('\t')
        adpunin2.append(float(row[7]))
        if i == 61:
            break
        i += 1
index = np.array(index)
ori = np.array(ori)
uni = np.array(uni)
adpuni1 = np.array(adpuni1)
adpuni2 = np.array(adpuni2)
adpunin1 = np.array(adpunin1)
adpunin2 = np.array(adpunin2)
mhrw = np.array(mhrw)
fig = plt.figure(figsize=(12,7))
ax1 = fig.add_subplot(111)
ax1.set_xlabel('user space %s' %(r'$(10^6)$'))
ax1.set_ylabel('ratio')
sns.lineplot(index[uni>0],uni[uni>0],label='UNI')
sns.scatterplot(index[uni>0],uni[uni>0])
sns.lineplot(index[adpuni1>0],adpuni1[adpuni1>0],label=r'adpUNI$(10^6)$')
sns.scatterplot(index[adpuni1>0],adpuni1[adpuni1>0])
sns.lineplot(index[adpuni2>0],adpuni2[adpuni2>0],label=r'adpUNI$(5x10^6)$')
sns.scatterplot(index[adpuni2>0],adpuni2[adpuni2>0])
sns.lineplot(index[adpunin1>0],adpunin1[adpunin1>0],label=r'adpUNI+N$(10^6)$')
sns.scatterplot(index[adpunin1>0],adpunin1[adpunin1>0])
sns.lineplot(index[adpunin2>0],adpunin2[adpunin2>0],label=r'adpUNI+N$(5x10^6)$')
sns.scatterplot(index[adpunin2>0],adpunin2[adpunin2>0])
sns.lineplot(index[mhrw>0],mhrw[mhrw>0],label='MHRW')
sns.scatterplot(index[mhrw>0],mhrw[mhrw>0])
ax1.legend(loc="upper left")

ax2 = ax1.twinx()
plt.plot(index[ori>0],ori[ori>0],color='black',linestyle='--',marker='o',label='original')
ax2.legend(loc="upper right")
plt.text(0.25,0.93,'(a)',transform=ax2.transAxes)

plt.savefig(r'H:\testData\twitter\result\twi_uniform3.pdf',dpi = 300)
plt.show()