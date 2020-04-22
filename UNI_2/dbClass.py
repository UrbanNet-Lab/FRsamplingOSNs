from pymysql import *

class Db(object):
    def __init__(self):
        self.conn = connect(host='127.0.0.1', port=3306, db='twitter', user='students',
                            passwd='MySQL@DellR740XD', charset='utf8')
        self.cursor = self.conn.cursor()

    def createNodeTable(self):
        sql1 = "DROP TABLE IF EXISTS UNIN_500000_1"
        sql2 = "CREATE TABLE UNIN_500000_1 (uid INT UNSIGNED PRIMARY KEY,isTar INT)"
        try:
            self.cursor.execute(sql1)
            self.cursor.execute(sql2)
            self.conn.commit()
        except Exception as e:
            print(e)

    def insertSampleID(self,Id,f):
        flag = True
        sql1 = "SELECT * FROM UNIN_500000_1 WHERE uid=%d" %Id
        sql2 = "INSERT INTO UNIN_500000_1 (uid,isTar) VALUES (%d,%d)" %(Id,f)
        try:
            self.cursor.execute(sql1)
            if self.cursor.rowcount == 1:
                flag = False
            else:
                self.cursor.execute(sql2)
                self.conn.commit()
        except Exception as e:
            print(e)
        return flag

    def testID(self,Id):
        # self.cursor = self.conn.cursor()
        sql = "SELECT * FROM nodes WHERE uid='%d'" %Id
        flag = False
        try:
            self.cursor.execute(sql)
            self.cursor.fetchall()
            if self.cursor.rowcount==1:
                flag = True
            return flag
        except Exception as e:
            print(e)


    def getSampleID(self,Id):
        # self.cursor = self.conn.cursor()
        sql = "SELECT * FROM UNIN_500000_1 WHERE uid=%d" %Id
        flag = False
        try:
            self.cursor.execute(sql)
            self.cursor.fetchall()
            if self.cursor.rowcount>0:
                flag = True
            # self.cursor.close()
            return flag
        except Exception as e:
            print(e)

    def getNeighbours(self,aId):
        self.cursor = self.conn.cursor()
        sql1 = "SELECT suid FROM edges WHERE tuid=%d" %aId
        sql2 = "SELECT tuid FROM edges WHERE suid=%d" %aId
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

    def closeConn(self):
        self.cursor.close()
        self.conn.close()