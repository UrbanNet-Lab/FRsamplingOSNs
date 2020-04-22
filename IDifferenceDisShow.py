#the code is to get the figure of distribution of difference between the targeted node and its neighbors 
#of adpUNI+N and UNI+N for Sina weibo 
import seaborn as sns
import pandas as pd
from pylab import mpl
import matplotlib.pyplot as plt
mpl.rcParams['font.serif'] = ['Times']
mpl.rcParams['font.size'] = 12.0


# font2 = {'family' : 'Times New Roman',
# 'weight' : 'normal',
# 'size'   : 16,
# }

data1 = pd.read_csv(r"H:\testData\UNI32_2\addNeighbors\500000_150000_1\IDifference.txt",header=None)
data2 = pd.read_csv(r"H:\testData\UNI_2\addNeighbors\IDifferenceDis.txt",header=None)
fig = plt.figure(figsize=(12,5))
ax1 = fig.add_subplot(121)
sns.distplot(data1[0])
plt.title('adpUNI+N')
plt.ylabel('P(difference)')
plt.xlabel('difference')


ax2 = fig.add_subplot(122)
sns.distplot(data2[0])
plt.title('UNI+N')
# plt.ylabel('P(difference)',font2)
plt.xlabel('difference')
plt.savefig(r'H:\testData\UNI32_2\result3\IDifferenceDis.png')
plt.show()