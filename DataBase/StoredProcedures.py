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

mycursor.execute(
    "CREATE PROCEDURE sp_AddBooks(p_loginId VARCHAR(255), p_isbn VARCHAR(255), p_Name VARCHAR(255),p_Description VARCHAR(255), p_onCollection BOOLEAN, p_interested BOOLEAN) "
    "BEGIN SET @userId = (SELECT userId FROM user WHERE loginId = p_loginId LIMIT 1); "
    "INSERT INTO book(bookName, description, ISBN) VALUES (p_Name, p_Description, p_isbn);"
    "SET @bookID = LAST_INSERT_ID();"
    "INSERT INTO userbooks(userId, bookId, interested, onCollection) values(@userId, bookId, p_interested, p_onCollection);END; ")

mycursor.execute(
    "CREATE PROCEDURE sp_AddUserBook(p_loginId VARCHAR(255), p_bookId INT, p_onCollection BOOLEAN, p_interested BOOLEAN)"
    "BEGIN set @userId = (select userId from user WHERE loginId = p_loginId LIMIT 1);"
    "INSERT INTO userbooks(userId, bookId, interested, onCollection)"
    "values (@userId, p_bookId, p_interested, p_onCollection);"
    "END;")
