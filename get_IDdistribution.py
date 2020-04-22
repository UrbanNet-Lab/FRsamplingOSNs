#the code is to get the distribution of valid user IDs for Sina weibo
import math
import numpy as np
import os

def statistic(file):
    Dict = {}
    with open(file,'r') as f:
        for row in f.readlines():
            row = int(row.strip('\n'))
            if row >= 0 and row <= 2**34:
                index = row // 10**5
                if index not in Dict.keys():
                    Dict[index] = 1
                else:
                    Dict[index] += 1
    return Dict

def statistic2(file):
    Dict = {}
    with open(file,'r') as f:
        for line in f.readlines():
            x = 0
            line = line.strip('\n')
            if int(line)>0:
                x = int(math.log(int(line),2))
            key = 2**x
            if key not in Dict.keys():
                Dict[key] = 1
            else:
                Dict[key] += 1
    return Dict

nodeFile = '/hdb/students/cgr/nodes_47.txt'
intervalLength = 10**5
aDict = statistic(nodeFile)
destFile = '/hdb/students/cgr/entireNetwork/ID_Dis3.txt'

i = 0
with open(destFile,'w') as f:
    while i <= 2**34//intervalLength:
      value = 0
      if i in aDict.keys():
          value = aDict[i]
      f.write('%d,%d\n' %(i,value))
      i += 1