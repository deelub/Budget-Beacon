#First step is to connect the database to ms sql. It will be enter prise managed.From the sql file we can begin with the loggingexpenses

import mysql.connector

def test_DB_connection():
    global budget_beacon_db,mycursor
    connected=False
    if connected==False:
        try:
            #sql connection made here
            budget_beacon_db= mysql.connector.connect(
                host="localhost",
                user="root",
                password="Christelle#6"
            )
            mycursor= budget_beacon_db.cursor()    
            if budget_beacon_db.is_connected():
                connected=True     
                    
        except mysql.connector.Error as error:            #Have command to retry connection
            print("Database connection unsuccesful, error: " + error)
            # budget_beacon_db.reconnect()

def create_DB():  #Catgegories:

    mycursor= budget_beacon_db.cursor()
    mycursor.execute("CREATE DATABASE {name}'s budget")
    
    
    mycursor.execute("""
                        CREATE TABLES General Budget (
                            Food VARCHAR(255),
                            Savings VARCHAR(255),
                            Insurance VARCHAR(255),
                            Transport VARCHAR(255),
                            Housing VARCHAR(255),
                            Food VARCHAR(255),
                            Toiletries VARCHAR(255),
                            Leisure VARCHAR(255)
                            )
                        """)