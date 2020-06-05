import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="very_strong_password",
    database="myBooks"
)

mycursor = mydb.cursor()

mycursor.execute("ALTER TABLE userbooks ADD COLUMN interested BOOLEAN")

mycursor.execute("ALTER TABLE userbooks ADD COLUMN onCollection BOOLEAN;")
