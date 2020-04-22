#the code is to get the distribution of ID difference of the target node with its neighbors of adpUNI+N and UNI+N for Sina weibo
from pymysql import *
import sys

conn = connect(host='127.0.0.1',port=3306,db='crawled_weibo_smaller',user='students',passwd='MySQL@DellR740XD',charset='utf8')
myCursor = conn.cursor()

def getNeighbors(data):
    sql1 = "select suid from edges where tuid=%d" %data
    sql2 = "select tuid from edges where suid=%d" %data
    neighbors = set()
    try:
        myCursor.execute(sql1)
        result1 = myCursor.fetchall()
        for row in result1:
            neighbors.add(row[0])
        myCursor.execute(sql2)
        result2 = myCursor.fetchall()
        for row in result2:
            neighbors.add(row[0])
        return neighbors
    except Exception as e:
        print(e)
path = input("path:")
nodeFile = '%s/targetNode/500000.txt' %path

nodeSet = set()
with open(nodeFile,'r') as f:
    for row in f.readlines():
        row = row.strip('\n')
        nodeSet.add(int(row))

resultFile = '%s/IDifference.txt' %path
nodeTemp = set()
with open(resultFile,'w') as f:
    for ele in nodeSet:
        nodeTemp.add(ele)
        neiList = getNeighbors(ele)
        for data in neiList:
            if data in nodeSet and data not in nodeTemp:
                dif = ele - data
                if dif < 0:
                    dif = -dif
                f.write('%d\n' %(dif))
myCursor.close()