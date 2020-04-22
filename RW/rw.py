from pymysql import *
import os
import random

conn = connect(host='127.0.0.1', port=3306, db='twitter', user='students',
                   passwd='MySQL@DellR740XD', charset='utf8')
myCursor = conn.cursor()

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

seed = input("please input the first node:")
seed = int(seed)

dirName = "RW_%s" %seed
filePath = "/hdb/students/cgr/RW_data/twitter/%s" %dirName
# repeat_nodeDir = "%s/repeatNode" %filePath
unique_nodeDir = "%s/uniqueNode" %filePath
recordFile = "%s/record.txt" %filePath
# edgeDir = "%s/edges" %filePath
mkdir([unique_nodeDir])
unNode = set()
# targetEdge = []
step = 1
Id = seed
unNode.add(Id)
print(step,Id)
neighbours = getNeighbours(Id)
while len(unNode) <= 5000000:
    if neighbours:
        index = random.randint(0,len(neighbours)-1)
        nextId = neighbours[index]
        Id = nextId
        # reNode.append(Id)
        unNode.add(Id)
        # targetEdge.append((Id,nextId))
        if len(unNode)!=0 and len(unNode)%10000==0:
            with open('%s/%d.txt' %(unique_nodeDir,len(unNode)),'w') as f:
                for ele in unNode:
                    f.write('%d\n' %ele)
        step += 1
        print(step, Id)
        if step % 1000 == 0:
            with open(recordFile,'a+') as f:
                f.write('%d\t%d\t%.5f\n' %(step,len(unNode),len(unNode)/step))
        neighbours = getNeighbours(Id)
    else:
        print("Neighbour list is empty!")
myCursor.close()
conn.close()















