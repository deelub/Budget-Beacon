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
                            Savings FLOAT(255),
                            Insurance FLOAT(255),
                            Transport FLOAT(255),
                            Housing FLOAT(255),
                            Food FLOAT(255),
                            Toiletries FLOAT(255),
                            Leisure FLOAT(255)
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