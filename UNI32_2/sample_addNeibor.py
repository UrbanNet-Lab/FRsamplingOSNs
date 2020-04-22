from bufferClass import *
from dbClass import *
from basicClass import *
import shutil
import os
import random
import collections
import time

class G:
    #输入
    tarStp = input("total target steps:")
    inteNum = input("the number of intervals divided:")
    recRate = input("the record rate:")
    testNum = input("the test number:")
    # seedNode = input("the seed node:")
    #采样次数
    targetSteps = int(tarStp)
    #划分的区间数
    intervalNum = int(inteNum)
    #采样概率最低阈值
    alpha = round(1/intervalNum,6)
    recordRate = int(recRate)
    intervalLength = 2**32//intervalNum

    #缓存区声明
    samIDSet = set()
    tarIDLists = IDBuffer()
    intervalLists = Intervals()
    samProList = []
    indexList = []


    #数据目录声明
    dirName = '%s_%s_%s' %(tarStp,inteNum,testNum)
    filePath = '/hdb/students/cgr/UNI32_2_data/%s' %dirName
    nodeDir = '%s/targetNode' %filePath
    intervalDir = '%s/interval' %filePath
    recordTxt = '%s/record.txt' %(filePath)

    db = Db()
    ID_Set = set()

    targetStep = 0
    step = 1

def getNode():
    nodeFile = '/hdb/students/cgr/nodes.txt'
    with open(nodeFile,'r') as f:
        for row in f.readlines():
            row = row.strip('\n')
            G.ID_Set.add(int(row))

def mkdir():
    folder1 = os.path.exists(G.nodeDir)
    if not folder1:
        os.makedirs(G.nodeDir)

    folder2 = os.path.exists(G.intervalDir)
    if not folder2:
        os.makedirs(G.intervalDir)

    print("folders are made successfully!")

def divideInterval():
    i = 0
    L = (2**32-1)//G.intervalLength
    while i<=L:
        aInterval = Interval()
        aInterval.set_index(i)
        aInterval.set_lowBound(i*G.intervalLength)
        aInterval.set_upBound(aInterval.get_lowBound()+G.intervalLength)
        aInterval.set_samPro(G.alpha)
        G.intervalLists.add_inter(aInterval)
        # G.samProDict[i] = G.alpha
        G.samProList.append(G.alpha)
        G.indexList.append(i)
        i += 1

def record1():
    nodePath = '%s/%d.txt' % (G.nodeDir, G.targetStep)
    if G.targetStep == G.recordRate:
        G.tarIDLists.write_ids(nodePath, G.recordRate)
    elif G.targetStep != 0 and G.targetStep % G.recordRate == 0:
        pstep = G.targetStep - G.recordRate
        f1 = open('%s/%d.txt' % (G.nodeDir, pstep), 'r')
        f2 = open(nodePath, 'w')
        shutil.copyfileobj(f1, f2)
        f1.close()
        f2.close()
        G.tarIDLists.write_ids(nodePath, G.recordRate)

def record2():
    if G.step % 1000 == 0:
        with open(G.recordTxt, 'a+') as f:
            TTR = round(G.targetStep / G.step, 5)
            f.write('%d\t%d\t%.5f\n' % (G.step,G.targetStep,TTR))
    if G.step % 10000 == 0:
        G.intervalLists.write_intervals('%s/%d.txt' %(G.intervalDir,G.step))

# def record2(s):
#     if G.step % 1000 == 0:
#         with open(G.recordTxt, 'a+') as f:
#             f.write('%d\t%d\t%f\n' % (G.step,G.targetStep,(time.time()-s)))

def sort_samPro(b,inteIndex):
    aInterval = G.intervalLists.get_interval(inteIndex)
    aIndex = G.indexList.index(inteIndex)
    if b>aInterval.get_samPro():
        i = aIndex-1
        while i>=0 and b>G.samProList[i]:
            G.samProList[i+1] = G.samProList[i]
            G.indexList[i+1] = G.indexList[i]
            i = i-1
        G.samProList[i+1] = b
        G.indexList[i+1] = inteIndex
    else:
        j = aIndex+1
        while j<len(G.samProList) and b<G.samProList[j]:
            G.samProList[j-1] = G.samProList[j]
            G.indexList[j-1] = G.indexList[j]
            j = j+1
        G.samProList[j-1] = b
        G.indexList[j-1] = inteIndex


def id_do(id):
    interIndex = id//G.intervalLength
    aInterval = G.intervalLists.get_interval(interIndex)
    nodeFlag = False
    

    if id in G.ID_Set:
        aInterval.set_tarNum()  #修改命中次数
        G.tarIDLists.add_tarID(id)
        G.targetStep += 1
        nodeFlag = True
        print("%d,%d target!" %(G.step,id))
        # nei = G.db.getNeighbours(id)
        record1()
    else:
        print("%d,%d no target!" %(G.step,id))
    aInterval.set_samNum() #修改采样次数
    if aInterval.get_samNum >= temp//3 and aInterval.get_tarNum()==0:
        aInterval.set_onSample(False)
    b = round(aInterval.get_tarNum()/aInterval.get_samNum()*(1-aInterval.get_samNum()/ temp),6)
    if b<G.alpha:
        b = G.alpha
    if b!=aInterval.get_samPro():
        sort_samPro(b,interIndex)
        aInterval.set_samPro(b)
    record2()
    G.step += 1
    return nodeFlag

mkdir()
getNode()
divideInterval()
while G.targetStep <= G.targetSteps:
    targetIndex = -1
    i = 0
    neighbours = []
    while i<len(G.samProList):
        RP = random.random()
        if RP<=G.samProList[i]:
            targetIndex = G.indexList[i]
            break
        i += 1
    if targetIndex>-1 and targetIndex<len(G.samProList):
        flag = False
        count = 1
        temp = aInterval.get_upBound()-aInterval.get_lowBound()
        id = random.randint(aInterval.get_lowBound(),aInterval.get_upBound()-1)
        while id in G.samIDSet:
            id = random.randint(aInterval.get_lowBound(),aInterval.get_upBound()-1)
            count += 1
            if count == temp:
                flag = True
                break
        if not flag:
            G.samIDSet.add(id)
            if id in G.ID_Set:
                G.tarIDLists.add_tarID(id)
                G.targetStep += 1
                aInterval.set_tarNum()
                print('%d,%d target!' % (G.step, id))
                neighbours = G.db.getNeighbours(id)
                record1()
            else:
                print('%d,%d no target!' % (G.step, id))
            aInterval.set_samNum()
            if aInterval.get_samNum >= temp//3 and aInterval.get_tarNum()==0:
                aInterval.set_onSample(False)
            b = round(aInterval.get_tarNum() / aInterval.get_samNum() * (1 - aInterval.get_samNum() / temp), 6)
            if b < G.alpha:
                b = G.alpha
            if b != aInterval.get_samPro():
                sort_samPro(b,targetIndex)
                aInterval.set_samPro(b)
            record2()
            G.step += 1
            if neighbours:
                for ele in neighbours:
                    if ele not in G.samIDSet:
                        G.samIDSet.add(ele)
                        id_do(ele)
    else:
        id = random.randint(0,2**32-1)
        while id in G.samIDSet:
            id = random.randint(0,2**32-1)
        G.samIDSet.add(id)
        if id_do(id):
            neighbours = G.db.getNeighbours(id)
            for ele in neighbours:
                if ele not in G.samIDSet:
                    G.samIDSet.add(ele)
                    id_do(ele)
G.db.closeConn()
with open(G.recordTxt, 'a+') as f:
    TTR = round(G.targetStep / (G.step-1), 5)
    f.write('%d\t%d\t%.5f\n' % ((G.step-1),G.targetStep,TTR))
G.intervalLists.write_intervals('%s/%d.txt' % (G.intervalDir,  (G.step-1)))
