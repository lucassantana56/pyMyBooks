import mysql.connector


def getDatabase():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="very_strong_password",
        database="myBooks"
    )
    return mydb


class Book:
    def addMyBook(self, loginId, isbn, name, description, onCollection, interested):
        sqlquery = "SELECT bookId FROM book USE INDEX (indexUniqueISBN) WHERE  = %s"
        param = (isbn,)
        conn = getDatabase()
        cursor = conn.cursor()
        cursor.execute(sqlquery, param)
        result = cursor.fetchall()
        if result is None:
            cursor.callproc('sp_AddBooks', (loginId, isbn, name, description, onCollection, interested))
            conn.commit()
            return cursor.rowcount()
        else:
            cursor.callproc('sp_AddBooks', (loginId, result, onCollection, interested))
            conn.commit()
            return cursor.rowcount()

    def updateMyBooks(self, loginId, isbn, onCollection, interested):
        sql = "UPDATE userbooks " \
              "SET interested = " + interested + " , onCollection = " + onCollection + " " \
                                                                                       " WHERE bookId = (SELECT bookId FROM book WHERE ISBN =" + isbn + " LIMIT 1)" \
                                                                                                                                                        "AND userId = (SELECT userId FROM user WHERE loginId =" + loginId + " LIMIT 1) "
        conn = getDatabase()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        return cursor.rowcount()
