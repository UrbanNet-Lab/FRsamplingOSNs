#the code is to get the KS distance of degree,clustering coefficient and k-core distribution of all sampling methods for Twitter.
import numpy as np
from scipy import stats

def getData1(file):
	 data = []
	 with open(file,'r') as f:
	 	for row in f.readlines():
	 		row  = row.strip('\n').split(',')
	 		if row[0] != '2.00':
		 		for i in range(int(row[1])):
		 			data.append(float(row[0]))
	 return data

def getData2(file):
	 data = []
	 with open(file,'r') as f:
	 	for row in f.readlines():
	 		row  = row.strip('\n').split('\t')
	 		if row[0] != '0':
		 		for i in range(int(row[1])):
		 			data.append(int(row[0]))
	 return data

def get_avgKS1(files,data):
	ks_value = []
	for file in files:
		data1 = getData1(file)
		data1 = np.array(data1)
		ks = stats.ks_2samp(data,data1)
		ks_value.append(ks.statistic)
	return sum(ks_value)/len(ks_value)

def get_avgKS2(files,data):
	ks_value = []
	for file in files:
		data1 = getData2(file)
		data1 = np.array(data1)
		ks = stats.ks_2samp(data,data1)
		ks_value.append(ks.statistic)
	return sum(ks_value)/len(ks_value)

path = r'H:\testData\twitter'

deg_data = np.array(getData2(r'%s\original\alldegree.txt' %path))
# core_data = np.array(getData2(r'%s\original\induced_core.txt' %path))
# cc_data = np.array(getData1(r'%s\original\induced_cluster.txt' %path))

#uni
ud = get_avgKS2([r'%s\uni\noNeighbours\1000000\alldegree.txt' %path],deg_data)
# uk = get_avgKS2([r'%s\uni\noNeighbours\1000000\induced_core.txt' %path],core_data)
# uc = get_avgKS1([r'%s\uni\noNeighbours\1000000\induced_cluster.txt' %path],cc_data)
print('uni:')
print('degree:%f' %ud)
# print('degree:%f,core:%f,cc:%f' %(ud,uk,uc))

#RN
rdFile1 = r'%s\rn\1\1000000\alldegree.txt' %path
rdFile2 = r'%s\rn\2\1000000\alldegree.txt' %path
rdFile3 = r'%s\rn\3\1000000\alldegree.txt' %path
nd = get_avgKS2([rdFile1,rdFile2,rdFile3],deg_data)

# rkFile1 = r'%s\rn\1\1000000\induced_core.txt' %path
# rkFile2 = r'%s\rn\2\1000000\induced_core.txt' %path
# rkFile3 = r'%s\rn\3\1000000\induced_core.txt' %path
# nk = get_avgKS2([rkFile1,rkFile2,rkFile3],core_data)

# rcFile1 = r'%s\rn\1\1000000\induced_cluster.txt' %path
# rcFile2 = r'%s\rn\2\1000000\induced_cluster.txt' %path
# rcFile3 = r'%s\rn\3\1000000\induced_cluster.txt' %path
# nc = get_avgKS1([rcFile1,rcFile2,rcFile3],cc_data)
print('rn:')
print('degree:%f' %nd)
# print('degree:%f,core:%f,cc:%f' %(nd,nk,nc))

#adpUNI
aPath = r'%s\adp\noNeighbours' %path
adFile11 = r'%s\10000\1\alldegree1.txt' %aPath
adFile12 = r'%s\10000\2\alldegree1.txt' %aPath
adFile13 = r'%s\10000\3\alldegree1.txt' %aPath
ad1 = get_avgKS2([adFile11,adFile12,adFile13],deg_data)

# akFile11 = r'%s\10000\1\induced_core.txt' %aPath
# akFile12 = r'%s\10000\2\induced_core.txt' %aPath
# akFile13 = r'%s\10000\3\induced_core.txt' %aPath
# ak1 = get_avgKS2([akFile11,akFile12,akFile13],core_data)
# # axk1,ayk1 = get_core(akFile11)

# acFile11 = r'%s\10000\1\induced_cluster.txt' %aPath
# acFile12 = r'%s\10000\2\induced_cluster.txt' %aPath
# acFile13 = r'%s\10000\3\induced_cluster.txt' %aPath
# ac1 = get_avgKS1([acFile11,acFile12,acFile13],cc_data)
# # axc1,ayc1 = get_cc(acFile12)
print('adpuni:')
print('degree:%f' %ad1)
# print('degree:%f,core:%f,cc:%f' %(ad1,ak1,ac1))

# adpUNI+N
aPath2 = r'%s\adp\addNeighbours' %path
adFile21 = r'%s\10000\1\alldegree1.txt' %aPath2
adFile22 = r'%s\10000\2\alldegree1.txt' %aPath2
adFile23 = r'%s\10000\3\alldegree1.txt' %aPath2
ad2 = get_avgKS2([adFile21,adFile22,adFile23],deg_data)

# akFile21 = r'%s\10000\1\induced_core.txt' %aPath2
# akFile22 = r'%s\10000\2\induced_core.txt' %aPath2
# akFile23 = r'%s\10000\3\induced_core.txt' %aPath2
# ak2 = get_avgKS2([akFile21,akFile22,akFile23],core_data)

# acFile21 = r'%s\10000\1\induced_cluster.txt' %aPath2
# acFile22 = r'%s\10000\2\induced_cluster.txt' %aPath2
# acFile23 = r'%s\10000\3\induced_cluster.txt' %aPath2
# ac2 = get_avgKS1([acFile21,acFile22,acFile23],cc_data)
print('adpuni+n:')
print('degree:%f' %ad2)
# print('degree:%f,core:%f,cc:%f' %(ad2,ak2,ac2))

#mhrw
mPath = r'%s\mhrw' %path
mFile1 = r'%s\MHRW_21277270\alldegree.txt' %mPath
mFile2 = r'%s\MHRW_44511742\alldegree.txt' %mPath
md = get_avgKS2([mFile1,mFile2],deg_data)
print('mhrw:')
print('degree:%f' %md)

#rw
rPath = r'%s\rw' %path
wdFile1 = r'%s\rw_21277270\1000000\alldegree.txt' %rPath
wdFile2 = r'%s\rw_44511742\1000000\alldegree.txt' %rPath
wd = get_avgKS2([wdFile1,wdFile2],deg_data)
wxd,wyd = get_deg(wdFile1)

# wkFile1 = r'%s\rw_21277270\1000000\induced_core.txt' %rPath
# wkFile2 = r'%s\rw_44511742\1000000\induced_core.txt' %rPath
# wk = get_avgKS2([wkFile1,wkFile2],core_data)
# # wxk,wyk = get_core(wkFile1)

# wcFile1 = r'%s\rw_21277270\1000000\induced_cluster.txt' %rPath
# wcFile2 = r'%s\rw_44511742\1000000\induced_cluster.txt' %rPath
# wc = get_avgKS1([wcFile1,wcFile2],cc_data)
# print('rw:')
# print('degree:%f' %wd)
# # print('degree:%f,core:%f,cc:%f' %(wd,wk,wc))

# #bfs
bPath = r'%s\bfs' %path
bdFile1 = r'%s\bfs_21277270\1000000\alldegree.txt' %bPath
bdFile2 = r'%s\bfs_44511742\1000000\alldegree.txt' %bPath
bd = get_avgKS2([bdFile1,bdFile2],deg_data)
bxd,byd = get_deg(bdFile1)

# bkFile1 = r'%s\bfs_21277270\1000000\induced_core.txt' %bPath
# bkFile2 = r'%s\bfs_44511742\1000000\induced_core.txt' %bPath
# bk = get_avgKS2([bkFile1,bkFile2],core_data)
# # bxk,byk = get_core(bkFile1)

# bcFile1 = r'%s\bfs_21277270\1000000\induced_cluster.txt' %bPath
# bcFile2 = r'%s\bfs_44511742\1000000\induced_cluster.txt' %bPath
# bc = get_avgKS1([bcFile1,bcFile2],cc_data)
print('bfs:')
print('degree:%f' %bd)
# print('degree:%f,core:%f,cc:%f' %(bd,bk,bc))

