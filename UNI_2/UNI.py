#UNI对twitter数据集的采样
from dbClass import *
import random
import shutil
import os
import time

class G:
    conn = connect(host='127.0.0.1', port=3306, db='crawled_weibo_smaller', user='students',
               passwd='MySQL@DellR740XD', charset='utf8')
    # conn = connect(host='127.0.0.1', port=3306, db='twitter', user='students',
    #            passwd='MySQL@DellR740XD', charset='utf8')
    myCursor = conn.cursor()
    targetSteps = int(input("the target number:"))
    recordRate =  int(input("the record rate:"))
    testNum = input("the test num:")

    destPath = '/hdb/students/cgr/UNI_2_data'
    tarNodeDir = '%s/targetNode' %destPath
    recordFile = '%s/record.txt' %(destPath)

    nodeSet = set() #存储原始网络的所有节点
    # edgeDict = {} #存储原始网络的所有边
    # db = Db()
    tarNodeList = [] #存储命中的节点
    restNodeSet = set() #存储没有命中的节点

    tarStep = 0
    samStep = 1
    

def mkdir():
    if not os.path.exists(G.tarNodeDir):
        os.makedirs(G.tarNodeDir)

def recordNode():
    if G.tarStep == G.recordRate:
        with open('%s/%d.txt' %(G.tarNodeDir,G.tarStep),'w') as f:
            for ele in G.tarNodeList:
                f.write('%d\n' %ele)
    elif G.tarStep != 0 and G.tarStep % G.recordRate == 0:
        pstep = G.tarStep - G.recordRate
        f1 = open('%s/%d.txt' % (G.tarNodeDir, pstep), 'r')
        f2 = open('%s/%d.txt' %(G.tarNodeDir,G.tarStep), 'a+')
        shutil.copyfileobj(f1, f2)
        f1.close()
        i = pstep
        while i < G.tarStep:
            f2.write("%d\n" %G.tarNodeList[i])
            i += 1
        f2.close()

def recordOTR():
    if G.samStep%1000 == 0:
        with open(G.recordFile,'a+') as f:
            f.write('%d\t%d\t%.5f\n' %(G.samStep,G.tarStep,G.tarStep/G.samStep))

def getNeighbours(id):
    sql1 = "select tuid from edges where suid=%d" %id
    sql2 = "select suid from edges where tuid=%d" %id
    neiSet = set()
    try:
        G.myCursor.execute(sql1)
        result1 = G.myCursor.fetchall()
        for data in result1:
            neiSet.add(data[0])
        G.myCursor.execute(sql2)
        result2 = G.myCursor.fetchall()
        for data in result2:
            neiSet.add(data[0])
        return neiSet
    except Exception as e:
        print(e)

def sample(aId):
    nodeFlag = False
    if aId in G.nodeSet:
        print("%d,%d target!" %(G.samStep,aId))
        G.tarStep += 1
        G.tarNodeList.append(aId)
        nodeFlag = True
        getNeighbours(aId)
        recordNode()
    else:
        print("%d,%d no target!" %(G.samStep,aId))
        G.restNodeSet.add(aId)
    recordOTR()
    G.samStep += 1
    return nodeFlag

def find(arr,tar):
    n = len(arr)
    if n < 1:
        return False
    mid = n//2
    if arr[mid] == tar:
        return True
    elif arr[mid] > tar:
        return find(arr[0:mid],tar)
    else:
        return find(arr[mid+1:],tar)

def getNode():
    nodeFile = '/hdb/students/cgr/nodes.txt'
    with open(nodeFile,'r') as f:
        for row in f.readlines():
            row = row.strip('\n').split(',')
            G.nodeSet.add(int(row[0]))


mkdir()
getNode()
while True:
    Id = random.randint(0,(2**32)-1)
    if find(G.tarNodeList,Id) or Id in G.restNodeSet:
        Id = random.randint(0,(2**32)-1)
    if sample(Id):
        if G.tarStep % 1000000 == 0:
            if input('Stop or Continue:') == 'S':
                flag = true
   

with open(G.recordFile,'a+') as f:
    f.write('%d\t%d\t%.5f\n' %(G.samStep-1,G.tarStep,G.tarStep/(G.samStep-1)))
G.myCursor.close()
G.conn.close()
