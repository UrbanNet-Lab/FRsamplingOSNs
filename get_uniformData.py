#the code is to get the ratio of targeted IDs to the number of 
#valid user IDs in each interval of UNI,adpUNI and MHRW for Twitter and Sina weibo
import math
import numpy as np
import os

def statistic(file):
    Dict = {}
    with open(file,'r') as f:
        for row in f.readlines():
            row = int(row.strip('\n'))
            index = row // 10**5
            if index not in Dict.keys():
                Dict[index] = 1
            else:
                Dict[index] += 1
    return Dict

def sta_mhrw(path):
    Dict = {}
    for file in os.listdir(path):
        with open(os.path.join(path,file),'r') as f:
            for row in f.readlines():
                row = int(row.strip('\n'))
                index = row // 10**6
                if index not in Dict.keys():
                    Dict[index] = 1
                else:
                    Dict[index] += 1
    return Dict

orig = statistic(r'/home/students/twitter_rv/nodes.txt')  
path2 = r'/hdb/students/cgr/MHRW_data/twitter'
intervalLength = 10**6

md1 = sta_mhrw('%s/MHRW_21277270/repeatNode/' %path2)
md2 = sta_mhrw('%s/MHRW_44511742/repeatNode/' %path2)

dest2 = '%s/mhrwIDsta_100w.txt' %path2
with open(dest2,'w') as f:
    f.write('index\toriginal\tmhrw1\tmhrw2\toriginalRatio\tmhrwRatio1\tmhrwRatio2\n')
    i = 0
    while i <= 2**32//intervalLength:
        m1 = 0
        if i in md1.keys():
            m1 = md1[i]
        m2 = 0
        if i in md2.keys():
            m2 = md2[i]
        oriValue = 0
        if i in orig.keys():
            oriValue = orig[i]
        ratio = oriValue/intervalLength
        ratio5 = 0.0
        ratio6 = 0.0
        if oriValue != 0:
            ratio5 = round(m1 / oriValue,4)
            ratio6 = round(m2 / oriValue,4)
        f.write('%d\t%d\t%d\t%d\t%.4f\t%.4f\t%.4f\n' %(i,oriValue,m1,m2,ratio,ratio5,ratio6))
        print(i)
        i += 1
