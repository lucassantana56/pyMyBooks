
import mysql.connector


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="very_strong_password"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE myBooks")




