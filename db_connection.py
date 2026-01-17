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
def DB_restrictions():
    global insurance,savings,housing
    print("The following questions will betterhelp budget beacon make your budgeting experience seamless, please ensure that you answeer all questions accurately, respond witht he appropriate index")
    
    savings_check=int(input("Do you save money monthly, or at all ? \n1.Yes \n2.No "))
    
    insurance_check=int(input("Do you pay for insurance ? \n1.Yes \n2.No "))
    housing_check=int(input("Do you pay for housing ? \n1.Yes \n2.No "))
    
    if savings_check==1:
        pass
    else:
        savings=(None)
    
    if insurance_check==1:
        pass
    else:
        insurance=(None)
    
    if housing_check==1:
        pass
    else:
        housing=(None)