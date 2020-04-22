#the code is to get the figure of sampling efficiency of UNI,adpUNI,adpUNI+N and MHRW for Sina weibo and Twitter. 
import matplotlib.pyplot as plt
from pylab import mpl
import sys
import pandas as pd
import numpy as np
import seaborn as sns
mpl.rcParams['font.serif'] = ['Times']
mpl.rcParams['font.size'] = 12.0
sns.set_style('whitegrid')

def getxy(fiels):
    newData = pd.DataFrame()
    # x = pd.DataFrame()
    for file in fiels:
        data = pd.read_csv(file,header=-1,delimiter='\t')
        # newData = pd.concat([newData,data[1]],axis=1,ignore_index=True)
        # print(data)
        newData = pd.concat([newData,data.iloc[0:861,1:2]],axis=1,ignore_index=True)
        # newData = pd.concat([newData,data.iloc[0:66661,1:2]],axis=1,ignore_index=True)
        # if len(data)>=len(x):
        #     x = data[0]

    newData['avg'] = newData.mean(axis=1)
    # newData['std'] = newData.std(axis=1)
    newData['st'] = [i*1000 for i in range(1,862)]
    # newData['tar'] = newData['st']*newData['avg']
    # print(newData)
    return newData

def getxy2(fiels):
	newData = pd.DataFrame()
	x = pd.DataFrame()
	for file in fiels:
		data = pd.read_csv(file,header=-1,delimiter='\t')
		newData = pd.concat([newData,data[1]],axis=1,ignore_index=True)
		if len(data)>=len(x):
			x = data[0]

	newData['avg'] = newData.mean(axis=1)
	# newData['std'] = newData.std(axis=1)
	newData['st'] = x
	# newData['tar'] = newData['st']*newData['avg']
	# print(newData)
	return newData

def binarySearch(data,target):
    low = 0
    high = len(data)
    while low<=high:
        mid = low+(high-low)//2
        if data[mid]>target:
            high = mid-1
        elif data[mid]<target:
            low = mid+1
        else:
            return mid
    if low<len(data) and data[low]>=target:
        return low
    else:
        return -1

path1 = r'H:\testData\twitter\adp\noNeighbours'
path2 = r'H:\testData\twitter\adp\addNeighbours'

path3 = r'H:\testData\twitter\mhrw'

ufile = r'H:\testData\twitter\uni\noNeighbours\record.txt'

mfile1 = r'%s\MHRW_21277270\record.txt' %path3
mfile2 = r'%s\MHRW_44511742\record.txt' %path3
mdata = getxy([mfile1,mfile2])
mx1 = mdata.iloc[810,3]
my1 = mdata.iloc[810,2]


file11 = r'%s\10000\record1.txt' %path1
file12 = r'%s\10000\record2.txt' %path1
file13 = r'%s\10000\record3.txt' %path1
adpdata1 = getxy([file11,file12,file13])
dx11 = adpdata1.iloc[810,4]
dy11 = adpdata1.iloc[810,3]



file21 = r'%s\50000\record1.txt' %path1
file22 = r'%s\50000\record2.txt' %path1
file23 = r'%s\50000\record3.txt' %path1
adpdata2 = getxy([file21,file22,file23])
dx21 = adpdata2.iloc[810,4]
dy21 = adpdata2.iloc[810,3]


file31 = r'%s\100000\record1.txt' %path1
file32 = r'%s\100000\record2.txt' %path1
file33 = r'%s\100000\record3.txt' %path1
adpdata3 = getxy([file31,file32,file33])
dx31 = adpdata3.iloc[810,4]
dy31 = adpdata3.iloc[810,3]


file41 = r'%s\150000\record1.txt' %path1
file42 = r'%s\150000\record2.txt' %path1
file43 = r'%s\150000\record3.txt' %path1
adpdata4 = getxy([file41,file42,file43])
dx41 = adpdata4.iloc[810,4]
dy41 = adpdata4.iloc[810,3]

udata = getxy([ufile])
ux1 = udata.iloc[810,2]
uy1 = udata.iloc[810,1]


f = plt.figure(figsize=(14,10))
ax1 = f.add_subplot(221)
sns.lineplot(adpdata1['st'],adpdata1['avg'],ax=ax1)
sns.lineplot(adpdata2['st'],adpdata2['avg'],ax=ax1)
sns.lineplot(adpdata3['st'],adpdata3['avg'],ax=ax1)
sns.lineplot(adpdata4['st'],adpdata4['avg'],ax=ax1)
sns.lineplot(mdata['st'],mdata['avg'],ax=ax1)
sns.lineplot(udata['st'],udata['avg'],ax=ax1)
plt.scatter([dx11,dx21,dx31,dx41,mx1,ux1],[dy11,dy21,dy31,dy41,my1,uy1],s=10,color = 'b')
plt.plot([dx11,dx11],[dy11,0],'r--',lw=2,alpha=0.7)

ax1.set_xlabel('sample times')
ax1.set_ylabel('sampling size')
ax1.set_xscale('log')
plt.text(0.1,0.94,'(a)',ha='center',va='center',transform=ax1.transAxes)

f11 = r'%s\10000\record1.txt' %path2
f12 = r'%s\10000\record2.txt' %path2
f13 = r'%s\10000\record3.txt' %path2
f1 = getxy([f11,f12,f13])
fx11 = f1.iloc[810,4]
fy11 = f1.iloc[810,3]

f21 = r'%s\50000\record1.txt' %path2
f22 = r'%s\50000\record2.txt' %path2
f23 = r'%s\50000\record3.txt' %path2
f2 = getxy([f21,f22,f23])
fx21 = f2.iloc[810,4]
fy21 = f2.iloc[810,3]

f31 = r'%s\100000\record1.txt' %path2
f32 = r'%s\100000\record2.txt' %path2
f33 = r'%s\100000\record3.txt' %path2
f3 = getxy([f31,f32,f33])
fx31 = f3.iloc[810,4]
fy31 = f3.iloc[810,3]

f41 = r'%s\150000\record1.txt' %path2
f42 = r'%s\150000\record2.txt' %path2
f43 = r'%s\150000\record3.txt' %path2
f4 = getxy([f41,f42,f43])
fx41 = f4.iloc[810,4]
fy41 = f4.iloc[810,3]

ax2 = f.add_subplot(222)
sns.lineplot(f1['st'],f1['avg'],ax=ax2,label=r'$I=1x10^4$')
sns.lineplot(f2['st'],f2['avg'],ax=ax2,label=r'$I=5x10^4$')
sns.lineplot(f3['st'],f3['avg'],ax=ax2,label=r'$I=1x10^5$')
sns.lineplot(f4['st'],f4['avg'],ax=ax2,label=r'$I=1.5x10^5$')
sns.lineplot(mdata['st'],mdata['avg'],ax=ax2,label='MHRW')
sns.lineplot(udata['st'],udata['avg'],ax=ax2,label='UNI')
plt.scatter([fx11,fx21,fx31,fx41,mx1,ux1],[fy11,fy21,fy31,fy41,my1,uy1],s=10,color = 'b')
plt.plot([fx11,fx11],[fy11,0],'r--',lw=2,alpha=0.7)
ax2.set_xlabel('sample times')
ax2.set_ylabel('')
ax2.set_title('adpUNI+N')
ax2.set_xscale('log')
plt.text(0.1,0.94,'(b)',ha='center',va='center',transform=ax2.transAxes)
plt.legend(loc='center left')


p1 = r'H:\testData\UNI32_2\noNeighbors'
p2 = r'H:\testData\UNI32_2\addNeighbors'
p3 = r'H:\testData\MHRW_4'

uf = r'H:\testData\UNI_2\noNeighbors\record.txt'

mf1 = r'%s\MHRW_48046\record.txt' %p3
mf2 = r'%s\MHRW_507327\record.txt' %p3
mf3 = r'%s\MHRW_2700698\record.txt' %p3
mf4 = r'%s\MHRW_1666560985\record.txt' %p3
mf5 = r'%s\MHRW_1771473791\record.txt' %p3
mfL = [mf1,mf2,mf3,mf4,mf5] 
md = getxy2(mfL)
mx_1 = md.iloc[66659,6]
my_1 = md.iloc[66659,5]

nfile11 = r'%s\500000_10000_1\record.txt' %p1
nfile12 = r'%s\500000_10000_2\record.txt' %p1
nfile13 = r'%s\500000_10000_3\record.txt' %p1
nfile14 = r'%s\500000_10000_4\record.txt' %p1
nfile15 = r'%s\500000_10000_5\record.txt' %p1
nfileList1 = [nfile11,nfile12,nfile13,nfile14,nfile15]
ndata1 = getxy2(nfileList1)
ndx11 = ndata1.iloc[66659,6]
ndy11 = ndata1.iloc[66659,5]

nfile21 = r'%s\500000_50000_1\record.txt' %p1
nfile22 = r'%s\500000_50000_2\record.txt' %p1
nfile23 = r'%s\500000_50000_3\record.txt' %p1
nfile24 = r'%s\500000_50000_4\record.txt' %p1
nfile25 = r'%s\500000_50000_5\record.txt' %p1
nfileList2 = [nfile21,nfile22,nfile23,nfile24,nfile25]
ndata2 = getxy2(nfileList2)
ndx21 = ndata2.iloc[66659,6]
ndy21 = ndata2.iloc[66659,5]

nfile31 = r'%s\500000_100000_1\record.txt' %p1
nfile32 = r'%s\500000_100000_2\record.txt' %p1
nfile33 = r'%s\500000_100000_3\record.txt' %p1
nfile34 = r'%s\500000_100000_4\record.txt' %p1
nfile35 = r'%s\500000_100000_5\record.txt' %p1
nfileList3 = [nfile31,nfile32,nfile33,nfile34,nfile35]
ndata3 = getxy2(nfileList3)
ndx31 = ndata3.iloc[66659,6]
ndy31 = ndata3.iloc[66659,5]

nfile42 = r'%s\500000_150000_2\record.txt' %p1
nfile43 = r'%s\500000_150000_3\record.txt' %p1
# file44 = r'%s\500000_150000_4\record.txt' %path1
nfile45 = r'%s\500000_150000_5\record.txt' %p1
nfileList4 = [nfile42,nfile43,nfile45]
ndata4 = getxy2(nfileList4)
ndx41 = ndata4.iloc[66659,4]
ndy41 = ndata4.iloc[66659,3]

ud = getxy2([uf])
ux_1 = ud.iloc[66659,2]
uy_1 = ud.iloc[66659,1]

# f = plt.figure(figsize=(14,5))
ax3 = f.add_subplot(223)
sns.lineplot(ndata1['st'],ndata1['avg'],ax=ax3)
sns.lineplot(ndata2['st'],ndata2['avg'],ax=ax3)
sns.lineplot(ndata3['st'],ndata3['avg'],ax=ax3)
sns.lineplot(ndata4['st'],ndata4['avg'],ax=ax3)
sns.lineplot(md['st'],md['avg'],ax=ax3)
sns.lineplot(ud['st'],ud['avg'],ax=ax3)

plt.scatter([ndx11,ndx21,ndx31,ndx41,mx_1,ux_1],[ndy11,ndy21,ndy31,ndy41,my_1,uy_1],s=10,color = 'b')
plt.plot([ndx11,ndx11],[ndy11,0],'r--',lw=2,alpha=0.7)
ax3.set_xlabel('sample times')
ax3.set_ylabel('sampling size')
# ax1.set_title('adpUNI')
ax3.set_xscale('log')
# ax1.set_ylim([0.0,0.03])
plt.text(0.1,0.94,'(c)',ha='center',va='center',transform=ax3.transAxes)

af11 = r'%s\500000_10000_1\record.txt' %p2
af12 = r'%s\500000_10000_2\record.txt' %p2
af13 = r'%s\500000_10000_3\record.txt' %p2
af14 = r'%s\500000_10000_4\record.txt' %p2
af15 = r'%s\500000_10000_5\record.txt' %p2
af1 = getxy2([af11,af12,af13,af14,af15])
afx11 = af1.iloc[66659,6]
afy11 = af1.iloc[66659,5]

af21 = r'%s\500000_50000_1\record.txt' %p2
af22 = r'%s\500000_50000_2\record.txt' %p2
af23 = r'%s\500000_50000_3\record.txt' %p2
af24 = r'%s\500000_50000_4\record.txt' %p2
af25 = r'%s\500000_50000_5\record.txt' %p2
af2 = getxy2([af21,af22,af23,af24,af25])
afx21 = af2.iloc[66659,6]
afy21 = af2.iloc[66659,5]

af31 = r'%s\500000_100000_1\record.txt' %p2
af32 = r'%s\500000_100000_2\record.txt' %p2
af33 = r'%s\500000_100000_3\record.txt' %p2
af34 = r'%s\500000_100000_4\record.txt' %p2
af35 = r'%s\500000_100000_5\record.txt' %p2
af3 = getxy2([af31,af32,af33,af34,af35])
afx31 = af3.iloc[66659,6]
afy31 = af3.iloc[66659,5]

af41 = r'%s\500000_150000_1\record.txt' %p2
af42 = r'%s\500000_150000_2\record.txt' %p2
af43 = r'%s\500000_150000_3\record.txt' %p2
af44 = r'%s\500000_150000_4\record.txt' %p2
af45 = r'%s\500000_150000_5\record.txt' %p2
af4 = getxy2([af41,af42,af43,af44,af45])
afx41 = af4.iloc[66659,6]
afy41 = af4.iloc[66659,5]

ax4 = f.add_subplot(224)
sns.lineplot(af1['st'],af1['avg'],ax=ax4,label=r'$I=1x10^4$')
sns.lineplot(af2['st'],af2['avg'],ax=ax4,label=r'$I=5x10^4$')
sns.lineplot(af3['st'],af3['avg'],ax=ax4,label=r'$I=1x10^5$')
sns.lineplot(af4['st'],af4['avg'],ax=ax4,label=r'$I=1.5x10^5$')
sns.lineplot(md['st'],md['avg'],ax=ax4,label='MHRW')
sns.lineplot(ud['st'],ud['avg'],ax=ax4,label='UNI')

plt.scatter([afx11,afx21,afx31,afx41,mx_1,ux_1],[afy11,afy21,afy31,afy41,my_1,uy_1],s=10,color = 'b')
plt.plot([afx11,afx11],[afy11,0],'r--',lw=2,alpha=0.7)

ax4.set_xlabel('sample times')
ax4.set_ylabel('')
# ax2.set_title('adpUNI+N')
ax4.set_xscale('log')
# ax2.set_ylim([0.0,0.175])
plt.legend(loc='best')
plt.text(0.1,0.94,'(d)',ha='center',va='center',transform=ax4.transAxes)
plt.legend(loc='center left')
plt.savefig(r'H:\testData\UNI32_2\result3\efficiency.pdf',dpi = 300)
plt.show()