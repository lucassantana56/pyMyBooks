import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="very_strong_password",
    database="myBooks"
)

mycursor = mydb.cursor()

mycursor.execute(
    "CREATE PROCEDURE sp_createUser( p_userName VARCHAR(255), p_email VARCHAR(255), p_password VARCHAR(255),p_loginId VARCHAR(255)) "
    "BEGIN if (SELECT EXISTS (SELECT 1 FROM User WHERE userName = p_username)) THEN SELECT 'Username Exists !!'; ELSE   "
    "INSERT INTO User(userName, email, password,loginId) "
    "values (p_userName,p_email, p_password); END IF; END ")
