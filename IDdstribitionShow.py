#the code is to get the figures of distribution of valid user IDs for Sina weibo in the entire user space
import matplotlib.pyplot as plt
import numpy as np
import math
from matplotlib.ticker import LogLocator,MultipleLocator
import seaborn as sns
import matplotlib as mpl
sns.set_style('whitegrid')
mpl.rcParams['font.serif'] = ['Times']
mpl.rcParams['font.size'] = 12



file1 = r'H:\testData\ID_64.txt'
var1 = []
value1 = []
with open(file1,'r') as f:
    for row in f.readlines():
        row = row.strip('\n').split(',')
        if int(row[1]) != 0:
            var1.append(int(row[0]))
            value1.append(int(row[1])/473572141)

file2 = r'H:\testData\entireNetwork\ID_Dis2.txt'
var2 = []
value2 = []
with open(file2,'r') as f:
    for row in f.readlines():
        row = row.strip('\n').split(',')
        if int(row[1])!=0:
            var2.append(int(row[0]))
            value2.append(int(row[1]))

file3 = r'H:\testData\entireNetwork\ID_Dis3.txt'
var3 = []
value3 = []
with open(file3,'r') as f:
    for row in f.readlines():
        row = row.strip('\n').split(',')
        if int(row[0])<50000 and int(row[1])!=0:
            var3.append(int(row[0])/10**2)
            value3.append(int(row[1]))

fig = plt.figure(num = 1,figsize=(18,5))
ax1 = fig.add_subplot(131)
plt.xlabel('user sapce')
plt.ylabel('frequency of valid IDs')
plt.xscale('log',basex=2)
x_major1 = LogLocator(base=2,numticks=16)   #numticks为刻度数量
# x_major1 = MultipleLocator(25)
ax1.xaxis.set_major_locator(x_major1)
plt.yscale('log')
plt.text(0.03,0.9,'(a)',ha='center',va='center',transform=ax1.transAxes)
# sns.regplot(var3,value3,fit_reg = False,scatter_kws={'alpha':0.3,'s':10})
sns.lineplot(var1,value1)
sns.scatterplot(var1,value1)
plt.savefig(r'H:\testData\entireNetwork\result\ID_Dis1.png')

ax2 = fig.add_subplot(132)
plt.xlabel('user sapce %s' %(r'$(10^8)$'))
x_major2 = MultipleLocator(20)
ax2.xaxis.set_major_locator(x_major2)
plt.yscale('log')
plt.text(0.03,0.9,'(b)',ha='center',va='center',transform=ax2.transAxes)
sns.regplot(var2,value2,fit_reg = False,scatter_kws={'alpha':0.3,'s':10})
plt.savefig(r'H:\testData\entireNetwork\result\ID_Dis2.png')

ax3 = fig.add_subplot(133)
plt.xlabel('user sapce %s' %(r'$(10^7)$'))
x_major3 = MultipleLocator(25)
ax3.xaxis.set_major_locator(x_major3)
plt.yscale('log')
plt.xlim([0,500])
plt.text(0.05,0.9,'(c)',ha='center',va='center',transform=ax3.transAxes)
sns.regplot(var3,value3,fit_reg = False,scatter_kws={'alpha':0.3,'s':10})
plt.savefig(r'H:\testData\entireNetwork\result\ID_Dis3.png')
plt.show()

#twitter
# dataFile = r'H:\testData\twitter\ID_Dis2.txt'
# var = []
# value1 = []
# with open(dataFile,'r') as f:
#     for row in f.readlines():
#         row = row.strip('\n').split(',')
#         if int(row[1])!=0:
#             var.append(int(row[0]))
#             value1.append(int(row[1])/41652230)
            
# fig = plt.figure(figsize=(10,5))
# ax1 = fig.add_subplot(111)
# ax1.set_xlabel('user sapce %s' %(r'$(10^8)$'))
# ax1.set_ylabel('frequency of valid IDs')
# x_major2 = MultipleLocator(40)
# ax1.xaxis.set_major_locator(x_major2)
# sns.regplot(var,value1,fit_reg = False,scatter_kws={'alpha':0.3,'s':10})
# sns.lineplot(var,value2,label='UNI')
# sns.lineplot(var,value3,label='adpUNI+N')
# ax1.legend(loc="upper left")

# ax2 = ax1.twinx()
# sns.lineplot(var,value4,label='original')
# ax2.legend(loc="upper right")
# plt.text(1.0,-0.05,r'$(x10^8)$',ha='right',va='top',transform=ax2.transAxes)
# # sns.lineplot(x='index',y='original_ratio',ci=None,data=data)
# plt.show()


