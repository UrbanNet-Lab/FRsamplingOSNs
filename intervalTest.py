#the code is to get the figure of KS distance of degree,clustering coefficient and k-core distribution
# of adpUNI and adpUNI+N under different interval number with increasing sampling size for Sina weibo and Twitter.
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pylab import mpl
from matplotlib.ticker import LogLocator,MultipleLocator
mpl.rcParams['font.serif'] = ['Times']
mpl.rcParams['font.size'] = 12.0
# sns.set_style(style='whitegrid')

df = pd.DataFrame(pd.read_excel(r'H:\testData\UNI32_2\result3\intervalTest\interval.xlsx',sheet_name='weibo'))
g = sns.FacetGrid(df,hue='interval(I)',col='distribution',row='method',despine=False,height=4,aspect=1,legend_out=False)
g = (g.map(plt.plot,'sample size','KS Distance',marker='.').add_legend())
g.axes[0,0].set_title('degree',)
g.axes[0,1].set_title('cc')
g.axes[0,2].set_title('k-core')
g.axes[1,0].set_title('')
g.axes[1,1].set_title('')
g.axes[1,2].set_title('')
g.axes[0,0].set_ylim([0.0,0.4])
g.axes[1,0].set_ylim([0.0,0.4])
plt.text(0.1,0.95,'(a)',ha='center',va='center',transform=g.axes[0,0].transAxes)
plt.text(0.1,0.95,'(b)',ha='center',va='center',transform=g.axes[0,1].transAxes)
plt.text(0.1,0.95,'(c)',ha='center',va='center',transform=g.axes[0,2].transAxes)
plt.text(0.1,0.95,'(d)',ha='center',va='center',transform=g.axes[1,0].transAxes)
plt.text(0.1,0.95,'(e)',ha='center',va='center',transform=g.axes[1,1].transAxes)
plt.text(0.1,0.95,'(f)',ha='center',va='center',transform=g.axes[1,2].transAxes)
plt.text(0.9,-0.08,r'$(10^5)$',ha='right',va='top',transform=g.axes[1,2].transAxes)
# plt.savefig(r'H:\testData\UNI32_2\result3\intervalTest\interval.pdf',dpi=300)
plt.show()