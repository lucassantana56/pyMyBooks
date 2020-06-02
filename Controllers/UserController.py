from flask import Flask
from flask_restful import Api, Resource, abort, reqparse
from webargs import fields, validate
from webargs.flaskparser import use_kwargs, parser
import mysql.connector
from mysql.connector import Error
import random
import string


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
    return mysql.connect()


class User:
    def createuser(self, p_username, p_email, p_password):
        p_loginId = randomString()
        conn = getDatabase()
        cursor = conn.cursor()
        cursor.callproc('sp_createUser', (p_username, p_email, p_password, p_loginId))
        data = cursor.fetchall()
        if len(data) is 0:
            conn.commit()
            return p_loginId
        else:
            return 0
