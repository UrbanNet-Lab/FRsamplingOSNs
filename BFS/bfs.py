from pymysql import *
import os

conn = connect(host='127.0.0.1', port=3306, db='twitter', user='students',
                   passwd='MySQL@DellR740XD', charset='utf8')
myCursor = conn.cursor()

def getNeighbours(id):
    
    sql1 = "select tuid from edges where suid=%d" %id
    sql2 = "select suid from edges where tuid=%d" %id
    neiList = set()
    try:
        myCursor.execute(sql1)
        result1 = myCursor.fetchall()
        for data in result1:
            neiList.add(data[0])
        myCursor.execute(sql2)
        result2 = myCursor.fetchall()
        for data in result2:
            neiList.add(data[0])
        return neiList
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

dirName = "BFS_%s" %seed
filePath = "/hdb/students/cgr/BFS_3/twitter/%s" %dirName
nodeDir = "%s/targetNode" %filePath
# edgeDir = "%s/edges" %filePath
mkdir([nodeDir])
nodeQueue = []
targetNode = set()
step = 0
nodeQueue.append(seed)
while step<=5000000 and nodeQueue:
    Id = nodeQueue.pop(0)
    while Id in targetNode:
        Id = nodeQueue.pop(0)
    targetNode.add(Id)
    step += 1
    print('%d,%d' %(step,Id))
    if step!=0 and step%10000==0:
        with open('%s/%d.txt' %(nodeDir,step),'w') as f:
            for ele in targetNode:
                f.write('%d\n' %ele) 
    neighbors = getNeighbours(Id)
    if neighbors:
        for ele in neighbors:
            nodeQueue.append(ele)
if step <= 5000000:
    print('the seed is not suitable!')
myCursor.close()
conn.close()