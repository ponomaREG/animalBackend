from app import app
import sqlite3


db = sqlite3.connect(app.config['DB_ANIMAL'],check_same_thread=False)

class SqlExecuter:

    @staticmethod
    def getRowsPacked(query):
        cursor = db.execute(query)
        allRows = cursor.fetchall()
        names = [description[0] for description in cursor.description]
        cursor.close()
        result = []
        for row in allRows:
            rowDict = {}
            i = 0
            for name in names:
                rowDict[name] = row[i]
                i+=1
            result.append(rowDict)
        return result

    @staticmethod
    def executeQuery(query):
        cursor = db.execute(query)
        lastrowid = cursor.lastrowid
        db.commit()
        cursor.close()
        return lastrowid