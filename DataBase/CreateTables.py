import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="very_strong_password",
    database="myBooks"
)

mycursor = mydb.cursor()

mycursor.execute(
    "CREATE TABLE User (userId INT AUTO_INCREMENT PRIMARY KEY, userName VARCHAR(255) NOT NULL ,email VARCHAR(255) NOT NULL,password VARCHAR(16) NOT NULL,loginId VARCHAR(255) NOT NULL)")

mycursor.execute(
    "CREATE TABLE UserBooks (userBookId INT AUTO_INCREMENT PRIMARY KEY,userId INT, bookId int, interested  )")

mycursor.execute(
    "CREATE TABLE Book (bookId INT AUTO_INCREMENT PRIMARY KEY, bookName VARCHAR(255) NOT NULL,  description VARCHAR(255) NOT NULL, ISBN  varchar(13) NOT NULL) "
)

mycursor.execute("ALTER TABLE UserBooks ADD FOREIGN KEY (BookId) REFERENCES Book(bookId)")

mycursor.execute("ALTER TABLE UserBooks ADD FOREIGN KEY (userId) REFERENCES User(userId)")
