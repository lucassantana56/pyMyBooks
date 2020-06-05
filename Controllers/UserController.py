import random
import string

import mysql.connector


def randomString(stringLength=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


def getDatabase():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="very_strong_password",
        database="myBooks"
    )
    return mydb


class User:
    def createuser(self, p_username, p_email, p_password):
        try:
            p_loginId = randomString()
            conn = getDatabase()
            cursor = conn.cursor()
            cursor.callproc('sp_createUser', (p_username, p_email, p_password, p_loginId))
            conn.commit()
            return p_loginId
        except mysql.connector.Error as error:
            return "Error creating the user please come back later"
        finally:
            if (conn.is_connected()):
                cursor.close()
                conn.close()
            print("MySQL connection is closed")

    def verifyUserExists(self, p_email, p_password):
        try:
            sqlquery = "select loginId,userName from User USE INDEX(indexEmailAndPassword) WHERE password=" + p_password + " AND email = %s"
            emailparam = (p_email,)
            conn = getDatabase()
            cursor = conn.cursor()
            cursor.execute(sqlquery, emailparam)
            result = cursor.fetchall()
            if len(result) == 0:
                return "User not exist"
            for row in result:
                id = row[0],
                name = row[1]
            return id, name
        except mysql.connector.Error as error:
            print(error)
            return "Error on login the user please come back later"
        finally:
            if (conn.is_connected()):
                cursor.close()
                conn.close()
            print("MySQL connection is closed")
