from dbClass import *
import shutil
import os
import random

class G:
    # targetSteps = int(input("the target number:"))
    recordRate =  int(input("the record rate:"))
    testNum = int(input("the test number:"))
    step = 1
    targetStep = 0

    targetNode = []
    restNodeSet = set()
    db = Db()

    nodeSet = set() #存储原始网络的所有节点

    # 建立数据目录
    filePath = '/hdb/students/cgr/UNI_2_data/twitter/addNeighbours/%d' %testNum
    nodeDir = '%s/targetNode' %filePath
    recordFile = '%s/record.txt' %filePath

def getNode():
    nodeFile = '/home/students/twitter_rv/nodes.txt'
    with open(nodeFile,'r') as f:
        for row in f.readlines():
            row = row.strip('\n')
            G.nodeSet.add(int(row))

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

def mkdir():
    folder1 = os.path.exists(G.nodeDir)
    if not folder1:
        os.makedirs(G.nodeDir)

def record1():
    if G.targetStep == G.recordRate:
        with open('%s/%d.txt' % (G.nodeDir, G.targetStep), 'w') as f:
            for ele in G.targetNode:
                f.write('%d\n' % ele)
    elif G.targetStep != 0 and G.targetStep % G.recordRate == 0:
        pstep = G.targetStep - G.recordRate
        f1 = open('%s/%d.txt' % (G.nodeDir, pstep), 'r')
        f2 = open('%s/%d.txt' % (G.nodeDir,G.targetStep), 'a+')
        shutil.copyfileobj(f1, f2)
        f1.close()
        i = pstep
        while i < G.targetStep:
            f2.write("%d\n" % G.targetNode[i])
            i += 1
        f2.close()
def record2():
    if G.step%1000 == 0:
        with open(G.recordFile,'a+') as f:
            f.write('%d\t%d\t%.5f\n' %(G.step,G.targetStep,G.targetStep/G.step))

def id_do(aId):
    nodeFlag = False
    if aId in G.nodeSet:
        print("%d,%d target!" % (G.step, aId))
        G.targetStep += 1
        G.targetNode.append(aId)
        record1()
        nodeFlag = True
    else:
        G.restNodeSet.add(aId)
        print("%d,%d no target!" % (G.step, aId))
    record2()
    G.step += 1
    return nodeFlag

mkdir()
getNode()
while G.targetStep <= 5000000:
    Id = random.randint(0,2**32-1)
    while find(G.targetNode,Id) or Id in G.restNodeSet:
        Id = random.randint(0,2**32-1)
    if id_do(Id):
        neiList = G.db.getNeighbours(Id)
        for ele in neiList:
            if not find(G.targetNode,ele):
                id_do(ele)
with open(G.recordFile,'a+') as f:
    f.write('%d\t%d\t%.5f' %(G.step-1,G.targetStep,G.targetStep/(G.step-1)))
G.db.closeConn()