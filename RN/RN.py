from pymysql import *
import random
import os

conn = connect(host='127.0.0.1',port=3306,db='twitter',user='students',passwd='MySQL@DellR740XD',charset='utf8')
myCursor = conn.cursor()

def getIDs():
    sql = "SELECT uid FROM nodes"
    IDLists = set()
    try:
        myCursor.execute(sql)
        results = myCursor.fetchall()
        for row in results:
            IDLists.add(row[0])
        myCursor.close()
        return IDLists
    except Exception as e:
        print(e)

IDs = getIDs()
conn.close()

needNode = input('the number of targetNode:')
testNum = input('the number of test:')
p = int(needNode)/len(IDs)
nodeDir = '/hdb/students/cgr/RN/twitter/%s/targetNode' %testNum
if not os.path.exists(nodeDir):
    os.makedirs(nodeDir)
target = 0
targetNode = set()
while target<int(needNode):
    for ele in IDs:
        q = random.random()
        if q>=p:
            if ele not in targetNode:
                targetNode.add(ele)
                target += 1
                print(target,ele)
                if target % 100000 == 0:
                    with open('%s/100000.txt' %nodeDir,'w') as f:
                        for ele in targetNode:
                            f.write('%d\n' %ele)
                if target>=int(needNode):
                    break
with open('%s/1000000.txt' %nodeDir,'w') as f:
	for ele in targetNode:
		f.write('%d\n' %ele)

