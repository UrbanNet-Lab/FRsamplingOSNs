#the code is to get the figure of fitting of the complementary cumulative 
#distribution(ccdf) of the original network for Sina weibo and Twitter.
import matplotlib.pyplot as plt
from pylab import mpl
import sys
import pandas as pd
import numpy as np
import seaborn as sns
from scipy import optimize
mpl.rcParams['font.serif'] = ['Times']
mpl.rcParams['font.size'] = 12.0

def get_deg3(file):
	aDict = {}
	with open(file,'r') as f:
		for row in f.readlines():
			row = row.strip('\n').split(',')
			if int(row[0])!=0:
				aDict[int(row[0])] = int(row[1])
	x = [i for i in sorted(aDict.keys())]
	y = [aDict[i] for i in x]
	sumy = 0
	for i in range(len(y)):
		sumy += y[i]
	z = []
	for i in range(len(x)):
		asum = 0
		for j in range(i+1):
			asum += y[j]
		z.append(1-asum/sumy)
	# return x,z
	return x[:len(x)-1],z[:len(z)-1]

def get_deg4(file):
	aDict = {}
	with open(file,'r') as f:
		for row in f.readlines():
			row = row.strip('\n').split('\t')
			if int(row[0])!=0:
				aDict[int(row[0])] = int(row[1])
	x = [i for i in sorted(aDict.keys())]
	y = [aDict[i] for i in x]
	sumy = 0
	for i in range(len(y)):
		sumy += y[i]
	z = []
	for i in range(len(x)):
		asum = 0
		for j in range(i+1):
			asum += y[j]
		z.append(1-asum/sumy)
	# return x,z
	return x[:len(x)-1],z[:len(z)-1]



def func_t(x, a,c,b1,b2):
    return a*pow(x+c,-b1)*np.exp((-b2)*x)
def func(x, a,c,b1):
    return a*pow(x+c,-b1)*np.exp(-0.0001*x)

def func_w(x, a,b1,b2):
    return a*pow(x,-b1)*np.exp((-b2)*x)


path = r'H:\testData'
path2 = r'H:\testData\twitter'

oxd,oyd = get_deg3(r'%s\entireNetwork\induced_degree.txt' %path)
popt1, pcov1 = optimize.curve_fit(func, oxd, oyd, p0=None,maxfev=10000)
print(popt1)

oxdt,oydt = get_deg4(r'%s\original\alldegree.txt' %path2)
todx =  np.log10(np.array(oxdt))
tody = np.log10(np.array(oydt))
tfo = np.polyfit(todx,tody,deg=1)
print("Twitter_orig:",tfo)
tvo = np.polyval(tfo,todx)
tvo = [10**i for i in tvo]


f = plt.figure(figsize=(12,5))
ax1 = f.add_subplot(121)
plt.plot(oxd,oyd,'bo',markersize=1)
plt.plot(oxd,popt1[0]*pow(oxd+popt1[1],-popt1[2])*np.exp(-0.0001*np.array(oxd)))
ax1.set_title('Sina weibo',fontsize=16)
ax1.set_xlabel('degree',fontsize=12)
ax1.set_ylabel('P(X>x)',fontsize=12)
ax1.set_yscale('log')
ax1.set_xscale('log')

ax2 = f.add_subplot(122)
plt.plot(oxdt,oydt,'bo',markersize=1)
plt.plot(oxdt,tvo)
ax2.set_title('Twitter',fontsize=16)
ax2.set_xlabel('degree',fontsize=12)
ax2.set_yscale('log')
ax2.set_xscale('log')
plt.savefig(r'H:\testData\UNI32_2\result3\degDis_fit2.pdf',dpi=300)
plt.show()