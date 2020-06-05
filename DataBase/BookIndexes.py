import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="very_strong_password",
    database="myBooks"
)

mycursor = mydb.cursor()

mycursor.execute(
    "CREATE UNIQUE INDEX indexUniqueISBN ON Book(ISBN)")

mycursor.execute(
    "CREATE INDEX nameAndISBN ON Book(bookName,ISBN)")
