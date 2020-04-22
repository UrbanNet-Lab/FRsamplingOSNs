#the code is to get the figure of degree,clustering coefficient and k-core distribution of all sampling methods for twitter
import matplotlib.pyplot as plt
from pylab import mpl
import sys
import pandas as pd
import numpy as np
import seaborn as sns
mpl.rcParams['font.serif'] = ['Times']
mpl.rcParams['font.size'] = 12.0

def get_cc(file):
	data = {}
	with open(file,'r') as f:
		for row in f.readlines():
			row = row.strip('\n').split(',')
			if row[0]!='2.00':
				data[float(row[0])] = int(row[1])
	X  = [i for i in sorted(data.keys())]
	Y = [data[i] for i in X]
	if 'original' in file or 'uni' in file:
		sumY = 0
		for i in range(len(Y)):
			sumY += Y[i]
		z = []
		for i in range(len(X)):
			temp = 0
			for j in range(i+1):
				temp += Y[j]
			z.append(temp/sumY)
		return X,z
	return X,Y

def get_avgcc(files):
	cDict = {}
	for file in files:
		 induced_cluster,ratio = get_cc(file)
		 for c,r in zip(induced_cluster,ratio):
		 	cDict.setdefault(c,[]).append(r)
	avginduced_cluster = {}
	for ele in cDict.keys():
		avginduced_cluster[ele] = sum(cDict[ele])/len(cDict[ele])

	x = sorted(avginduced_cluster.keys())
	y = [avginduced_cluster[i] for i in x]
	z = []
	for i in range(len(x)):
		temp = 0
		for j in range(i+1):
			temp += y[j]
		z.append(temp/sum(y))
	return x,z

def get_core(file):
	aDict = {}
	with open(file,'r') as f:
		for row in f.readlines():
			row = row.strip('\n').split(',')
			if int(row[0])!=0:
				aDict[int(row[0])] = int(row[1])
	x = [i for i in sorted(aDict.keys())]
	y = [aDict[i] for i in x]
	if 'original' in file or 'uni' in file:
		sumy = 0
		for i in range(len(y)):
			sumy += y[i]
		z = []
		for i in range(len(x)):
			asum = 0
			for j in range(i):
				asum += y[j]
			z.append(1-asum/sumy)
		return x,z
	# x = [i/max(x) for i in x]
	return x,y
	# return x,y

def get_avgcore(files):
	cDict = {}
	for file in files:
		 core,ratio = get_core(file)
		 for c,r in zip(core,ratio):
		 	cDict.setdefault(c,[]).append(r)
	avgCore = {}
	for ele in cDict.keys():
		avgCore[ele] = sum(cDict[ele])/len(cDict[ele])

	x = [i for i in sorted(avgCore.keys())]
	y = [avgCore[i] for i in x]
	sumy = 0
	for i in range(len(y)):
		sumy += y[i]
	z = []
	for i in range(len(x)):
	 	asum = 0
	 	for j in range(i):
	 		asum += y[j]
	 	z.append(1-asum/sumy) 
	return x,z


def get_deg(file):
	aDict = {}
	with open(file,'r') as f:
		for row in f.readlines():
			row = row.strip('\n').split('\t')
			if int(row[0])!=0:
				aDict[int(row[0])] = int(row[1])
	x = [i for i in sorted(aDict.keys())]
	y = [aDict[i] for i in x]
	if 'original' in file or 'uni' in file:
		sumy = 0
		for i in range(len(y)):
			sumy += y[i]
		z = []
		for i in range(len(x)):
			asum = 0
			for j in range(i):
				asum += y[j]
			z.append(1-asum/sumy)
		return x,z
	# x = [i/max(x) for i in x]
	return x,y
	# return x,y


def get_avgdegree(files):
	degreeDict = {}
	for file in files:
		 degree,ratio = get_deg(file)
		 for d,r in zip(degree,ratio):
		 	degreeDict.setdefault(d,[]).append(r)
	avgDeg = {}
	for ele in degreeDict.keys():
		avgDeg[ele] = sum(degreeDict[ele])/len(degreeDict[ele])

	x = sorted(avgDeg.keys())
	y = [avgDeg[i] for i in x]
	sumy = 0
	for i in range(len(y)):
		sumy += y[i]
	z = []
	for i in range(len(x)):
	 	asum = 0
	 	for j in range(i):
	 		asum += y[j]
	 	z.append(1-asum/sumy) 
	return x,z


#节点在原网中的度分布比较
path = r'H:\testData\twitter'

#原网
oxd,oyd = get_deg(r'%s\original\alldegree.txt' %path)
# oxk,oyk = get_core(r'%s\original\induced_core.txt' %path)
# oxc,oyc = get_cc(r'%s\original\induced_cluster.txt' %path)

#uni
uxd,uyd = get_deg(r'%s\uni\noNeighbours\1000000\alldegree.txt' %path)
# uxk,uyk = get_core(r'%s\uni\noNeighbours\1000000\induced_core.txt' %path)
# uxc,uyc = get_cc(r'%s\uni\noNeighbours\1000000\induced_cluster.txt' %path)

#uni+n
# auxd,auyd = get_deg(r'%s\UNI_2\addNeighbors\sampleNet\alldegree.txt' %path)
# auxk,auyk = get_core(r'%s\UNI_2\addNeighbors\sampleNet\induced_core.txt' %path)
# auxc,auyc = get_cc(r'%s\UNI_2\addNeighbors\sampleNet\induced_cluster.txt' %path)

#RN
rdFile1 = r'%s\rn\1\1000000\alldegree.txt' %path
rdFile2 = r'%s\rn\2\1000000\alldegree.txt' %path
rdFile3 = r'%s\rn\3\1000000\alldegree.txt' %path
rxd,ryd = get_avgdegree([rdFile1,rdFile2,rdFile3])
# rxd,ryd = get_deg(rdFile1)

# rkFile1 = r'%s\rn\1\1000000\induced_core.txt' %path
# rkFile2 = r'%s\rn\2\1000000\induced_core.txt' %path
# rkFile3 = r'%s\rn\3\1000000\induced_core.txt' %path
# rxk,ryk = get_avgcore([rkFile1,rkFile2,rkFile3])
# rxk,ryk = get_core(rkFile1)

# rcFile1 = r'%s\rn\1\1000000\induced_cluster.txt' %path
# rcFile2 = r'%s\rn\2\1000000\induced_cluster.txt' %path
# rcFile3 = r'%s\rn\3\1000000\induced_cluster.txt' %path
# rxc,ryc = get_avgcc([rcFile1,rcFile2,rcFile3])
# rxc,ryc = get_cc(rcFile1)

#adpUNI
aPath = r'%s\adp\noNeighbours' %path
adFile11 = r'%s\10000\1\alldegree.txt' %aPath
adFile12 = r'%s\10000\2\alldegree.txt' %aPath
adFile13 = r'%s\10000\3\alldegree.txt' %aPath
axd1,ayd1 = get_avgdegree([adFile11,adFile12,adFile13])
# axd1,ayd1 = get_deg(adFile11)

# akFile11 = r'%s\10000\1\induced_core.txt' %aPath
# akFile12 = r'%s\10000\2\induced_core.txt' %aPath
# akFile13 = r'%s\10000\3\induced_core.txt' %aPath
# axk1,ayk1 = get_avgcore([akFile11,akFile12,akFile13])
# axk1,ayk1 = get_core(akFile11)

# acFile11 = r'%s\10000\1\induced_cluster.txt' %aPath
# acFile12 = r'%s\10000\2\induced_cluster.txt' %aPath
# acFile13 = r'%s\10000\3\induced_cluster.txt' %aPath
# axc1,ayc1 = get_avgcc([acFile11,acFile12,acFile13])
# axc1,ayc1 = get_cc(acFile11)


# adpUNI+N
aPath2 = r'%s\adp\addNeighbours' %path
adFile21 = r'%s\10000\1\alldegree.txt' %aPath2
adFile22 = r'%s\10000\2\alldegree.txt' %aPath2
adFile23 = r'%s\10000\3\alldegree.txt' %aPath2
axd2,ayd2 = get_avgdegree([adFile21,adFile22,adFile23])
# axd2,ayd2 = get_deg(adFile21)

# akFile21 = r'%s\10000\1\induced_core.txt' %aPath2
# akFile22 = r'%s\10000\2\induced_core.txt' %aPath2
# akFile23 = r'%s\10000\3\induced_core.txt' %aPath2
# axk2,ayk2 = get_avgcore([akFile21,akFile22,akFile23])
# axk2,ayk2 = get_core(akFile21)

# acFile21 = r'%s\10000\1\induced_cluster.txt' %aPath2
# acFile22 = r'%s\10000\2\induced_cluster.txt' %aPath2
# acFile23 = r'%s\10000\3\induced_cluster.txt' %aPath2
# axc2,ayc2 = get_avgcc([acFile21,acFile22,acFile23])
# axc2,ayc2 = get_cc(acFile21)

#mhrw
mPath = r'%s\mhrw' %path
mFile1 = r'%s\MHRW_21277270\alldegree.txt' %mPath
mFile2 = r'%s\MHRW_44511742\alldegree.txt' %mPath
# mFile2 = r'%s\MHRW_2700698\500000\induced_core.txt' %mPath
# mFile3 = r'%s\MHRW_2700698\500000\induced_cluster.txt' %mPath
mxd,myd = get_avgdegree([mFile1,mFile2])
# mxk,myk = get_core(mFile2)
# mxc,myc = get_cc(mFile3)

# #rw
rPath = r'%s\rw' %path
wdFile1 = r'%s\rw_21277270\1000000\alldegree.txt' %rPath
wdFile2 = r'%s\rw_44511742\1000000\alldegree.txt' %rPath
wxd,wyd = get_avgdegree([wdFile1,wdFile2])
# wxd,wyd = get_deg(wdFile1)

# wkFile1 = r'%s\rw_21277270\1000000\induced_core.txt' %rPath
# wkFile2 = r'%s\rw_44511742\1000000\induced_core.txt' %rPath
# wxk,wyk = get_avgcore([wkFile1,wkFile2])
# # wxk,wyk = get_core(wkFile1)

# wcFile1 = r'%s\rw_21277270\1000000\induced_cluster.txt' %rPath
# wcFile2 = r'%s\rw_44511742\1000000\induced_cluster.txt' %rPath
# wxc,wyc = get_avgcc([wcFile1,wcFile2])
# wxc,wyc = get_cc(wcFile1)

#bfs
bPath = r'%s\bfs' %path
bdFile1 = r'%s\bfs_21277270\1000000\alldegree.txt' %bPath
bdFile2 = r'%s\bfs_44511742\1000000\alldegree.txt' %bPath
bxd,byd = get_avgdegree([bdFile1,bdFile2])
# bxd,byd = get_deg(bdFile1)

# bkFile1 = r'%s\bfs_21277270\1000000\induced_core.txt' %bPath
# bkFile2 = r'%s\bfs_44511742\1000000\induced_core.txt' %bPath
# bxk,byk = get_avgcore([bkFile1,bkFile2])
# # bxk,byk = get_core(bkFile1)

# bcFile1 = r'%s\bfs_21277270\1000000\induced_cluster.txt' %bPath
# bcFile2 = r'%s\bfs_44511742\1000000\induced_cluster.txt' %bPath
# bxc,byc = get_avgcc([bcFile1,bcFile2])
# bxc,byc = get_cc(bcFile1)

f = plt.figure(figsize=(7,5))
ax1 = f.add_subplot(1,1,1)
sns.lineplot(oxd,oyd,linewidth=2.0,ax=ax1,alpha=1.0,label = 'original')
# plt.plot(oxd,oyd,marker='.',lw=1.0,color = sns.xkcd_rgb['mid blue'],alpha=1)
sns.lineplot(uxd,uyd,linewidth=2.0,ax=ax1,alpha=0.5,label = 'UNI')
# # plt.plot(uxd,uyd,marker='.',lw=1.0,color = sns.xkcd_rgb['pumpkin orange'],linestyle='--',alpha=0.6)
sns.lineplot(rxd,ryd,linewidth=2.0,ax=ax1,alpha=0.5, label = 'RN')
# # plt.plot(rxd,ryd,marker='.',lw=1.0,color = sns.xkcd_rgb['off green'],linestyle='--',alpha=0.6)
sns.lineplot(axd1,ayd1,linewidth=2.0,ax=ax1,alpha=1.0, label = 'adpUNI')
# # plt.plot(axd1,ayd1,marker='.',lw=1.0,color = sns.xkcd_rgb['tomato red'],alpha=1)
sns.lineplot(axd2,ayd2,linewidth=2.0,ax=ax1,alpha=1.0, label = 'adpUNI+N')
# plt.plot(axd2,ayd2,marker='.',lw=1.0,color = sns.xkcd_rgb['lighter purple'],alpha=1)
# sns.lineplot(auxd,auyd,linewidth=2.0,ax=ax1,alpha=0.8)
sns.lineplot(mxd,myd,linewidth=2.0,ax=ax1,alpha=0.5,label='MHRW')
sns.lineplot(wxd,wyd,linewidth=2.0,ax=ax1,alpha=0.5, label = 'RW')
# plt.plot(wxd,wyd,marker='.',lw=1.0,color = sns.xkcd_rgb['medium brown'],linestyle='--',alpha=0.6)
sns.lineplot(bxd,byd,linewidth=2.0,ax=ax1,alpha=0.5, label = 'BFS')
# plt.plot(bxd,byd,marker='.',lw=1.0,color = sns.xkcd_rgb['plum'],linestyle='--',alpha=0.6)
# sns.scatterplot(bxd,byd)
ax1.set_xlabel('degree')
ax1.set_ylabel('P(X>=x)')
ax1.set_yscale('log')
ax1.set_xscale('log')
ax1.set_title('twitter')
plt.text(0.9,0.9,'(b)',ha='center',va='center',transform=ax1.transAxes)

# ax2 = f.add_subplot(1,3,2)
# sns.lineplot(oxk,oyk,linewidth=2.0,ax=ax2,alpha=1.0)
# sns.lineplot(uxk,uyk,linewidth=2.0,ax=ax2,alpha=0.5)
# sns.lineplot(rxk,ryk,linewidth=2.0,ax=ax2,alpha=0.5)
# sns.lineplot(axk1,ayk1,linewidth=2.0,ax=ax2,alpha=1.0)
# sns.lineplot(axk2,ayk2,linewidth=2.0,ax=ax2,alpha=1.0)
# # sns.lineplot(auxk,auyk,linewidth=2.0,ax=ax2,alpha=0.8)
# # sns.lineplot(mxk,myk,linewidth=2.0,ax=ax2,alpha=0.7)
# sns.lineplot(wxk,wyk,linewidth=2.0,ax=ax2,alpha=0.5)
# sns.lineplot(bxk,byk,linewidth=2.0,ax=ax2,alpha=0.5)
# ax2.set_xlabel('k-core')
# ax2.set_ylabel('P(X>=x)')
# # ax2.set_yscale('log')
# ax2.set_xscale('log')
# plt.text(0.9,0.9,'(b)',ha='center',va='center',transform=ax2.transAxes)

# ax3 = f.add_subplot(1,3,3)
# sns.lineplot(oxc,oyc,ax=ax3,linewidth=2.0,alpha=1.0,label='original')
# sns.lineplot(uxc,uyc,ax=ax3,linewidth=2.0,alpha=0.5,label='UNI')
# sns.lineplot(rxc,ryc,ax=ax3,linewidth=2.0,alpha=0.5,label='RN')
# sns.lineplot(axc1,ayc1,ax=ax3,linewidth=2.0,alpha=1.0,label='adpUNI')
# sns.lineplot(axc2,ayc2,ax=ax3,linewidth=2.0,alpha=1.0,label='adpUNI+N')
# # sns.lineplot(auxc,auyc,linewidth=2.0,ax=ax3,alpha=0.8,label='UNI+N')
# # sns.lineplot(mxc,myc,ax=ax3,linewidth=2.0,alpha=0.7,label='MHRW')
# sns.lineplot(wxc,wyc,ax=ax3,linewidth=2.0,alpha=0.5,label='RW')
# sns.lineplot(bxc,byc,ax=ax3,linewidth=2.0,alpha=0.5,label='BFS')
# ax3.set_xlabel('cc')
# ax3.set_ylabel('P(X<=x)')
# # ax3.set_yscale('log')
# # # plt.legend(bbox_to_anchor=(1.05,0.5),loc=6,borderaxespad=0)
# plt.legend(loc='best')
# plt.text(0.1,0.9,'(c)',ha='center',va='center',transform=ax3.transAxes)

plt.savefig(r'H:\testData\twitter\result\twi_unbias.pdf',dpi = 300)
plt.show()
