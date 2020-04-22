from pymysql import *
from basicClass import *

class Db(object):
    def __init__(self):
        self.conn = connect(host='127.0.0.1',port=3306,db='weibo_47b',user='students',passwd='MySQL@DellR740XD',charset='utf8')
        # self.conn = connect(host='127.0.0.1',port=3306,db='twitter',user='students',passwd='MySQL@DellR740XD',charset='utf8')

    def createNodeTable(self,targetStep,intervalNum):
        self.cursor = self.conn.cursor()
        tableName = 'sam_%d_%d'%(targetStep,intervalNum)
        sql1 = "DROP TABLE IF EXISTS %s" %tableName
        sql2 = "CREATE TABLE %s (uid INT UNSIGNED PRIMARY KEY,isTar INT)"%tableName
        try:
            self.cursor.execute(sql1)
            self.cursor.execute(sql2)
            self.conn.commit()
            self.cursor.close()
        except Exception as e:
            print(e)

    def createIntervalTable(self,targetStep,intervalNum):
        self.cursor = self.conn.cursor()
        tableName = 'inter_%d_%d'%(targetStep,intervalNum)
        sql1 = "DROP TABLE IF EXISTS %s"%tableName
        sql2 = "CREATE TABLE %s (inteIndex INT PRIMARY KEY,low INT UNSIGNED,up INT UNSIGNED,targetNum INT,sampleNum INT,samplePro DOUBLE(7,6),INDEX (samplePro))"%tableName
        try:
            self.cursor.execute(sql1)
            self.cursor.execute(sql2)
            self.conn.commit()
            self.cursor.close()
        except Exception as e:
            print(e)

    def insertSampleID(self,aId,f,targetStep,intervalNum):
        self.cursor = self.conn.cursor()
        flag = True
        tableName = 'sam_%d_%d' % (targetStep, intervalNum)
        sql1 = "SELECT * FROM %s WHERE uid=%d" % (tableName, aId)
        sql2 = "INSERT INTO %s (uid,isTar) VALUES (%d,%d)" % (tableName, aId,f)
        try:
            self.cursor.execute(sql1)
            if self.cursor.rowcount == 1:
                flag = False
            else:
                self.cursor.execute(sql2)
                self.conn.commit()
            self.cursor.close()
        except Exception as e:
            print(e)
        return flag

    def testID(self,aId):
        self.cursor = self.conn.cursor()
        sql = "SELECT * FROM all_nodes WHERE uid='%d'" %aId
        flag = False
        try:
            self.cursor.execute(sql)
            self.cursor.fetchall()
            if self.cursor.rowcount==1:
                flag = True
            self.cursor.close()
        except Exception as e:
            print(e)
        return flag

    def insertInterval(self,targetStep,intervalNum,aInterval):
        self.cursor = self.conn.cursor()
        tableName = 'inter_%d_%d' %(targetStep,intervalNum)
        sql = "INSERT INTO %s (inteIndex,low,up,targetNum,sampleNum,samplePro) VALUES ('%d','%d','%d','%d','%d','%f')" %(tableName,aInterval.get_index(),aInterval.get_lowBound(),aInterval.get_upBound(),aInterval.get_tarNum(),aInterval.get_samNum(),aInterval.get_samPro())
        try:
            self.cursor.execute(sql)
            self.conn.commit()
            self.cursor.close()
        except Exception as e:
            print(e)

    def updateInterval(self,targetStep,intervalNum,interIndex,samNum,tarNum,samPro):
        self.cursor = self.conn.cursor()
        tableName = 'inter_%d_%d' % (targetStep, intervalNum)
        sql = "UPDATE %s SET sampleNum=%d,targetNum=%d,samplePro=%f WHERE inteIndex=%d" %(tableName,samNum,tarNum,samPro,interIndex)
        try:
            self.cursor.execute(sql)
            self.conn.commit()
            self.cursor.close()
        except Exception as e:
            print(e)

    def getNeighbours(self,aId):
        self.cursor = self.conn.cursor()
        sql1 = "SELECT suid FROM all_edges WHERE tuid=%d" %aId
        sql2 = "SELECT tuid FROM all_edges WHERE suid=%d" %aId
        neighbour = set()
        try:
            self.cursor.execute(sql1)
            result1 = self.cursor.fetchall()
            for row in result1:
                neighbour.add(row[0])
            self.cursor.execute(sql2)
            result2 = self.cursor.fetchall()
            for row in result2:
                neighbour.add(row[0])
            return neighbour
        except Exception as e:
            print(e)

    def getSampleID(self,aId,targetStep,intervalNum):
        self.cursor = self.conn.cursor()
        tableName = 'sam_%d_%d' % (targetStep, intervalNum)
        sql = "SELECT * FROM %s WHERE uid=%d" % (tableName, aId)
        flag = False
        try:
            self.cursor.execute(sql)
            self.cursor.fetchall()
            if self.cursor.rowcount>0:
                flag = True
            self.cursor.close()
        except Exception as e:
            print(e)
        return flag

    def get_samProLists(self,targetStep,intervalNum):
        self.cursor = self.conn.cursor()
        tableName = 'inter_%d_%d' % (targetStep, intervalNum)
        sql = "SELECT inteIndex,samplePro FROM %s ORDER BY samplePro DESC" %tableName
        samProLists = []
        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            for row in results:
                samProLists.append([row[0],row[1]])
            self.cursor.close()
            return samProLists
        except Exception as e:
            print(e)

    def getIDs(self):
        self.cursor = self.conn.cursor()
        sql = "SELECT uid FROM nodes"
        IDLists = set()
        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            for row in results:
                IDLists.add(row[0])
            self.cursor.close()
            return IDLists
        except Exception as e:
            print(e)
            
    def closeConn(self):
        self.conn.close()
