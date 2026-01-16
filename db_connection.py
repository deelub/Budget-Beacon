#First step is to connect the database to ms sql. It will be enter prise managed.From the sql file we can begin with the loggingexpenses

import mysql.connector

def Test_DB_Connection():
    connected=False
    try:
        mydb= mysql.connector.connect(
            host="localhost",
            user="root",
            password="Christelle#6"
        )

        mycursor= mydb.cursor(
            mycursor.execute("CREATE DATABASE Budget Agenda")
        )
        connected=True
    except FileNotFoundError as error:
        print("Database connection unsuccesful")
    