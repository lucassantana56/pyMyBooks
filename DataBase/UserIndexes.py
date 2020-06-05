import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="very_strong_password",
    database="myBooks"
)

mycursor = mydb.cursor()

mycursor.execute(
    "CREATE UNIQUE INDEX indexUniqueEmailAndPassword ON User(userName,email,password)")

mycursor.execute(
    "CREATE INDEX indexEmailAndPassword ON User(email,password)")
