from pymysql import *
import os
import random
import shutil
import time

# conn = connect(host='127.0.0.1', port=3306, db='twitter', user='students',
#                passwd='MySQL@DellR740XD', charset='utf8')
conn = connect(host='127.0.0.1', port=3306, db='crawled_weibo_smaller', user='students',
               passwd='MySQL@DellR740XD', charset='utf8')
myCursor = conn.cursor()

# def getEdges():
#     sql = "select * from edges"
#     edgeDict = {}
#     try:
#         myCursor.execute(sql)
#         result = myCursor.fetchall()
#         for row in result:
#             u,v = row
#             if u not in edgeDict.keys():
#                 edgeDict[u] = []
#             if v not in edgeDict[u]:
#                 edgeDict[u].append(v)
#             if v not in edgeDict.keys():
#                 edgeDict[v] = []
#             if u not in edgeDict[v]:
#                 edgeDict[v].append(u)
#             myCursor.close()
#         return edgeDict
#     except Exception as e:
#         print(e)

def getNeighbours(id):
    sql1 = "select tuid from edges where suid=%d" %id
    sql2 = "select suid from edges where tuid=%d" %id
    neiSet = set()
    try:
        myCursor.execute(sql1)
        result1 = myCursor.fetchall()
        for data in result1:
            neiSet.add(data[0])
        myCursor.execute(sql2)
        result2 = myCursor.fetchall()
        for data in result2:
            neiSet.add(data[0])
        return list(neiSet)
    except Exception as e:
        print(e)

def mkdir(dirs):
    for ele in dirs:
        folder = os.path.exists(ele)
        if not folder:
            os.makedirs(ele)
    print("folders are made successfully!")

Id = input("please input the first node:")
Id = int(Id)
testNum = input("the test num:")
dirName = "MHRW_%s" %Id
filePath = "/hdb/students/cgr/MHRW_data/weibo/%s" %dirName
repeat_nodeDir = "%s/repeatNode" %filePath
unique_nodeDir = "%s/uniqueNode" %filePath
recordTxt = "%s/record.txt" %(filePath)
# edgeDir = "%s/edges" %filePath
mkdir([repeat_nodeDir,unique_nodeDir])
# edges = getEdges()
#conn.close()
repeatNode = []
uniqueNode = set()
# targetEdge = []
step = 1
print(step,Id)
repeatNode.append(Id)
uniqueNode.add(Id)
# start = time.time()
neighbours = getNeighbours(Id)
while True:
    if neighbours:
        index = random.randint(0,len(neighbours)-1)
        testId = neighbours[index]
        testNeighbours = getNeighbours(testId)
        if len(neighbours)/len(testNeighbours) >= random.random():
            # targetEdge.append([Id,testId])
            Id = testId
            neighbours = testNeighbours
            uniqueNode.add(Id)
            if len(uniqueNode)!=0 and len(uniqueNode)%10000==0:
                with open('%s/%d.txt' %(unique_nodeDir,len(uniqueNode)),'w') as f:
                    for ele in uniqueNode:
                        f.write('%d\n' %ele)
                # with open('%s/%d.txt' %(edgeDir,len(uniqueNode)),'w') as f:
                #     for ele in targetEdge:
                #         f.write('%d\t%d\n' %(ele[0],ele[1]))
                
            if len(uniqueNode)!=0 and len(uniqueNode)%100000==0:
                if input('stop or continue:')=='S':
                    break
        repeatNode.append(Id)
        step += 1
        print(step,Id)
        if step%1000 == 0:
            with open(recordTxt,'a+') as f:
                f.write('%d\t%d\n' %(step,len(uniqueNode)))
        if step!=0 and step%10000 == 0:
            with open('%s/%d.txt' %(repeat_nodeDir,step),'w') as f:
                for ele in repeatNode:
                    f.write('%d\n' %ele)
            repeatNode.clear()

    else:
        print("Neighbour list is empty!")
        exit()
myCursor.close()
conn.close()















